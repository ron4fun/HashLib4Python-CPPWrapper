# HashLib4Python-CPPWrapper
HashLib4Python is a cython wrapper around [HashLib4CPP](https://www.github.com/ron4fun/HashLib4CPP) library that provides an easy to use interface for computing hashes and checksums of strings, files and bytearrays.

**Supported Algorithms:**

    Non-Cryptographic 32-bits Hash Algorithms: AP, BKDR, Bernstein, Bernstein1, DEK, DJB, 
    ELF, FNV, FNV1a, JS, Jenkins3, Murmur2, MurmurHash3_x86_32, OneAtTime, PJW, RS, 
    Rotating, SDBM, ShiftAndXor, SuperFast, XXHash32.

    Non-Cryptographic 64-bits Algorithms: FNV, FNV1a, Murmur2_64, SipHash2_4, XXHash64.

    Non-Cryptographic 128-bits Algorithms: MurmurHash3_x86_128, MurmurHash3_x64_128. 

    Checksum Algorithms: Adler32, All CRC Variants from CRC3 to CRC64. 

    Cryptographic Algorithms: GOST, Grindahl, HAS160, Haval, MD2, MD4, MD5, Panama, 
    RadioGatun, RIPEMD, RIPEMD128, RIPEMD160, RIPEMD256, RIPEMD320, SHA0, SHA1, SHA2-224,
    SHA2-256, SHA2-384, SHA2-512, SHA2-512-224, SHA2-512-256, SHA3-224, SHA3-256, SHA3-384, 
    SHA3-512,Snefru128, Snefru256, Tiger, Tiger2, WhirlPool.

    HMAC only for Crypto hashes.
    
    PBKDF2_HMAC only for Crypto hashes.


#####Installing the Library:
	Copy "HashFactory.pyd" to your python library package path. Very well tested with 
	Python 2.7, but should also work well with Python3.

#####Non-Cryptographic 32-bits Hash Usage:
	The function call for the hashes without keys accepts 3 parameters
	i.e (a_string, a_PyMODE, an_encoding='UTF-8'): AP, BKDR, Bernstein, Bernstein1, DEK, 
	DJB, ELF, FNV, FNV1a, JS, Jenkins3, OneAtTime, PJW, RS, Rotating, SDBM, ShiftAndXor,
	SuperFast. 

	The function call for hashes with keys (must be within the range of uint32_t else 
	throws an exception) accepts 4 parameters
	i.e (a_string, a_PyMODE, a_key=0, an_encoding='UTF-8'): Murmur2, MurmurHash3_x86_32,
	XXHash32.


**Usage Examples.**

    >>> import HashFactory
    >>>
	>>> mode = HashFactory.PyMODE.a_STRING
	>>> HashFactory.PyHash32.CreateMurmur2("123456789", mode, 0x1234567)
	'2091F2A4'
    >>> HashFactory.PyHash32.CreateShiftAndXor("one hundred", mode, 'utf-16')
	'000464C5'
	>>>


#####Non-Cryptographic 64-bits Hash Usage:
	The function call for the hashes without keys accepts 3 parameters
	i.e (a_string, a_PyMODE, an_encoding='UTF-8'): FNV, FNV1a.

	The function call for hashes with keys (must be within the range of uint32_t for
	Murmur2_64 and uint64_t for XXHash64 else throws an exception) accepts 4 parameters
	i.e (a_string, a_PyMODE, a_key=0, an_encoding='UTF-8'): Murmur2_64, XXHash64.
	
	The function call for hashes with 2 keys (each must be within the range of uint64_t
	else throws an exception) accepts 5 parameters
	i.e (a_string, a_PyMODE, a_key1=0x0001020304050607, a_key2=0x08090A0B0C0D0E0F,
	an_encoding='UTF-8'): SipHash2_4.


**Usage Examples.**

    >>> import HashFactory
    >>>
	>>> mode = HashFactory.PyMODE.a_STRING
	>>> HashFactory.PyHash64.CreateMurmur2("123456789", mode, 0x1234567)
	'E62A6B5A9A18B38D'
    >>> HashFactory.PyHash64.CreateFNV1a("password", mode)
	'4B1A493507B3A318'
	>>> HashFactory.PyHash64.CreateSipHash2_4("", mode, 523523543, 799893466473)
	'A9A07216A8627A43'
	>>> 


#####Non-Cryptographic 128-bits Hash Usage:
	The function call for hashes with keys (must be within the range of uint32_t else
	throws an exception) accepts 4 parameters
	i.e (a_string, a_PyMODE, a_key=0, an_encoding='UTF-8'): MurmurHash3_x86_128, 
	MurmurHash3_x64_128.
	


**Usage Examples.**

    >>> import HashFactory
    >>>
	>>> mode = HashFactory.PyMODE.a_STRING
	>>> HashFactory.PyHash128.CreateMurmurHash3_x86_128("Where am I?", mode, 123456789)
	'622F766154BF065B8307AE5F01424486'
    >>> HashFactory.PyHash128.CreateMurmurHash3_x64_128("Where am I?", mode, 123456789)
	'62A73291675851DBAAD64C68DBAF0B0F'
	>>> 


#####Checksum Hash Usage:
	The function call for Adler32 hash accepts 3 parameters
	i.e (a_string, a_PyMODE, an_encoding='UTF-8').

	The function call for all CRC variants from CRC3 to CRC64 accepts 4 parameters
	i.e (a_PyCRCStandard, a_string, a_PyMODE, an_encoding='UTF-8').


**Usage Examples.**

    >>> import HashFactory
    >>>
	>>> mode = HashFactory.PyMODE.a_STRING
	>>> crc_standard = HashFactory.PyCRCStandard._CRC32
	>>>
	>>> HashFactory.PyChecksum.CreateCRC16_BUYPASS("I love programming", mode)
	'EBDA'
	>>> HashFactory.PyChecksum.CreateCRC64_ECMA("I love programming", mode)
	'7432AB8A85028EEB'
	>>> HashFactory.PyChecksum.CreateCRC(crc_standard, "123456789", mode)
	'CBF43926'
	>>> crc_standard = HashFactory.PyCRCStandard._CRC64_GOISO
    >>> HashFactory.PyChecksum.CreateCRC(crc_standard, "123456789", mode)
	'B90956C775A41001'
	>>>


#####Cryptographic Hash Usage:
	The function call for all the cryptographic hashes accepts 8 parameters
	i.e (a_string, a_PyMODE, a_key="", a_PyHASH=PyHASH._NORMAL, a_salt="", 
	an_iterations=1000, a_byte_count=32, an_encoding='UTF-8')
	
	The key is a string. When calculating PBKDF the a_string and a_PyMODE can be set to 
	any value since they are not used in the internal computation.
	
	


**Usage Examples.**

    >>> import HashFactory
    >>>
	>>> mode = HashFactory.PyMODE.a_STRING
	>>> hmac = HashFactory.PyHASH._HMAC
	>>> pbkdf = HashFactory.PyHASH._PBKDF
	>>>
	>>> HashFactory.PyCrypto.CreateMD5("123456789", mode)
	'25F9E794323B453885F5181F1B624D0B'
	>>> HashFactory.PyCrypto.CreateSHA1("123456789", mode, "password", hmac)
	'0DE64C07F673AB08DFB9FCA384F8DD9FB221DC08'
	>>> HashFactory.PyCrypto.CreateSHA2_256("", mode, "password", pbkdf, "salt",
	100000, 32)
	'0394A2EDE332C9A13EB82E9B24631604C31DF978B4E2F0FBD2C549944F9D79A5'
	>>>
	


###License

This "Software" is Licensed Under  **`Mozilla Public License 2.0`** .