import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(1000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")

