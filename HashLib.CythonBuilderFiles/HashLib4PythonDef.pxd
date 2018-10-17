from libcpp.string cimport string
from libcpp.vector cimport vector
from libc.stdint cimport uint8_t, uint16_t, int32_t, uint32_t, int64_t, uint64_t


########################################################
## shared_ptr
########################################################
cdef extern from "boost\shared_ptr.hpp" namespace "boost":
	cppclass shared_ptr[T]:
		T* get()



########################################################
## shared_ptr
########################################################
cdef extern from "HashLib4CPPWrapper.h":
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


########################################################
## Converters
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass TConverters:
		@staticmethod
		string toUpper(string &) except +
		@staticmethod
		uint32_t ReadBytesAsUInt32LE(vector[uint8_t], int32_t) except +
		@staticmethod
		uint64_t ReadBytesAsUInt64LE(vector[uint8_t], int32_t) except +
		@staticmethod
		vector[uint8_t] ReadUInt32AsBytesLE(uint32_t) except +
		@staticmethod
		vector[uint8_t] ReadUInt64AsBytesLE(uint64_t) except +
		@staticmethod
		vector[uint8_t] ConvertHexStringToBytes(string &) except +
		@staticmethod
		vector[uint8_t] ConvertStringToBytes(string &) except +
		@staticmethod
		string ConvertBytesToHexString(vector[uint8_t] &, bint) except +


########################################################
## IHashResult
########################################################
cdef extern from "Interfaces\HlpIHashResult.h":
	ctypedef shared_ptr[IIHashResult] IHashResult
	cdef cppclass IIHashResult:
		vector[uint8_t] GetBytes() except +
		uint8_t GetUInt8() except +
		uint16_t GetUInt16() except +
		uint32_t GetUInt32() except +
		int32_t GetInt32() except +
		uint64_t GetUInt64() except +
		string ToString(bint) except +
		int32_t GetHashCode() except +
		bint CompareTo(IHashResult &) except +


########################################################
## IHash
########################################################
cdef extern from "Interfaces\HlpIHash.h":
	ctypedef shared_ptr[IIHash] IHash
	cdef cppclass IIHash:
		string GetName() except +
		int32_t GetBlockSize() except +
		int32_t GetHashSize() except +
		int32_t GetBufferSize() except +
		void SetBufferSize(int32_t) except +

		IHash Clone() except +

		IHashResult ComputeString(string &) except +
		IHashResult ComputeBytes(vector[uint8_t] &) except +
		IHashResult ComputeFile(string &, int64_t, int64_t) except +

		void Initialize() except +

		void TransformBytes(vector[uint8_t] &, int32_t, int32_t) except +
		void TransformBytes(vector[uint8_t] &, int32_t) except +
		void TransformBytes(vector[uint8_t] &) except +

		IHashResult TransformFinal() except +

		void TransformString(string &) except +
		void TransformFile(string &, int64_t, int64_t) except +


########################################################
## ICRC
########################################################
cdef extern from "Interfaces\HlpICRC.h":
	ctypedef shared_ptr[IICRC] ICRC
	cdef cppclass IICRC(IHash):
		ICRC CloneCRC() except +

		vector[string] GetNames() except +
		int32_t GetWidth() except +
		uint64_t GetPolynomial() except +
		uint64_t GetInit() except +
		bint GetReflectIn() except +
		bint GetReflectOut() except +
		uint64_t GetXOROut() except +
		uint64_t GetCheckValue() except +


########################################################
## IHashWithKey
########################################################
cdef extern from "Interfaces\HlpIHashInfo.h":
	cdef cppclass IIWithKey(IIHash):
		vector[uint8_t] GetKey() except +
		void SetKey(vector[uint8_t] &) except +


########################################################
## IHashWithKey
########################################################
cdef extern from "Interfaces\HlpIHashInfo.h":
	ctypedef shared_ptr[IIHashWithKey] IHashWithKey
	cdef cppclass IIHashWithKey(IIWithKey):
		IHashWithKey CloneHashWithKey() except +


