"""Library for getting text from alto xml pages from the National Library of Norway using the fulltext API"""
import requests
from bs4 import BeautifulSoup
from typing import NamedTuple, Optional, Iterable, TypedDict
import pandas as pd
import os
from tqdm import tqdm

urn = "URN:NBN:no-nb_digibok_2014110308039"
api_str = "https://api.nb.no/catalog/v1/metadata/{urn}/altos/{urn}_{page}"


def format_number(number):
    return "{:04d}".format(number)


def get_alto(urn: str, page: int = 1):
    """Get alto from a page in a book from the National Library of Norway.
    Args:
        urn (str): URN number for the book
        page (int): page number
    Returns:
        str: text from the page
    """
    r = requests.get(api_str.format(urn=urn, page=format_number(page)))

    if r.status_code != 200:
        # print(r.status_code, api_str.format(urn=urn, page=format_number(page)))
        raise ValueError("Could not get page {} from urn {}".format(page, urn))
    return r.text


def check_alto_style(soup: BeautifulSoup) -> str:
    if soup.find("ComposedBlock"):
        return "alto_2"
    elif soup.find("composedblock"):
        return "alto_3"
    elif soup.find("PrintSpace"):
        return "alto_1"
    else:
        raise ValueError("Could not find alto style")


def get_text(soup: BeautifulSoup) -> str:
    """Get text from a alto soup object.

    Args:
        soup (BeautifulSoup): soup object from alto xml page

    Returns:
        str: text from the page
    """
    alto_dict: dict = {
        "composed_block": {
            "alto_2": "ComposedBlock",
            "alto_3": "composedblock",
            "alto_1": "PrintSpace",
        },
        "text_block": {
            "alto_2": "TextBlock",
            "alto_3": "textblock",
            "alto_1": "TextBlock",
        },
        "text_line": {"alto_2": "TextLine", "alto_3": "textline", "alto_1": "TextLine"},
        "string": {"alto_2": "String", "alto_3": "string", "alto_1": "String"},
        "content": {"alto_2": "CONTENT", "alto_3": "content", "alto_1": "CONTENT"},
    }

    alto_style = check_alto_style(soup)

    text = ""
    for composed_block in soup.find_all(alto_dict["composed_block"][alto_style]):
        for text_block in composed_block.find_all(alto_dict["text_block"][alto_style]):
            for text_line in text_block.find_all(alto_dict["text_line"][alto_style]):
                for string in text_line.find_all(alto_dict["string"][alto_style]):
                    # print(string["CONTENT"])
                    text += string[alto_dict["content"][alto_style]] + " "
                text += "\n"
            text += "\n"
        text += "\n"

    return text
