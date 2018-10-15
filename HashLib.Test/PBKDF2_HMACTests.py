from TestConstants import *
import unittest

class PBKDF2_HMACSHA1TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedString = "BFDE6BE94DF7E11DD409BCE20A0255EC327CB936FFE93643";
        self.Password = bytearray([0x70, 0x61, 0x73, 0x73, 0x77, 0x6F, 0x72, 0x64])
        self.Salt = bytearray([0x78, 0x57, 0x8E, 0x5A, 0x5D, 0x63, 0xCB, 0x06])

        self.hash = HashLib4Python.PyCrypto.CreateSHA1()
        
    def test_TestOne(self):
        pbkdf = HashLib4Python.PyPBKDF2_HMAC.CreatePBKDF2_HMAC(self.hash,
                                                               self.Password,
                                                               self.Salt,
                                                               2048)
        ActualString = HashLib4Python.PyConverters.ConvertBytesToHexString(
                        pbkdf.GetBytes(24)
                        )
        self.assertTrue(self.ExpectedString == ActualString)


class PBKDF2_HMACSHA2_256TestCase(unittest.TestCase):
    def setUp(self):
        self.ExpectedString = "0394A2EDE332C9A13EB82E9B24631604C31DF978B4E2F0FBD2C549944F9D79A5";
        self.Password = bytearray("password")
        self.Salt = bytearray("salt")

        self.hash = HashLib4Python.PyCrypto.CreateSHA2_256()
        
    def test_TestOne(self):
        pbkdf = HashLib4Python.PyPBKDF2_HMAC.CreatePBKDF2_HMAC(self.hash,
                                                               self.Password,
                                                               self.Salt,
                                                               100000)
        
        ActualString = HashLib4Python.PyConverters.ConvertBytesToHexString(
                        pbkdf.GetBytes(32)
                        )
        self.assertTrue(self.ExpectedString == ActualString)


if __name__ ==  '__main__':
    unittest.main()

    
