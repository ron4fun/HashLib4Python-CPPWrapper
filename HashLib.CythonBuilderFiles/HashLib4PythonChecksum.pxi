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


cdef class PyCRC(PyICRC):
	def __cinit__(self, a_value):
		self.thisptr = new TCRC(HashLib4CPPWrapper.CreateCRC(a_value))

	def Clone(self):
		cdef TCRC hash = self.thisptr.Clone()
		result = PyCRC()
		del result.thisptr
		result.thisptr = new TCRC(hash)
		return result


cdef class PyCRC16_BUYPASS(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateCRC16_BUYPASS())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyCRC16_BUYPASS()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


cdef class PyCRC32_PKZIP(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateCRC32_PKZIP())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyCRC32_PKZIP()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


cdef class PyCRC32_CASTAGNOLI(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateCRC32_CASTAGNOLI())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyCRC32_CASTAGNOLI()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


cdef class PyCRC64_ECMA(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateCRC64_ECMA())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyCRC64_ECMA()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


cdef class PyAdler32(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateAdler32())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyAdler32()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result	


########################################################
## PyChecksum
########################################################
cdef class PyChecksum:
	@staticmethod
	def CreateCRC(a_value):
		return PyCRC(a_value)

	@staticmethod
	def CreateCRC16_BUYPASS():
		return PyCRC16_BUYPASS()

	@staticmethod
	def CreateCRC32_PKZIP():
		return PyCRC32_PKZIP()

	@staticmethod
	def CreateCRC32_CASTAGNOLI():
		return PyCRC32_CASTAGNOLI()

	@staticmethod
	def CreateCRC64_ECMA():
		return PyCRC64_ECMA()

	@staticmethod
	def CreateAdler32():
		return PyAdler32()

		