#ifndef HASHLIB4CPPWRAPPER_H
#define HASHLIB4CPPWRAPPER_H


#include "Utils\HlpHashLibTypes.h"
#include "Interfaces\HlpIHash.h"
#include "Interfaces\HlpIHashResult.h"
#include "Interfaces\HlpICRC.h"
#include "Interfaces\HlpIHashInfo.h"
#include "Interfaces\IBlake2BConfigurations\HlpIBlake2BConfig.h"
#include "Interfaces\IBlake2SConfigurations\HlpIBlake2SConfig.h"

// ====================== TConverters Implementation ======================
////////////////////
// TConverters
///////////////////
class TConverters
{
public:
	static string toUpper(const string &);
	static uint32_t ReadBytesAsUInt32LE(const HashLibByteArray &, const int32_t);
	static uint64_t ReadBytesAsUInt64LE(const HashLibByteArray &, const int32_t);
	static HashLibByteArray ReadUInt32AsBytesLE(const uint32_t);
	static HashLibByteArray ReadUInt64AsBytesLE(const uint64_t);
	static HashLibByteArray ConvertHexStringToBytes(const string &);
	static HashLibByteArray ConvertStringToBytes(const string &);
	static string ConvertBytesToHexString(const HashLibByteArray &, const bool);

};


// ====================== THashResult Class ======================
////////////////////
// THashResult Class
///////////////////

class THashResult
{
public:
	THashResult();

	THashResult(IHashResult ptr);

	THashResult(const HashLibByteArray &value);

	THashResult(const THashResult &value);

	HashLibByteArray GetBytes() const;
	uint8_t GetUInt8() const;
	uint16_t GetUInt16() const;
	uint32_t GetUInt32() const;
	int32_t GetInt32() const;
	uint64_t GetUInt64() const;
	string ToString(const bool a_group = false) const;
	int32_t GetHashCode() const;
	bool CompareTo(const THashResult &a_hashResult) const;
	bool CompareTo(const HashLibByteArray &value) const;

private:
	IHashResult ptr = nullptr;
};


// ====================== THash Class ======================
////////////////////
// THash Class
///////////////////

class THash
{
public:
	THash();

	THash(IHash ptr);

	THash(const THash &value);

	IHash Copy();

	string GetName() const;
	int32_t GetBlockSize() const;
	int32_t GetHashSize() const;
	int32_t GetBufferSize() const;
	void SetBufferSize(const int32_t value);

	THash Clone() const;

	THashResult ComputeString(const string &a_data);
	THashResult ComputeBytes(const HashLibByteArray &a_data);
	THashResult ComputeFile(const string &a_file_name,
		const int64_t a_from = 0, const int64_t a_length = -1);

	void Initialize();

	void TransformBytes(const HashLibByteArray &a_data, int32_t a_index, int32_t a_length);
	void TransformBytes(const HashLibByteArray &a_data, const int32_t a_index);
	void TransformBytes(const HashLibByteArray &a_data);

	THashResult TransformFinal();

	void TransformString(const string &a_data);
	void TransformFile(const string &a_file_name,
		const int64_t a_from = 0, const int64_t a_length = -1);

private:
	IHash ptr = nullptr;

};


// ====================== TCRC Class ======================
////////////////////
// TCRC Class
///////////////////

class TCRC : public THash
{
public:
	TCRC();

	TCRC(ICRC ptr);

	TCRC(const TCRC &value);

	TCRC Clone() const;

	HashLibStringArray GetNames() const;
	int32_t GetWidth() const;
	uint64_t GetPolynomial() const;
	uint64_t GetInit() const;
	bool GetReflectIn() const;
	bool GetReflectOut() const;
	uint64_t GetXOROut() const;
	uint64_t GetCheckValue() const;

private:
	ICRC ptr = nullptr;

};


// ====================== THashWithKey Class ======================
////////////////////
// THashWithKey Class
///////////////////

class THashWithKey : public THash
{
public:
	THashWithKey();

	THashWithKey(IHashWithKey ptr);

	THashWithKey(const THashWithKey &value);

	THashWithKey Clone() const;

	HashLibByteArray GetKey() const;
	void SetKey(const HashLibByteArray &value);
	int32_t GetKeyLength() const;

private:
	IHashWithKey ptr = nullptr;

};


// ====================== THMAC Class ======================
////////////////////
// THMAC Class
///////////////////

