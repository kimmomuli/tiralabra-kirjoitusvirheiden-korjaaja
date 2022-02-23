# Testausdokumentti

### Testikattavuus

### Mitä on testattu

```
tests

  services
    damerau_levenshtein_test.py
    fix_text_test.py
    
  words
    trie_test.py
    word_service_test.py

```

`damerau_levenshtein_test.py` testaa Damerau–Levenshtein-algoritmin

`fix_text_test.py` testaa sanojen korjausta

`trie_test.py` testaan Trie-tietorakenteen oikeellisuuden.

`word_service_test.py` testaa myös Trie-rakennetta ja että tiedoston luku onnistuu oikein.

Käyttöliittymää eli `ui.py` ja `index.py` ei testata ollenkaan.

### [Ohjeet](https://github.com/kimmomuli/tiralabra-kirjoitusvirheiden-korjaaja/blob/main/dokumentit/k%C3%A4ytt%C3%B6ohje.md)
