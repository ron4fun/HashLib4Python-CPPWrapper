from TestConstants import *
from Blake2BTestVectors import *
from Blake2STestVectors import *


class GostTestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "CE85B99CC46752FFFEE35CAB9A7B0278ABB4C2D2055CFF685AF4912C49490F8D"
        self.ExpectedHashOfDefaultData = "21DCCFBF20D313170333BA15596338FB5964267328EB42CA10E269B7045FF856"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "DE9D68F7793C829E7369AC09493A7749B2637A7B1D572A70549936E09F2D1D82"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "6E4E2895E194BEB0A083B1DED6C4084F5E7F37BAAB988D288D9707235F2F8294"
        self.ExpectedHashOfOnetoNine = "264B4E433DEE474AEC465FA9C725FE963BC4B4ABC4FDAC63B7F73B671663AFC9"
        self.ExpectedHashOfabcde = "B18CFD04F92DC1D83325036BC723D36DB25EDE41AE879D2545FC7F377B700899"

        self.gost = HashLib4Python.PyCrypto.CreateGost()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.gost)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.gost)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.gost.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.gost.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.gost.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.gost.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.gost.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGost()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGost()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGost()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGost()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateGost()

        self.HashCloneIsUnique(Hash)


class GOST3411_2012_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "3F539A213E97C802CC229D474C6AA32A825A360B2A933A949FD925208D9CE1BB"
        self.ExpectedHashOfQuickBrownFox = "3E7DEA7F2384B6C5A3D0E24AAA29C05E89DDD762145030EC22C71A6DB8B2C1F4"

        self.gost = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()
        
    def test_TestQuickBrownFox(self):
        ActualString = self.gost.ComputeString(QuickBrownDog).ToString()
        self.assertTrue(self.ExpectedHashOfQuickBrownFox == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.gost.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_256()

        self.HashCloneIsUnique(Hash)


class GOST3411_2012_512TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "8E945DA209AA869F0455928529BCAE4679E9873AB707B55315F56CEB98BEF0A7362F715528356EE83CDA5F2AAC4C6AD2BA3A715C1BCD81CB8E9F90BF4C1C1A8A"
        self.ExpectedHashOfQuickBrownFox = "D2B793A0BB6CB5904828B5B6DCFB443BB8F33EFC06AD09368878AE4CDC8245B97E60802469BED1E7C21A64FF0B179A6A1E0BB74D92965450A0ADAB69162C00FE"

        self.gost = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()
        
    def test_TestQuickBrownFox(self):
        ActualString = self.gost.ComputeString(QuickBrownDog).ToString()
        self.assertTrue(self.ExpectedHashOfQuickBrownFox == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.gost.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateGOST3411_2012_512()

        self.HashCloneIsUnique(Hash)

        
class Grindahl256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "45A7600159AF54AE110FCB6EA0F38AD57875EAC814F74D2CBC247D28C89923E6"
        self.ExpectedHashOfDefaultData = "AC72E90B0F3F5864A0AF3C43E2A73E393DEBF22AB81B6786ADE22B4517DAAAB6"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "02D964EE346B0C333CEC0F5D7E68C5CFAAC1E3CB0C06FE36418E17AA3AFCA2BE"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "65BA6F8EFA5B566D556EC8E3A2EC67DB7EE9BDEE663F17A8B8E7FAD067481023"
        self.ExpectedHashOfOnetoNine = "D2460846C5FE9E4750985CC9244D2458BEFD884435121FE56528022A3C7605B7"
        self.ExpectedHashOfabcde = "5CDA73422F36E41087795BB6C21D577BAAF114E4A6CCF33D919E700EE2489FE2"

        self.grindahl256 = HashLib4Python.PyCrypto.CreateGrindahl256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.grindahl256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.grindahl256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.grindahl256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.grindahl256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.grindahl256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.grindahl256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.grindahl256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl256()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl256()

        self.HashCloneIsUnique(Hash)

        
class Grindahl512TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "EE0BA85F90B6D232430BA43DD0EDD008462591816962A355602ED214FAAE54A9A4607D6F577CE950421FF58AEA53F51A7A9F5CCA894C3776104D43568FEA1207"
        self.ExpectedHashOfDefaultData = "540F3C6A5070DA391BBA7121DB8F8745752D3515164498FC82CB5B4D837632CF3F256D85C4A0B7F34A86936FAB07BDA2DF2BFDD59AFDBD901E1347C2001DB1AD"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "59A3F868AE1844BA9B683760D62C73E6E254BE6F46DF923F45118F32E9E1AB80A9056AA8A4792F0D6B8C709919C0ACC64EF64FC013C919758841AE6026F47E61"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "7F067A454A4F6300982CAE37900171C627992A75A5567E0D3A51BC6672F79C5AC0CEF5978E933B713F38494DDF26114994C47689AC93EEC9B8EF7892C3B24087"
        self.ExpectedHashOfOnetoNine = "6845F20B8A9DB083F307844506D342ED0FEE0D16BAF64B22E6C07552CB8C907E936FEDCD885B72C1B05813F722B5706C112AD59D3421CFD88CAA1CFB40EF1BEF"
        self.ExpectedHashOfabcde = "F282C47F31831EAB58B8EE9D1EEE3B9B5A6A86354EEFE84CA3176BED5AB447E6D5AC82316F2D6FAAD350848E2D418336A57772D96311DA8BC51C93087204C6A5"

        self.grindahl512 = HashLib4Python.PyCrypto.CreateGrindahl512()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.grindahl512)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.grindahl512)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.grindahl512.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.grindahl512.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.grindahl512.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.grindahl512.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.grindahl512.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)
        
    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl512()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl512()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl512()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl512()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateGrindahl512()

        self.HashCloneIsUnique(Hash)
        
class HAS160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "307964EF34151D37C8047ADEC7AB50F4FF89762D"
        self.ExpectedHashOfDefaultData = "2773EDAC4501514254D7B1DF091D6B7652250A52"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "7D2F0051F2BD817A4C27F126882353BCD300B7CA"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "53970A7AC510A85D0E22FF506FED5B57188A8B3F"
        self.ExpectedHashOfOnetoNine = "A0DA48CCD36C9D24AA630D4B3673525E9109A83C"
        self.ExpectedHashOfabcde = "EEEA94C2F0450B639BC2ACCAF4AEB172A5885313"

        self.has160 = HashLib4Python.PyCrypto.CreateHAS160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.has160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.has160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.has160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.has160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.has160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.has160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.has160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHAS160()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHAS160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHAS160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHAS160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHAS160()

        self.HashCloneIsUnique(Hash)
        

class Haval_3_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "C68F39913F901F3DDF44C707357A7D70"
        self.ExpectedHashOfDefaultData = "04AF7562BA75D5767ADE2A71E4BE33DE"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "E5639CDBE9AE8B58DEC50065909624D4"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "9D49ED7B5D42C64F590A164C5D1AAE9F"
        self.ExpectedHashOfOnetoNine = "F2F92D4E5CA6B92A5B5FC5AC822C39D2"
        self.ExpectedHashOfabcde = "51D4032478AA59182916E6C111FA79A6"

        self.haval_3_128 = HashLib4Python.PyCrypto.CreateHaval_3_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_3_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_3_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_3_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_3_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_3_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_128()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_128()

        self.HashCloneIsUnique(Hash)


class Haval_4_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "EE6BBF4D6A46A679B3A856C88538BB98"
        self.ExpectedHashOfDefaultData = "C815192C498CF266D0EB32E90D60892E"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "37A443E8FB7DE00C28BCE8D3F47BECE8"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "9A0B60DEB9F9FBB2A9DAD87A8C653E72"
        self.ExpectedHashOfOnetoNine = "52DFE2F3DA02591061B02DBDC1510F1C"
        self.ExpectedHashOfabcde = "61634059D9B8336FEB32CA27533ED284"

        self.haval_4_128 = HashLib4Python.PyCrypto.CreateHaval_4_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_4_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_4_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_4_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_4_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_4_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_128()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_128()

        self.HashCloneIsUnique(Hash)
        

class Haval_5_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "184B8482A0C050DCA54B59C7F05BF5DD"
        self.ExpectedHashOfDefaultData = "B335D2DC38EFB9D937B803F7581AF88D"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "AB287584D5D67B006986F039321FBA2F"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "1D5D93E71FF0B324C54ADD1FBDE1F4E4"
        self.ExpectedHashOfOnetoNine = "8AA1C1CA3A7E4F983654C4F689DE6F8D"
        self.ExpectedHashOfabcde = "11C0532F713332D45D6769376DD6EB3B"

        self.haval_5_128 = HashLib4Python.PyCrypto.CreateHaval_5_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_5_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_5_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_5_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_5_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_5_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_128()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_128()

        self.HashCloneIsUnique(Hash)

        
