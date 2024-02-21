from pymongo.collection import Collection
from collections import Counter
import pandas as pd


def count_token(token: str, collection: Collection) -> int:
    """Count the number of times a token appears in a MongoDB collection

    Args:
        token (str): target token
        collection (Collection): MongoDB collection

    Returns:
        int: Number of times the token appears in the collection
    """
    total_count = 0
    for doc in collection.find():
        total_count += doc["text"].count(
            token
        )  # Replace 'text_field' with the name of your field containing the text
    return total_count


def word_frequency(collection: Collection) -> pd.DataFrame:
    """Count the frequency of words in a MongoDB collection

    Args:
        collection (Collection): MongoDB collection containing text tokens

    Returns:
        pd.DataFrame: DataFrame with word frequency
    """

    # Initialize a counter for all texts
    total_frequency = Counter()

    for doc in collection.find():
        words = doc["tokens"]
        total_frequency.update(words)

    return pd.DataFrame.from_dict(
        total_frequency, orient="index", columns=["frequency"]
    ).sort_values(by="frequency", ascending=False)
