from TestConstants import *
import unittest

checkValues = {HashLib4Python.PyCRCStandard._CRC3_GSM: 0x4,
               HashLib4Python.PyCRCStandard._CRC3_ROHC: 0x6,
               HashLib4Python.PyCRCStandard._CRC4_INTERLAKEN: 0xB,
               HashLib4Python.PyCRCStandard._CRC4_ITU: 0x7,
               HashLib4Python.PyCRCStandard._CRC5_EPC: 0x00,
               HashLib4Python.PyCRCStandard._CRC5_ITU: 0x07,
               HashLib4Python.PyCRCStandard._CRC5_USB: 0x19,
               HashLib4Python.PyCRCStandard._CRC6_CDMA2000A: 0x0D,
               HashLib4Python.PyCRCStandard._CRC6_CDMA2000B: 0x3B,
               HashLib4Python.PyCRCStandard._CRC6_DARC: 0x26,
               HashLib4Python.PyCRCStandard._CRC6_GSM: 0x13,
               HashLib4Python.PyCRCStandard._CRC6_ITU: 0x06,
               HashLib4Python.PyCRCStandard._CRC7: 0x75,
               HashLib4Python.PyCRCStandard._CRC7_ROHC: 0x53,
               HashLib4Python.PyCRCStandard._CRC7_UMTS: 0x61,
               HashLib4Python.PyCRCStandard._CRC8: 0xF4,
               HashLib4Python.PyCRCStandard._CRC8_AUTOSAR: 0xDF,
               HashLib4Python.PyCRCStandard._CRC8_BLUETOOTH: 0x26,
               HashLib4Python.PyCRCStandard._CRC8_CDMA2000: 0xDA,
               HashLib4Python.PyCRCStandard._CRC8_DARC: 0x15,
               HashLib4Python.PyCRCStandard._CRC8_DVBS2: 0xBC,
               HashLib4Python.PyCRCStandard._CRC8_EBU: 0x97,
               HashLib4Python.PyCRCStandard._CRC8_GSMA: 0x37,
               HashLib4Python.PyCRCStandard._CRC8_GSMB: 0x94,
               HashLib4Python.PyCRCStandard._CRC8_ICODE: 0x7E,
               HashLib4Python.PyCRCStandard._CRC8_ITU: 0xA1,
               HashLib4Python.PyCRCStandard._CRC8_LTE: 0xEA,
               HashLib4Python.PyCRCStandard._CRC8_MAXIM: 0xA1,
               HashLib4Python.PyCRCStandard._CRC8_OPENSAFETY: 0x3E,
               HashLib4Python.PyCRCStandard._CRC8_ROHC: 0xD0,
               HashLib4Python.PyCRCStandard._CRC8_SAEJ1850: 0x4B,
               HashLib4Python.PyCRCStandard._CRC8_WCDMA: 0x25,
               HashLib4Python.PyCRCStandard._CRC10: 0x199,
               HashLib4Python.PyCRCStandard._CRC10_CDMA2000: 0x233,
               HashLib4Python.PyCRCStandard._CRC10_GSM: 0x12A,
               HashLib4Python.PyCRCStandard._CRC11: 0x5A3,
               HashLib4Python.PyCRCStandard._CRC11_UMTS: 0x061,
               HashLib4Python.PyCRCStandard._CRC12_CDMA2000: 0xD4D,
               HashLib4Python.PyCRCStandard._CRC12_DECT: 0xF5B,
               HashLib4Python.PyCRCStandard._CRC12_GSM: 0xB34,
               HashLib4Python.PyCRCStandard._CRC12_UMTS: 0xDAF,
               HashLib4Python.PyCRCStandard._CRC13_BBC: 0x04FA,
               HashLib4Python.PyCRCStandard._CRC14_DARC: 0x082D,
               HashLib4Python.PyCRCStandard._CRC14_GSM: 0x30AE,
               HashLib4Python.PyCRCStandard._CRC15: 0x059E,
               HashLib4Python.PyCRCStandard._CRC15_MPT1327: 0x2566,
               HashLib4Python.PyCRCStandard._ARC: 0xBB3D,
               HashLib4Python.PyCRCStandard._CRC16_AUGCCITT: 0xE5CC,
               HashLib4Python.PyCRCStandard._CRC16_BUYPASS: 0xFEE8,
               HashLib4Python.PyCRCStandard._CRC16_CCITTFALSE: 0x29B1,
               HashLib4Python.PyCRCStandard._CRC16_CDMA2000: 0x4C06,
               HashLib4Python.PyCRCStandard._CRC16_CMS: 0xAEE7,
               HashLib4Python.PyCRCStandard._CRC16_DDS110: 0x9ECF,
               HashLib4Python.PyCRCStandard._CRC16_DECTR: 0x007E,
               HashLib4Python.PyCRCStandard._CRC16_DECTX: 0x007F,
               HashLib4Python.PyCRCStandard._CRC16_DNP: 0xEA82,
               HashLib4Python.PyCRCStandard._CRC16_EN13757: 0xC2B7,
               HashLib4Python.PyCRCStandard._CRC16_GENIBUS: 0xD64E,
               HashLib4Python.PyCRCStandard._CRC16_GSM: 0xCE3C,
               HashLib4Python.PyCRCStandard._CRC16_LJ1200: 0xBDF4,
               HashLib4Python.PyCRCStandard._CRC16_MAXIM: 0x44C2,
               HashLib4Python.PyCRCStandard._CRC16_MCRF4XX: 0x6F91,
               HashLib4Python.PyCRCStandard._CRC16_OPENSAFETYA: 0x5D38,
               HashLib4Python.PyCRCStandard._CRC16_OPENSAFETYB: 0x20FE,
               HashLib4Python.PyCRCStandard._CRC16_PROFIBUS: 0xA819,
               HashLib4Python.PyCRCStandard._CRC16_RIELLO: 0x63D0,
               HashLib4Python.PyCRCStandard._CRC16_T10DIF: 0xD0DB,
               HashLib4Python.PyCRCStandard._CRC16_TELEDISK: 0x0FB3,
               HashLib4Python.PyCRCStandard._CRC16_TMS37157: 0x26B1,
               HashLib4Python.PyCRCStandard._CRC16_USB: 0xB4C8,
               HashLib4Python.PyCRCStandard._CRCA: 0xBF05,
               HashLib4Python.PyCRCStandard._KERMIT: 0x2189,
               HashLib4Python.PyCRCStandard._MODBUS: 0x4B37,
               HashLib4Python.PyCRCStandard._X25: 0x906E,
               HashLib4Python.PyCRCStandard._XMODEM: 0x31C3,
               HashLib4Python.PyCRCStandard._CRC17_CANFD: 0x04F03,
               HashLib4Python.PyCRCStandard._CRC21_CANFD: 0x0ED841,
               HashLib4Python.PyCRCStandard._CRC24: 0x21CF02,
               HashLib4Python.PyCRCStandard._CRC24_BLE: 0xC25A56,
               HashLib4Python.PyCRCStandard._CRC24_FLEXRAYA: 0x7979BD,
               HashLib4Python.PyCRCStandard._CRC24_FLEXRAYB: 0x1F23B8,
               HashLib4Python.PyCRCStandard._CRC24_INTERLAKEN: 0xB4F3E6,
               HashLib4Python.PyCRCStandard._CRC24_LTEA: 0xCDE703,
               HashLib4Python.PyCRCStandard._CRC24_LTEB: 0x23EF52,
               HashLib4Python.PyCRCStandard._CRC30_CDMA: 0x04C34ABF,
               HashLib4Python.PyCRCStandard._CRC31_PHILIPS: 0x0CE9E46C,
               HashLib4Python.PyCRCStandard._CRC32: 0xCBF43926,
               HashLib4Python.PyCRCStandard._CRC32_AUTOSAR: 0x1697D06A,
               HashLib4Python.PyCRCStandard._CRC32_BZIP2: 0xFC891918,
               HashLib4Python.PyCRCStandard._CRC32C: 0xE3069283,
               HashLib4Python.PyCRCStandard._CRC32D: 0x87315576,
               HashLib4Python.PyCRCStandard._CRC32_MPEG2: 0x0376E6E7,
               HashLib4Python.PyCRCStandard._CRC32_POSIX: 0x0376E6E7,
               HashLib4Python.PyCRCStandard._CRC32Q: 0x3010BF7F,
               HashLib4Python.PyCRCStandard._JAMCRC: 0x340BC6D9,
               HashLib4Python.PyCRCStandard._XFER: 0xBD0BE338,
               HashLib4Python.PyCRCStandard._CRC40_GSM: 0xD4164FC646,
               HashLib4Python.PyCRCStandard._CRC64: 0x6C40DF5F0B497347,
               HashLib4Python.PyCRCStandard._CRC64_GOISO: 0xB90956C775A41001,
               HashLib4Python.PyCRCStandard._CRC64_WE: 0x62EC59E3F1A4F00A,
               HashLib4Python.PyCRCStandard._CRC64_XZ: 0x995DC9BBDF1939FA
               }
		
class Adler32TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "00000001"
        self.ExpectedHashOfDefaultData = "25D40524"
        self.ExpectedHashOfOnetoNine = "091E01DE"
        self.ExpectedHashOfabcde = "05C801F0"

        self.adler = HashLib4Python.PyChecksum.CreateAdler32()
        
    def test_TestBytesabcde(self):
        ActualString = self.adler.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.adler.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.adler.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.adler.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.adler.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


class CRCTestCase(unittest.TestCase):
    def test_TestCheckValue(self):
        for i in range(101):
            crc = HashLib4Python.PyChecksum.CreateCRC(i)
            ActualString = crc.ComputeString(OnetoNine).ToString()
            ExpectedInt = checkValues[i]
            self.assertTrue(ExpectedInt == int(ActualString, 16))
    
  
if __name__ ==  '__main__':
    unittest.main()
