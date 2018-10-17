########################################################
## PyIHashResult
########################################################
cdef class PyIHashResult:
	cdef THashResult *thisptr
	def __cinit__(self, vector[uint8_t] hash):
		self.thisptr = new THashResult(hash)

	def __dealloc__(self):
		del self.thisptr

	def GetBytes(self):
		return self.thisptr.GetBytes()

	def GetUInt8(self):
		return self.thisptr.GetUInt8()

	def GetUInt16(self):
		return self.thisptr.GetUInt16()

	def GetUInt32(self):
		return self.thisptr.GetUInt32()

	def GetInt32(self):
		return self.thisptr.GetInt32()

	def GetUInt64(self):
		return self.thisptr.GetUInt64()

	def ToString(self, a_group = False):
		return self.thisptr.ToString(a_group)

	def GetHashCode(self):
		return self.thisptr.GetHashCode()

	def CompareTo(self, PyIHashResult other):
		cdef bint value = self.thisptr.CompareTo(other.GetBytes())
		return value


########################################################
## PyIHash
########################################################
cdef class PyIHash:
	cdef THash *thisptr
	def __cinit__(self):
		self.thisptr = NULL

	def __dealloc__(self):
		del self.thisptr

	def GetName(self):
		return self.thisptr.GetName()

	def GetBlockSize(self):
		return self.thisptr.GetBlockSize()

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def GetBufferSize(self):
		return self.thisptr.GetBufferSize()

	def SetBufferSize(self, int32_t value):
		self.thisptr.SetBufferSize(value)

	def Clone(self):
		raise NotImplementedError('Error')

	def ComputeString(self, string value):
		cdef THashResult result = self.thisptr.ComputeString(value)
		return PyIHashResult(result.GetBytes())

	def ComputeBytes(self, vector[uint8_t] value):
		cdef THashResult result = self.thisptr.ComputeBytes(value)
		return PyIHashResult(result.GetBytes())

	def ComputeFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		cdef THashResult result = self.thisptr.ComputeFile(a_filename, a_from, a_length)
		return PyIHashResult(result.GetBytes())

	def Initialize(self):
		self.thisptr.Initialize()

	def TransformBytes(self, vector[uint8_t] a_value, int32_t a_index = 0, int32_t a_length = -1):
		if a_length == -1:
			a_length = len(a_value)

		self.thisptr.TransformBytes(a_value, a_index, a_length)

	def TransformFinal(self):
		cdef THashResult result = self.thisptr.TransformFinal()
		return PyIHashResult(result.GetBytes())

	def TransformString(self, string a_value):
		self.thisptr.TransformString(a_value)

	def TransformFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		self.thisptr.TransformFile(a_filename, a_from, a_length)


########################################################
## PyICRC
########################################################
cdef class PyICRC:
	cdef TCRC *thisptr
	def __cinit__(self):
		self.thisptr = NULL

	def __dealloc__(self):
		del self.thisptr

	def GetName(self):
		return self.thisptr.GetName()

	def GetBlockSize(self):
		return self.thisptr.GetBlockSize()

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def GetBufferSize(self):
		return self.thisptr.GetBufferSize()

	def SetBufferSize(self, int32_t value):
		self.thisptr.SetBufferSize(value)

	def Clone(self):
		raise NotImplementedError('Error')

	def ComputeString(self, string value):
		cdef THashResult result = self.thisptr.ComputeString(value)
		return PyIHashResult(result.GetBytes())

	def ComputeBytes(self, vector[uint8_t] value):
		cdef THashResult result = self.thisptr.ComputeBytes(value)
		return PyIHashResult(result.GetBytes())

	def ComputeFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		cdef THashResult result = self.thisptr.ComputeFile(a_filename, a_from, a_length)
		return PyIHashResult(result.GetBytes())

	def Initialize(self):
		self.thisptr.Initialize()

	def TransformBytes(self, vector[uint8_t] a_value, int32_t a_index = 0, int32_t a_length = -1):
		if a_length == -1:
			a_length = len(a_value)

		self.thisptr.TransformBytes(a_value, a_index, a_length)

	def TransformFinal(self):
		cdef THashResult result = self.thisptr.TransformFinal()
		return PyIHashResult(result.GetBytes())

	def TransformString(self, string a_value):
		self.thisptr.TransformString(a_value)

	def TransformFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		self.thisptr.TransformFile(a_filename, a_from, a_length)


	def GetNames(self):
		return self.thisptr.GetNames()
		
	def GetWidth(self):
		return self.thisptr.GetWidth()

	def GetPolynomial(self):
		return self.thisptr.GetPolynomial()

	def GetInit(self):
		return self.thisptr.GetInit()

	def GetReflectIn(self):
		return self.thisptr.GetReflectIn()

	def GetReflectOut(self):
		return self.thisptr.GetReflectOut()

	def GetXOROut(self):
		return self.thisptr.GetXOROut()

	def GetCheckValue(self):
		return self.thisptr.GetCheckValue()


