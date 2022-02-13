
# Riippuvuudet
Voit asentaa riippuvuudet komennolla 
```
poetry install
```



# Ohjeet
Mene projekti kansioon komennolla 
```
cd projekti
```
## Ohjelman käynnistys

Voit ajaa ohjelman komennolla 
```
poetry run invoke start
```
## Testit

Testit ajetaan komennolla
```
poetry run invoke coverage
```

Testikattavuus onnistuu ajamalla
```
poetry run invoke coverage-report
```
Nyt projekti hakemistoon ilmestyy htmlcov-hakemisto. Siellä sijaitseva index.html sisältää testikattavuuden. Jos käytössäsi on chrome voit avata tiedoston `google-chrome htmlcov/index.html`

Jos haluat ajaa testikattavuuden terminaalissa, sekin onnistuu komennolla
```
poetry run invoke coverage-terminal-report
```

## Pylint
Koodin laatutarkistuksen voi ajaa komennolla 
```
poetry run invoke pylint
```



## Kaikki komennot
Kaikki komennot voi selvittää

```
poetry run invoke --list
```



# Ohjeet virtuaaliympäristössä

## Testit
HUOM! aja komennot projekti hakemistossa, johon pääset `cd projekti` 

Käynnistetään virtuaaliympäristö 

```
poetry shell
```
Voit lopettaa virtuaaliympäristön komennolla exit.

Testit voi ajaa
```
coverage run --branch -m pytest src
```

Testikattavuus terminaalissa
```
coverage report -m
```
Tai voit vaihtoehtoisesti ajaa testikattavuuden html tiedostoon komennolla 
```
coverage html
```
Komento luo hakemiston htmlcov. Avaamalla siellä sijaitseva tiedosto index.html sisältää testikattavuuden.

## Pylint
Käynnistetään virtuaaliympäristö 

```
poetry shell
```
Voit lopettaa virtuaaliympäristön komennolla exit.

Pylint laatutarkistuksen voi suorittaa komennolla.
```
pylint src
```
