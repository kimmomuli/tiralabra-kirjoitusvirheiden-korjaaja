# Määrittelydokumentti

Tarkoituksena on tehdä Pythonilla sovellus kirjoitusvirheiden korjaaja sovellus. Sovellukseen voi kirjoittaa tekstiä ja ohjelma tulostaa korjatun tekstin. Sovelluksessa sanasto tallennetaan käyttämällä trie-tietorakennetta. Virheet korjataan etäisyysmittojen avulla.

## [Trie-tietorakenne](https://en.wikipedia.org/wiki/Trie)
Trie-tietorakenne on optimaalinen sanojen säilykseen. O-analyysillä mitattuna trie-tietorakenteessa on tilavuus- ja aikavaativuus sama eli O(n). 
Oikeita sanoja voi siis hakea suhteellisen nopeasti.

## [Damerau–Levenshtein -etäisyys](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
Damerau–Levenshtein -etäisyyttä käytetään virheellisen sanan korjaamiseen. Tällä algoritmillä suurin osa kirjoitusvirheitä pitäisi korjaantua, joten se sopii tähän projektiin hyvin.
Aikavaativuus on O(M * N * MAX(M, N)), missä M ja N ovat merkkijonojen pituuksia. MAX(M, N) tarkoittaa pitempää merkkijonoa. [Tilavaativuus](https://www.baeldung.com/cs/levenshtein-distance-computation) on O(MAX(M, N)).

## Sanasto
Ohjelma lukee sanat tiedostosta. Tiedosto sanoista, joita käytän löytyy [täältä](https://github.com/hugovk/everyfinnishword).

## Muuta

Dokumentointi tehdään suomen kielellä.

Voin tehdä vertaisarvionteja projekteihin, jotka on tehty Pythonilla, Javalla tai JavaScriptilla.

Tietojenkäsittelytieteen kandidaatti (TKT) 

## Lähteet
Trie-tietorakenteen aikavaativuudet ja Damerau–Levenshtein -algoritmin aikavaativuuden sain wikipediasta.
[https://en.wikipedia.org/wiki/Trie](https://en.wikipedia.org/wiki/Trie)
[https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
Damerau–Levenshtein -algoritmin tilavaativuuden sain baeldung -sivulta.
[https://www.baeldung.com/cs/levenshtein-distance-computation](https://www.baeldung.com/cs/levenshtein-distance-computation)
