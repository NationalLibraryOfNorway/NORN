import re


def is_valid_digibok_urn(string: str) -> bool:
    pattern = r"^URN:NBN:no-nb_digibok_\d+$"
    return re.match(pattern, string) is not None