class Haval_3_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "D353C3AE22A25401D257643836D7231A9A95F953"
        self.ExpectedHashOfDefaultData = "4A5E28CA30029D2D04287E6C807E74D297A7FC74"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "B42F2273A6220C65B5ADAE1A9A1188B9D4398D2A"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "E686A2E785EA222FA28911D9243567EB72362D3C"
        self.ExpectedHashOfOnetoNine = "39A83AF3293CDAC04DE1DF3D0BE7A1F9D8AAB923"
        self.ExpectedHashOfabcde = "8D7C2218BDD8CB0608BA2479751B44BB15F1FC1F"

        self.haval_3_160 = HashLib4Python.PyCrypto.CreateHaval_3_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_3_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_3_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_3_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_3_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_3_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_160()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_160()

        self.HashCloneIsUnique(Hash)
        
class Haval_4_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "1D33AAE1BE4146DBAACA0B6E70D7A11F10801525"
        self.ExpectedHashOfDefaultData = "9E86A9E2D964CCF9019593C88F40AA5C725E0912"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "E7969DB764172896F2467CF74F62BBE231E2772D"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "6FEAC0105DA74AEDC8FA76A1CF0848C8CA94BA28"
        self.ExpectedHashOfOnetoNine = "B03439BE6F2A3EBED93AC86846D029D76F62FD99"
        self.ExpectedHashOfabcde = "F74B326FE2CE8F5BA151B85B16E67B28FE71F131"

        self.haval_4_160 = HashLib4Python.PyCrypto.CreateHaval_4_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_4_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_4_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_4_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_4_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_4_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_160()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_160()

        self.HashCloneIsUnique(Hash)

        
class Haval_5_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "255158CFC1EED1A7BE7C55DDD64D9790415B933B"
        self.ExpectedHashOfDefaultData = "A9AB9AB152BB4413B717228C3A65E75644542A35"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "EF034569FB10312F89F3FC09DDD9AA5C783A7E21"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "A0FFFE2DE177281E64C5D0A9DC81BFFDF14F6031"
        self.ExpectedHashOfOnetoNine = "11F592B3A1A1A9C0F9C638C33B69E442D06C1D99"
        self.ExpectedHashOfabcde = "53734616DD6761E2A1D2BD520035287972625385"

        self.haval_5_160 = HashLib4Python.PyCrypto.CreateHaval_5_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_5_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_5_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_5_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_5_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_5_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_160()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_160()

        self.HashCloneIsUnique(Hash)

        
class Haval_3_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "E9C48D7903EAF2A91C5B350151EFCB175C0FC82DE2289A4E"
        self.ExpectedHashOfDefaultData = "4235822851EB1B63D6B1DB56CF18EBD28E0BC2327416D5D1"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "AE216E5FA60AE76305DA19EE908FA0531FFE52BCC6A2AB5F"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "3E72C9200EAA6ED8D2EF60B8773BAF147A94E98A1FF4E70B"
        self.ExpectedHashOfOnetoNine = "6B92F078E73AF2E0F9F049FAA5016D32173A3D62D2F08554"
        self.ExpectedHashOfabcde = "4A106D88931B60DF1BA352782141C473E79019022D65D7A5"

        self.haval_3_192 = HashLib4Python.PyCrypto.CreateHaval_3_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_3_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_3_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_3_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_3_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_3_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_192()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_192()

        self.HashCloneIsUnique(Hash)

        
class Haval_4_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4A8372945AFA55C7DEAD800311272523CA19D42EA47B72DA"
        self.ExpectedHashOfDefaultData = "54D4FD0DE4228D55F826B627A128A765378B1DC1F8E6CD75"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "F5C16DFD598655201E6C636B363484FFAED4CCA27F3366A1"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "8AB3C2ED5E17CC15EE9D0740185BFFC53C054BC71B9A44AA"
        self.ExpectedHashOfOnetoNine = "A5C285EAD0FF2F47C15C27B991C4A3A5007BA57137B18D07"
        self.ExpectedHashOfabcde = "88A58D9011CA363A3F3CD113FFEAA44870C07CC14E94FB1B"

        self.haval_4_192 = HashLib4Python.PyCrypto.CreateHaval_4_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_4_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_4_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_4_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_4_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_4_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_192()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_192()

        self.HashCloneIsUnique(Hash)
        
        
class Haval_5_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4839D0626F95935E17EE2FC4509387BBE2CC46CB382FFE85"
        self.ExpectedHashOfDefaultData = "ED197F026B20DB6362CBC62BDD28E0B34F1E287966D84E3B"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "C28A804383403F608CB4A6473BCAF744CF25E62AF28C5934"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "AB2C407C403A82EEADF2A0B3F4B66B34A12322159E7A95B6"
        self.ExpectedHashOfOnetoNine = "EC32312AA79775539675C9BA83D079FFC7EA498FA6173A46"
        self.ExpectedHashOfabcde = "CDDF16E273A09E9E2F1D7D4761C2D35E1DD6EE327F1F5AFD"

        self.haval_5_192 = HashLib4Python.PyCrypto.CreateHaval_5_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_5_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_5_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_5_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_5_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_5_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_192()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_192()

        self.HashCloneIsUnique(Hash)

        
class Haval_3_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "C5AAE9D47BFFCAAF84A8C6E7CCACD60A0DD1932BE7B1A192B9214B6D"
        self.ExpectedHashOfDefaultData = "12B7BFA1D36D0163E876A1474EB33CF5BC24C1BBBB181F28ACEE8D36"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "64F21A46C5B17F4AAD8C28F970428BAA00C4096132369A7E5C0B2F67"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "2C403CCE41533900919919CA9B8A637AEC0A1E1F7FA154F978592B6B"
        self.ExpectedHashOfOnetoNine = "28E8CC65356B43ACBED4DD70F11D0827F17C4442D323AAA0A0DE285F"
        self.ExpectedHashOfabcde = "177DA8770D5BF50E1B5D82DD60DF2635102D490D86F876E70F7A4080"

        self.haval_3_224 = HashLib4Python.PyCrypto.CreateHaval_3_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_3_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_3_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_3_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_3_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_3_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_224()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_224()

        self.HashCloneIsUnique(Hash)


class Haval_4_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "3E56243275B3B81561750550E36FCD676AD2F5DD9E15F2E89E6ED78E"
        self.ExpectedHashOfDefaultData = "DA7AB9D08D42C1819C04C7064891DB700DD05C960C3192CB615758B0"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "462C126C107ADA83089EB66168831EB6804BA6062EC8D049B9B47D2B"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "334328027BA2D8F218F8BF374853252D3150FA774D0CBD6F674AEFE0"
        self.ExpectedHashOfOnetoNine = "9A08D0CF1D52BB1AC22F6421CFB902E700C4C496B3E990F4606F577D"
        self.ExpectedHashOfabcde = "3EEF5DC9C3B3DE0F142DB08B89C21A1FDB1C64D7B169425DBA161190"

        self.haval_4_224 = HashLib4Python.PyCrypto.CreateHaval_4_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_4_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_4_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_4_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_4_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_4_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_224()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_224()

        self.HashCloneIsUnique(Hash)

        
class Haval_5_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4A0513C032754F5582A758D35917AC9ADF3854219B39E3AC77D1837E"
        self.ExpectedHashOfDefaultData = "D5FEA825ED7B8CBF23938425BAFDBEE9AD127A685EFCA4559BD54892"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "1DD7A2CF3F32F5C447F50D5A3F6B9C421B243E310C3C292581F95447"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "12B6415C63F4BBA34F0ADD23EEB74AC7EE8A07420D652BF619B9E9D1"
        self.ExpectedHashOfOnetoNine = "2EAADFB8007D9A4D8D7F21182C2913D569F801B44D0920D4CE8A01F0"
        self.ExpectedHashOfabcde = "D8CBE8D06DC58095EC0E69F1C1A4D4A90893AAE80401779CEB6646A9"

        self.haval_5_224 = HashLib4Python.PyCrypto.CreateHaval_5_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_5_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_5_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_5_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_5_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_5_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_224()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_224()

        self.HashCloneIsUnique(Hash)

        
class Haval_3_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4F6938531F0BC8991F62DA7BBD6F7DE3FAD44562B8C6F4EBF146D5B4E46F7C17"
        self.ExpectedHashOfDefaultData = "9AA25FF9D7559F108E01014C27EBEEA34E8D82BD1A6105D28A53791B74C4C024"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "A587C118D2A575F91A7D3986F0893A32F8DBE13218D4B3CDB93DD0B7566E5003"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "7E24B475617096B102F0F64572E297144B35683476D1768CB35C0E0A43A6BF8F"
        self.ExpectedHashOfOnetoNine = "63E8D0AEEC87738F1E820294CBDF7961CD2246B3620B4BAC81BE0B9827D612C7"
        self.ExpectedHashOfabcde = "3913AB70F6219EEFE10B202DE5991EFDBC4A808203BD60BBFBFC043383AE8F90"

        self.haval_3_256 = HashLib4Python.PyCrypto.CreateHaval_3_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_3_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_3_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_3_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_3_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_3_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_3_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_256()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_3_256()

        self.HashCloneIsUnique(Hash)



