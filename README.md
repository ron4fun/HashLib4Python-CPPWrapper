# HashLib4Python
HashLib4Python is a cython wrapper around [HashLib4CPP](https://www.github.com/ron4fun/HashLib4CPP) library that provides an easy to use interface for computing hashes and checksums of strings, files and bytearrays.

It also supports **Incremental Hashing**, **Cloning** and **NullDigest**.

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
    SHA3-512, Keccak-224, Keccak-256, Keccak-384, Keccak-512, Snefru128, Snefru256, Tiger,
	Tiger2, WhirlPool, Blake2B, Blake2S, Streebog (GOST3411_2012_256, GOST3411_2012_512).

    HMAC only for Crypto hashes.
    
    PBKDF2_HMAC only for Crypto hashes.


#####Installing the Library:
	Copy "HashLib4Python.pyd" to your python library package path. It has been very well
	tested with Python 2.7, but should also work well with Python3.

#####HashLib4Python Quick Guide:
	# This improved library provides 6 Interfaces (objects) to work with:
	> PyIHash
	> PyIHashResult
	> PyIHashWithKey
	> PyICRC
	> PyIHMAC
	> PyIPBKDF2_HMAC
	> PyIBlake2SConfig
	> PyIBlake2BConfig
	
	# All the hashes will return a PyIHash except:
	> All CRC Variants from CRC3 to CRC64 created from PyCRC or PyChecksum.CreateCRC 
	  function. They all return PyICRC interface.
	  You can get the list of all available CRC variants from PyCRCStandard function.
	> All hashes with key i.e Murmur2, MurmurHash3_x86_32, XXHash32, Murmur2_64,
	  SipHash2_4, XXHash64, MurmurHash3_x86_128, MurmurHash3_x64_128.
	  They all return PyIHashWithKey interface.

	# How to use HMAC
	> Only hash with PyIHash interface can perform HMAC, preferably Crypto hashes.
	> To create a HMAC interface pass the hash instance to the PyIHMAC or
	  PyHMAC.CreateHMAC function.

	# How to use PBKDF2_HMAC
	> Only hash with PyIHash interface can perform HMAC, preferably Crypto hashes.
	> To create a PBKDF2_HMAC interface pass the hash instance to the PyIPBKDF2_HMAC
	  or PyPBKDF2_HMAC.CreatePBKDF2_HMAC function.


**Note**

	The result from the computation of hashes is returned as a PyIHashResult interface.

**Usage Examples.**

    >>> import HashLib4Python
    >>>
	>>> crc_standard = HashFactory.PyCRCStandard._CRC32
	>>> crc = HashLib4Python.PyChecksum.CreateCRC(crc_standard)
	>>> crc.GetName()
	'CRC-32'
	>>>
	>>> md5 = HashLib4Python.PyCrypto.CreateMD5()
	>>> result = md5.ComputeString("")
	>>> result.ToString()
	'D41D8CD98F00B204E9800998ECF8427E'
    >>>
	>>> hmac = HashLib4Python.PyHMAC.CreateHMAC(md5)
	>>> hmac.SetKey(bytearray("password"))
	>>> hmac_clone = hmac.Clone()
	>>> result = hmac.ComputeString("Hello World")
	>>> hmac_clone.Initialize()
	>>> hmac_clone.TransformString("Hello World")
	>>> result_clone = hmac.TransformFinal()
	>>> result.CompareTo(result_clone)
	True
	>>>
	>>> config = HashLib4Python.PyIBlake2SConfig()
	>>> config.SetKey(bytearray("password"))
	>>> blake = HashLib4Python.PyCrypto.CreateBlake2S(config)
	>>> blake.ComputeString("").ToString()
	'94A045C666013340E470E8EC0B2D58A9EF7E7556B6CD7DA6A3F5DFADBE877A21'
	>>>
	


###License

This "Software" is Licensed Under  **`Mozilla Public License 2.0`** .