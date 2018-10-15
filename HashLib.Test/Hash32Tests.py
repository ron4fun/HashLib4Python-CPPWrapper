from TestConstants import *
import unittest

class APTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "AAAAAAAA"
        self.ExpectedHashOfDefaultData = "7F14EFED"
        self.ExpectedHashOfOnetoNine = "C0E86BE5"
        self.ExpectedHashOfabcde = "7F6A697A"

        self.ap = HashLib4Python.PyHash32.CreateAP()
        
    def test_TestBytesabcde(self):
        ActualString = self.ap.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ap.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ap.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ap.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ap.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class BernsteinTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "C4635F48"
        self.ExpectedHashOfOnetoNine = "35CDBB82"
        self.ExpectedHashOfabcde = "0F11B894"

        self.bernstein = HashLib4Python.PyHash32.CreateBernstein()
        
    def test_TestBytesabcde(self):
        ActualString = self.bernstein.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bernstein.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bernstein.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bernstein.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bernstein.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class Bernstein1TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "2D122E48"
        self.ExpectedHashOfOnetoNine = "3BABEA14"
        self.ExpectedHashOfabcde = "0A1DEB04"

        self.bernstein1 = HashLib4Python.PyHash32.CreateBernstein1()
        
    def test_TestBytesabcde(self):
        ActualString = self.bernstein1.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bernstein1.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bernstein1.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bernstein1.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bernstein1.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class BKDRTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "29E11B15"
        self.ExpectedHashOfOnetoNine = "DE43D6D5"
        self.ExpectedHashOfabcde = "B3EDEA13"

        self.bkdr = HashLib4Python.PyHash32.CreateBKDR()
        
    def test_TestBytesabcde(self):
        ActualString = self.bkdr.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bkdr.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bkdr.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bkdr.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bkdr.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
 

class DEKTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "8E01E947"
        self.ExpectedHashOfOnetoNine = "AB4ACBA5"
        self.ExpectedHashOfabcde = "0C2080E5"

        self.dek = HashLib4Python.PyHash32.CreateDEK()
        
    def test_TestBytesabcde(self):
        ActualString = self.dek.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.dek.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.dek.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.dek.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.dek.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
 

class DJBTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "C4635F48"
        self.ExpectedHashOfOnetoNine = "35CDBB82"
        self.ExpectedHashOfabcde = "0F11B894"

        self.djb = HashLib4Python.PyHash32.CreateDJB()
        
    def test_TestBytesabcde(self):
        ActualString = self.djb.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.djb.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.djb.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.djb.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.djb.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class ELFTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "01F5B2CC"
        self.ExpectedHashOfOnetoNine = "0678AEE9"
        self.ExpectedHashOfabcde = "006789A5"

        self.elf = HashLib4Python.PyHash32.CreateELF()
        
    def test_TestBytesabcde(self):
        ActualString = self.elf.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.elf.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.elf.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.elf.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.elf.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class FNVTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "BE611EA3"
        self.ExpectedHashOfOnetoNine = "D8D70BF1"
        self.ExpectedHashOfabcde = "B2B39969"

        self.fnv = HashLib4Python.PyHash32.CreateFNV()
        
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


class FNV1aTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "811C9DC5"
        self.ExpectedHashOfDefaultData = "1892F1F8"
        self.ExpectedHashOfOnetoNine = "BB86B11C"
        self.ExpectedHashOfabcde = "749BCF08"

        self.fnv1a = HashLib4Python.PyHash32.CreateFNV1a()
        
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
        

class Jenkins3TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "F0F69CEF"
        self.ExpectedHashOfOnetoNine = "845D9A96"
        self.ExpectedHashOfabcde = "026D72DE"

        self.jenkins3 = HashLib4Python.PyHash32.CreateJenkins3()
        
    def test_TestBytesabcde(self):
        ActualString = self.jenkins3.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.jenkins3.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.jenkins3.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.jenkins3.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.jenkins3.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class JSTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4E67C6A7"
        self.ExpectedHashOfDefaultData = "683AFCFE"
        self.ExpectedHashOfOnetoNine = "90A4224B"
        self.ExpectedHashOfabcde = "62E8C8B5"

        self.js = HashLib4Python.PyHash32.CreateJS()
        
    def test_TestBytesabcde(self):
        ActualString = self.js.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.js.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.js.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.js.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.js.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class Murmur2TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "30512DE6"
        self.ExpectedHashOfOnetoNine = "DCCB0167"
        self.ExpectedHashOfabcde = "5F09A8DE"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "B15D52F0"

        self.murmur2 = HashLib4Python.PyHash32.CreateMurmur2()
        
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
        Hash = HashLib4Python.PyHash32.CreateMurmur2()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