class THMAC
{
public:
	THMAC();

	THMAC(THash ptr);
	
	THMAC(const THMAC &value);

	string GetName() const;
	int32_t GetBlockSize() const;
	int32_t GetHashSize() const;
	int32_t GetBufferSize() const;
	void SetBufferSize(const int32_t value);

	THMAC Clone() const;

	THash CloneTHash() const;

	THashResult ComputeString(const string &a_data);
	THashResult ComputeBytes(const HashLibByteArray &a_data);
	THashResult ComputeFile(const string &a_file_name,
		const int64_t a_from = 0, const int64_t a_length = -1);

	void Initialize();

	void TransformBytes(const HashLibByteArray &a_data, int32_t a_index, int32_t a_length);
	void TransformBytes(const HashLibByteArray &a_data, const int32_t a_index);
	void TransformBytes(const HashLibByteArray &a_data);

	THashResult TransformFinal();

	void TransformString(const string &a_data);
	void TransformFile(const string &a_file_name,
		const int64_t a_from = 0, const int64_t a_length = -1);
	
	HashLibByteArray GetKey() const;
	void SetKey(const HashLibByteArray &value);
	int32_t GetKeyLength() const;

private:
	IHMAC ptr = nullptr;

};


// ====================== TPBKDF2_HMAC Class ======================
////////////////////
// TPBKDF2_HMAC Class
///////////////////

class TPBKDF2_HMAC
{
public:
	TPBKDF2_HMAC();

	TPBKDF2_HMAC(THash ptr, const HashLibByteArray &, const HashLibByteArray &, const uint32_t);

	TPBKDF2_HMAC(const TPBKDF2_HMAC &value);

	HashLibByteArray GetBytes(const int32_t bc);

private:
	IPBKDF2_HMAC ptr = nullptr;

};

// ====================== TBlake2BConfig Class ======================
////////////////////
// TBlake2BConfig Class
///////////////////

class TBlake2BConfig
{
public:
	TBlake2BConfig();

	TBlake2BConfig(const int32_t a_hash_size);

	TBlake2BConfig(const TBlake2BConfig &value);
	
	IBlake2BConfig GetConfig() const;

	HashLibByteArray GetPersonalisation() const;
	void SetPersonalisation(const HashLibByteArray &value);
	HashLibByteArray GetSalt() const;
	void SetSalt(const HashLibByteArray &value);
	HashLibByteArray GetKey() const;
	void SetKey(const HashLibByteArray &value);
	int32_t GetHashSize() const;
	void SetHashSize(const int32_t value);

private:
	IBlake2BConfig ptr = nullptr;

};

// ====================== TBlake2SConfig Class ======================
////////////////////
// TBlake2SConfig Class
///////////////////

class TBlake2SConfig
{
public:
	TBlake2SConfig();

	TBlake2SConfig(const int32_t a_hash_size);

	TBlake2SConfig(const TBlake2SConfig &value);

	IBlake2SConfig GetConfig() const;

	HashLibByteArray GetPersonalisation() const;
	void SetPersonalisation(const HashLibByteArray &value);
	HashLibByteArray GetSalt() const;
	void SetSalt(const HashLibByteArray &value);
	HashLibByteArray GetKey() const;
	void SetKey(const HashLibByteArray &value);
	int32_t GetHashSize() const;
	void SetHashSize(const int32_t value);

private:
	IBlake2SConfig ptr = nullptr;

};

// ====================== HashLib4CPPWrapper Class ======================
////////////////////
// HashLib4CPPWrapper
///////////////////

class HashLib4CPPWrapper
{
public:
	// ====================== NullDigest ======================
	static IHash CreateNullDigest();

	// ====================== Checksum ======================
	static ICRC CreateCRC(const CRCStandard &);
	static IHash CreateCRC16_BUYPASS();
	static IHash CreateCRC32_PKZIP();
	static IHash CreateCRC32_CASTAGNOLI();
	static IHash CreateCRC64_ECMA();
	static IHash CreateAdler32();

