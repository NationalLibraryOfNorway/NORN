from dhlab.nbtokenizer import tokenize as tok
from typing import Generator, List
from dataclasses import dataclass
import pandas as pd
from pymongo.collection import Collection


# Concordance
def get_text_from_token(token: str, collection: Collection) -> List[dict]:
    """Get all texts containing a token from a MongoDB collection"""
    return list(collection.find({"text": {"$regex": ".*" + token + ".*"}}))


def find_indexes(lst: List[str], element: str) -> List[int]:
    """Find indexes of an element in a list

    Args:
        lst (List[str]): list of tokens
        element (str): token to find

    Returns:
        List[int]: indexes of tokens
    """
    return [index for index, value in enumerate(lst) if value == element]


def concordance(
    token: str,
    token_lst: List[str],
    before: int = 5,
    after: int = 5,
    return_tokens: bool = False,
) -> Generator[str, str, str]:
    """Get a concordance for a token in a text

    Args:
        token (str): _description_
        token_lst (List[str]): _description_
        before (int, optional): _description_. Defaults to 5.
        after (int, optional): _description_. Defaults to 5.
        return_tokens (bool, optional): _description_. Defaults to False.

    Yields:
        Generator[str, str, str]: _description_
    """

    token_indexes = find_indexes(token_lst, token)

    for token_index in token_indexes:
        start = token_index - before  # Find the start of the concordance
        end = token_index + after  # Find the end of the concordance
        # yield token_lst[start:end]  # Return the concordance
        before_tokens = token_lst[start:token_index]
        after_tokens = token_lst[token_index + 1 : end]
        # yield (before_tokens, token, after_tokens)
        if return_tokens:
            yield before_tokens, token, after_tokens
        else:
            yield " ".join(before_tokens), token, " ".join(after_tokens)


@dataclass
class ConcRes:
    text_id: str
    before: str
    token: str
    after: str


def get_concordance(token: str, collection: Collection, before=5, after=5):
    """Get concordance for a token in a MongoDB collection"""
    texts = get_text_from_token(token, collection)

    concs = []
    for text in texts:
        conc_generator = concordance(token, text["tokens"], before, after)
        conc_list = [x for x in conc_generator]
        for x in conc_list:
            before_txt, token, after_txt = x
            concs.append(ConcRes(text["_id"], before_txt, token, after_txt))

    return pd.DataFrame(concs)
