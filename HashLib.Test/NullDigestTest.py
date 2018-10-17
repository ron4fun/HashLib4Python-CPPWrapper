from TestConstants import *


class NullDigestTestCase(BaseTestCase):
    def setUp(self):

        self.nullDigest = HashLib4Python.PyNullDigestFactory.CreateNullDigest()
       
    def test_TestBytesabcde(self):
        BytesABCDE = bytearray("abcde")
        self.assertTrue(-1 == self.nullDigest.GetBlockSize())
        self.assertTrue(-1 == self.nullDigest.GetHashSize())

        self.nullDigest.Initialize()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.nullDigest.TransformBytes(BytesABCDE)

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(len(BytesABCDE) == self.nullDigest.GetHashSize())

        Result = self.nullDigest.TransformFinal().GetBytes()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.assertTrue(BytesABCDE == bytearray(Result))
	
    def test_TestEmptyBytes(self):
        self.nullDigest = HashLib4Python.PyNullDigestFactory.CreateNullDigest()

        BytesEmpty = bytearray("")
        self.assertTrue(-1 == self.nullDigest.GetBlockSize())
        self.assertTrue(-1 == self.nullDigest.GetHashSize())

        self.nullDigest.Initialize()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.nullDigest.TransformBytes(BytesEmpty)

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(len(BytesEmpty) == self.nullDigest.GetHashSize())

        Result = self.nullDigest.TransformFinal().GetBytes()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.assertTrue(BytesEmpty == bytearray(Result))

    def test_TestIncrementalHash(self):
        self.nullDigest = HashLib4Python.PyNullDigestFactory.CreateNullDigest()

        BytesZeroToNine = bytearray("0123456789")
        self.assertTrue(-1 == self.nullDigest.GetBlockSize())
        self.assertTrue(-1 == self.nullDigest.GetHashSize())

        self.nullDigest.Initialize()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.nullDigest.TransformBytes(BytesZeroToNine[:4])

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(4 == self.nullDigest.GetHashSize())

        self.nullDigest.TransformBytes(BytesZeroToNine[4:])

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(10 == self.nullDigest.GetHashSize())

        Result = self.nullDigest.TransformFinal().GetBytes()

        self.assertTrue(0 == self.nullDigest.GetBlockSize())
        self.assertTrue(0 == self.nullDigest.GetHashSize())

        self.assertTrue(BytesZeroToNine == bytearray(Result))

    def test_TestHashCloneIsCorrect(self):
        nullDigest = HashLib4Python.PyNullDigestFactory.CreateNullDigest()

        self.HashCloneIsCorrectTestHelper(nullDigest)

    def test_TestHashCloneIsUnique(self):
        nullDigest = HashLib4Python.PyNullDigestFactory.CreateNullDigest()

        self.HashCloneIsUnique(nullDigest)

  
if __name__ ==  '__main__':
    unittest.main()