class Haval_4_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "C92B2E23091E80E375DADCE26982482D197B1A2521BE82DA819F8CA2C579B99B"
        self.ExpectedHashOfDefaultData = "B5E97F406CBD4C36CC549072713E733EE31A5F9F23DD6C5982D3A239A9B38434"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "ED5D88C730ED3EB103DDE96AD42DA60825A9B8B0D8BD2ED580EBF92B851B12E7"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "FD0122B375A581D3F06DB6EB992F9A3F46657091E427BB8BD247D835CC086437"
        self.ExpectedHashOfOnetoNine = "DDC95DF473DD169456484BEB4B04EDCA83A5572D9D7ECCD00092365AE4EF8D79"
        self.ExpectedHashOfabcde = "8F9B46785E52C6C48A0178EDC66D3C23C220D15E52C3C8A13E1CD45D21369193"

        self.haval_4_256 = HashLib4Python.PyCrypto.CreateHaval_4_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_4_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_4_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_4_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_4_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_4_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_4_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_256()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_4_256()

        self.HashCloneIsUnique(Hash)


class Haval_5_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "BE417BB4DD5CFB76C7126F4F8EEB1553A449039307B1A3CD451DBFDC0FBBE330"
        self.ExpectedHashOfDefaultData = "E5061D6F4F8645262C5C923F8E607CD77D69CE772E3DE559132B460309BFB516"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "267B5C9F0A093726E47541C8F1DEADD400AD9AEE0145A59FBD5A18BA2877101E"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "C702F985817A2596D7E0BB073D71DFEF72D77BD45599DD4F7E5D83A8EAF7268B"
        self.ExpectedHashOfOnetoNine = "77FD61460DB5F89DEFC9A9296FAB68A1730EA6C9C0037A9793DAC8492C0A953C"
        self.ExpectedHashOfabcde = "C464C9A669D5B43E4C34808114DCE4ECC732D1B71407E7F05468D0B15BFF7E30"

        self.haval_5_256 = HashLib4Python.PyCrypto.CreateHaval_5_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.haval_5_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.haval_5_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.haval_5_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.haval_5_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.haval_5_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.haval_5_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_256()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateHaval_5_256()

        self.HashCloneIsUnique(Hash)
        

class MD2TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "8350E5A3E24C153DF2275C9F80692773"
        self.ExpectedHashOfDefaultData = "DFBE28FF5A3C23CAA85BE5848F16524E"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "03D7546FEADF29A91CEB40290A27E081"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "C5F4625462CD5CF7723C19E8566F6790"
        self.ExpectedHashOfOnetoNine = "12BD4EFDD922B5C8C7B773F26EF4E35F"
        self.ExpectedHashOfabcde = "DFF9959487649F5C7AF5D0680A9A5D22"

        self.md2 = HashLib4Python.PyCrypto.CreateMD2()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md2)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md2)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.md2.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.md2.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.md2.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.md2.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.md2.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD2()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD2()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD2()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD2()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateMD2()

        self.HashCloneIsUnique(Hash)
        

class MD4TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "31D6CFE0D16AE931B73C59D7E0C089C0"
        self.ExpectedHashOfDefaultData = "A77EAB8C3432FD9DD1B87C3C5C2E9C3C"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "7E30F4DA95992DBA450E345641DE5CEC"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "BF21F9EC05E480EEDB12AF20181713E3"
        self.ExpectedHashOfOnetoNine = "2AE523785D0CAF4D2FB557C12016185C"
        self.ExpectedHashOfabcde = "9803F4A34E8EB14F96ADBA49064A0C41"

        self.md4 = HashLib4Python.PyCrypto.CreateMD4()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md4)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md4)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.md4.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.md4.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.md4.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.md4.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.md4.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD4()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD4()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD4()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD4()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateMD4()

        self.HashCloneIsUnique(Hash)

        
class MD5TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "D41D8CD98F00B204E9800998ECF8427E"
        self.ExpectedHashOfDefaultData = "462EC1E50C8F2D5C387682E98F9BC842"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "696D0706C43816B551D874B9B3E4B7E6"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "09F705F43799213192622CCA6DF68941"
        self.ExpectedHashOfOnetoNine = "25F9E794323B453885F5181F1B624D0B"
        self.ExpectedHashOfabcde = "AB56B4D92B40713ACC5AF89985D4B786"

        self.md5 = HashLib4Python.PyCrypto.CreateMD5()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md5)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.md5)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.md5.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.md5.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.md5.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.md5.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.md5.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestHMACCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD5()

        self.HMACCloneIsCorrect(Hash)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD5()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateMD5()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateMD5()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateMD5()

        self.HashCloneIsUnique(Hash)

        
class PanamaTestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "AA0CC954D757D7AC7779CA3342334CA471ABD47D5952AC91ED837ECD5B16922B"
        self.ExpectedHashOfDefaultData = "69A05A5A5DDB32F5589257458BBDD059FB30C4486C052D81029DDB2864E90813"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "93226A060B4A82D1D9FBEE6B78424F8E3E871BE7DA77A9D17D5C78D5F415E631"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "3C15C9B7CDC77470BC02CA96711B66FAA976AC2044F6F177ABCA93B1442EA376"
        self.ExpectedHashOfOnetoNine = "3C83D2C9109DE4D1FA64833683A7C280591A7CFD8516769EA879E56A4AD39B99"
        self.ExpectedHashOfabcde = "B064E5476A3F511105B75305FC2EC31578A6B200FB5084CF937C179F1C52A891"

        self.panama = HashLib4Python.PyCrypto.CreatePanama()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.panama)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.panama)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.panama.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.panama.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.panama.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.panama.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.panama.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreatePanama()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreatePanama()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreatePanama()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreatePanama()

        self.HashCloneIsUnique(Hash)


class RadioGatun32TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "F30028B54AFAB6B3E55355D277711109A19BEDA7091067E9A492FB5ED9F20117"
        self.ExpectedHashOfDefaultData = "17B20CF19B3FC84FD2FFE084F07D4CD4DBBC50E41048D8259EB963B0A7B9C784"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "CD48D590665EA2C066A0C26E2620D567C75090DE38045B88C53BFAE685D67886"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "72EB7D36180C1B1BBF88E062FEC7419DBB4849892623D332821C1B0D71D6D513"
        self.ExpectedHashOfOnetoNine = "D77629174F56D8451F73CBE80EC7A20EF2DD65C46A1480CD004CBAA96F3FA1FD"
        self.ExpectedHashOfabcde = "A593059B12513A1BD88A2D433F07B239BC14743AF0FF7294837B5DF756BF9C7A"

        self.radioGatun32 = HashLib4Python.PyCrypto.CreateRadioGatun32()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.radioGatun32)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.radioGatun32)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.radioGatun32.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.radioGatun32.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.radioGatun32.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.radioGatun32.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.radioGatun32.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun32()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun32()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun32()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun32()

        self.HashCloneIsUnique(Hash)

        
class RadioGatun64TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "64A9A7FA139905B57BDAB35D33AA216370D5EAE13E77BFCDD85513408311A584"
        self.ExpectedHashOfDefaultData = "43B3208CE2E6B23D985087A84BD583F713A9002280BF2785B1EE569B12C15054"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "B9CBBB9FE06144CF5E369BDBBCB2C76EBBE8904061C356BA9A06FE2D96E4037F"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "FA280F80C1323C32AACC7F1CAB3808FE2BB8880F901AE6F03BD14D6D1884B267"
        self.ExpectedHashOfOnetoNine = "76A565017A42B258F5C8C9D2D9FD4C7347947A659ED142FF61C1BEA592F103C5"
        self.ExpectedHashOfabcde = "36B4DD23A97424844662E882AD1DA1DBAD8CB435A57F380455393C9FF9DE9D37"

        self.radioGatun64 = HashLib4Python.PyCrypto.CreateRadioGatun64()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.radioGatun64)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.radioGatun64)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.radioGatun64.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.radioGatun64.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.radioGatun64.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.radioGatun64.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.radioGatun64.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun64()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun64()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun64()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRadioGatun64()

        self.HashCloneIsUnique(Hash)

        
class RIPEMDTestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "9F73AA9B372A9DACFB86A6108852E2D9"
        self.ExpectedHashOfDefaultData = "B3F629A9786744AA105A2C150869C236"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "B06D09CE5452ADEEADF468E00DAC5C8B"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "219ACFCF07BDB775FBA73DACE1E97E08"
        self.ExpectedHashOfOnetoNine = "C905B44C6429AD0A1934550037D4816F"
        self.ExpectedHashOfabcde = "68D2362617E85CF1BF7381DF14045DBB"

        self.ripemd = HashLib4Python.PyCrypto.CreateRIPEMD()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.ripemd.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ripemd.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ripemd.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ripemd.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ripemd.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD()

        self.HashCloneIsUnique(Hash)

        
