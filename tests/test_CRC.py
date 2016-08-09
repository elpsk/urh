import unittest

from urh.signalprocessing.encoding import encoding
from urh.util.crc import crc_generic

class TestCRC(unittest.TestCase):
    # Testmethode muss immer mit Präfix test_* starten
    def test_crc(self):
        c = crc_generic(polynomial="8_en")
        e = encoding()

        bitstr = ["010101010110100111011010111011101110111011100110001011101010001011101110110110101101",
                  "010101010110101001101110111011101110111011100110001011101010001011101110110111100101",
                  "010101010110100111010010111011101110111011100110001011101010001011101110110110100101"]
        print()
        for v in bitstr:
            nv = ""
            for i in range(0, len(v)):
                if v[i] == "1":
                    nv += "0"
                else:
                    nv += "1"

            print(e.bit2hex(e.str2bit(nv[1:])), len(v[:]))
            print(e.bit2hex(c.crc(e.str2bit(v[4:-8]))))

