from typing import Iterable, Optional, List
import re
import pandas as pd
import numpy as np
from norn.utils import is_valid_digibok_urn
from dataclasses import dataclass
from tqdm import tqdm
from norn.alto_tools import get_alto


@dataclass
class Poem:
    urn: str
    title: str
    page_start: int
    page_end: int
    overlapp: str
    digital_visning: str
    comment: str
    pages: Optional[Iterable[str]] = None


@dataclass
class PoemCollection:
    poems: List[Poem]
    urn: str
    author: str
    title: str
    year: int
    publisher: str
    publisher_place: str


def create_list_of_books(df: pd.DataFrame, remove_empty=True) -> List[Poem]:
    book_list: List[PoemCollection] = []
    book = None

    for i, row in df.iterrows():
        # if row[0] is not np.nan:
        if is_valid_digibok_urn(str(row[0])):
            if book is not None:
                book_list.append(book)
            book = PoemCollection([], *row[:6])
        else:
            if row[1] == "Tittel på dikt":
                continue
            elif row[1] is np.nan:
                continue
            else:
                if book is not None:
                    book.poems.append(Poem(book.urn, *row[1:7]))

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
    data = "/home/larsm/projects/NORN/poems/Extract_poems/1890 enkeltdikt.xlsx"

    df = pd.read_excel(data, header=None)
    poems = create_list_of_books(df)

    df = pd.DataFrame(poems)

    assert PoemsTester(poems), "Poems not valid"


if __name__ == "__main__":
    main()
