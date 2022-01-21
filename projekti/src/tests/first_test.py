import unittest
from index import Maksukortti

class TestIndex(unittest.TestCase):
    def setUp(self):
      pass

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(10)

        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")