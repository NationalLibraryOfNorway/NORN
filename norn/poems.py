from typing import NamedTuple, Iterable
import re


class Poem(NamedTuple):
    urn: str
    title: str
    page_start: int
    page_end: int
    overlapp: str
    digital_visning: str
    comment: str
    
    
    
class PoemCollection(NamedTuple):
    poems: Iterable[Poem]
    urn : str
    author: str
    title: str
    year: int
    publisher: str
    publisher_place: str
    
    
def is_valid_urn(string: str):
    pattern = r'^URN:NBN:no-nb_digibok_\d+$'
    return re.match(pattern, string) is not None