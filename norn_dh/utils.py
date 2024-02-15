import re


def is_valid_digibok_urn(string: str) -> bool:
    """Check that string is a valid URN for a digibok from the National Library of Norway.

    Args:
        string (str): string to check

    Returns:
        bool: True if string is a valid URN for a digibok from the National Library of Norway, else False
    """
    pattern = r"^URN:NBN:no-nb_digibok_\d+$"
    return re.match(pattern, string) is not None
