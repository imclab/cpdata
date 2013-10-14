import unittest
import cpdata

class CPDataTest(unittest.TestCase):

    def test_size(self):
        g = cpdata.Graph("http://aims.fao.org/aos/geopolitical.owl")
        self.assertEquals(g.size(), 42)