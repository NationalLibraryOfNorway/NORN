"""Corpus tools

Functions for working with NORN corpora.
"""

import dhlab as dh
from pandas import DataFrame


def check_corpus(df: DataFrame):
    """Checks some basic properties of a NORN corpus

    Args:
        df (DataFrame): dataframe with metadata for NORN korpus
    """
    print("Number of rows in metadata: {}".format(len(df)))
    print("Number of unique urns in metadata: {}".format(len(df["urn"].unique())))
    print(
        "Number of unique dhlabids in metadata: {}".format(len(df["dhlabid"].unique()))
    )
    print("Number of rows with dhlabid {}".format(len(df[df["dhlabid"].notna()])))
    print("Number of rows without dhlabid {}".format(len(df[df["dhlabid"].isna()])))

    # Compare with dhlab
    c = dh.Corpus()
    c.extend_from_identifiers(df["urn"])
    print("Korpus rows: {}".format(len(c.frame)))