	// ====================== Crypto ======================
	static IHash CreateBlake2B(const TBlake2BConfig *config = nullptr);
	static IHash CreateBlake2B_160();
	static IHash CreateBlake2B_256();
	static IHash CreateBlake2B_384();
	static IHash CreateBlake2B_512();
	static IHash CreateBlake2S(const TBlake2SConfig *config = nullptr);
	static IHash CreateBlake2S_128();
	static IHash CreateBlake2S_160();
	static IHash CreateBlake2S_224();
	static IHash CreateBlake2S_256();
	static IHash CreateGost();
	static IHash CreateGOST3411_2012_256();
	static IHash CreateGOST3411_2012_512();
	static IHash CreateGrindahl256();
	static IHash CreateGrindahl512();
	static IHash CreateHAS160();
	static IHash CreateHaval_3_128();
	static IHash CreateHaval_3_160();
	static IHash CreateHaval_3_192();
	static IHash CreateHaval_3_224();
	static IHash CreateHaval_3_256();
	static IHash CreateHaval_4_128();
	static IHash CreateHaval_4_160();
	static IHash CreateHaval_4_192();
	static IHash CreateHaval_4_224();
	static IHash CreateHaval_4_256();
	static IHash CreateHaval_5_128();
	static IHash CreateHaval_5_160();
	static IHash CreateHaval_5_192();
	static IHash CreateHaval_5_224();
	static IHash CreateHaval_5_256();
	static IHash CreateMD2();
	static IHash CreateMD4();
	static IHash CreateMD5();
	static IHash CreatePanama();
	static IHash CreateRIPEMD();
	static IHash CreateRIPEMD128();
	static IHash CreateRIPEMD160();
	static IHash CreateRIPEMD256();
	static IHash CreateRIPEMD320();
	static IHash CreateRadioGatun32();
	static IHash CreateRadioGatun64();
	static IHash CreateSHA0();
	static IHash CreateSHA1();
	static IHash CreateSHA2_224();
	static IHash CreateSHA2_256();
	static IHash CreateSHA2_384();
	static IHash CreateSHA2_512();
	static IHash CreateSHA2_512_224();
	static IHash CreateSHA2_512_256();
	static IHash CreateSHA3_224();
	static IHash CreateSHA3_256();
	static IHash CreateSHA3_384();
	static IHash CreateSHA3_512();
	static IHash CreateKeccak_224();
	static IHash CreateKeccak_256();
	static IHash CreateKeccak_384();
	static IHash CreateKeccak_512();
	static IHash CreateSnefru_8_128();
	static IHash CreateSnefru_8_256();
	static IHash CreateTiger2_3_128();
	static IHash CreateTiger2_3_160();
	static IHash CreateTiger2_3_192();
	static IHash CreateTiger2_4_128();
	static IHash CreateTiger2_4_160();
	static IHash CreateTiger2_4_192();
	static IHash CreateTiger2_5_128();
	static IHash CreateTiger2_5_160();
	static IHash CreateTiger2_5_192();
	static IHash CreateTiger_3_128();
	static IHash CreateTiger_3_160();
	static IHash CreateTiger_3_192();
	static IHash CreateTiger_4_128();
	static IHash CreateTiger_4_160();
	static IHash CreateTiger_4_192();
	static IHash CreateTiger_5_128();
	static IHash CreateTiger_5_160();
	static IHash CreateTiger_5_192();
	static IHash CreateWhirlPool();
	
	// ====================== Hash32 ======================
	static IHash CreateAP();
	static IHash CreateBernstein();
	static IHash CreateBernstein1();
	static IHash CreateBKDR();
	static IHash CreateDEK();
	static IHash CreateDJB();
	static IHash CreateELF();
	static IHash CreateFNV_32();
	static IHash CreateFNV1a_32();
	static IHash CreateJenkins3();
	static IHash CreateJS();
	static IHashWithKey CreateMurmur2_32();
	static IHashWithKey CreateMurmurHash3_x86_32();
	static IHash CreateOneAtTime();
	static IHash CreatePJW();
	static IHash CreateRotating();
	static IHash CreateRS();
	static IHash CreateSDBM();
	static IHash CreateShiftAndXor();
	static IHash CreateSuperFast();
	static IHashWithKey CreateXXHash32();

	// ====================== Hash64 ======================
	static IHash CreateFNV_64();
	static IHash CreateFNV1a_64();
	static IHashWithKey CreateMurmur2_64();
	static IHashWithKey CreateXXHash64();
	static IHashWithKey CreateSipHash2_4();

	// ====================== Hash128 ======================
	static IHashWithKey CreateMurmurHash3_x64_128();
	static IHashWithKey CreateMurmurHash3_x86_128();

};

#endif // !HASHLIB4CPPWRAPPER_H