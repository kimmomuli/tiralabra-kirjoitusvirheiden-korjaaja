
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