########################################################
## IIHMAC
########################################################
cdef extern from "Interfaces\HlpIHashInfo.h":
	ctypedef shared_ptr[IIHMAC] IHMAC
	cdef cppclass IIHMAC(IIWithKey):
		IHMAC CloneHMAC() except +


########################################################
## IIKDF
########################################################
cdef extern from "Interfaces\HlpIKDF.h":
	ctypedef shared_ptr[IIKDF] IKDF
	cdef cppclass IIKDF:
		vector[uint8_t] GetBytes(int32_t) except +


########################################################
## IIPBKDF2_HMAC
########################################################
cdef extern from "Interfaces\HlpIHashInfo.h":
	ctypedef shared_ptr[IIPBKDF2_HMAC] IPBKDF2_HMAC
	cdef cppclass IIPBKDF2_HMAC(IIKDF):
		pass

########################################################
## IIBlake2BConfig
########################################################
cdef extern from "Interfaces\IBlake2BConfigurations\HlpIBlake2BConfig.h":
	ctypedef shared_ptr[IIBlake2BConfig] IBlake2BConfig
	cdef cppclass IIBlake2BConfig:
		vector[uint8_t] GetPersonalisation() except +
		void SetPersonalisation(vector[uint8_t] &) except +
		vector[uint8_t] GetSalt() except +
		void SetSalt(vector[uint8_t] &) except +
		vector[uint8_t] GetKey() except +
		void SetKey(vector[uint8_t] &) except +
		int32_t GetHashSize() except +
		void SetHashSize(int32_t) except +
		

########################################################
## IIBlake2SConfig
########################################################
cdef extern from "Interfaces\IBlake2SConfigurations\HlpIBlake2SConfig.h":
	ctypedef shared_ptr[IIBlake2SConfig] IBlake2SConfig
	cdef cppclass IIBlake2SConfig:
		vector[uint8_t] GetPersonalisation() except +
		void SetPersonalisation(vector[uint8_t] &) except +
		vector[uint8_t] GetSalt() except +
		void SetSalt(vector[uint8_t] &) except +
		vector[uint8_t] GetKey() except +
		void SetKey(vector[uint8_t] &) except +
		int32_t GetHashSize() except +
		void SetHashSize(int32_t) except +


########################################################
## THashResult
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass THashResult:
		THashResult()
		THashResult(IHashResult)
		THashResult(vector[uint8_t] &)
		IHashResult ptr
		THashResult(THashResult &)
		vector[uint8_t] GetBytes()
		uint8_t GetUInt8()
		uint16_t GetUInt16()
		uint32_t GetUInt32()
		int32_t GetInt32()
		uint64_t GetUInt64()
		string ToString(bint)
		int32_t GetHashCode()
		bint CompareTo(vector[uint8_t] &)


########################################################
## THash
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass THash:
		THash()
		THash(IHash)
		IHash ptr
		THash(THash &)
		string GetName()
		int32_t GetBlockSize()
		int32_t GetHashSize()
		int32_t GetBufferSize()
		void SetBufferSize(int32_t)

		THash Clone()

		THashResult ComputeString(string &)
		THashResult ComputeBytes(vector[uint8_t] &) 
		THashResult ComputeFile(string &, int64_t, int64_t)

		void Initialize()

		void TransformBytes(vector[uint8_t] &, int32_t, int32_t)
		void TransformBytes(vector[uint8_t] &, int32_t)
		void TransformBytes(vector[uint8_t] &)

		THashResult TransformFinal()

		void TransformString(string &)
		void TransformFile(string &, int64_t, int64_t)