########################################################
## PyIHashWithKey
########################################################
cdef class PyIHashWithKey:
	cdef THashWithKey *thisptr
	def __cinit__(self):
		self.thisptr = NULL

	def __dealloc__(self):
		del self.thisptr

	def GetName(self):
		return self.thisptr.GetName()

	def GetBlockSize(self):
		return self.thisptr.GetBlockSize()

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def GetBufferSize(self):
		return self.thisptr.GetBufferSize()

	def SetBufferSize(self, int32_t value):
		self.thisptr.SetBufferSize(value)

	def Clone(self):
		raise NotImplementedError('Error')

	def ComputeString(self, string value):
		cdef THashResult result = self.thisptr.ComputeString(value)
		return PyIHashResult(result.GetBytes())

	def ComputeBytes(self, vector[uint8_t] value):
		cdef THashResult result = self.thisptr.ComputeBytes(value)
		return PyIHashResult(result.GetBytes())

	def ComputeFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		cdef THashResult result = self.thisptr.ComputeFile(a_filename, a_from, a_length)
		return PyIHashResult(result.GetBytes())

	def Initialize(self):
		self.thisptr.Initialize()

	def TransformBytes(self, vector[uint8_t] a_value, int32_t a_index = 0, int32_t a_length = -1):
		if a_length == -1:
			a_length = len(a_value)

		self.thisptr.TransformBytes(a_value, a_index, a_length)

	def TransformFinal(self):
		cdef THashResult result = self.thisptr.TransformFinal()
		return PyIHashResult(result.GetBytes())

	def TransformString(self, string a_value):
		self.thisptr.TransformString(a_value)

	def TransformFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		self.thisptr.TransformFile(a_filename, a_from, a_length)


	def GetKey(self):
		return self.thisptr.GetKey()

	def SetKey(self, vector[uint8_t] a_value):
		self.thisptr.SetKey(a_value)
	
	def GetKeyLength(self):
		return self.thisptr.GetKeyLength()