class MurmurHash3_x86_32TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "3D97B9EB"
        self.ExpectedHashOfRandomString = "A8D02B9A"
        self.ExpectedHashOfZerotoFour = "19D02170"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "514E28B7"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "B05606FE"

        self.murmurhash3_x86_32 = HashLib4Python.PyHash32.CreateMurmurHash3_x86_32()
        
    def test_TestRandomString(self):
        ActualString = self.murmurhash3_x86_32.ComputeString(RandomStringRecord).ToString()
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmurhash3_x86_32.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmurhash3_x86_32.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmurhash3_x86_32.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.murmurhash3_x86_32.ComputeString(ZerotoFour).ToString()
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        Hash = HashLib4Python.PyHash32.CreateMurmurHash3_x86_32()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    1)
                    )
        ActualString = Hash.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        Hash = HashLib4Python.PyHash32.CreateMurmurHash3_x86_32()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


class OneAtTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "4E379A4F"
        self.ExpectedHashOfOnetoNine = "C66B58C5"
        self.ExpectedHashOfabcde = "B98559FC"

        self.oneattime = HashLib4Python.PyHash32.CreateOneAtTime()
        
    def test_TestBytesabcde(self):
        ActualString = self.oneattime.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.oneattime.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.oneattime.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.oneattime.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.oneattime.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class PJWTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "01F5B2CC"
        self.ExpectedHashOfOnetoNine = "0678AEE9"
        self.ExpectedHashOfabcde = "006789A5"

        self.pjw = HashLib4Python.PyHash32.CreatePJW()
        
    def test_TestBytesabcde(self):
        ActualString = self.pjw.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.pjw.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.pjw.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.pjw.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.pjw.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class RotatingTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "158009D3"
        self.ExpectedHashOfOnetoNine = "1076548B"
        self.ExpectedHashOfabcde = "00674525"

        self.rotating = HashLib4Python.PyHash32.CreateRotating()
        
    def test_TestBytesabcde(self):
        ActualString = self.rotating.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.rotating.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.rotating.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.rotating.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.rotating.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class RSTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "9EF98E63"
        self.ExpectedHashOfOnetoNine = "704952E9"
        self.ExpectedHashOfabcde = "A4A13F5D"

        self.rs = HashLib4Python.PyHash32.CreateRS()
        
    def test_TestBytesabcde(self):
        ActualString = self.rs.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.rs.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.rs.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.rs.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.rs.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class SDBMTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "3001A5C9"
        self.ExpectedHashOfOnetoNine = "68A07035"
        self.ExpectedHashOfabcde = "BD500063"

        self.sdbm = HashLib4Python.PyHash32.CreateSDBM()
        
    def test_TestBytesabcde(self):
        ActualString = self.sdbm.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sdbm.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sdbm.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sdbm.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sdbm.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class ShiftAndXorTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "BD0A7DA4"
        self.ExpectedHashOfOnetoNine = "E164F745"
        self.ExpectedHashOfabcde = "0731B823"

        self.shiftandxor = HashLib4Python.PyHash32.CreateShiftAndXor()
        
    def test_TestBytesabcde(self):
        ActualString = self.shiftandxor.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.shiftandxor.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.shiftandxor.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.shiftandxor.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.shiftandxor.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class SuperFastTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "F00EB3C0"
        self.ExpectedHashOfOnetoNine = "9575A2E9"
        self.ExpectedHashOfabcde = "51ED072E"

        self.superfast = HashLib4Python.PyHash32.CreateSuperFast()
        
    def test_TestBytesabcde(self):
        ActualString = self.superfast.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.superfast.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.superfast.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.superfast.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.superfast.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class XXHash32TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "02CC5D05"
        self.ExpectedHashOfDefaultData = "6A1C7A99"
        self.ExpectedHashOfRandomString = "CE8CF448"
        self.ExpectedHashOfZerotoFour = "8AA3B71C"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "0B2CB792"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "728C6772"

        self.xxhash32 = HashLib4Python.PyHash32.CreateXXHash32()
        
    def test_TestDefaultData(self):
        ActualString = self.xxhash32.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.xxhash32.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.xxhash32.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestRandomString(self):
        ActualString = self.xxhash32.ComputeString(RandomStringTobacco).ToString()
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.xxhash32.ComputeString(ZerotoFour).ToString()
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        Hash = HashLib4Python.PyHash32.CreateXXHash32()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    1)
                    )
        ActualString = Hash.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        Hash = HashLib4Python.PyHash32.CreateXXHash32()
        Hash.SetKey(HashLib4Python.PyConverters.ReadUInt32AsBytesLE(
                    MaxUInt32)
                    )
        ActualString = Hash.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


if __name__ ==  '__main__':
    unittest.main()