class RIPEMD128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "CDF26213A150DC3ECB610F18F6B38B46"
        self.ExpectedHashOfDefaultData = "75891B00B2874EDCAF7002CA98264193"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "E93930A64EF6807C4D80EF30DF86AFA7"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "BA844D13A1215E20634A49D5599197EF"
        self.ExpectedHashOfOnetoNine = "1886DB8ACDCBFEAB1E7EE3780400536F"
        self.ExpectedHashOfabcde = "A0A954BE2A779BFB2129B72110C5782D"

        self.ripemd128 = HashLib4Python.PyCrypto.CreateRIPEMD128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.ripemd128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ripemd128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ripemd128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ripemd128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ripemd128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD128()

        self.HashCloneIsUnique(Hash)

        
class RIPEMD160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "9C1185A5C5E9FC54612808977EE8F548B2258D31"
        self.ExpectedHashOfDefaultData = "0B8EAC9A2EA1E267750CE639D83A84B92631462B"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "4C373970BDB829BE3B6E0B2D9F510E9C35C9B583"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "76D728D9BF39ED42E0C451A9526E3F0D929F067D"
        self.ExpectedHashOfOnetoNine = "D3D0379126C1E5E0BA70AD6E5E53FF6AEAB9F4FA"
        self.ExpectedHashOfabcde = "973398B6E6C6CFA6B5E6A5173F195CE3274BF828"

        self.ripemd160 = HashLib4Python.PyCrypto.CreateRIPEMD160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.ripemd160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ripemd160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ripemd160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ripemd160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ripemd160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD160()

        self.HashCloneIsUnique(Hash)

        
class RIPEMD256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "02BA4C4E5F8ECD1877FC52D64D30E37A2D9774FB1E5D026380AE0168E3C5522D"
        self.ExpectedHashOfDefaultData = "95EF1FFAB0EF6229F58CAE347426ADE3C412BCEB1057DAED0062BBDEE4BEACC6"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "F1149704222B7ABA1F9C14B0E9A67909C53605E07614CF8C47CB357083EA3A6B"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "D59B820A708FA31C39BD33BA88CB9A25516A3BA2BA99A74223FCE0EC0F9BFB1B"
        self.ExpectedHashOfOnetoNine = "6BE43FF65DD40EA4F2FF4AD58A7C1ACC7C8019137698945B16149EB95DF244B7"
        self.ExpectedHashOfabcde = "81D8B58A3110A9139B4DDECCB031409E8AF023067CF4C6F0B701DAB9ECC0EB4E"

        self.ripemd256 = HashLib4Python.PyCrypto.CreateRIPEMD256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.ripemd256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ripemd256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ripemd256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ripemd256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ripemd256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD256()

        self.HashCloneIsUnique(Hash)

        
class RIPEMD320TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "22D65D5661536CDC75C1FDF5C6DE7B41B9F27325EBC61E8557177D705A0EC880151C3A32A00899B8"
        self.ExpectedHashOfDefaultData = "004A1899CCA02BFD4055129304D55F364E35F033BB74B784AFC93F7268291D8AF84F2C64C5CCACD0"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "248D14ED08F0F49D175F4DC487A64B81F06D78077D1CF975BBE5D47627995990EBE45E6B7EDF9362"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "4D3DFCCB43E5A60611A850C2141086CB16752505BA12E1B7953EA8859CB1E1DF3A698562A46DB41C"
        self.ExpectedHashOfOnetoNine = "7E36771775A8D279475D4FD76B0C8E412B6AD085A0002475A148923CCFA5D71492E12FA88EEAF1A9"
        self.ExpectedHashOfabcde = "A94DC1BC825DB64E97718305CE36BFEF32CC5410A630999678BCD89CC38C424269012EC8C5A95830"

        self.ripemd320 = HashLib4Python.PyCrypto.CreateRIPEMD320()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd320)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.ripemd320)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.ripemd320.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.ripemd320.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.ripemd320.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.ripemd320.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.ripemd320.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD320()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD320()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD320()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateRIPEMD320()

        self.HashCloneIsUnique(Hash)

        
class SHA0TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "F96CEA198AD1DD5617AC084A3D92C6107708C0EF"
        self.ExpectedHashOfDefaultData = "C9CBBE593DE122CA36B13CC37FE2CA8D5606FEED"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "CDA87167A558311B9154F372F21A453030BBE16A"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "EAA73E85DCAC5BAD0A0E71C0695F901FC32DB38A"
        self.ExpectedHashOfOnetoNine = "F0360779D2AF6615F306BB534223CF762A92E988"
        self.ExpectedHashOfabcde = "D624E34951BB800F0ACAE773001DF8CFFE781BA8"

        self.sha0 = HashLib4Python.PyCrypto.CreateSHA0()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha0)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha0)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha0.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha0.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha0.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha0.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha0.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA0()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA0()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA0()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA0()

        self.HashCloneIsUnique(Hash)
        

class SHA1TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "DA39A3EE5E6B4B0D3255BFEF95601890AFD80709"
        self.ExpectedHashOfDefaultData = "C8389876E94C043C47BA4BFF3D359884071DC310"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "E70699720F4222E3A4A4474F14F13CBC3316D9B2"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "CD409025AA5F34ABDC660856463155B23C89B16A"
        self.ExpectedHashOfOnetoNine = "F7C3BC1D808E04732ADF679965CCC34CA7AE3441"
        self.ExpectedHashOfabcde = "03DE6C570BFE24BFC328CCD7CA46B76EADAF4334"

        self.sha1 = HashLib4Python.PyCrypto.CreateSHA1()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha1)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha1)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha1.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha1.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha1.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha1.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha1.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)


    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA1()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA1()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA1()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA1()

        self.HashCloneIsUnique(Hash)

        
class SHA2_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "D14A028C2A3A2BC9476102BB288234C415A2B01F828EA62AC5B3E42F"
        self.ExpectedHashOfDefaultData = "DF2B86ED008508F542443C4B1810AA5A0F5658692B808EEB1D0A2F7E"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "86855E59D8B09A3C7632D4E176C4B65C549255F417FEF9EEF2D4167D"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "EC47E83DB5DD735EBB7AA4A898460950B16A3A0FA48E4BB9184EA3D1"
        self.ExpectedHashOfOnetoNine = "9B3E61BF29F17C75572FAE2E86E17809A4513D07C8A18152ACF34521"
        self.ExpectedHashOfabcde = "BDD03D560993E675516BA5A50638B6531AC2AC3D5847C61916CFCED6"

        self.sha2_224 = HashLib4Python.PyCrypto.CreateSHA2_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_224()

        self.HashCloneIsUnique(Hash)

        
class SHA2_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
        self.ExpectedHashOfDefaultData = "BCF45544CB98DDAB731927F8760F81821489ED04C0792A4D254134887BEA9E38"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "BC05A7D3B13A4A67445C62389564D35B18F33A0C6408EC8DA0CB2506AE6E2D14"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "92678A1C746AAEAA1D3F0C9DAC4BCA73801D278B51C1F6861D49C9A2C1175687"
        self.ExpectedHashOfOnetoNine = "15E2B0D3C33891EBB0F1EF609EC419420C20E320CE94C65FBC8C3312448EB225"
        self.ExpectedHashOfabcde = "36BBE50ED96841D10443BCB670D6554F0A34B761BE67EC9C4A8AD2C0C44CA42C"

        self.sha2_256 = HashLib4Python.PyCrypto.CreateSHA2_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_256()

        self.HashCloneIsUnique(Hash)

        
class SHA2_384TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "38B060A751AC96384CD9327EB1B1E36A21FDB71114BE07434C0CC7BF63F6E1DA274EDEBFE76F65FBD51AD2F14898B95B"
        self.ExpectedHashOfDefaultData = "05D165ADA4A6F9F550CB6F9A0E00401E628B302FA5D7F3824361768758421F83102AC611B2710F5168579CFB11942869"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "162295D136DB47205EDF45BF8687E5599DFA80C6AE79D83C03E729C48D373E19638ADD5B5D603558234DF755404CCF9E"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "3D6DCED731DAF3599CC0971646C1A8B8CCC61650722F111A9EB26CE7B65189EB220EACB09152D9A09065099FE6C1FDC9"
        self.ExpectedHashOfOnetoNine = "EB455D56D2C1A69DE64E832011F3393D45F3FA31D6842F21AF92D2FE469C499DA5E3179847334A18479C8D1DEDEA1BE3"
        self.ExpectedHashOfabcde = "4C525CBEAC729EAF4B4665815BC5DB0C84FE6300068A727CF74E2813521565ABC0EC57A37EE4D8BE89D097C0D2AD52F0"

        self.sha2_384 = HashLib4Python.PyCrypto.CreateSHA2_384()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_384)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_384)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_384.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_384.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_384.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_384.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_384.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_384()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_384()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_384()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_384()

        self.HashCloneIsUnique(Hash)
        

