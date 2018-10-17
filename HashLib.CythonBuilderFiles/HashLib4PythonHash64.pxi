cdef class PyFNV_64(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateFNV_64())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyFNV_64()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyFNV1a_64(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateFNV1a_64())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyFNV1a_64()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyMurmur2_64(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateMurmur2_64())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyMurmur2_64()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result

cdef class PyXXHash64(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateXXHash64())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyXXHash64()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result

cdef class PySipHash2_4(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateSipHash2_4())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PySipHash2_4()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result

########################################################
## PyHash64
########################################################
cdef class PyHash64:
	@staticmethod
	def CreateFNV():
		return PyFNV_64()

	@staticmethod
	def CreateFNV1a():
		return PyFNV1a_64()

	@staticmethod
	def CreateMurmur2():
		return PyMurmur2_64()
		
	@staticmethod
	def CreateXXHash64():
		return PyXXHash64()

	@staticmethod
	def CreateSipHash2_4():
		return PySipHash2_4()

