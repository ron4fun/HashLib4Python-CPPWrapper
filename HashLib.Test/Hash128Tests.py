from TestConstants import *
import unittest

class MurmurHash3_x64_128TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000000000000000000000000000"
        self.ExpectedHashOfDefaultData = "705BD3C954B94BE056F06B68662E6364"
        self.ExpectedHashOfRandomString = "D30654ABBD8227E367D73523F0079673"
        self.ExpectedHashOfZerotoFour = "0F04E459497F3FC1ECCC6223A28DD613"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "4610ABE56EFF5CB551622DAA78F83583"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "ADFD14988FB1F8582A1B67C1BBACC218"

        self.murmurhash3_x64_128 = HashLib4Python.PyHash128.CreateMurmurHash3_x64_128()
       
    def test_TestRandomString(self):
        ActualString = self.murmurhash3_x64_128.ComputeString(RandomStringTobacco).ToString()
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmurhash3_x64_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmurhash3_x64_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmurhash3_x64_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.murmurhash3_x64_128.ComputeString(ZerotoFour).ToString()
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        Hash = HashLib4Python.PyHash128.CreateMurmurHash3_x64_128()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        Hash = HashLib4Python.PyHash128.CreateMurmurHash3_x64_128()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    1)
                    )
        ActualString = Hash.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)


class MurmurHash3_x86_128TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000000000000000000000000000"
        self.ExpectedHashOfDefaultData = "B35E1058738E067BF637B17075F14B8B"
        self.ExpectedHashOfRandomString = "9B5B7BA2EF3F7866889ADEAF00F3F98E"
        self.ExpectedHashOfZerotoFour = "35C5B3EE7B3B211600AE108800AE1088"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "88C4ADEC54D201B954D201B954D201B9"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "55315FA9E8129C7390C080B8FDB1C972"

        self.murmurhash3_x86_128 = HashLib4Python.PyHash128.CreateMurmurHash3_x86_128()
       
    def test_TestRandomString(self):
        ActualString = self.murmurhash3_x86_128.ComputeString(RandomStringTobacco).ToString()
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmurhash3_x86_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmurhash3_x86_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmurhash3_x86_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.murmurhash3_x86_128.ComputeString(ZerotoFour).ToString()
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        Hash = HashLib4Python.PyHash128.CreateMurmurHash3_x86_128()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        Hash = HashLib4Python.PyHash128.CreateMurmurHash3_x86_128()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    1)
                    )
        ActualString = Hash.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

  
if __name__ ==  '__main__':
    unittest.main()