class SHA2_512TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "CF83E1357EEFB8BDF1542850D66D8007D620E4050B5715DC83F4A921D36CE9CE47D0D13C5D85F2B0FF8318D2877EEC2F63B931BD47417A81A538327AF927DA3E"
        self.ExpectedHashOfDefaultData = "0A5DA12B113EBD3DEA4C51FD10AFECF1E2A8EE6C3848A0DD4407141ADDA04375068D85A1EEF980FAFF68DC3BF5B1B3FBA31344178042197B5180BD95530D61AC"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "FB795F2A85271149E6A6E2668AAF54DB5946DC669C1C8432BED856AEC9A1A461B5FC13FE8AE0861E6A8F53D711FDDF76AC60A5CCC8BA334325FDB9472A7A71F4"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "DEDFCEAD40225068527D0E53B7C892226E188891D939E21A0777A40EA2E29D7233638C178C879F26088A502A887674C01DF61EAF1635D707D114097ED1D0D762"
        self.ExpectedHashOfOnetoNine = "D9E6762DD1C8EAF6D61B3C6192FC408D4D6D5F1176D0C29169BC24E71C3F274AD27FCD5811B313D681F7E55EC02D73D499C95455B6B5BB503ACF574FBA8FFE85"
        self.ExpectedHashOfabcde = "878AE65A92E86CAC011A570D4C30A7EAEC442B85CE8ECA0C2952B5E3CC0628C2E79D889AD4D5C7C626986D452DD86374B6FFAA7CD8B67665BEF2289A5C70B0A1"

        self.sha2_512 = HashLib4Python.PyCrypto.CreateSHA2_512()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_512.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_512.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_512.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_512.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_512.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512()

        self.HashCloneIsUnique(Hash)

        
class SHA2_512_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "6ED0DD02806FA89E25DE060C19D3AC86CABB87D6A0DDD05C333B84F4"
        self.ExpectedHashOfDefaultData = "7A95749FB7F4489A45275556F5D905D28E1B637DCDD6537336AB6234"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "B932866547894977F6E4C61D137FFC2508C639BA6786F45AC64731C8"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "9BC318A84B90F7FF55C53E3F4B602EAD13BB579EB1794455B29562B4"
        self.ExpectedHashOfOnetoNine = "F2A68A474BCBEA375E9FC62EAAB7B81FEFBDA64BB1C72D72E7C27314"
        self.ExpectedHashOfabcde = "880E79BB0A1D2C9B7528D851EDB6B8342C58C831DE98123B432A4515"

        self.sha2_512_224 = HashLib4Python.PyCrypto.CreateSHA2_512_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_512_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_512_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_512_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_512_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_512_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_224()

        self.HashCloneIsUnique(Hash)

        
class SHA2_512_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "C672B8D1EF56ED28AB87C3622C5114069BDD3AD7B8F9737498D0C01ECEF0967A"
        self.ExpectedHashOfDefaultData = "E1792BAAAEBFC58E213D0BA628BF2FF22CBA10526075702F7C1727B76BEB107B"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "5EF407B913662BE3D98F5DA20D55C2A45D3F3E4FF771B2C2A482E35F6A757E71"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "1467239C9D47E1962905D03D7006170A04D05E4508BB47E30AD9481FBDA975FF"
        self.ExpectedHashOfOnetoNine = "1877345237853A31AD79E14C1FCB0DDCD3DF9973B61AF7F906E4B4D052CC9416"
        self.ExpectedHashOfabcde = "DE8322B46E78B67D4431997070703E9764E03A1237B896FD8B379ED4576E8363"

        self.sha2_512_256 = HashLib4Python.PyCrypto.CreateSHA2_512_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.sha2_512_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.sha2_512_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.sha2_512_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.sha2_512_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.sha2_512_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.sha2_512_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSHA2_512_256()

        self.HashCloneIsUnique(Hash)

        
class Snefru_8_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "8617F366566A011837F4FB4BA5BEDEA2B892F3ED8B894023D16AE344B2BE5881"
        self.ExpectedHashOfDefaultData = "230826DA59215F22AF36663491AECC4872F663722A5A7932428CB8196F7AF78D"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "EEE63DC493FCDAA2F826FFF81DB4BAC53CBBFD933BEA3B65C8BEBB576D921623"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "7E33D94C5A09B2E5F800417128BCF3EF2EDCB971884789A35AE4AA7F13A18147"
        self.ExpectedHashOfOnetoNine = "1C7DEDC33125AF7517970B97B635777FFBA8905D7A0B359776E3E683B115F992"
        self.ExpectedHashOfabcde = "8D2891FC6020D7DC93F7561C0CFDDE26426192B3E364A1F52B634482009DC8C8"

        self.snefru_8_256 = HashLib4Python.PyCrypto.CreateSnefru_8_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.snefru_8_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.snefru_8_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.snefru_8_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.snefru_8_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.snefru_8_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.snefru_8_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.snefru_8_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_256()

        self.HashCloneIsUnique(Hash)

        
class Snefru_8_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "8617F366566A011837F4FB4BA5BEDEA2"
        self.ExpectedHashOfDefaultData = "1EA32485C121D07D1BD22FC4EDCF554F"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "296DEC851C9F6A6C9E1FD42679CE3FD2"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "B7D06604FCA943939525BA82BA69706E"
        self.ExpectedHashOfOnetoNine = "486D27B1F5F4A20DEE14CC466EDA9069"
        self.ExpectedHashOfabcde = "ADD78FA0BEA8F6283FE5D011BE6BCA3B"

        self.snefru_8_128 = HashLib4Python.PyCrypto.CreateSnefru_8_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.snefru_8_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.snefru_8_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.snefru_8_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.snefru_8_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.snefru_8_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.snefru_8_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.snefru_8_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateSnefru_8_128()

        self.HashCloneIsUnique(Hash)

        
class Tiger_3_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "3293AC630C13F0245F92BBB1766E1616"
        self.ExpectedHashOfDefaultData = "C76C85CE853F6E9858B507DA64E33DA2"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "331B89BDEC8B418091A883C139B3F858"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "0FA849F65841F2E621E2C882BE7CF80F"
        self.ExpectedHashOfOnetoNine = "0672665140A491BB35040AA9943D769A"
        self.ExpectedHashOfabcde = "BFD4041233531F1EF1E9A66D7A0CEF76"

        self.tiger_3_128 = HashLib4Python.PyCrypto.CreateTiger_3_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_3_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_3_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_3_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_3_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_3_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_128()

        self.HashCloneIsUnique(Hash)

        
class Tiger_4_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "24CC78A7F6FF3546E7984E59695CA13D"
        self.ExpectedHashOfDefaultData = "42CAAEB3A7218E379A78E4F1F7FBADA4"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "5365F31B5077249CA8C0C11FB29E06C1"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "856B697CEB606B1DF42B475D0C5587B5"
        self.ExpectedHashOfOnetoNine = "D9902D13011BD217DE965A3BA709F5CE"
        self.ExpectedHashOfabcde = "7FD0E2FAEC50261EF48D3B87C554EE73"

        self.tiger_4_128 = HashLib4Python.PyCrypto.CreateTiger_4_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_4_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_4_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_4_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_4_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_4_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_128()

        self.HashCloneIsUnique(Hash)

        
class Tiger_5_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "E765EBE4C351724A1B99F96F2D7E62C9"
        self.ExpectedHashOfDefaultData = "D6B8DCEA252160A4CBBF6A57DA9ABA78"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "67B3B43D5CE62BE8B54805E315576F06"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "49D450EC293D5565CE82284FA52FDC51"
        self.ExpectedHashOfOnetoNine = "BCCCB6421B3EC291A062A33DFF21BA76"
        self.ExpectedHashOfabcde = "1AB49D19F3C93B6FF4AB536951E5A6D0"

        self.tiger_5_128 = HashLib4Python.PyCrypto.CreateTiger_5_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_5_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_5_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_5_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_5_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_5_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_128()

        self.HashCloneIsUnique(Hash)
        

