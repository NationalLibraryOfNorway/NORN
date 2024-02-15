"""Tools for working with poems from the National Library of Norway"""
from typing import Iterable, Optional, List
import re
import pandas as pd
import numpy as np
from norn_dh.utils import is_valid_digibok_urn
from dataclasses import dataclass
from tqdm import tqdm
from norn_dh.alto_tools import get_alto


@dataclass
class Poem:
    """Poem class
    
    Represents a poem from the National Library of Norway from the Norn poems project
    """
    urn: str
    title: str
    page_start: int
    page_end: int
    overlapp: str
    digital_visning: str
    comment: str
    dhlabid: Optional[str] = None
    pages: Optional[Iterable[str]] = None


@dataclass
class PoemCollection:
    """Poem collection class
    
    Represents a collection of poems from the National Library of Norway from the Norn poems project
    """
    poems: List[Poem]
    urn: str
    author: str
    title: str
    year: int
    publisher: Optional[str] = None
    publisher_place: Optional[str] = None


def process_master_sheet(df: pd.DataFrame) -> List[PoemCollection]:
    """Process master sheet from Ranveig
    
    Create list of PoemCollection objects from master sheet

    Args:
        df (pd.DataFrame): dataframe from Ranveig

    Returns:
        List[PoemCollection]: List of PoemCollection objects
    """
    book_list: List[PoemCollection] = []
    book = None

    for _, row in df.iterrows():
        if is_valid_digibok_urn(str(row.iloc[0])):
            if book is not None:
                book_list.append(book)
            
            # Year is in row 3 or 4
            if row.iloc[3] is not np.nan:
                year = int(row.iloc[3])
            elif[4] is not np.nan:
                year = int(row.iloc[4])
            
            book = PoemCollection(poems=[], urn=row.iloc[0], author=row.iloc[1], title=row.iloc[2], year=year)
        else:
            if row.iloc[1] == "Tittel på dikt":
                continue
            elif row.iloc[1] is np.nan:
                continue
            elif row.iloc[0] == "1890 enkeltdikt":
                continue
            else:
                if book is not None:                    
                    book.poems.append(Poem(book.urn, *row.iloc[1:7]))
                else:
                    raise ValueError("Book is None")
                    
    return book_list
    

def create_list_of_books(df: pd.DataFrame, remove_empty=True) -> List[Poem]:
    """Create list of poems from dataframe

    Args:
        df (pd.DataFrame): dataframe from Ranveig
        remove_empty (bool, optional): drop books with no poem entries. Defaults to True.

    Returns:
        List[Poem]: List of poems objects
    """
    book_list = process_master_sheet(df)

    if remove_empty:
        poems_list = [x.poems for x in book_list if len(x.poems) > 0]
    else:
        poems_list = [x.poems for x in book_list]

    poems = [x for sublist in poems_list for x in sublist]  # Flatten list of lists

    return poems


class PoemsTester:
    def __init__(self, poems: pd.DataFrame | Iterable[Poem]):
        """Test that list of poems is valid

        Args:
            poems (pd.DataFrame | Iterable[Poem]): Iterable of poems class
        """

        if isinstance(poems, pd.DataFrame):
            poems = [Poem(*x) for x in poems.values]

        self.poems = poems

        assert self.test_urn(), "URN not valid"
        assert self.test_page_start(), "Page start not valid"
        assert self.test_page_end(), "Page end not valid"

        print("All tests passed")

    def test_urn(self):
        return all([is_valid_digibok_urn(x.urn) for x in self.poems])

    def test_page_start(self):
        return all([isinstance(x.page_start, int) for x in self.poems])

    def test_page_end(self):
        return all([isinstance(x.page_end, int) for x in self.poems])

    def test_overlapp(self):
        return all([isinstance(x, str) for x in self.poems])


def main():
    data = "../poems/Extract_poems/1890 enkeltdikt.xlsx"

    df = pd.read_excel(data, header=None)
    poems = create_list_of_books(df)

    df = pd.DataFrame(poems)

    assert PoemsTester(poems), "Poems not valid"


if __name__ == "__main__":
    main()
