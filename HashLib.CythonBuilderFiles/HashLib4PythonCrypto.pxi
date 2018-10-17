cdef class PyBlake2B(PyIHash):
	def __cinit__(self, PyIBlake2BConfig config = None):
		cdef TBlake2BConfig *config_ptr = NULL
		if config:
			config_ptr = config.thisptr

		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2B(config_ptr))

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2B()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2B_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2B_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2B_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2B_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2B_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2B_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2B_384(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2B_384())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2B_384()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2B_512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2B_512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2B_512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2S(PyIHash):
	def __cinit__(self, PyIBlake2SConfig config = None):
		cdef TBlake2SConfig *config_ptr = NULL
		if config:
			config_ptr = config.thisptr

		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2S(config_ptr))

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2S()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2S_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2S_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2S_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2S_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2S_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2S_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2S_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2S_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2S_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBlake2S_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBlake2S_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBlake2S_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyGost(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateGost())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyGost()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyGOST3411_2012_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateGOST3411_2012_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyGOST3411_2012_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyGOST3411_2012_512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateGOST3411_2012_512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyGOST3411_2012_512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyGrindahl256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateGrindahl256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyGrindahl256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyGrindahl512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateGrindahl512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyGrindahl512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHAS160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHAS160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHAS160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_3_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_3_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_3_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_3_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_3_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_3_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_3_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_3_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_3_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_3_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_3_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_3_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_3_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_3_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_3_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_4_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_4_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_4_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_4_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_4_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_4_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_4_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_4_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_4_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_4_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_4_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_4_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_4_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_4_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_4_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_5_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_5_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_5_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_5_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_5_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_5_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_5_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_5_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_5_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_5_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_5_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_5_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyHaval_5_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateHaval_5_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyHaval_5_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyMD2(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateMD2())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyMD2()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyMD4(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateMD4())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyMD4()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyMD5(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateMD5())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyMD5()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyPanama(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreatePanama())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyPanama()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRIPEMD(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRIPEMD())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRIPEMD()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRIPEMD128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRIPEMD128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRIPEMD128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRIPEMD160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRIPEMD160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRIPEMD160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRIPEMD256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRIPEMD256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRIPEMD256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRIPEMD320(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRIPEMD320())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRIPEMD320()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRadioGatun32(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRadioGatun32())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRadioGatun32()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRadioGatun64(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRadioGatun64())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRadioGatun64()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA0(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA0())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA0()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA1(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA1())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA1()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_384(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_384())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_384()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_512_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_512_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_512_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA2_512_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA2_512_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA2_512_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA3_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA3_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA3_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA3_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA3_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA3_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA3_384(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA3_384())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA3_384()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySHA3_512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSHA3_512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySHA3_512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyKeccak_224(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateKeccak_224())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyKeccak_224()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyKeccak_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateKeccak_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyKeccak_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyKeccak_384(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateKeccak_384())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyKeccak_384()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyKeccak_512(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateKeccak_512())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyKeccak_512()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySnefru_8_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSnefru_8_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySnefru_8_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySnefru_8_256(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSnefru_8_256())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySnefru_8_256()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_3_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_3_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_3_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_3_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_3_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_3_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_3_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_3_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_3_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_4_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_4_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_4_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_4_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_4_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_4_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_4_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_4_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_4_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_5_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_5_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_5_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_5_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_5_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_5_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger2_5_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger2_5_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger2_5_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_3_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_3_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_3_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_3_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_3_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_3_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_3_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_3_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_3_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_4_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_4_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_4_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_4_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_4_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_4_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_4_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_4_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_4_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_5_128(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_5_128())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_5_128()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_5_160(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_5_160())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_5_160()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyTiger_5_192(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateTiger_5_192())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyTiger_5_192()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyWhirlPool(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateWhirlPool())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyWhirlPool()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

