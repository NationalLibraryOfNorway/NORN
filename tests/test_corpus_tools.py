import pandas as pd
from norn.config import DATA_BASEPATH
from norn.corpus_tools import check_corpus

def test_check_corpus():
    df = pd.read_excel(DATA_BASEPATH / "1800-1839_metadata.xlsx")
    check_corpus(df)