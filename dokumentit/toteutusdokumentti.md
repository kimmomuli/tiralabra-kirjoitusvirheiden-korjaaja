# Toteutusdokumentti

### Ohjelman rakenne

`index.py` starttaa ohjelman käynnistämällä graafisen käyttöliittymän tiedostosta `ui.py`.

`ui.py` alustaa olion `FixText` tiedostosta `fix_text.py`

`FixText` hoitaa siis sanojen korjauksen.
`FixText` alustaa `WordService` olion tiedostosta `word_service.py`.
`FixText` voi käyttää myös algoritmia tiedostosta `damerau_levenshtein.py`.

`WordService` on olio jonka kautta käytetään `trie.py` tiedostossa olevaa `Trie`-rakennetta.
`WordService` hoitaa myös sanojen luvun `kaikkisanat.txt --> Trie`




Hakemistorakenne on seuraava:

```
index.py
  
  services
    damerau_levenshtein.py
    fix_text.py
  
  ui
    ui.py
    
  words
    kaikkisanat.txt
    trie.py
    word_service.py
  
  tests
```

Testeillä on sama rakenne kuin itse ohjelmalla eli
```

tests

  services
    damerau_levenshtein_test.py
    fix_text_test.py
    
  words
    trie_test.py
    word_service_test.py

```

Käyttöliittymää ei testata tässä projektissa ollenkaan.



### Aika- ja tilavaativuudet

Trien aika- ja tilavaativuudet `O(n)`

Damerau–Levenshtein etäisyydessä aikavaativuus ja tilavaativuus on `O(nm)`, missä n ja m ovat sanojen pituudet.

### Parannusehdotukset

Ohjelma ei tue tällä hetkellä kuin perusmuodossa olevia sanoja. 
Samalla idealla voisi yrittää toteuttaa korjaajaa, joka ottaa huomioon sanojen taivutukset. (Tarkkuus on paljon huonompi, jonka takia en totetuttanut taivutusta)
Myös isot kirjaimet voisi korjata isoksi kirjaimeksi.
Yksi mahdollinen parannusehdotus voisi olla, että jos sanan jälkeen on piste niin ohjelma tunnistaa sen lauseen lopuksi eikä yritä korjata sitä osana sanaa.

### Lähteet

[Trie](https://en.wikipedia.org/wiki/Trie)

[Damerau–Levenshtein](https://www.baeldung.com/cs/levenshtein-distance-computation)
