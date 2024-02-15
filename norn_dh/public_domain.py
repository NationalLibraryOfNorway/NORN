import requests

api_base_path = "https://api.nb.no/catalog/v1/items/{}?fields=accessInfo&expand=false"


def check_urn(urn_to_check: str) -> bool | dict:
    """Check if a text is free to use.

    Args:
        urn_to_check (str): National library text id (urn) to check

    Returns:
        bool: True if the text is free to use
    """
    response = requests.get(api_base_path.format(urn_to_check))
    if response.status_code == 200:
        return response.json()["accessInfo"]["isPublicDomain"]
    else:
        return {"error" : f"Could not find urn {urn_to_check}"}