########################################################
## TCRC
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass TCRC:
		TCRC()
		TCRC(ICRC)
		ICRC ptr
		TCRC(TCRC &)

		string GetName()
		int32_t GetBlockSize()
		int32_t GetHashSize()
		int32_t GetBufferSize()
		void SetBufferSize(int32_t)

		TCRC Clone()

		THashResult ComputeString(string &)
		THashResult ComputeBytes(vector[uint8_t] &) 
		THashResult ComputeFile(string &, int64_t, int64_t)

		void Initialize()

		void TransformBytes(vector[uint8_t] &, int32_t, int32_t)
		void TransformBytes(vector[uint8_t] &, int32_t)
		void TransformBytes(vector[uint8_t] &)

		THashResult TransformFinal()

		void TransformString(string &)
		void TransformFile(string &, int64_t, int64_t)

		vector[string] GetNames()
		int32_t GetWidth()
		uint64_t GetPolynomial()
		uint64_t GetInit()
		bint GetReflectIn()
		bint GetReflectOut()
		uint64_t GetXOROut()
		uint64_t GetCheckValue()


########################################################
## THashWithKey
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass THashWithKey:
		THashWithKey()
		THashWithKey(IHashWithKey)
		IHashWithKey ptr
		THashWithKey(THashWithKey &)

		string GetName()
		int32_t GetBlockSize()
		int32_t GetHashSize()
		int32_t GetBufferSize()
		void SetBufferSize(int32_t)

		THashWithKey Clone()

		THashResult ComputeString(string &)
		THashResult ComputeBytes(vector[uint8_t] &) 
		THashResult ComputeFile(string &, int64_t, int64_t)

		void Initialize()

		void TransformBytes(vector[uint8_t] &, int32_t, int32_t)
		void TransformBytes(vector[uint8_t] &, int32_t)
		void TransformBytes(vector[uint8_t] &)

		THashResult TransformFinal()

		void TransformString(string &)
		void TransformFile(string &, int64_t, int64_t)

		vector[uint8_t] GetKey()
		void SetKey(vector[uint8_t] &)
		int32_t GetKeyLength()


########################################################
## THMAC
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass THMAC:
		THMAC()
		THMAC(THash)
		IHMAC ptr
		THMAC(THMAC &)

		string GetName()
		int32_t GetBlockSize()
		int32_t GetHashSize()
		int32_t GetBufferSize()
		void SetBufferSize(int32_t)

		THMAC Clone()

		THash CloneTHash()

		THashResult ComputeString(string &)
		THashResult ComputeBytes(vector[uint8_t] &) 
		THashResult ComputeFile(string &, int64_t, int64_t)

		void Initialize()

		void TransformBytes(vector[uint8_t] &, int32_t, int32_t)
		void TransformBytes(vector[uint8_t] &, int32_t)
		void TransformBytes(vector[uint8_t] &)

		THashResult TransformFinal()

		void TransformString(string &)
		void TransformFile(string &, int64_t, int64_t)

		vector[uint8_t] GetKey()
		void SetKey(vector[uint8_t] &)
		int32_t GetKeyLength()


########################################################
## TPBKDF2_HMAC
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass TPBKDF2_HMAC:
		TPBKDF2_HMAC()
		TPBKDF2_HMAC(THash, vector[uint8_t] &, vector[uint8_t] &, uint32_t)
		IPBKDF2_HMAC ptr
		TPBKDF2_HMAC(TPBKDF2_HMAC &)

		vector[uint8_t] GetBytes(int32_t)


########################################################
## TBlake2BConfig
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass TBlake2BConfig:
		TBlake2BConfig()
		TBlake2BConfig(int32_t)
		IBlake2BConfig ptr
		TBlake2BConfig(TBlake2BConfig &)

		IBlake2BConfig GetConfig()

		vector[uint8_t] GetPersonalisation()
		void SetPersonalisation(vector[uint8_t] &)
		vector[uint8_t] GetSalt()
		void SetSalt(vector[uint8_t] &)
		vector[uint8_t] GetKey()
		void SetKey(vector[uint8_t] &)
		int32_t GetHashSize()
		void SetHashSize(int32_t)