class Tiger_3_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "3293AC630C13F0245F92BBB1766E16167A4E5849"
        self.ExpectedHashOfDefaultData = "C76C85CE853F6E9858B507DA64E33DA27DE49F86"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "6C256489CD5E62C9B9F236523B030A56CCDF5A8C"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "45AF6513756EB15B9504CE8212F3D43AE739E470"
        self.ExpectedHashOfOnetoNine = "0672665140A491BB35040AA9943D769A47BE83FE"
        self.ExpectedHashOfabcde = "BFD4041233531F1EF1E9A66D7A0CEF76A3E0FE75"

        self.tiger_3_160 = HashLib4Python.PyCrypto.CreateTiger_3_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_3_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_3_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_3_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_3_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_3_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger_4_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "24CC78A7F6FF3546E7984E59695CA13D804E0B68"
        self.ExpectedHashOfDefaultData = "42CAAEB3A7218E379A78E4F1F7FBADA432E1D4B6"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "FE4F2273571AD900BB6A2935AD9E4E53DE98B24B"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "E8E8B8EF52CF7866A4E0AEAE7DE79878D5564997"
        self.ExpectedHashOfOnetoNine = "D9902D13011BD217DE965A3BA709F5CE7E75ED2C"
        self.ExpectedHashOfabcde = "7FD0E2FAEC50261EF48D3B87C554EE739E8FBD98"

        self.tiger_4_160 = HashLib4Python.PyCrypto.CreateTiger_4_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_4_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_4_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_4_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_4_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_4_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger_5_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "E765EBE4C351724A1B99F96F2D7E62C9AACBE64C"
        self.ExpectedHashOfDefaultData = "D6B8DCEA252160A4CBBF6A57DA9ABA78E4564864"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "5ACE8DB66A68836ADAC0BD563D43C01E82181E32"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "5F403B5F7F9A341545F55265698DD77DB8D3D6D4"
        self.ExpectedHashOfOnetoNine = "BCCCB6421B3EC291A062A33DFF21BA764596C58E"
        self.ExpectedHashOfabcde = "1AB49D19F3C93B6FF4AB536951E5A6D05EF6394C"

        self.tiger_5_160 = HashLib4Python.PyCrypto.CreateTiger_5_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_5_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_5_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_5_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_5_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_5_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger_3_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "3293AC630C13F0245F92BBB1766E16167A4E58492DDE73F3"
        self.ExpectedHashOfDefaultData = "C76C85CE853F6E9858B507DA64E33DA27DE49F8601F6A830"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "E46789FA64BFEE51EE17C7D257B6DF892A39FA9A7BC65CF9"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "9B53DDED2647666E9C31CF0F93B3B83E9FF64DF4532F3DDC"
        self.ExpectedHashOfOnetoNine = "0672665140A491BB35040AA9943D769A47BE83FEF2126E50"
        self.ExpectedHashOfabcde = "BFD4041233531F1EF1E9A66D7A0CEF76A3E0FE756B36A7D7"

        self.tiger_3_192 = HashLib4Python.PyCrypto.CreateTiger_3_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_3_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_3_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_3_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_3_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_3_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_3_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_3_192()

        self.HashCloneIsUnique(Hash)

        
class Tiger_4_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "24CC78A7F6FF3546E7984E59695CA13D804E0B686E255194"
        self.ExpectedHashOfDefaultData = "42CAAEB3A7218E379A78E4F1F7FBADA432E1D4B6A41827B0"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "31C5440140BD657ECEBA5172E7853E526290060C1A6335D1"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "D1113A9110545D0F3C97BE1451A8FAED205B1F27B3D74560"
        self.ExpectedHashOfOnetoNine = "D9902D13011BD217DE965A3BA709F5CE7E75ED2CB791FEA6"
        self.ExpectedHashOfabcde = "7FD0E2FAEC50261EF48D3B87C554EE739E8FBD98F9A0B332"

        self.tiger_4_192 = HashLib4Python.PyCrypto.CreateTiger_4_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_4_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_4_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_4_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_4_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_4_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_4_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_4_192()

        self.HashCloneIsUnique(Hash)


class Tiger_5_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "E765EBE4C351724A1B99F96F2D7E62C9AACBE64C63B5BCA2"
        self.ExpectedHashOfDefaultData = "D6B8DCEA252160A4CBBF6A57DA9ABA78E45648645715E3CE"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "C8A09D6DB257C85B99051F3BC410F56C4D92EEBA311005DC"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "8D56E7164C246EAF4708AAEECFE4DD439F5B4396A54049A6"
        self.ExpectedHashOfOnetoNine = "BCCCB6421B3EC291A062A33DFF21BA764596C58E30854A92"
        self.ExpectedHashOfabcde = "1AB49D19F3C93B6FF4AB536951E5A6D05EF6394C3471A08F"

        self.tiger_5_192 = HashLib4Python.PyCrypto.CreateTiger_5_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger_5_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger_5_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger_5_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger_5_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger_5_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger_5_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger_5_192()

        self.HashCloneIsUnique(Hash)


class Tiger2_3_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4441BE75F6018773C206C22745374B92"
        self.ExpectedHashOfDefaultData = "DEB1924D290E3D5567792A8171BFC44F"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "9B3B854233FD1AFC80D17179039F6F7B"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "0393C69DD393D9E15C723DFAE88C3059"
        self.ExpectedHashOfOnetoNine = "82FAF69673762B9FD8A0C902BDB395C1"
        self.ExpectedHashOfabcde = "E1F0DAC9E852ECF1270FB691C35506D4"

        self.tiger2_3_128 = HashLib4Python.PyCrypto.CreateTiger2_3_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_3_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_3_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_3_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_3_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_3_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_128()

        self.HashCloneIsUnique(Hash)


class Tiger2_4_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "6A7201A47AAC2065913811175553489A"
        self.ExpectedHashOfDefaultData = "22EE5BFE174B8C1C23361306C3E8F32C"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "787FFD7B098895A03139CBEBA0FBCCE8"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "A24C1DD76CACA54D3CB2BDDE5E40D84E"
        self.ExpectedHashOfOnetoNine = "75B7D71ACD40FE5B5D3263C1F68F4CF5"
        self.ExpectedHashOfabcde = "9FBB0FBF818C0302890CE373559D2370"

        self.tiger2_4_128 = HashLib4Python.PyCrypto.CreateTiger2_4_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_4_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_4_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_4_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_4_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_4_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_128()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_5_128TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "61C657CC0C3C147ED90779B36A1E811F"
        self.ExpectedHashOfDefaultData = "7F71F95B346733E7022D4B85BDA9C51E"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "B0D4AAA0A3239A5B242979DBE02C3373"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "F545BB88FBE3E5FB85E6DE063D081B66"
        self.ExpectedHashOfOnetoNine = "F720446C9BFDC8479D9FA53BC8B9144F"
        self.ExpectedHashOfabcde = "14F45FAC4BE0302E740CCC6FE99D75A6"

        self.tiger2_5_128 = HashLib4Python.PyCrypto.CreateTiger2_5_128()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_128)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_128)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_5_128.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_5_128.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_5_128.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_5_128.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_5_128.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_128()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_128()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_128()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_128()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_3_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4441BE75F6018773C206C22745374B924AA8313F"
        self.ExpectedHashOfDefaultData = "DEB1924D290E3D5567792A8171BFC44F70B5CD13"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "74B33C922DD679DC7144EF9F6BE807A8F1C370FE"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "71028DCDC197492195110EA5CFF6B3E04912FF25"
        self.ExpectedHashOfOnetoNine = "82FAF69673762B9FD8A0C902BDB395C12B0CBDDC"
        self.ExpectedHashOfabcde = "E1F0DAC9E852ECF1270FB691C35506D4BEDB12A0"

        self.tiger2_3_160 = HashLib4Python.PyCrypto.CreateTiger2_3_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_3_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_3_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_3_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_3_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_3_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_4_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "6A7201A47AAC2065913811175553489ADD0F8B99"
        self.ExpectedHashOfDefaultData = "22EE5BFE174B8C1C23361306C3E8F32C92075577"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "4C7CE724E7021DF3B53FA997C49E07E4DF9EA0F7"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "283A6ED11043AAA947A12843DC5C4B16283BE633"
        self.ExpectedHashOfOnetoNine = "75B7D71ACD40FE5B5D3263C1F68F4CF5A5DA963B"
        self.ExpectedHashOfabcde = "9FBB0FBF818C0302890CE373559D23702D87C69B"

        self.tiger2_4_160 = HashLib4Python.PyCrypto.CreateTiger2_4_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_4_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_4_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_4_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_4_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_4_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_5_160TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "61C657CC0C3C147ED90779B36A1E811F1D27F406"
        self.ExpectedHashOfDefaultData = "7F71F95B346733E7022D4B85BDA9C51E904825F7"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "89CFB85851EA674DF045CDDE4BAC3C3037E01BDE"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "DDEE30DCE9CD2A11C38ADA8AC94FD5BD90EC1BA4"
        self.ExpectedHashOfOnetoNine = "F720446C9BFDC8479D9FA53BC8B9144FC3FE42ED"
        self.ExpectedHashOfabcde = "14F45FAC4BE0302E740CCC6FE99D75A6CAB0E177"

        self.tiger2_5_160 = HashLib4Python.PyCrypto.CreateTiger2_5_160()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_160)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_160)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_5_160.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_5_160.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_5_160.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_5_160.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_5_160.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_160()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_160()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_160()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_160()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_3_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "4441BE75F6018773C206C22745374B924AA8313FEF919F41"
        self.ExpectedHashOfDefaultData = "DEB1924D290E3D5567792A8171BFC44F70B5CD13480D6D5C"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "8540FF4EBA4C823EEC5EDC244D83B93381B75CE92F753005"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "C70FA522EACE7D870F914A086BD1D9807A6FDC405C5A09DB"
        self.ExpectedHashOfOnetoNine = "82FAF69673762B9FD8A0C902BDB395C12B0CBDDC66957838"
        self.ExpectedHashOfabcde = "E1F0DAC9E852ECF1270FB691C35506D4BEDB12A09D6BF911"

        self.tiger2_3_192 = HashLib4Python.PyCrypto.CreateTiger2_3_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_3_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_3_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_3_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_3_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_3_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_3_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_3_192()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_4_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "6A7201A47AAC2065913811175553489ADD0F8B99E65A0955"
        self.ExpectedHashOfDefaultData = "22EE5BFE174B8C1C23361306C3E8F32C92075577F9115C2A"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "0B3BB091C80889FB2E65FCA6ADCEC87147311F242AEC5519"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "3B182344C171E8843B3D30887274FC7248A7CCD49AA84E77"
        self.ExpectedHashOfOnetoNine = "75B7D71ACD40FE5B5D3263C1F68F4CF5A5DA963B39413ACA"
        self.ExpectedHashOfabcde = "9FBB0FBF818C0302890CE373559D23702D87C69B9D1B29D5"

        self.tiger2_4_192 = HashLib4Python.PyCrypto.CreateTiger2_4_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_4_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_4_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_4_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_4_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_4_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_4_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_4_192()

        self.HashCloneIsUnique(Hash)

        
