import pandas as pd
from pymongo.collection import Collection


def get_all_tokens(collection: Collection) -> list:
    """Get all documents from a MongoDB collection"""
    return pd.DataFrame(collection.find({}, {"tokens": 1, "_id": 1}))


def get_dtm(collection):

    df = get_all_tokens(collection)

    s = df.set_index("_id").tokens.explode()  # Explode tokens
    t = (
        s.to_frame()
        .reset_index()
        .reset_index()
        .rename(columns={"index": "n"})
        .groupby(["_id", "tokens"])
        .count()
    )  # Count tokens
    r = t.reset_index().sort_values(by=["n"], ascending=False)  # Sort by count
    return r.pivot(columns="_id", values="n", index="tokens").fillna(
        0
    )  # Pivot table, fill NaN with 0
