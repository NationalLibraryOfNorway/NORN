# README

NORN  


## Data

- Konsensuskorpuset (`konsensuskorpus_master.xlsx`) inneholder manuelt kuraterte rader med metadata om bøker fra 1800-tallslitteraturen som omtales i Litteraturhistoriske verk som "nasjonalromantiske". 
- `Data/1800-1839_metadata.xlsx` inneholder metadata om 101 verk som ble publisert fra 1800 og før 1840.
- `Data/1840-1869_metadata.xlsx` inneholder metadata om 239 verk som ble publisert fra 1840, før 1870.

### Prosessering 

Dataprossesseringen er dokumentert i notebooks i repoet. 

- `do_analysis.ipynb` aggregerer opp annotasjonene i konsensuskorpuset. 
- `add_imagination_metadata.ipynb` henter inn URN-lister for delkorpusene og legger til metadata. 
