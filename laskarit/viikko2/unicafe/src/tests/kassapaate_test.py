import unittest
from kassapaate import kassapaate_data
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luotu_kassapaate(self):
        print(kassapaate_data(self.kassapaate))
        self.assertDictEqual(kassapaate_data(self.kassapaate), {
            'eurot': 1000,
            'sentit': 0,
            'edulliset': 0,
            'maukaat': 0
        })
    
    def test_maksuriittaa(self):
        edullinen_maksu = 300
        maukas_maksu = 500
        edullinen_vaihto = self.kassapaate.syo_edullisesti_kateisella(edullinen_maksu)
        maukas_vaihto = self.kassapaate.syo_maukkaasti_kateisella(maukas_maksu)

        kassa_data = kassapaate_data(self.kassapaate)
        kassa_data['edullinen_vaihto'] = edullinen_vaihto
        kassa_data['maukas_vaihto'] = maukas_vaihto

        self.assertDictEqual(kassa_data, {
            'eurot': 1006,
            'sentit': 40,
            'edulliset': 1,
            'maukaat': 1,
            'edullinen_vaihto': 60,
            'maukas_vaihto': 100
        })
    
    def test_maksu_ei_riita(self):
        edullinen_maksu = 200
        maukas_maksu = 300
        edullinen_vaihto = self.kassapaate.syo_edullisesti_kateisella(edullinen_maksu)
        maukas_vaihto = self.kassapaate.syo_maukkaasti_kateisella(maukas_maksu)

        kassa_data = kassapaate_data(self.kassapaate)
        kassa_data['edullinen_vaihto'] = edullinen_vaihto
        kassa_data['maukas_vaihto'] = maukas_vaihto

        self.assertDictEqual(kassa_data, {
            'eurot': 1000,
            'sentit': 0,
            'edulliset': 0,
            'maukaat': 0,
            'edullinen_vaihto': 200,
            'maukas_vaihto': 300
        })
    
    def test_maksu_riitta_kortti(self):
        edullinen_maksu = Maksukortti(300)
        maukas_maksu = Maksukortti(500)
        edullinen_vaihto = self.kassapaate.syo_edullisesti_kortilla(edullinen_maksu)
        maukas_vaihto = self.kassapaate.syo_maukkaasti_kortilla(maukas_maksu)

        kassa_data = kassapaate_data(self.kassapaate)
        kassa_data['edullinen_vaihto'] = edullinen_vaihto
        kassa_data['maukas_vaihto'] = maukas_vaihto

        self.assertDictEqual(kassa_data, {
            'eurot': 1000,
            'sentit': 0,
            'edulliset': 1,
            'maukaat': 1,
            'edullinen_vaihto': True,
            'maukas_vaihto': True
        })

    def test_maksu_riitta_kortti(self):
        edullinen_maksu = Maksukortti(200)
        maukas_maksu = Maksukortti(300)
        edullinen_vaihto = self.kassapaate.syo_edullisesti_kortilla(edullinen_maksu)
        maukas_vaihto = self.kassapaate.syo_maukkaasti_kortilla(maukas_maksu)

        kassa_data = kassapaate_data(self.kassapaate)
        kassa_data['edullinen_vaihto'] = edullinen_vaihto
        kassa_data['maukas_vaihto'] = maukas_vaihto

        self.assertDictEqual(kassa_data, {
            'eurot': 1000,
            'sentit': 0,
            'edulliset': 0,
            'maukaat': 0,
            'edullinen_vaihto': False,
            'maukas_vaihto': False
        })
    
    def test_lataa_rahaa(self):
        self.kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 300)
        self.assertListEqual([self.kassapaate.kassassa_rahaa, self.kortti.saldo], [100300, 300])
