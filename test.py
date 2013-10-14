import unittest
import cpdata

class CPDataTest(unittest.TestCase):

    def test_size(self):
        g = cpdata.Summarizer("http://aims.fao.org/aos/geopolitical.owl")
        self.assertEquals(g.size(), 23780)