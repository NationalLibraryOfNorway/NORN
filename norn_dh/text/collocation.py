from collections import Counter
from norn_dh.text.concordance import concordance
import pandas as pd
from pymongo.collection import Collection


def get_collocation(
    token: str, collection: Collection, before: int = 25, after: int = 25
) -> pd.DataFrame:
    """Get collocation for a token in a MongoDB collection

    Args:
        token (str): target token
        collection (Collection): MongoDB collection with text tokens
        before (int, optional): Length of text snippet before. Defaults to 25.
        after (int, optional): Length of text snippet after. Defaults to 25.

    Returns:
        pd.DataFrame: DataFrame with collocation frequency
    """
    res = []
    for text in collection.find():
        conc_generator = concordance(
            token, text["tokens"], before, after, return_tokens=True
        )
        res.append(conc_generator)

    counter = Counter()
    for gen in res:
        for text_before, _, text_after in gen:
            counter.update(text_before)
            counter.update(text_after)

    return pd.DataFrame.from_dict(counter, orient="index", columns=["frequency"])
