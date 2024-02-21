from norn_dh.text.concordance import get_concordance, get_text_from_token, find_indexes, concordance
from dhlab.nbtokenizer import tokenize as tok

def test_get_text_from_token():
    pass

def test_find_indexes():
    lst = ["test", "example", "test", "sample"]
    indexes = find_indexes(lst, "test")
    assert indexes == [0, 2]
    
def test_concordance():
    test_txt = "'62 \n\n\nNaar en gang mot natten det stunder, \nog Herren os gjensynet under, \n\nnokk vet jeg, hvem da oven sky \n\nvil kjærlig i møte os fly. \n\n\nOver vore to smaa døde. \n1. Lovise Margrete, \nfød den 14de januar 1864, død 12te november 1874. \n(Nu titte til hinanden de fagre blomfter fmaa.) \nDu vesle «Visestubben» for os saa ofte sang – \nsaa blødt og yndigt trilled dine toner – \nnu vil for dig jeg synge da her for siste gang, \nom lytte du kan fra fjerne zoner. \n\n\nThi der saa visst jeg haaber, at nu du flagrer om \nfra favn til favn imellem flægt og venner. \n\nSaa mange kjære sjæle dig der i møte kom, \n\nsaa mange smaaengle alt du fjender. \n\n\n3a slaa da dine triller nu fuldt i englekor! \n\nSvng sødt for Krift om rette barneglæden! \n\nDit livsensskudd det brødes saa braatt her paa jord, – \nnu blomstrer det blidt i himlens eden. \n\n\n\n\n65 \n\n\n2. Peder Pavels Aabel. \nfød 15 mai 1867, død 29de november 1874. \n«Jesus, lukk opp for mig! –» saa lød hans ord, \nmens han snart skalv og snart brann her paa jord. \nHerre du milde, ham tag i din arm, \nkvæg du den lille ved kjærlige barm! \n\n\nNu har hans nagende lidelser slutt, \nnu er han trøstet, vor trofaste gutt: \nHan skal faa leke med systeren sin – \nlukk ham, o Jesus i himmelen ind! \n\n\nTil Mama! \nJannar 1875. \n(Kommen, vakra blommor) \n\nMama! Tre smaajenter \nfløj ifjor dig glad i fang: \nDen som havde dem omkring sig, \naldrig savned spil og sang. \nSom lysalfer over enge \ndansed de saa lett og lo – \nmen hvor blev der av den ene? \nNu ser jeg ei mer end to. \n\n\n\n\n'"
    tokens = tok(test_txt)   
    lst = list(concordance("jeg", tokens))
    assert len(lst) == 4

def test_get_concordance():
    pass