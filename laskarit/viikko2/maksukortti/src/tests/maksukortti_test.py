import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_syo_tasarahalla(self):
        edulinen_kortti = Maksukortti(250)
        maukas_kortti = Maksukortti(400)

        edulinen_kortti.syo_edullisesti()
        maukas_kortti.syo_maukkaasti()

        self.assertListEqual([edulinen_kortti, maukas_kortti], [Maksukortti(0), Maksukortti(0)])

    def test_syo_ei_vie_saldoa_negatiiviseksi(self):
        edulinen_kortti = Maksukortti(200)
        maukas_kortti = Maksukortti(300)

        edulinen_kortti.syo_edullisesti()
        maukas_kortti.syo_maukkaasti()

        self.assertListEqual([edulinen_kortti, maukas_kortti], [Maksukortti(200), Maksukortti(300)])