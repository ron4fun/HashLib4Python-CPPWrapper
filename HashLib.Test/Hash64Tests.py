from TestConstants import *

class FNV64TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "0000000000000000"
        self.ExpectedHashOfDefaultData = "061A6856F5925B83"
        self.ExpectedHashOfOnetoNine = "B8FB573C21FE68F1"
        self.ExpectedHashOfabcde = "77018B280326F529"

        self.fnv = HashLib4Python.PyHash64.CreateFNV()
        
    def test_TestBytesabcde(self):
        ActualString = self.fnv.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.fnv.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.fnv.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.fnv.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.fnv.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateFNV()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateFNV()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyHash64.CreateFNV()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyHash64.CreateFNV()

        self.HashCloneIsUnique(Hash)

        
class FNV1a64TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "CBF29CE484222325"
        self.ExpectedHashOfDefaultData = "5997E22BF92B0598"
        self.ExpectedHashOfOnetoNine = "06D5573923C6CDFC"
        self.ExpectedHashOfabcde = "6348C52D762364A8"

        self.fnv1a = HashLib4Python.PyHash64.CreateFNV1a()
        
    def test_TestBytesabcde(self):
        ActualString = self.fnv1a.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.fnv1a.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.fnv1a.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.fnv1a.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.fnv1a.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateFNV1a()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateFNV1a()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyHash64.CreateFNV1a()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyHash64.CreateFNV1a()

        self.HashCloneIsUnique(Hash)


class Murmur2_64TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "0000000000000000"
        self.ExpectedHashOfDefaultData = "F78F3AF068158F5A"
        self.ExpectedHashOfOnetoNine = "F22BE622518FAF39"
        self.ExpectedHashOfabcde = "AF7BA284707E90C2"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "49F2E215E924B552"

        self.murmur2 = HashLib4Python.PyHash64.CreateMurmur2()
        
    def test_TestBytesabcde(self):
        ActualString = self.murmur2.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmur2.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmur2.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmur2.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.murmur2.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestWithDifferentKey(self):
        Hash = HashLib4Python.PyHash64.CreateMurmur2()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateMurmur2()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateMurmur2()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyHash64.CreateMurmur2()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyHash64.CreateMurmur2()

        self.HashCloneIsUnique(Hash)

        
class SipHash2_4TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "726FDB47DD0E0E31"
        self.ExpectedHashOfDefaultData = "AA43C4288619D24E"
        self.ExpectedHashOfOnetoNine = "CA60FC96020EFEFD"
        self.ExpectedHashOfabcde = "A74563E1EA79B873"
        self.ExpectedHashOfShortMessage = "AE43DFAED1AB1C00"

        self.siphash2_4 = HashLib4Python.PyHash64.CreateSipHash2_4()
        
    def test_TestBytesabcde(self):
        ActualString = self.siphash2_4.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.siphash2_4.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.siphash2_4.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.siphash2_4.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.siphash2_4.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestShortMessage(self):
        ActualString = self.siphash2_4.ComputeString(ShortMessage).ToString()
        self.assertTrue(self.ExpectedHashOfShortMessage == ActualString)

    def test_TestWithOutsideKey(self):
        Hash = HashLib4Python.PyHash64.CreateSipHash2_4()
        Hash.SetKey(HashLib4Python.PyConverters.ConvertHexStringToBytes(
                    HexStringAsKey)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateSipHash2_4()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateSipHash2_4()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyHash64.CreateSipHash2_4()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyHash64.CreateSipHash2_4()

        self.HashCloneIsUnique(Hash)


class XXHash64TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "EF46DB3751D8E999"
        self.ExpectedHashOfDefaultData = "0F1FADEDD0B77861"
        self.ExpectedHashOfRandomString = "C9C17BCD07584404"
        self.ExpectedHashOfZerotoFour = "34CB4C2EE6166F65"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "D5AFBA1336A3BE4B"
        self.ExpectedHashOfDefaultDataWithMaxUInt64AsKey = "68DCC1056096A94F"

        self.xxhash64 = HashLib4Python.PyHash64.CreateXXHash64()
        
    def test_TestRandomString(self):
        ActualString = self.xxhash64.ComputeString(RandomStringTobacco).ToString()
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.xxhash64.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.xxhash64.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.xxhash64.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.xxhash64.ComputeString(ZerotoFour).ToString()
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyMaxUInt64DefaultData(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt64AsBytesLE(
                    MaxUInt64)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt64AsKey == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt64AsBytesLE(
                    1)
                    )
        ActualString = Hash.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyHash64.CreateXXHash64()

        self.HashCloneIsUnique(Hash)
        

if __name__ ==  '__main__':
    unittest.main()
