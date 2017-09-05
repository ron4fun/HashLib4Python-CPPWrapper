from TestConstants import *
import unittest

class FNV64TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "0000000000000000"
        self.ExpectedHashOfDefaultData = "061A6856F5925B83"
        self.ExpectedHashOfOnetoNine = "B8FB573C21FE68F1"
        self.ExpectedHashOfabcde = "77018B280326F529"

        self.fnv = HashFactory.PyHash64.CreateFNV
        
    def test_TestBytesabcde(self):
        ActualString = self.fnv(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.fnv(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.fnv("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.fnv(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.fnv(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

        
class FNV1a64TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "CBF29CE484222325"
        self.ExpectedHashOfDefaultData = "5997E22BF92B0598"
        self.ExpectedHashOfOnetoNine = "06D5573923C6CDFC"
        self.ExpectedHashOfabcde = "6348C52D762364A8"

        self.fnv1a = HashFactory.PyHash64.CreateFNV1a
        
    def test_TestBytesabcde(self):
        ActualString = self.fnv1a(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.fnv1a(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.fnv1a("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.fnv1a(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.fnv1a(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class Murmur2_64TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "0000000000000000"
        self.ExpectedHashOfDefaultData = "F78F3AF068158F5A"
        self.ExpectedHashOfOnetoNine = "F22BE622518FAF39"
        self.ExpectedHashOfabcde = "AF7BA284707E90C2"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "49F2E215E924B552"

        self.murmur2 = HashFactory.PyHash64.CreateMurmur2
        
    def test_TestBytesabcde(self):
        ActualString = self.murmur2(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmur2(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmur2("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmur2(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.murmur2(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestWithDifferentKey(self):
        ActualString = self.murmur2(DefaultData, 0, MaxUInt32)
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


class SipHash2_4TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "726FDB47DD0E0E31"
        self.ExpectedHashOfDefaultData = "AA43C4288619D24E"
        self.ExpectedHashOfOnetoNine = "CA60FC96020EFEFD"
        self.ExpectedHashOfabcde = "A74563E1EA79B873"
        self.ExpectedHashOfShortMessage = "AE43DFAED1AB1C00"

        self.siphash2_4 = HashFactory.PyHash64.CreateSipHash2_4
        
    def test_TestBytesabcde(self):
        ActualString = self.siphash2_4(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.siphash2_4(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.siphash2_4("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.siphash2_4(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.siphash2_4(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestShortMessage(self):
        ActualString = self.siphash2_4(ShortMessage, 0)
        self.assertTrue(self.ExpectedHashOfShortMessage == ActualString)

    def test_TestWithOutsideKey(self):
        ActualString = self.siphash2_4(DefaultData, 0, 0x0001020304050607, 0x08090A0B0C0D0E0F)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)


class XXHash64TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "EF46DB3751D8E999"
        self.ExpectedHashOfDefaultData = "0F1FADEDD0B77861"
        self.ExpectedHashOfRandomString = "C9C17BCD07584404"
        self.ExpectedHashOfZerotoFour = "34CB4C2EE6166F65"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "D5AFBA1336A3BE4B"
        self.ExpectedHashOfDefaultDataWithMaxUInt64AsKey = "68DCC1056096A94F"

        self.xxhash64 = HashFactory.PyHash64.CreateXXHash64
        
    def test_TestRandomString(self):
        ActualString = self.xxhash64(RandomStringTobacco, 0)
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.xxhash64(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.xxhash64("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.xxhash64(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.xxhash64(ZerotoFour, 0)
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyMaxUInt64DefaultData(self):
        ActualString = self.xxhash64(DefaultData, 0, MaxUInt64)
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt64AsKey == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        ActualString = self.xxhash64(EmptyData, 0, 1)
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)


if __name__ ==  '__main__':
    unittest.main()
