# distutils: language = c++
# distutils: sources = HashLibWrapper.cpp

from libcpp.string cimport string
from libcpp.vector cimport vector
from libc.stdint cimport uint8_t, int32_t, uint32_t, int64_t, uint64_t

cdef extern from "HashLibWrapper.h":
	cdef enum MODE:
		a_STRING
		a_FILE

cdef extern from "HashLibWrapper.h":
	cdef enum HASH:
		a_NORMAL
		a_HMAC
		a_PBKDF

cdef extern from "HashLibWrapper.h":
	cdef enum CRCStandard:
		CRC3_GSM
		CRC3_ROHC
		CRC4_INTERLAKEN
		CRC4_ITU
		CRC5_EPC
		CRC5_ITU
		CRC5_USB
		CRC6_CDMA2000A
		CRC6_CDMA2000B
		CRC6_DARC
		CRC6_GSM
		CRC6_ITU
		CRC7
		CRC7_ROHC
		CRC7_UMTS
		CRC8
		CRC8_AUTOSAR
		CRC8_BLUETOOTH
		CRC8_CDMA2000
		CRC8_DARC
		CRC8_DVBS2
		CRC8_EBU
		CRC8_GSMA
		CRC8_GSMB
		CRC8_ICODE
		CRC8_ITU
		CRC8_LTE
		CRC8_MAXIM
		CRC8_OPENSAFETY
		CRC8_ROHC
		CRC8_SAEJ1850
		CRC8_WCDMA
		CRC10
		CRC10_CDMA2000
		CRC10_GSM
		CRC11
		CRC11_UMTS
		CRC12_CDMA2000
		CRC12_DECT
		CRC12_GSM
		CRC12_UMTS
		CRC13_BBC
		CRC14_DARC
		CRC14_GSM
		CRC15
		CRC15_MPT1327
		ARC
		CRC16_AUGCCITT
		CRC16_BUYPASS
		CRC16_CCITTFALSE
		CRC16_CDMA2000
		CRC16_CMS
		CRC16_DDS110
		CRC16_DECTR
		CRC16_DECTX
		CRC16_DNP
		CRC16_EN13757
		CRC16_GENIBUS
		CRC16_GSM
		CRC16_LJ1200
		CRC16_MAXIM
		CRC16_MCRF4XX
		CRC16_OPENSAFETYA
		CRC16_OPENSAFETYB
		CRC16_PROFIBUS
		CRC16_RIELLO
		CRC16_T10DIF
		CRC16_TELEDISK
		CRC16_TMS37157
		CRC16_USB
		CRCA
		KERMIT
		MODBUS
		X25
		XMODEM
		CRC17_CANFD
		CRC21_CANFD
		CRC24
		CRC24_BLE
		CRC24_FLEXRAYA
		CRC24_FLEXRAYB
		CRC24_INTERLAKEN
		CRC24_LTEA
		CRC24_LTEB
		CRC30_CDMA
		CRC31_PHILIPS
		CRC32
		CRC32_AUTOSAR
		CRC32_BZIP2
		CRC32C
		CRC32D
		CRC32_MPEG2
		CRC32_POSIX
		CRC32Q
		JAMCRC
		XFER
		CRC40_GSM
		CRC64
		CRC64_GOISO
		CRC64_WE
		CRC64_XZ