########################################################
## PyCrypto
########################################################
cdef class PyCrypto:
	@staticmethod
	def CreateBlake2B(PyIBlake2BConfig config = None):
		return PyBlake2B(config)

	@staticmethod
	def CreateBlake2B_160():
		return PyBlake2B_160()

	@staticmethod
	def CreateBlake2B_256():
		return PyBlake2B_256()

	@staticmethod
	def CreateBlake2B_384():
		return PyBlake2B_384()

	@staticmethod
	def CreateBlake2B_512():
		return PyBlake2B_512()

	@staticmethod
	def CreateBlake2S(PyIBlake2SConfig config = None):
		return PyBlake2S(config)

	@staticmethod
	def CreateBlake2S_128():
		return PyBlake2S_128

	@staticmethod
	def CreateBlake2S_160():
		return PyBlake2S_160()

	@staticmethod
	def CreateBlake2S_224():
		return PyBlake2S_224()

	@staticmethod
	def CreateBlake2S_256():
		return PyBlake2S_256()

	@staticmethod
	def CreateGost():
		return PyGost()

	@staticmethod
	def CreateGOST3411_2012_256():
		return PyGOST3411_2012_256()

	@staticmethod
	def CreateGOST3411_2012_512():
		return PyGOST3411_2012_512()

	@staticmethod
	def CreateGrindahl256():
		return PyGrindahl256()

	@staticmethod
	def CreateGrindahl512():
		return PyGrindahl512()

	@staticmethod
	def CreateHAS160():
		return PyHAS160()

	@staticmethod
	def CreateHaval_3_128():
		return PyHaval_3_128()

	@staticmethod
	def CreateHaval_3_160():
		return PyHaval_3_160()

	@staticmethod
	def CreateHaval_3_192():
		return PyHaval_3_192()

	@staticmethod
	def CreateHaval_3_224():
		return PyHaval_3_224()

	@staticmethod
	def CreateHaval_3_256():
		return PyHaval_3_256()

	@staticmethod
	def CreateHaval_4_128():
		return PyHaval_4_128()

	@staticmethod
	def CreateHaval_4_160():
		return PyHaval_4_160()

	@staticmethod
	def CreateHaval_4_192():
		return PyHaval_4_192()

	@staticmethod
	def CreateHaval_4_224():
		return PyHaval_4_224()

	@staticmethod
	def CreateHaval_4_256():
		return PyHaval_4_256()

	@staticmethod
	def CreateHaval_5_128():
		return PyHaval_5_128()

	@staticmethod
	def CreateHaval_5_160():
		return PyHaval_5_160()

	@staticmethod
	def CreateHaval_5_192():
		return PyHaval_5_192()

	@staticmethod
	def CreateHaval_5_224():
		return PyHaval_5_224()

	@staticmethod
	def CreateHaval_5_256():
		return PyHaval_5_256()

	@staticmethod
	def CreateMD2():
		return PyMD2()

	@staticmethod
	def CreateMD4():
		return PyMD4()

	@staticmethod
	def CreateMD5():
		return PyMD5()

	@staticmethod
	def CreatePanama():
		return PyPanama()

	@staticmethod
	def CreateRIPEMD():
		return PyRIPEMD()

	@staticmethod
	def CreateRIPEMD128():
		return PyRIPEMD128()

	@staticmethod
	def CreateRIPEMD160():
		return PyRIPEMD160()

	@staticmethod
	def CreateRIPEMD256():
		return PyRIPEMD256()

	@staticmethod
	def CreateRIPEMD320():
		return PyRIPEMD320()

	@staticmethod
	def CreateRadioGatun32():
		return PyRadioGatun32()

	@staticmethod
	def CreateRadioGatun64():
		return PyRadioGatun64()

	@staticmethod
	def CreateSHA0():
		return PySHA0()

	@staticmethod
	def CreateSHA1():
		return PySHA1()

	@staticmethod
	def CreateSHA2_224():
		return PySHA2_224()

	@staticmethod
	def CreateSHA2_256():
		return PySHA2_256()

	@staticmethod
	def CreateSHA2_384():
		return PySHA2_384()

	@staticmethod
	def CreateSHA2_512():
		return PySHA2_512()

	@staticmethod
	def CreateSHA2_512_224():
		return PySHA2_512_224()

	@staticmethod
	def CreateSHA2_512_256():
		return PySHA2_512_256()

	@staticmethod
	def CreateSHA3_224():
		return PySHA3_224()

	@staticmethod
	def CreateSHA3_256():
		return PySHA3_256()

	@staticmethod
	def CreateSHA3_384():
		return PySHA3_384()

	@staticmethod
	def CreateSHA3_512():
		return PySHA3_512()

	@staticmethod
	def CreateKeccak_224():
		return PyKeccak_224()

	@staticmethod
	def CreateKeccak_256():
		return PyKeccak_256()

	@staticmethod
	def CreateKeccak_384():
		return PyKeccak_384()

	@staticmethod
	def CreateKeccak_512():
		return PyKeccak_512()

	@staticmethod
	def CreateSnefru_8_128():
		return PySnefru_8_128()

	@staticmethod
	def CreateSnefru_8_256():
		return PySnefru_8_256()

	@staticmethod
	def CreateTiger2_3_128():
		return PyTiger2_3_128()

	@staticmethod
	def CreateTiger2_3_160():
		return PyTiger2_3_160()

	@staticmethod
	def CreateTiger2_3_192():
		return PyTiger2_3_192()

	@staticmethod
	def CreateTiger2_4_128():
		return PyTiger2_4_128()

	@staticmethod
	def CreateTiger2_4_160():
		return PyTiger2_4_160()

	@staticmethod
	def CreateTiger2_4_192():
		return PyTiger2_4_192()

	@staticmethod
	def CreateTiger2_5_128():
		return PyTiger2_5_128()

	@staticmethod
	def CreateTiger2_5_160():
		return PyTiger2_5_160()

	@staticmethod
	def CreateTiger2_5_192():
		return PyTiger2_5_192()

	@staticmethod
	def CreateTiger_3_128():
		return PyTiger_3_128()

	@staticmethod
	def CreateTiger_3_160():
		return PyTiger_3_160()

	@staticmethod
	def CreateTiger_3_192():
		return PyTiger_3_192()

	@staticmethod
	def CreateTiger_4_128():
		return PyTiger_4_128()

	@staticmethod
	def CreateTiger_4_160():
		return PyTiger_4_160()

	@staticmethod
	def CreateTiger_4_192():
		return PyTiger_4_192()

	@staticmethod
	def CreateTiger_5_128():
		return PyTiger_5_128()

	@staticmethod
	def CreateTiger_5_160():
		return PyTiger_5_160()

	@staticmethod
	def CreateTiger_5_192():
		return PyTiger_5_192()

	@staticmethod
	def CreateWhirlPool():
		return PyWhirlPool()

