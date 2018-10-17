cdef class PyMurmur2_32(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateMurmur2_32())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyMurmur2_32()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result


cdef class PyMurmurHash3_x86_32(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateMurmurHash3_x86_32())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyMurmurHash3_x86_32()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result


cdef class PyXXHash32(PyIHashWithKey):
	def __cinit__(self):
		self.thisptr = new THashWithKey(HashLib4CPPWrapper.CreateXXHash32())

	def Clone(self):
		cdef THashWithKey hash = self.thisptr.Clone()
		result = PyXXHash32()
		del result.thisptr
		result.thisptr = new THashWithKey(hash)
		return result


cdef class PyAP(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateAP())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyAP()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBernstein(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBernstein())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBernstein()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBernstein1(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBernstein1())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBernstein1()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyBKDR(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateBKDR())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyBKDR()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyDEK(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateDEK())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyDEK()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyDJB(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateDJB())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyDJB()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyELF(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateELF())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyELF()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyFNV_32(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateFNV_32())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyFNV_32()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyFNV1a_32(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateFNV1a_32())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyFNV1a_32()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyJenkins3(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateJenkins3())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyJenkins3()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyJS(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateJS())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyJS()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyOneAtTime(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateOneAtTime())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyOneAtTime()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyPJW(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreatePJW())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyPJW()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRotating(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRotating())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRotating()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyRS(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateRS())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyRS()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySDBM(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSDBM())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySDBM()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PyShiftAndXor(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateShiftAndXor())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PyShiftAndXor()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result

cdef class PySuperFast(PyIHash):
	def __cinit__(self):
		self.thisptr = new THash(HashLib4CPPWrapper.CreateSuperFast())

	def Clone(self):
		cdef THash hash = self.thisptr.Clone()
		result = PySuperFast()
		del result.thisptr
		result.thisptr = new THash(hash)
		return result


########################################################
## PyHash32
########################################################
cdef class PyHash32:
	@staticmethod
	def CreateMurmur2():
		return PyMurmur2_32()

	@staticmethod
	def CreateMurmurHash3_x86_32():
		return PyMurmurHash3_x86_32()

	@staticmethod
	def CreateXXHash32():
		return PyXXHash32()

	@staticmethod
	def CreateAP():
		return PyAP()

	@staticmethod
	def CreateBernstein():
		return PyBernstein()

	@staticmethod
	def CreateBernstein1():
		return PyBernstein1()

	@staticmethod
	def CreateBKDR():
		return PyBKDR()

	@staticmethod
	def CreateDEK():
		return PyDEK()

	@staticmethod
	def CreateDJB():
		return PyDJB()

	@staticmethod
	def CreateELF():
		return PyELF()

	@staticmethod
	def CreateFNV():
		return PyFNV_32()

	@staticmethod
	def CreateFNV1a():
		return PyFNV1a_32()

	@staticmethod
	def CreateJenkins3():
		return PyJenkins3()

	@staticmethod
	def CreateJS():
		return PyJS()

	@staticmethod
	def CreateOneAtTime():
		return PyOneAtTime()

	@staticmethod
	def CreatePJW():
		return PyPJW()

	@staticmethod
	def CreateRotating():
		return PyRotating()

	@staticmethod
	def CreateRS():
		return PyRS()

	@staticmethod
	def CreateSDBM():
		return PySDBM()

	@staticmethod
	def CreateShiftAndXor():
		return PyShiftAndXor()

	@staticmethod
	def CreateSuperFast():
		return PySuperFast()
		