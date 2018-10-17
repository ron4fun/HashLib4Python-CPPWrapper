# distutils: language = c++
# distutils: sources = HashLib4CPPWrapper.cpp


from HashLib4PythonDef cimport *
include "HashLib4PythonHeader.pxi"
include "HashLib4PythonChecksum.pxi"
include "HashLib4PythonCrypto.pxi"
include "HashLib4PythonHash32.pxi"
include "HashLib4PythonHash64.pxi"
include "HashLib4PythonHash128.pxi"


cdef class PyConverters:
	@staticmethod
	def toUpper(string a_value):
		return TConverters.toUpper(a_value)

	@staticmethod
	def ReadBytesAsUInt32LE(vector[uint8_t] a_value, int32_t a_index):
		return TConverters.ReadBytesAsUInt32LE(a_value, a_index)

	@staticmethod
	def ReadBytesAsUInt64LE(vector[uint8_t] a_value, int32_t a_index):
		return TConverters.ReadBytesAsUInt64LE(a_value, a_index)

	@staticmethod
	def ReadUInt32AsBytesLE(uint32_t a_value):
		return TConverters.ReadUInt32AsBytesLE(a_value)

	@staticmethod
	def ReadUInt64AsBytesLE(uint64_t a_value):
		return TConverters.ReadUInt64AsBytesLE(a_value)

	@staticmethod
	def ConvertHexStringToBytes(string a_value):
		return TConverters.ConvertHexStringToBytes(a_value)

	@staticmethod
	def ConvertStringToBytes(string a_value):
		return TConverters.ConvertStringToBytes(a_value)

	@staticmethod
	def ConvertBytesToHexString(vector[uint8_t] a_value, bint a_group = False):
		return TConverters.ConvertBytesToHexString(a_value, a_group)


cdef class PyNullDigest(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateNullDigest())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyNullDigest()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


########################################################
## PyNullDigestFactory
########################################################
cdef class PyNullDigestFactory:
	@staticmethod
	def CreateNullDigest():
		return PyNullDigest()


########################################################
## PyHMAC
########################################################
cdef class PyHMAC:
	@staticmethod
	def CreateHMAC(PyIHash hash):
		return PyIHMAC(hash)


########################################################
## PyPBKDF2_HMAC
########################################################
cdef class PyPBKDF2_HMAC:
	@staticmethod
	def CreatePBKDF2_HMAC(PyIHash hash, vector[uint8_t] a_password, vector[uint8_t] a_salt, uint32_t a_iterations):
		return PyIPBKDF2_HMAC(hash, a_password, a_salt, a_iterations)