class Tiger2_5_192TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "61C657CC0C3C147ED90779B36A1E811F1D27F406E3F37010"
        self.ExpectedHashOfDefaultData = "7F71F95B346733E7022D4B85BDA9C51E904825F73AF0E8AE"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "C583EDE2D12E49F48BD29642C69D4470016293F47374339F"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "19AD11BA8D3534C41CAA2A9DAA80958EDCDB0B67FF3BF55D"
        self.ExpectedHashOfOnetoNine = "F720446C9BFDC8479D9FA53BC8B9144FC3FE42ED1440C213"
        self.ExpectedHashOfabcde = "14F45FAC4BE0302E740CCC6FE99D75A6CAB0E177B4ADF2A8"

        self.tiger2_5_192 = HashLib4Python.PyCrypto.CreateTiger2_5_192()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_192)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.tiger2_5_192)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.tiger2_5_192.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.tiger2_5_192.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.tiger2_5_192.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.tiger2_5_192.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.tiger2_5_192.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_192()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_192()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_192()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateTiger2_5_192()

        self.HashCloneIsUnique(Hash)

        
class WhirlPoolTestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "19FA61D75522A4669B44E39C1D2E1726C530232130D407F89AFEE0964997F7A73E83BE698B288FEBCF88E3E03C4F0757EA8964E59B63D93708B138CC42A66EB3"
        self.ExpectedHashOfDefaultData = "9D2BB47D6F6D9F0DBAF08BEF416DE06C98CDF293F3D1AD2422A63A9ADFBD9AA33F888A1C6FE7C16DF33B2BD9FFD8EF160BCF6AB4F21B682DC238A3BE03AB0F12"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "A2CF231E2E01B310A91A7BF92435AE0258997AB969D0B2E09378C0F30C73E4434894A836B3F580683F58FC56DA87C685927AE0FC80D2548A35CD3C7528A83AC1"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "72B3CFC10CC32F9203670984407594B9F2A6C9F1A46C3FF7DF76AD07207758F96CF46C448A7687EBBA5EBC046984B4837320306EB27978A58B8CF447978CADEA"
        self.ExpectedHashOfOnetoNine = "21D5CB651222C347EA1284C0ACF162000B4D3E34766F0D00312E3480F633088822809B6A54BA7EDFA17E8FCB5713F8912EE3A218DD98D88C38BBF611B1B1ED2B"
        self.ExpectedHashOfabcde = "5D745E26CCB20FE655D39C9E7F69455758FBAE541CB892B3581E4869244AB35B4FD6078F5D28B1F1A217452A67D9801033D92724A221255A5E377FE9E9E5F0B2"

        self.whirlpool = HashLib4Python.PyCrypto.CreateWhirlPool()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.whirlpool)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.whirlpool)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.whirlpool.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.whirlpool.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.whirlpool.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.whirlpool.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.whirlpool.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateWhirlPool()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateWhirlPool()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateWhirlPool()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateWhirlPool()

        self.HashCloneIsUnique(Hash)


class Keccak_224TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "F71837502BA8E10837BDD8D365ADB85591895602FC552B48B7390ABD"
        self.ExpectedHashOfDefaultData = "1BA678212F840E95F076B4E3E75310D4DA4308E04396E07EF1683ACE"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "8C500F95CB013CBC16DEB6CB742D470E20404E0A1776647EAAB6E869"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "D6CE783743A36717F893DFF82DE89633F21089AFBE4F26431E269650"
        self.ExpectedHashOfOnetoNine = "06471DE6C635A88E7470284B2C2EBF9BD7E5E888CBBD128C21CB8308"
        self.ExpectedHashOfabcde = "16F91F7E036DF526340440C34C231862D8F6319772B670EEFD4703FF"

        self.keccak_224 = HashLib4Python.PyCrypto.CreateKeccak_224()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_224)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_224)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.keccak_224.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.keccak_224.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.keccak_224.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.keccak_224.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.keccak_224.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_224()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_224()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_224()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_224()

        self.HashCloneIsUnique(Hash)


class Keccak_256TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "C5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470"
        self.ExpectedHashOfDefaultData = "3FE42FE8CD6DAEF5ED7891846577F56AB35DC806424FC84A494C81E73BB06B5F"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "925FE69CEF38AA0D2CCBF6741ADD808F204CAA64EFA7E301A0A3EC332E40075E"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "1660234E7CCC29CFC8DEC8C6508AAF54EE48004EA9B56A15AC5742C89AAADA08"
        self.ExpectedHashOfOnetoNine = "2A359FEEB8E488A1AF2C03B908B3ED7990400555DB73E1421181D97CAC004D48"
        self.ExpectedHashOfabcde = "6377C7E66081CB65E473C1B95DB5195A27D04A7108B468890224BEDBE1A8A6EB"

        self.keccak_256 = HashLib4Python.PyCrypto.CreateKeccak_256()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_256)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_256)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.keccak_256.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.keccak_256.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.keccak_256.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.keccak_256.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.keccak_256.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_256()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_256()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_256()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_256()

        self.HashCloneIsUnique(Hash)


class Keccak_384TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "2C23146A63A29ACF99E73B88F8C24EAA7DC60AA771780CCC006AFBFA8FE2479B2DD2B21362337441AC12B515911957FF"
        self.ExpectedHashOfDefaultData = "6A53977DFA0BCDCF069635CF541AB64C7E41923FCB3A5B049AB98878411D0E71DF95FCAB0072F1AE8B931BF4490B823E"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "A7740E29EEF80306DA09D7AF0868E925D6144996F99A01F973F03C4BD85D1EC20567936CA34A443B62A890AD8D263D2A"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "044628643016E3EA30DE6CA3A8A1276F6BF1A5443CEF96BAA73199CF64FFC52D7F38254C671DB2933FFC8DD3E5B77223"
        self.ExpectedHashOfOnetoNine = "EFCCAE72CE14656C434751CF737E70A57AB8DD2C76F5ABE01E52770AFFD77B66D2B80977724A00A6D971B702906F8032"
        self.ExpectedHashOfabcde = "6E577A02A783232ACF34841399883F5F69D9AC78F48C7F4431CBC4F669C2A0F1CA3B1BECB7701B8315588D64D6C3746A"

        self.keccak_384 = HashLib4Python.PyCrypto.CreateKeccak_384()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_384)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_384)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.keccak_384.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.keccak_384.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.keccak_384.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.keccak_384.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.keccak_384.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_384()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_384()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_384()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_384()

        self.HashCloneIsUnique(Hash)


class Keccak_512TestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "0EAB42DE4C3CEB9235FC91ACFFE746B29C29A8C366B7C60E4E67C466F36A4304C00FA9CAF9D87976BA469BCBE06713B435F091EF2769FB160CDAB33D3670680E"
        self.ExpectedHashOfDefaultData = "27E67744299C2229F5008141E410B650BB7D70366B8A60BEAE52F8D6F4A8889D1BAEF53191FF53277FD6CFFE76937CDFAC40EB8EE6F32E3B146C05F961E970A8"
        self.ExpectedHashOfDefaultDataWithHMACWithLongKey = "53D5520C2E31F7EAAE1D95CF04663B18C2144AAF141F2630D6454162B3A890D75D59A9D99096411870FBF7A92A563AEA35AFED836DF652C6DF2AB4D373A754E3"
        self.ExpectedHashOfDefaultDataWithHMACWithShortKey = "6FA826F0AFFE589DFD1665264F5516D076F9FEC585FD4227095B467A50E963D45C1730232549E8DDB590C1518BA310612839BBCCDF34F6A0AD6AC8B91D393BE6"
        self.ExpectedHashOfOnetoNine = "40B787E94778266FB196A73B7A77EDF9DE2EF172451A2B87531324812250DF8F26FCC11E69B35AFDDBE639956C96153E71363F97010BC99405DD2D77B8C41986"
        self.ExpectedHashOfabcde = "37491BD4BF2A4629D4E35602E09812FA94BFC63BAEE4487075E2B6D73F36D01A7392A1719EDBBB5D1D6FA3BA0D144F18229ABC13B7933A4736D6AAB4A3177F18"

        self.keccak_512 = HashLib4Python.PyCrypto.CreateKeccak_512()
        
    def test_HMACWithDefaultDataAndLongKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_512)
        hmac.SetKey(bytearray(HMACLongStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithLongKey == ActualString)

    def test_HMACWithDefaultDataAndShortKey(self):
        hmac = HashLib4Python.PyIHMAC(self.keccak_512)
        hmac.SetKey(bytearray(HMACShortStringKey))
        ActualString = hmac.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultDataWithHMACWithShortKey == ActualString)

    def test_TestBytesabcde(self):
        ActualString = self.keccak_512.ComputeString(Bytesabcde).ToString()
        self.assertTrue(self.ExpectedHashOfabcde == ActualString)

    def test_TestDefaultData(self):
        ActualString = self.keccak_512.ComputeString(DefaultData).ToString()
        self.assertTrue(self.ExpectedHashOfDefaultData == ActualString)

    def test_TestEmptyStream(self):
        ActualString = self.keccak_512.ComputeFile("EmptyFile.txt").ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestEmptyString(self):
        ActualString = self.keccak_512.ComputeString(EmptyData).ToString()
        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestOnetoNine(self):
        ActualString = self.keccak_512.ComputeString(OnetoNine).ToString()
        self.assertTrue(self.ExpectedHashOfOnetoNine == ActualString)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_512()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_512()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_512()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateKeccak_512()

        self.HashCloneIsUnique(Hash)