########################################################
## TBlake2SConfig
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass TBlake2SConfig:
		TBlake2SConfig()
		TBlake2SConfig(int32_t)
		IBlake2SConfig ptr
		TBlake2SConfig(TBlake2SConfig &)

		IBlake2SConfig GetConfig()

		vector[uint8_t] GetPersonalisation()
		void SetPersonalisation(vector[uint8_t] &)
		vector[uint8_t] GetSalt()
		void SetSalt(vector[uint8_t] &)
		vector[uint8_t] GetKey()
		void SetKey(vector[uint8_t] &)
		int32_t GetHashSize()
		void SetHashSize(int32_t)


########################################################
## HashLib4CPPWrapper
########################################################
cdef extern from "HashLib4CPPWrapper.h":
	cdef cppclass HashLib4CPPWrapper:
		@staticmethod
		IHash CreateNullDigest() except +

		@staticmethod
		ICRC CreateCRC(CRCStandard &) except +
		@staticmethod
		IHash CreateCRC16_BUYPASS() except +
		@staticmethod
		IHash CreateCRC32_PKZIP() except +
		@staticmethod
		IHash CreateCRC32_CASTAGNOLI() except +
		@staticmethod
		IHash CreateCRC64_ECMA() except +
		@staticmethod
		IHash CreateAdler32() except +

		@staticmethod
		IHash CreateBlake2B(TBlake2BConfig *) except +
		@staticmethod
		IHash CreateBlake2B_160() except +
		@staticmethod
		IHash CreateBlake2B_256() except +
		@staticmethod
		IHash CreateBlake2B_384() except +
		@staticmethod
		IHash CreateBlake2B_512() except +
		@staticmethod
		IHash CreateBlake2S(TBlake2SConfig *) except +
		@staticmethod
		IHash CreateBlake2S_128() except +
		@staticmethod
		IHash CreateBlake2S_160() except +
		@staticmethod
		IHash CreateBlake2S_224() except +
		@staticmethod
		IHash CreateBlake2S_256() except +
		@staticmethod
		IHash CreateGost() except +
		@staticmethod
		IHash CreateGOST3411_2012_256() except +
		@staticmethod
		IHash CreateGOST3411_2012_512() except +
		@staticmethod
		IHash CreateGrindahl256() except +
		@staticmethod
		IHash CreateGrindahl512() except +
		@staticmethod
		IHash CreateHAS160() except +
		@staticmethod
		IHash CreateHaval_3_128() except +
		@staticmethod
		IHash CreateHaval_3_160() except +
		@staticmethod
		IHash CreateHaval_3_192() except +
		@staticmethod
		IHash CreateHaval_3_224() except +
		@staticmethod
		IHash CreateHaval_3_256() except +
		@staticmethod
		IHash CreateHaval_4_128() except +
		@staticmethod
		IHash CreateHaval_4_160() except +
		@staticmethod
		IHash CreateHaval_4_192() except +
		@staticmethod
		IHash CreateHaval_4_224() except +
		@staticmethod
		IHash CreateHaval_4_256() except +
		@staticmethod
		IHash CreateHaval_5_128() except +
		@staticmethod
		IHash CreateHaval_5_160() except +
		@staticmethod
		IHash CreateHaval_5_192() except +
		@staticmethod
		IHash CreateHaval_5_224() except +
		@staticmethod
		IHash CreateHaval_5_256() except +
		@staticmethod
		IHash CreateMD2() except +
		@staticmethod
		IHash CreateMD4() except +
		@staticmethod
		IHash CreateMD5() except +
		@staticmethod
		IHash CreatePanama() except +
		@staticmethod
		IHash CreateRIPEMD() except +
		@staticmethod
		IHash CreateRIPEMD128() except +
		@staticmethod
		IHash CreateRIPEMD160() except +
		@staticmethod
		IHash CreateRIPEMD256() except +
		@staticmethod
		IHash CreateRIPEMD320() except +
		@staticmethod
		IHash CreateRadioGatun32() except +
		@staticmethod
		IHash CreateRadioGatun64() except +
		@staticmethod
		IHash CreateSHA0() except +
		@staticmethod
		IHash CreateSHA1() except +
		@staticmethod
		IHash CreateSHA2_224() except +
		@staticmethod
		IHash CreateSHA2_256() except +
		@staticmethod
		IHash CreateSHA2_384() except +
		@staticmethod
		IHash CreateSHA2_512() except +
		@staticmethod
		IHash CreateSHA2_512_224() except +
		@staticmethod
		IHash CreateSHA2_512_256() except +
		@staticmethod
		IHash CreateSHA3_224() except +
		@staticmethod
		IHash CreateSHA3_256() except +
		@staticmethod
		IHash CreateSHA3_384() except +
		@staticmethod
		IHash CreateSHA3_512() except +
		@staticmethod
		IHash CreateKeccak_224() except +
		@staticmethod
		IHash CreateKeccak_256() except +
		@staticmethod
		IHash CreateKeccak_384() except +
		@staticmethod
		IHash CreateKeccak_512() except +
		@staticmethod
		IHash CreateSnefru_8_128() except +
		@staticmethod
		IHash CreateSnefru_8_256() except +
		@staticmethod
		IHash CreateTiger2_3_128() except +
		@staticmethod
		IHash CreateTiger2_3_160() except +
		@staticmethod
		IHash CreateTiger2_3_192() except +
		@staticmethod
		IHash CreateTiger2_4_128() except +
		@staticmethod
		IHash CreateTiger2_4_160() except +
		@staticmethod
		IHash CreateTiger2_4_192() except +
		@staticmethod
		IHash CreateTiger2_5_128() except +
		@staticmethod
		IHash CreateTiger2_5_160() except +
		@staticmethod
		IHash CreateTiger2_5_192() except +
		@staticmethod
		IHash CreateTiger_3_128() except +
		@staticmethod
		IHash CreateTiger_3_160() except +
		@staticmethod
		IHash CreateTiger_3_192() except +
		@staticmethod
		IHash CreateTiger_4_128() except +
		@staticmethod
		IHash CreateTiger_4_160() except +
		@staticmethod
		IHash CreateTiger_4_192() except +
		@staticmethod
		IHash CreateTiger_5_128() except +
		@staticmethod
		IHash CreateTiger_5_160() except +
		@staticmethod
		IHash CreateTiger_5_192() except +
		@staticmethod
		IHash CreateWhirlPool() except +

		@staticmethod
		IHash CreateAP() except +
		@staticmethod
		IHash CreateBernstein() except +
		@staticmethod
		IHash CreateBernstein1() except +
		@staticmethod
		IHash CreateBKDR() except +
		@staticmethod
		IHash CreateDEK() except +
		@staticmethod
		IHash CreateDJB() except +
		@staticmethod
		IHash CreateELF() except +
		@staticmethod
		IHash CreateFNV_32() except +
		@staticmethod
		IHash CreateFNV1a_32() except +
		@staticmethod
		IHash CreateJenkins3() except +
		@staticmethod
		IHash CreateJS() except +
		@staticmethod
		IHashWithKey CreateMurmur2_32() except +
		@staticmethod
		IHashWithKey CreateMurmurHash3_x86_32() except +
		@staticmethod
		IHash CreateOneAtTime() except +
		@staticmethod
		IHash CreatePJW() except +
		@staticmethod
		IHash CreateRotating() except +
		@staticmethod
		IHash CreateRS() except +
		@staticmethod
		IHash CreateSDBM() except +
		@staticmethod
		IHash CreateShiftAndXor() except +
		@staticmethod
		IHash CreateSuperFast() except +
		@staticmethod
		IHashWithKey CreateXXHash32() except +


		@staticmethod
		IHash CreateFNV_64() except + 
		@staticmethod
		IHash CreateFNV1a_64() except + 
		@staticmethod
		IHashWithKey CreateMurmur2_64() except + 
		@staticmethod
		IHashWithKey CreateXXHash64() except + 
		@staticmethod
		IHashWithKey CreateSipHash2_4() except + 


		@staticmethod
		IHashWithKey CreateMurmurHash3_x64_128() except + 
		@staticmethod
		IHashWithKey CreateMurmurHash3_x86_128() except + 