########################################################
## PyIHMAC
########################################################
cdef class PyIHMAC:
	cdef THMAC *thisptr
	def __cinit__(self, PyIHash hash):
		cdef THash ptr = hash.thisptr.Clone()
		self.thisptr = new THMAC(ptr)

	def __dealloc__(self):
		del self.thisptr

	def GetName(self):
		return self.thisptr.GetName()

	def GetBlockSize(self):
		return self.thisptr.GetBlockSize()

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def GetBufferSize(self):
		return self.thisptr.GetBufferSize()

	def SetBufferSize(self, int32_t value):
		self.thisptr.SetBufferSize(value)

	def Clone(self):
		hash = PyIHash()
		del hash.thisptr
		hash.thisptr = new THash(self.thisptr.CloneTHash())
		result = PyIHMAC(hash)
		del result.thisptr
		result.thisptr = new THMAC(self.thisptr.Clone())
		return result

	def ComputeString(self, string value):
		cdef THashResult result = self.thisptr.ComputeString(value)
		return PyIHashResult(result.GetBytes())

	def ComputeBytes(self, vector[uint8_t] value):
		cdef THashResult result = self.thisptr.ComputeBytes(value)
		return PyIHashResult(result.GetBytes())

	def ComputeFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		cdef THashResult result = self.thisptr.ComputeFile(a_filename, a_from, a_length)
		return PyIHashResult(result.GetBytes())

	def Initialize(self):
		self.thisptr.Initialize()

	def TransformBytes(self, vector[uint8_t] a_value, int32_t a_index = 0, int32_t a_length = -1):
		if a_length == -1:
			a_length = len(a_value)

		self.thisptr.TransformBytes(a_value, a_index, a_length)

	def TransformFinal(self):
		cdef THashResult result = self.thisptr.TransformFinal()
		return PyIHashResult(result.GetBytes())

	def TransformString(self, string a_value):
		self.thisptr.TransformString(a_value)

	def TransformFile(self, string a_filename, int64_t a_from = 0, int64_t a_length = -1):
		self.thisptr.TransformFile(a_filename, a_from, a_length)


	def GetKey(self):
		return self.thisptr.GetKey()

	def SetKey(self, vector[uint8_t] a_value):
		self.thisptr.SetKey(a_value)
	
	def GetKeyLength(self):
		return self.thisptr.GetKeyLength()


########################################################
## PyIPBKDF2_HMAC
########################################################
cdef class PyIPBKDF2_HMAC:
	cdef TPBKDF2_HMAC *thisptr
	def __cinit__(self, PyIHash hash, vector[uint8_t] a_password, vector[uint8_t] a_salt, uint32_t a_iterations):
		cdef THash ptr = hash.thisptr.Clone()
		self.thisptr = new TPBKDF2_HMAC(ptr, a_password, a_salt, a_iterations)

	def __dealloc__(self):
		del self.thisptr

	def GetBytes(self, int32_t byte_count):
		return self.thisptr.GetBytes(byte_count)


#######################################################
## PyIBlake2BConfig
########################################################
cdef class PyIBlake2BConfig:
	cdef TBlake2BConfig *thisptr
	def __cinit__(self, int32_t a_hash_size = 64):
		self.thisptr = new TBlake2BConfig(a_hash_size)

	def __dealloc__(self):
		del self.thisptr

	def GetPersonalisation(self):
		return self.thisptr.GetPersonalisation()

	def SetPersonalisation(self, vector[uint8_t] value):
		self.thisptr.SetPersonalisation(value)

	def GetSalt(self):
		return self.thisptr.GetSalt()

	def SetSalt(self, vector[uint8_t] value):
		self.thisptr.SetSalt(value)

	def GetKey(self):
		return self.thisptr.GetKey()

	def SetKey(self, vector[uint8_t] value):
		self.thisptr.SetKey(value)

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def SetHashSize(self, int32_t value):
		self.thisptr.SetHashSize(value)


#######################################################
## PyIBlake2SConfig
########################################################
cdef class PyIBlake2SConfig:
	cdef TBlake2SConfig *thisptr
	def __cinit__(self, int32_t a_hash_size = 32):
		self.thisptr = new TBlake2SConfig(a_hash_size)

	def __dealloc__(self):
		del self.thisptr

	def GetPersonalisation(self):
		return self.thisptr.GetPersonalisation()

	def SetPersonalisation(self, vector[uint8_t] value):
		self.thisptr.SetPersonalisation(value)

	def GetSalt(self):
		return self.thisptr.GetSalt()

	def SetSalt(self, vector[uint8_t] value):
		self.thisptr.SetSalt(value)

	def GetKey(self):
		return self.thisptr.GetKey()

	def SetKey(self, vector[uint8_t] value):
		self.thisptr.SetKey(value)

	def GetHashSize(self):
		return self.thisptr.GetHashSize()

	def SetHashSize(self, int32_t value):
		self.thisptr.SetHashSize(value)