class Blake2BTestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "786A02F742015903C6C6FD852552D272912F4740E15847618A86E217F71F5419D25E1031AFEE585313896444934EB04B903A685B1448B755D56F701AFE9BE2CE"
        self.ExpectedHashOfQuickBrownDog = "A8ADD4BDDDFD93E4877D2746E62817B116364A1FA7BC148D95090BC7333B3673F82401CF7AA2E4CB1ECD90296E3F14CB5413F8ED77BE73045B13914CDCD6A918"
     
        self.blake = HashLib4Python.PyCrypto.CreateBlake2B()
        
    def test_TestCheckKeyedTestVectors(self):
        Key = bytearray(64)
        for i in range(64):
            Key[i] = i

        config = HashLib4Python.PyIBlake2BConfig()
        config.SetKey(Key)
        
        blake2BWithKey = HashLib4Python.PyCrypto.CreateBlake2B(config)
        
        Input = bytearray()
        for i in range(len(KeyedBlake2B)):
            if i == 0:
                Input = bytearray()
            else:
                Input = bytearray(i)
                for j in range(i):
                    Input[j] = j

            ActualString = blake2BWithKey.ComputeBytes(Input).ToString()
            ExpectedString = KeyedBlake2B[i]

            self.assertTrue(ExpectedString == ActualString)

    def test_TestCheckTestVectors(self):
        for i in range(len(UnkeyedBlake2B)):
            if i == 0:
                Input = bytearray()
            else:
                Input = bytearray(i)
                for j in range(i):
                    Input[j] = j

            ActualString = self.blake.ComputeBytes(Input).ToString()
            ExpectedString = UnkeyedBlake2B[i]

            self.assertTrue(ExpectedString == ActualString)


    def test_TestNullKeyVsUnKeyed(self):
        MainData = bytearray(DefaultData)
        for Idx in range(1, 64 + 1):       
            configNoKeyed = HashLib4Python.PyIBlake2BConfig(Idx)
            configNullKeyed = HashLib4Python.PyIBlake2BConfig(Idx)
            configNullKeyed.SetKey(bytearray())

            ExpectedString = HashLib4Python.PyCrypto.CreateBlake2B(configNoKeyed).ComputeBytes(MainData).ToString()

            ActualString = HashLib4Python.PyCrypto.CreateBlake2B(configNullKeyed).ComputeBytes(MainData).ToString()

            self.assertTrue(ExpectedString == ActualString)

		
    def test_TestQuickBrownDog(self):
        self.blake.Initialize()
        self.blake.TransformString(QuickBrownDog)
        ActualString = self.blake.TransformFinal().ToString()

        self.assertTrue(self.ExpectedHashOfQuickBrownDog == ActualString)

    def test_TestEmpty(self):
        self.blake.Initialize()
        self.blake.TransformString(EmptyData)
        ActualString = self.blake.TransformFinal().ToString()

        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestSplits(self):
        Input = bytearray(20)
        for i in range(20):
            Input[i] = i

        for i in range(20 + 1):
            self.blake.Initialize()
            self.blake.TransformBytes(Input, 0, i)
            hash0 = self.blake.TransformFinal().ToString()

            for split1 in range(i + 1):
                for split2 in range(split1, i + 1):
                    self.blake.Initialize()
                    self.blake.TransformBytes(Input, 0, split1)
                    self.blake.TransformBytes(Input, split1, split2 - split1)
                    self.blake.TransformBytes(Input, split2, i - split2)
                    hash1 = self.blake.TransformFinal().ToString()

                    self.assertTrue(hash0 == hash1)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2B()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2B()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2B()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2B()

        self.HashCloneIsUnique(Hash)


class Blake2STestCase(BaseTestCase):
    def setUp(self):
        self.ExpectedHashOfEmptyData = "69217A3079908094E11121D042354A7C1F55B6482CA1A51E1B250DFD1ED0EEF9"
        self.ExpectedHashOfQuickBrownDog = "606BEEEC743CCBEFF6CBCDF5D5302AA855C256C29B88C8ED331EA1A6BF3C8812"
     
        self.blake = HashLib4Python.PyCrypto.CreateBlake2S()
        
    def test_TestCheckKeyedTestVectors(self):
        Key = bytearray(32)
        for i in range(32):
            Key[i] = i

        config = HashLib4Python.PyIBlake2SConfig()
        config.SetKey(Key)
        
        blake2SWithKey = HashLib4Python.PyCrypto.CreateBlake2S(config)
        
        Input = bytearray()
        for i in range(len(KeyedBlake2S)):
            if i == 0:
                Input = bytearray()
            else:
                Input = bytearray(i)
                for j in range(i):
                    Input[j] = j

            ActualString = blake2SWithKey.ComputeBytes(Input).ToString()
            ExpectedString = KeyedBlake2S[i]

            self.assertTrue(ExpectedString == ActualString)

    def test_TestCheckTestVectors(self):
        for i in range(len(UnkeyedBlake2S)):
            if i == 0:
                Input = bytearray()
            else:
                Input = bytearray(i)
                for j in range(i):
                    Input[j] = j

            ActualString = self.blake.ComputeBytes(Input).ToString()
            ExpectedString = UnkeyedBlake2S[i]

            self.assertTrue(ExpectedString == ActualString)


    def test_TestNullKeyVsUnKeyed(self):
        MainData = bytearray(DefaultData)
        for Idx in range(1, 32 + 1):       
            configNoKeyed = HashLib4Python.PyIBlake2SConfig(Idx)
            configNullKeyed = HashLib4Python.PyIBlake2SConfig(Idx)
            configNullKeyed.SetKey(bytearray())

            ExpectedString = HashLib4Python.PyCrypto.CreateBlake2S(configNoKeyed).ComputeBytes(MainData).ToString()

            ActualString = HashLib4Python.PyCrypto.CreateBlake2S(configNullKeyed).ComputeBytes(MainData).ToString()

            self.assertTrue(ExpectedString == ActualString)

		
    def test_TestQuickBrownDog(self):
        self.blake.Initialize()
        self.blake.TransformString(QuickBrownDog)
        ActualString = self.blake.TransformFinal().ToString()

        self.assertTrue(self.ExpectedHashOfQuickBrownDog == ActualString)

    def test_TestEmpty(self):
        self.blake.Initialize()
        self.blake.TransformString(EmptyData)
        ActualString = self.blake.TransformFinal().ToString()

        self.assertTrue(self.ExpectedHashOfEmptyData == ActualString)

    def test_TestSplits(self):
        Input = bytearray(20)
        for i in range(20):
            Input[i] = i

        for i in range(20 + 1):
            self.blake.Initialize()
            self.blake.TransformBytes(Input, 0, i)
            hash0 = self.blake.TransformFinal().ToString()

            for split1 in range(i + 1):
                for split2 in range(split1, i + 1):
                    self.blake.Initialize()
                    self.blake.TransformBytes(Input, 0, split1)
                    self.blake.TransformBytes(Input, split1, split2 - split1)
                    self.blake.TransformBytes(Input, split2, i - split2)
                    hash1 = self.blake.TransformFinal().ToString()

                    self.assertTrue(hash0 == hash1)

    def test_TestChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2S()
        
        self.ChunkedDataIncrementalHash(Hash)
        
    def test_TestIndexChunkedDataIncrementalHash(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2S()
        
        self.IndexChunkedDataIncrementalHash(Hash)

    def test_TestHashCloneIsCorrect(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2S()

        self.HashCloneIsCorrectTestHelper(Hash)

    def test_TestHashCloneIsUnique(self):
        Hash = HashLib4Python.PyCrypto.CreateBlake2S()

        self.HashCloneIsUnique(Hash)

        
if __name__ ==  '__main__':
    unittest.main()

    
