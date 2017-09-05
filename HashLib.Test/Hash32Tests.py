from TestConstants import *
import unittest

class APTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "AAAAAAAA"
        self.ExpectedHashOfDefaultData = "7F14EFED"
        self.ExpectedHashOfOnetoNine = "C0E86BE5"
        self.ExpectedHashOfabcde = "7F6A697A"

        self.ap = HashFactory.PyHash32.CreateAP
        
    def test_TestBytesabcde(self):
        ActualString = self.ap(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ap(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ap("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ap(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ap(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class BernsteinTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "C4635F48"
        self.ExpectedHashOfOnetoNine = "35CDBB82"
        self.ExpectedHashOfabcde = "0F11B894"

        self.bernstein = HashFactory.PyHash32.CreateBernstein
        
    def test_TestBytesabcde(self):
        ActualString = self.bernstein(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bernstein(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bernstein("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bernstein(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bernstein(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class Bernstein1TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "2D122E48"
        self.ExpectedHashOfOnetoNine = "3BABEA14"
        self.ExpectedHashOfabcde = "0A1DEB04"

        self.bernstein1 = HashFactory.PyHash32.CreateBernstein1
        
    def test_TestBytesabcde(self):
        ActualString = self.bernstein1(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bernstein1(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bernstein1("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bernstein1(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bernstein1(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class BKDRTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "29E11B15"
        self.ExpectedHashOfOnetoNine = "DE43D6D5"
        self.ExpectedHashOfabcde = "B3EDEA13"

        self.bkdr = HashFactory.PyHash32.CreateBKDR
        
    def test_TestBytesabcde(self):
        ActualString = self.bkdr(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.bkdr(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.bkdr("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.bkdr(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.bkdr(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
 

class DEKTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "8E01E947"
        self.ExpectedHashOfOnetoNine = "AB4ACBA5"
        self.ExpectedHashOfabcde = "0C2080E5"

        self.dek = HashFactory.PyHash32.CreateDEK
        
    def test_TestBytesabcde(self):
        ActualString = self.dek(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.dek(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.dek("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.dek(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.dek(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
 

class DJBTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00001505"
        self.ExpectedHashOfDefaultData = "C4635F48"
        self.ExpectedHashOfOnetoNine = "35CDBB82"
        self.ExpectedHashOfabcde = "0F11B894"

        self.djb = HashFactory.PyHash32.CreateDJB
        
    def test_TestBytesabcde(self):
        ActualString = self.djb(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.djb(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.djb("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.djb(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.djb(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class ELFTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "01F5B2CC"
        self.ExpectedHashOfOnetoNine = "0678AEE9"
        self.ExpectedHashOfabcde = "006789A5"

        self.elf = HashFactory.PyHash32.CreateELF
        
    def test_TestBytesabcde(self):
        ActualString = self.elf(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.elf(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.elf("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.elf(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.elf(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class FNVTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "BE611EA3"
        self.ExpectedHashOfOnetoNine = "D8D70BF1"
        self.ExpectedHashOfabcde = "B2B39969"

        self.fnv = HashFactory.PyHash32.CreateFNV
        
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


class FNV1aTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "811C9DC5"
        self.ExpectedHashOfDefaultData = "1892F1F8"
        self.ExpectedHashOfOnetoNine = "BB86B11C"
        self.ExpectedHashOfabcde = "749BCF08"

        self.fnv1a = HashFactory.PyHash32.CreateFNV1a
        
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
        

class Jenkins3TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "F0F69CEF"
        self.ExpectedHashOfOnetoNine = "845D9A96"
        self.ExpectedHashOfabcde = "026D72DE"

        self.jenkins3 = HashFactory.PyHash32.CreateJenkins3
        
    def test_TestBytesabcde(self):
        ActualString = self.jenkins3(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.jenkins3(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.jenkins3("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.jenkins3(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.jenkins3(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class JSTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4E67C6A7"
        self.ExpectedHashOfDefaultData = "683AFCFE"
        self.ExpectedHashOfOnetoNine = "90A4224B"
        self.ExpectedHashOfabcde = "62E8C8B5"

        self.js = HashFactory.PyHash32.CreateJS
        
    def test_TestBytesabcde(self):
        ActualString = self.js(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.js(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.js("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.js(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.js(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class Murmur2TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "30512DE6"
        self.ExpectedHashOfOnetoNine = "DCCB0167"
        self.ExpectedHashOfabcde = "5F09A8DE"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "B15D52F0"

        self.murmur2 = HashFactory.PyHash32.CreateMurmur2
        
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


class MurmurHash3_x86_32TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "3D97B9EB"
        self.ExpectedHashOfRandomString = "A8D02B9A"
        self.ExpectedHashOfZerotoFour = "19D02170"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "514E28B7"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "B05606FE"

        self.murmurhash3_x86_32 = HashFactory.PyHash32.CreateMurmurHash3_x86_32
        
    def test_TestRandomString(self):
        ActualString = self.murmurhash3_x86_32(RandomStringRecord, 0)
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.murmurhash3_x86_32(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.murmurhash3_x86_32("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.murmurhash3_x86_32(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.murmurhash3_x86_32(ZerotoFour, 0)
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        ActualString = self.murmurhash3_x86_32(EmptyData, 0, 1)
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        ActualString = self.murmurhash3_x86_32(DefaultData, 0, MaxUInt32)
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


class OneAtTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "4E379A4F"
        self.ExpectedHashOfOnetoNine = "C66B58C5"
        self.ExpectedHashOfabcde = "B98559FC"

        self.oneattime = HashFactory.PyHash32.CreateOneAtTime
        
    def test_TestBytesabcde(self):
        ActualString = self.oneattime(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.oneattime(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.oneattime("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.oneattime(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.oneattime(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class PJWTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "01F5B2CC"
        self.ExpectedHashOfOnetoNine = "0678AEE9"
        self.ExpectedHashOfabcde = "006789A5"

        self.pjw = HashFactory.PyHash32.CreatePJW
        
    def test_TestBytesabcde(self):
        ActualString = self.pjw(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.pjw(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.pjw("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.pjw(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.pjw(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
  

class RotatingTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "158009D3"
        self.ExpectedHashOfOnetoNine = "1076548B"
        self.ExpectedHashOfabcde = "00674525"

        self.rotating = HashFactory.PyHash32.CreateRotating
        
    def test_TestBytesabcde(self):
        ActualString = self.rotating(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.rotating(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.rotating("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.rotating(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.rotating(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class RSTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "9EF98E63"
        self.ExpectedHashOfOnetoNine = "704952E9"
        self.ExpectedHashOfabcde = "A4A13F5D"

        self.rs = HashFactory.PyHash32.CreateRS
        
    def test_TestBytesabcde(self):
        ActualString = self.rs(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.rs(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.rs("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.rs(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.rs(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class SDBMTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "3001A5C9"
        self.ExpectedHashOfOnetoNine = "68A07035"
        self.ExpectedHashOfabcde = "BD500063"

        self.sdbm = HashFactory.PyHash32.CreateSDBM
        
    def test_TestBytesabcde(self):
        ActualString = self.sdbm(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sdbm(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sdbm("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sdbm(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sdbm(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class ShiftAndXorTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "BD0A7DA4"
        self.ExpectedHashOfOnetoNine = "E164F745"
        self.ExpectedHashOfabcde = "0731B823"

        self.shiftandxor = HashFactory.PyHash32.CreateShiftAndXor
        
    def test_TestBytesabcde(self):
        ActualString = self.shiftandxor(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.shiftandxor(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.shiftandxor("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.shiftandxor(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.shiftandxor(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class SuperFastTestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000000"
        self.ExpectedHashOfDefaultData = "F00EB3C0"
        self.ExpectedHashOfOnetoNine = "9575A2E9"
        self.ExpectedHashOfabcde = "51ED072E"

        self.superfast = HashFactory.PyHash32.CreateSuperFast
        
    def test_TestBytesabcde(self):
        ActualString = self.superfast(Bytesabcde, 0)
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.superfast(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.superfast("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.superfast(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.superfast(OnetoNine, 0)
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class XXHash32TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "02CC5D05"
        self.ExpectedHashOfDefaultData = "6A1C7A99"
        self.ExpectedHashOfRandomString = "CE8CF448"
        self.ExpectedHashOfZerotoFour = "8AA3B71C"
        self.ExpectedHashOfEmptyDataWithOneAsKey = "0B2CB792"
        self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey = "728C6772"

        self.xxhash32 = HashFactory.PyHash32.CreateXXHash32
        
    def test_TestDefaultData(self):
        ActualString = self.xxhash32(DefaultData, 0)
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.xxhash32("EmptyFile.txt", 1)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.xxhash32(EmptyData, 0)
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestRandomString(self):
        ActualString = self.xxhash32(RandomStringTobacco, 0)
        self.assertTrue(self.ExpectedHashOfRandomString == ActualString)

    def test_TestZerotoFour(self):
        ActualString = self.xxhash32(ZerotoFour, 0)
        self.assertTrue(self.ExpectedHashOfZerotoFour == ActualString)

    def test_TestWithDifferentKeyOneEmptyString(self):
        ActualString = self.xxhash32(EmptyData, 0, 1)
        self.assertTrue(self.ExpectedHashOfEmptyDataWithOneAsKey == ActualString)

    def test_TestWithDifferentKeyMaxUInt32DefaultData(self):
        ActualString = self.xxhash32(DefaultData, 0, MaxUInt32)
        self.assertTrue(self.ExpectedHashOfDefaultDataWithMaxUInt32AsKey == ActualString)


if __name__ ==  '__main__':
    unittest.main()