cdef extern from "HashLibWrapper.h":
	cdef cppclass HashFactoryWrapper:
		@staticmethod
		string CreateCRC(CRCStandard &, string &, MODE &) except + 
		@staticmethod
		string CreateCRC16_BUYPASS(string &, MODE &) except +
		@staticmethod
		string CreateCRC32_PKZIP(string &, MODE &) except +
		@staticmethod
		string CreateCRC32_CASTAGNOLI(string &, MODE &) except +
		@staticmethod
		string CreateCRC64_ECMA(string &, MODE &) except +
		@staticmethod
		string CreateAdler32(string &, MODE &) except +

		@staticmethod
		string CreateGost(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateGrindahl256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateGrindahl512(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHAS160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_3_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_3_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_3_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateHaval_3_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_3_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_4_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_4_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_4_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_4_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateHaval_4_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_5_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_5_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_5_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateHaval_5_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateHaval_5_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateMD2(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateMD4(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateMD5(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreatePanama(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRIPEMD(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRIPEMD128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRIPEMD160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRIPEMD256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateRIPEMD320(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRadioGatun32(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateRadioGatun64(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA0(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA1(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA2_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateSHA2_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA2_384(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA2_512(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA2_512_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA2_512_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA3_224(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateSHA3_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA3_384(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSHA3_512(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSnefru_8_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateSnefru_8_256(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_3_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_3_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_3_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_4_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_4_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_4_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_5_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger2_5_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except + 
		@staticmethod
		string CreateTiger2_5_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_3_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_3_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_3_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_4_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_4_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_4_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_5_128(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_5_160(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateTiger_5_192(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		@staticmethod
		string CreateWhirlPool(string &, MODE &, string &, HASH &, string &, uint32_t, int32_t) except +
		
		@staticmethod
		string CreateAP(string &, MODE &) except + 
		@staticmethod
		string CreateBernstein(string &, MODE &) except +
		@staticmethod
		string CreateBernstein1(string &, MODE &) except +
		@staticmethod
		string CreateBKDR(string &, MODE &) except +
		@staticmethod
		string CreateDEK(string &, MODE &) except +
		@staticmethod
		string CreateDJB(string &, MODE &) except +
		@staticmethod
		string CreateELF(string &, MODE &) except + 
		@staticmethod
		string CreateFNV_32(string &, MODE &) except +
		@staticmethod
		string CreateFNV1a_32(string &, MODE &) except +
		@staticmethod
		string CreateJenkins3(string &, MODE &) except +
		@staticmethod
		string CreateJS(string &, MODE &) except +
		@staticmethod
		string CreateMurmur2_32(string &, MODE &, uint32_t) except +
		@staticmethod
		string CreateMurmurHash3_x86_32(string &, MODE &, uint32_t) except + 
		@staticmethod
		string CreateOneAtTime(string &, MODE &) except +
		@staticmethod
		string CreatePJW(string &, MODE &) except +
		@staticmethod
		string CreateRotating(string &, MODE &) except +
		@staticmethod
		string CreateRS(string &, MODE &) except +
		@staticmethod
		string CreateSDBM(string &, MODE &) except +
		@staticmethod
		string CreateShiftAndXor(string &, MODE &) except +
		@staticmethod
		string CreateSuperFast(string &, MODE &) except +
		@staticmethod
		string CreateXXHash32(string &, MODE &, uint32_t) except +

		@staticmethod
		string CreateFNV_64(string &, MODE &) except +
		@staticmethod
		string CreateFNV1a_64(string &, MODE &) except +
		@staticmethod
		string CreateMurmur2_64(string &, MODE &, uint32_t) except +
		@staticmethod
		string CreateXXHash64(string &, MODE &, uint64_t) except +
		@staticmethod
		string CreateSipHash2_4(string &, MODE &, uint64_t, uint64_t) except +

		@staticmethod
		string CreateMurmurHash3_x64_128(string &, MODE &, uint32_t) except +
		@staticmethod
		string CreateMurmurHash3_x86_128(string &, MODE &, uint32_t) except +
	

cdef class PyMODE:
	_STRING = a_STRING
	_FILE = a_FILE

cdef class PyHASH:
	_NORMAL = a_NORMAL
	_HMAC = a_HMAC
	_PBKDF = a_PBKDF

cdef class PyCRCStandard:
	_CRC3_GSM = CRC3_GSM
	_CRC3_ROHC = CRC3_ROHC
	_CRC4_INTERLAKEN = CRC4_INTERLAKEN
	_CRC4_ITU = CRC4_ITU
	_CRC5_EPC = CRC5_EPC
	_CRC5_ITU = CRC5_ITU
	_CRC5_USB = CRC5_USB
	_CRC6_CDMA2000A = CRC6_CDMA2000A
	_CRC6_CDMA2000B = CRC6_CDMA2000B
	_CRC6_DARC = CRC6_DARC
	_CRC6_GSM = CRC6_GSM
	_CRC6_ITU = CRC6_ITU
	_CRC7 = CRC7
	_CRC7_ROHC = CRC7_ROHC
	_CRC7_UMTS = CRC7_UMTS
	_CRC8 = CRC8
	_CRC8_AUTOSAR = CRC8_AUTOSAR
	_CRC8_BLUETOOTH = CRC8_BLUETOOTH
	_CRC8_CDMA2000 = CRC8_CDMA2000
	_CRC8_DARC = CRC8_DARC
	_CRC8_DVBS2 = CRC8_DVBS2
	_CRC8_EBU = CRC8_EBU
	_CRC8_GSMA = CRC8_GSMA
	_CRC8_GSMB = CRC8_GSMB
	_CRC8_ICODE = CRC8_ICODE
	_CRC8_ITU = CRC8_ITU
	_CRC8_LTE = CRC8_LTE
	_CRC8_MAXIM = CRC8_MAXIM
	_CRC8_OPENSAFETY = CRC8_OPENSAFETY
	_CRC8_ROHC = CRC8_ROHC
	_CRC8_SAEJ1850 = CRC8_SAEJ1850
	_CRC8_WCDMA = CRC8_WCDMA
	_CRC10 = CRC10
	_CRC10_CDMA2000 = CRC10_CDMA2000
	_CRC10_GSM = CRC10_GSM
	_CRC11 = CRC11
	_CRC11_UMTS = CRC11_UMTS
	_CRC12_CDMA2000 = CRC12_CDMA2000
	_CRC12_DECT = CRC12_DECT
	_CRC12_GSM = CRC12_GSM
	_CRC12_UMTS = CRC12_UMTS
	_CRC13_BBC = CRC13_BBC
	_CRC14_DARC = CRC14_DARC
	_CRC14_GSM = CRC14_GSM
	_CRC15 = CRC15
	_CRC15_MPT1327 = CRC15_MPT1327
	_ARC = ARC
	_CRC16_AUGCCITT = CRC16_AUGCCITT
	_CRC16_BUYPASS = CRC16_BUYPASS
	_CRC16_CCITTFALSE = CRC16_CCITTFALSE
	_CRC16_CDMA2000 = CRC16_CDMA2000
	_CRC16_CMS = CRC16_CMS
	_CRC16_DDS110 = CRC16_DDS110
	_CRC16_DECTR = CRC16_DECTR
	_CRC16_DECTX = CRC16_DECTX
	_CRC16_DNP = CRC16_DNP
	_CRC16_EN13757 = CRC16_EN13757
	_CRC16_GENIBUS = CRC16_GENIBUS
	_CRC16_GSM = CRC16_GSM
	_CRC16_LJ1200 = CRC16_LJ1200
	_CRC16_MAXIM = CRC16_MAXIM
	_CRC16_MCRF4XX = CRC16_MCRF4XX
	_CRC16_OPENSAFETYA = CRC16_OPENSAFETYA
	_CRC16_OPENSAFETYB = CRC16_OPENSAFETYB
	_CRC16_PROFIBUS = CRC16_PROFIBUS
	_CRC16_RIELLO = CRC16_RIELLO
	_CRC16_T10DIF = CRC16_T10DIF
	_CRC16_TELEDISK = CRC16_TELEDISK
	_CRC16_TMS37157 = CRC16_TMS37157
	_CRC16_USB = CRC16_USB
	_CRCA = CRCA
	_KERMIT = KERMIT
	_MODBUS = MODBUS
	_X25 = X25
	_XMODEM = XMODEM
	_CRC17_CANFD = CRC17_CANFD
	_CRC21_CANFD = CRC21_CANFD
	_CRC24 = CRC24
	_CRC24_BLE = CRC24_BLE
	_CRC24_FLEXRAYA = CRC24_FLEXRAYA
	_CRC24_FLEXRAYB = CRC24_FLEXRAYB
	_CRC24_INTERLAKEN = CRC24_INTERLAKEN
	_CRC24_LTEA = CRC24_LTEA
	_CRC24_LTEB = CRC24_LTEB
	_CRC30_CDMA = CRC30_CDMA
	_CRC31_PHILIPS = CRC31_PHILIPS
	_CRC32 = CRC32
	_CRC32_AUTOSAR = CRC32_AUTOSAR
	_CRC32_BZIP2 = CRC32_BZIP2
	_CRC32C = CRC32C
	_CRC32D = CRC32D
	_CRC32_MPEG2 = CRC32_MPEG2
	_CRC32_POSIX = CRC32_POSIX
	_CRC32Q = CRC32Q
	_JAMCRC = JAMCRC
	_XFER = XFER
	_CRC40_GSM = CRC40_GSM
	_CRC64 = CRC64
	_CRC64_GOISO = CRC64_GOISO
	_CRC64_WE = CRC64_WE
	_CRC64_XZ = CRC64_XZ


def transformText(a_text, an_encoding):
	py_byte_string = a_text.encode(an_encoding)
	cdef char* c_string = py_byte_string
	a_text = c_string
	return a_text


########################################################
## Checksum
########################################################
cdef class PyChecksum:
	@staticmethod
	def CreateCRC(a_value, a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateCRC(a_value, a_text, a_mode)

	@staticmethod
	def CreateCRC16_BUYPASS(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateCRC16_BUYPASS(a_text, a_mode)

	@staticmethod
	def CreateCRC32_PKZIP(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateCRC32_PKZIP(a_text, a_mode)

	@staticmethod
	def CreateCRC32_CASTAGNOLI(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateCRC32_CASTAGNOLI(a_text, a_mode)

	@staticmethod
	def CreateCRC64_ECMA(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateCRC64_ECMA(a_text, a_mode)

	@staticmethod
	def CreateAdler32(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateAdler32(a_text, a_mode)


########################################################
## Crypto
########################################################
cdef class PyCrypto:
	@staticmethod
	def CreateGost(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateGost(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateGrindahl256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateGrindahl256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateGrindahl512(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateGrindahl512(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHAS160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHAS160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_3_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_3_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_3_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_3_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_3_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_3_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateHaval_3_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_3_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_3_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_3_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_4_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_4_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_4_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_4_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_4_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_4_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_4_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_4_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateHaval_4_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_4_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_5_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_5_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_5_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_5_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_5_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_5_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateHaval_5_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_5_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateHaval_5_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateHaval_5_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateMD2(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMD2(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateMD4(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMD4(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateMD5(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMD5(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreatePanama(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreatePanama(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRIPEMD(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRIPEMD(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRIPEMD128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRIPEMD128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRIPEMD160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRIPEMD160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRIPEMD256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRIPEMD256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateRIPEMD320(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRIPEMD320(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRadioGatun32(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRadioGatun32(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateRadioGatun64(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRadioGatun64(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA0(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA0(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA1(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA1(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA2_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateSHA2_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA2_384(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_384(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA2_512(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_512(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA2_512_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_512_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA2_512_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA2_512_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA3_224(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA3_224(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateSHA3_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA3_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA3_384(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA3_384(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSHA3_512(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSHA3_512(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSnefru_8_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSnefru_8_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateSnefru_8_256(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSnefru_8_256(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_3_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_3_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_3_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_3_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_3_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_3_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_4_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_4_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_4_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_4_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_4_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_4_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_5_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_5_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger2_5_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_5_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)
 
	@staticmethod
	def CreateTiger2_5_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger2_5_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_3_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_3_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_3_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_3_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_3_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_3_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_4_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_4_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_4_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_4_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_4_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_4_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_5_128(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_5_128(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_5_160(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_5_160(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateTiger_5_192(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateTiger_5_192(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)

	@staticmethod
	def CreateWhirlPool(a_text, a_mode, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", an_iterations=1000, a_byte_count=32, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateWhirlPool(a_text, a_mode, a_key, a_PyHASH, a_salt, an_iterations, a_byte_count)



########################################################
## Hash32
########################################################
cdef class PyHash32:
	@staticmethod
	def CreateAP(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateAP(a_text, a_mode)

	@staticmethod
	def CreateBernstein(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateBernstein(a_text, a_mode)

	@staticmethod
	def CreateBernstein1(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateBernstein1(a_text, a_mode)

	@staticmethod
	def CreateBKDR(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateBKDR(a_text, a_mode)

	@staticmethod
	def CreateDEK(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateDEK(a_text, a_mode)

	@staticmethod
	def CreateDJB(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateDJB(a_text, a_mode)

	@staticmethod
	def CreateELF(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateELF(a_text, a_mode) 

	@staticmethod
	def CreateFNV(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateFNV_32(a_text, a_mode)

	@staticmethod
	def CreateFNV1a(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateFNV1a_32(a_text, a_mode)

	@staticmethod
	def CreateJenkins3(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateJenkins3(a_text, a_mode)

	@staticmethod
	def CreateJS(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateJS(a_text, a_mode)

	@staticmethod
	def CreateMurmur2(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMurmur2_32(a_text, a_mode, a_key)

	@staticmethod
	def CreateMurmurHash3_x86_32(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMurmurHash3_x86_32(a_text, a_mode, a_key)

	@staticmethod
	def CreateOneAtTime(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateOneAtTime(a_text, a_mode)

	@staticmethod
	def CreatePJW(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreatePJW(a_text, a_mode)

	@staticmethod
	def CreateRotating(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRotating(a_text, a_mode)

	@staticmethod
	def CreateRS(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateRS(a_text, a_mode)

	@staticmethod
	def CreateSDBM(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSDBM(a_text, a_mode)

	@staticmethod
	def CreateShiftAndXor(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateShiftAndXor(a_text, a_mode)

	@staticmethod
	def CreateSuperFast(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSuperFast(a_text, a_mode)

	@staticmethod
	def CreateXXHash32(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateXXHash32(a_text, a_mode, a_key)


########################################################
## Hash64
########################################################
cdef class PyHash64:
	@staticmethod
	def CreateFNV(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateFNV_64(a_text, a_mode)
	
	@staticmethod
	def CreateFNV1a(a_text, a_mode, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateFNV1a_64(a_text, a_mode)

	@staticmethod
	def CreateMurmur2(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMurmur2_64(a_text, a_mode, a_key)

	@staticmethod
	def CreateXXHash64(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateXXHash64(a_text, a_mode, a_key)

	@staticmethod
	def CreateSipHash2_4(a_text, a_mode, a_key1=0x0001020304050607, a_key2=0x08090A0B0C0D0E0F, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateSipHash2_4(a_text, a_mode, a_key1, a_key2)


########################################################
## Hash128
########################################################
cdef class PyHash128:
	@staticmethod
	def CreateMurmurHash3_x64_128(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMurmurHash3_x64_128(a_text, a_mode, a_key)

	@staticmethod
	def CreateMurmurHash3_x86_128(a_text, a_mode, a_key=0, an_encoding='UTF-8'):
		a_text = transformText(a_text, an_encoding)
		return HashFactoryWrapper.CreateMurmurHash3_x86_128(a_text, a_mode, a_key)

