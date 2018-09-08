#include "stdafx.h"
#include "HashLibWrapper.h"
#include "Base\HlpHashFactory.h"

HashLibByteArray convertStringToBytes(const string &value) 
{
	vector<uint8_t> bytes(value.begin(), value.end());
	return bytes;
}

string ComputeWithoutKey(IHash hash, const string &s, MODE state)
{
	switch (state)
	{
	case a_STRING:
		return hash->ComputeString(s)->ToString();
	case a_FILE:
		return hash->ComputeFile(s)->ToString();
	}
	throw ArgumentHashLibException("Invalid mode");
} // end ComputeWithoutKey

string ComputeWithoutKey(IHMAC hash, const string &s, MODE state)
{
	switch (state)
	{
	case a_STRING:
		return hash->ComputeString(s)->ToString();
	case a_FILE:
		return hash->ComputeFile(s)->ToString();
	}
	throw ArgumentHashLibException("Invalid mode");
} // end ComputeWithoutKey

string ComputeWithOneKey(IHashWithKey hash, const string &s, MODE state, const uint32_t key)
{
	if (key) hash->SetKey(BitConverter::GetBytes(key));

	return ComputeWithoutKey(hash, s, state);
} // end ComputeWithoutKey

string ComputeWithOneKey(IHashWithKey hash, const string &s, MODE state, const uint64_t key)
{
	if (key) hash->SetKey(BitConverter::GetBytes(key));

	return ComputeWithoutKey(hash, s, state);
} // end ComputeWithoutKey

string ComputeWithTwoKeys(IHashWithKey hash, const string &s, MODE state, const uint64_t key1, const uint64_t key2)
{
	if (key1) 
	{
		HashLibByteArray bytes1 = Converters::ReadUInt64AsBytesLE(key1);
		if (key2) 
		{
			HashLibByteArray bytes2 = Converters::ReadUInt64AsBytesLE(key2);
			bytes2.insert(bytes2.end(), bytes1.begin(), bytes1.end());
			bytes1 = bytes2;
		}

		reverse(bytes1.begin(), bytes1.end());
		
		hash->SetKey(bytes1);
	}

	return ComputeWithoutKey(hash, s, state);
} // end ComputeWithoutKey

string cryptoHashHandler(IHash hash, const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHMAC hmac;

	switch (hash_type)
	{
	case a_NORMAL:
		return ComputeWithoutKey(hash, s, state);
	case a_HMAC:
		hmac = HashFactory::HMAC::CreateHMAC(hash);
		hmac->SetKey(Converters::ConvertStringToBytes(key));
		return ComputeWithoutKey(hmac, s, state);
	case a_PBKDF:
		HashLibByteArray Key = HashFactory::PBKDF2_HMAC::CreatePBKDF2_HMAC(hash, 
			Converters::ConvertStringToBytes(key),
			Converters::ConvertStringToBytes(salt), iterations)->GetBytes(bc);

		return Converters::ConvertBytesToHexString(Key, false);
	}
	throw ArgumentHashLibException("Invalid mode");
}

// ====================== Checksum ======================

string HashFactoryWrapper::CreateCRC(const CRCStandard &value, const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateCRC(value);
	return ComputeWithoutKey(hs, s, state);
} // end function CreateCRC

