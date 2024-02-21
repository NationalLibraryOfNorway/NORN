import dhlab as dh
import pandas as pd


def make_imagination_corpus():
    """Bygg hele imagination-korpuset fra dhlab"""

    import requests

    def query_imag_corpus(
        category=None,
        author=None,
        title=None,
        year=None,
        publisher=None,
        place=None,
        oversatt=None,
    ):
        """Fetch data from imagination corpus"""
        params = locals()
        params = {key: params[key] for key in params if params[key] is not None}
        # print(params)
        r = requests.get(f"{dh.constants.BASE_URL}/imagination", params=params)
        return r.json()

    # kategoriene
    cats = [
        "Barnelitteratur",
        "Biografi / memoar",
        "Diktning: Dramatikk",
        "Diktning: Dramatikk # Diktning: oversatt",
        "Diktning: Epikk",
        "Diktning: Epikk # Diktning: oversatt",
        "Diktning: Lyrikk",
        "Diktning: Lyrikk # Diktning: oversatt",
        "Diverse",
        "Filosofi / estetikk / språk",
        "Historie / geografi",
        "Lesebok / skolebøker / pedagogikk",
        "Litteraturhistorie / litteraturkritikk",
        "Naturvitenskap / medisin",
        "Reiselitteratur",
        "Religiøse / oppbyggelige tekster",
        "Samfunn / politikk / juss",
        "Skisser / epistler / brev / essay / kåseri",
        "Taler / sanger / leilighetstekster",
        "Teknologi / håndverk / landbruk / havbruk",
    ]

    # bygg en dataramme for hver kategori
    a = dict()
    for c in cats:
        a[c] = dh.Corpus()
        a[c].extend_from_identifiers(query_imag_corpus(category=c))
        a[c] = a[c].frame
        a[c]["category"] = c

    # lim alt sammen til et stort korpus
    imag_all = pd.concat([a[c] for c in a])
    imag_all.year = imag_all.year.astype(int)
    imag_all.dhlabid = imag_all.dhlabid.astype(int)

    return imag_all
