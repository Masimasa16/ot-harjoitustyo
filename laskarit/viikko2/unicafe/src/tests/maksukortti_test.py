import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_lataa_rahaa_positiivinen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)
    
    def test_ota_rahaa_onistuu(self):
        maara_onituu = 300
        maara_epaonistuu = 1100

        onituu = self.maksukortti.ota_rahaa(maara_onituu)
        epaonituu = self.maksukortti.ota_rahaa(maara_epaonistuu)

        self.assertListEqual([self.maksukortti.saldo, onituu, epaonituu], [700, True, False])
    
    def test__str__(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')
    
    