string HashFactoryWrapper::CreateCRC16_BUYPASS(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateCRC16_BUYPASS();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateCRC16_BUYPASS

string HashFactoryWrapper::CreateCRC32_PKZIP(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateCRC32_PKZIP();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateCRC32_PKZIP

string HashFactoryWrapper::CreateCRC32_CASTAGNOLI(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateCRC32_CASTAGNOLI();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateCRC32_CASTAGNOLI

string HashFactoryWrapper::CreateCRC64_ECMA(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateCRC64_ECMA();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateCRC64_ECMA

string HashFactoryWrapper::CreateAdler32(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Checksum::CreateAdler32();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateAdler32

// ====================== Crypto ======================
string HashFactoryWrapper::CreateGost(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateGost();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateGost

string HashFactoryWrapper::CreateGrindahl256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateGrindahl256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateGrindahl256

string HashFactoryWrapper::CreateGrindahl512(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateGrindahl512();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateGrindahl512

string HashFactoryWrapper::CreateHAS160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHAS160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHAS160

string HashFactoryWrapper::CreateHaval_3_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_3_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_3_128

string HashFactoryWrapper::CreateHaval_3_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_3_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_3_160

string HashFactoryWrapper::CreateHaval_3_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_3_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_3_192

string HashFactoryWrapper::CreateHaval_3_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_3_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_3_224

string HashFactoryWrapper::CreateHaval_3_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_3_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_3_256

string HashFactoryWrapper::CreateHaval_4_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_4_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_4_128

string HashFactoryWrapper::CreateHaval_4_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_4_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_4_160

string HashFactoryWrapper::CreateHaval_4_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_4_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_4_192

string HashFactoryWrapper::CreateHaval_4_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_4_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_4_224

string HashFactoryWrapper::CreateHaval_4_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_4_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_4_256

string HashFactoryWrapper::CreateHaval_5_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_5_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_5_128

string HashFactoryWrapper::CreateHaval_5_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_5_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_5_160

string HashFactoryWrapper::CreateHaval_5_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_5_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_5_192

string HashFactoryWrapper::CreateHaval_5_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_5_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_5_224

string HashFactoryWrapper::CreateHaval_5_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateHaval_5_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateHaval_5_256

string HashFactoryWrapper::CreateMD2(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateMD2();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateMD2

string HashFactoryWrapper::CreateMD4(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateMD4();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateMD4

string HashFactoryWrapper::CreateMD5(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateMD5();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateMD5

string HashFactoryWrapper::CreatePanama(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreatePanama();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreatePanama

string HashFactoryWrapper::CreateRIPEMD(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRIPEMD();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRIPEMD

string HashFactoryWrapper::CreateRIPEMD128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRIPEMD128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRIPEMD128

string HashFactoryWrapper::CreateRIPEMD160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRIPEMD160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRIPEMD160

string HashFactoryWrapper::CreateRIPEMD256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRIPEMD256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRIPEMD256

string HashFactoryWrapper::CreateRIPEMD320(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRIPEMD320();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRIPEMD320

string HashFactoryWrapper::CreateRadioGatun32(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRadioGatun32();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRadioGatun32

string HashFactoryWrapper::CreateRadioGatun64(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateRadioGatun64();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateRadioGatun64

string HashFactoryWrapper::CreateSHA0(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA0();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA0

string HashFactoryWrapper::CreateSHA1(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA1();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA1

string HashFactoryWrapper::CreateSHA2_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_224

string HashFactoryWrapper::CreateSHA2_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_256

string HashFactoryWrapper::CreateSHA2_384(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_384();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_384

string HashFactoryWrapper::CreateSHA2_512(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_512();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_512

string HashFactoryWrapper::CreateSHA2_512_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_512_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_512_224

string HashFactoryWrapper::CreateSHA2_512_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA2_512_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA2_512_256

string HashFactoryWrapper::CreateSHA3_224(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA3_224();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA3_224

string HashFactoryWrapper::CreateSHA3_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA3_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA3_256

string HashFactoryWrapper::CreateSHA3_384(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA3_384();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA3_384

string HashFactoryWrapper::CreateSHA3_512(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSHA3_512();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSHA3_512

string HashFactoryWrapper::CreateSnefru_8_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSnefru_8_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSnefru_8_128

string HashFactoryWrapper::CreateSnefru_8_256(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateSnefru_8_256();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateSnefru_8_256

string HashFactoryWrapper::CreateTiger2_3_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_3_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_3_128

string HashFactoryWrapper::CreateTiger2_3_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_3_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_3_160

string HashFactoryWrapper::CreateTiger2_3_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_3_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_3_192

string HashFactoryWrapper::CreateTiger2_4_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_4_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_4_128

string HashFactoryWrapper::CreateTiger2_4_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_4_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_4_160

string HashFactoryWrapper::CreateTiger2_4_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_4_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_4_192

string HashFactoryWrapper::CreateTiger2_5_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_5_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_5_128

string HashFactoryWrapper::CreateTiger2_5_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_5_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_5_160

string HashFactoryWrapper::CreateTiger2_5_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger2_5_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger2_5_192

string HashFactoryWrapper::CreateTiger_3_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_3_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_3_128

string HashFactoryWrapper::CreateTiger_3_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_3_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_3_160

string HashFactoryWrapper::CreateTiger_3_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_3_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_3_192

string HashFactoryWrapper::CreateTiger_4_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_4_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_4_128

string HashFactoryWrapper::CreateTiger_4_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_4_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_4_160

string HashFactoryWrapper::CreateTiger_4_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_4_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_4_192

string HashFactoryWrapper::CreateTiger_5_128(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_5_128();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_5_128

string HashFactoryWrapper::CreateTiger_5_160(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_5_160();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_5_160

string HashFactoryWrapper::CreateTiger_5_192(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateTiger_5_192();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateTiger_5_192

string HashFactoryWrapper::CreateWhirlPool(const string &s, const MODE &state, const string &key, const HASH &hash_type, const string &salt, const uint32_t iterations, const int32_t bc)
{
	IHash hs = HashFactory::Crypto::CreateWhirlPool();
	return cryptoHashHandler(hs, s, state, key, hash_type, salt, iterations, bc);
} // end function CreateWhirlPool

// ====================== Hash32 ======================
string HashFactoryWrapper::CreateAP(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateAP();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateAP

string HashFactoryWrapper::CreateBernstein(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateBernstein();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateBernstein

string HashFactoryWrapper::CreateBernstein1(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateBernstein1();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateBernstein1

string HashFactoryWrapper::CreateBKDR(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateBKDR();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateBKDR

string HashFactoryWrapper::CreateDEK(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateDEK();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateDEK

string HashFactoryWrapper::CreateDJB(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateDJB();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateDJB

string HashFactoryWrapper::CreateELF(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateELF();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateELF

string HashFactoryWrapper::CreateFNV_32(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateFNV();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateFNV

string HashFactoryWrapper::CreateFNV1a_32(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateFNV1a();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateFNV1a

string HashFactoryWrapper::CreateJenkins3(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateJenkins3();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateJenkins3

string HashFactoryWrapper::CreateJS(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateJS();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateJS

string HashFactoryWrapper::CreateMurmur2_32(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash32::CreateMurmur2();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateMurmur2

string HashFactoryWrapper::CreateMurmurHash3_x86_32(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash32::CreateMurmurHash3_x86_32();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateMurmurHash3_x86_32

string HashFactoryWrapper::CreateOneAtTime(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateOneAtTime();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateOneAtTime

string HashFactoryWrapper::CreatePJW(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreatePJW();
	return ComputeWithoutKey(hs, s, state);
} // end function CreatePJW

string HashFactoryWrapper::CreateRotating(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateRotating();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateRotating

string HashFactoryWrapper::CreateRS(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateRS();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateRS

string HashFactoryWrapper::CreateSDBM(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateSDBM();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateSDBM

string HashFactoryWrapper::CreateShiftAndXor(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateShiftAndXor();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateShiftAndXor

string HashFactoryWrapper::CreateSuperFast(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash32::CreateSuperFast();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateSuperFast

string HashFactoryWrapper::CreateXXHash32(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash32::CreateXXHash32();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateXXHash32

// ====================== Hash64 ======================
string HashFactoryWrapper::CreateFNV_64(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash64::CreateFNV();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateFNV

string HashFactoryWrapper::CreateFNV1a_64(const string &s, const MODE &state)
{
	IHash hs = HashFactory::Hash64::CreateFNV1a();
	return ComputeWithoutKey(hs, s, state);
} // end function CreateFNV1a

string HashFactoryWrapper::CreateMurmur2_64(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash64::CreateMurmur2();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateMurmur2

string HashFactoryWrapper::CreateXXHash64(const string &s, const MODE &state, const uint64_t key)
{
	IHashWithKey hs = HashFactory::Hash64::CreateXXHash64();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateXXHash64

string HashFactoryWrapper::CreateSipHash2_4(const string &s, const MODE &state, const uint64_t key1, const uint64_t key2)
{
	IHashWithKey hs = HashFactory::Hash64::CreateSipHash2_4();
	return ComputeWithTwoKeys(hs, s, state, key1, key2);
} // end function CreateSipHash2_4

// ====================== Hash128 ======================
string HashFactoryWrapper::CreateMurmurHash3_x64_128(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash128::CreateMurmurHash3_x64_128();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateMurmurHash3_x64_128

string HashFactoryWrapper::CreateMurmurHash3_x86_128(const string &s, const MODE &state, const uint32_t key)
{
	IHashWithKey hs = HashFactory::Hash128::CreateMurmurHash3_x86_128();
	return ComputeWithOneKey(hs, s, state, key);
} // end function CreateMurmurHash3_x86_128
