cdef class PyMurmurHash3_x64_128(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateMurmurHash3_x64_128())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyMurmurHash3_x64_128()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result

cdef class PyMurmurHash3_x86_128(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateMurmurHash3_x86_128())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyMurmurHash3_x86_128()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result

########################################################
## PyHash128
########################################################
cdef class PyHash128:
	@staticmethod
	def CreateMurmurHash3_x64_128():
		return PyMurmurHash3_x64_128()

	@staticmethod
	def CreateMurmurHash3_x86_128():
		return PyMurmurHash3_x86_128()
