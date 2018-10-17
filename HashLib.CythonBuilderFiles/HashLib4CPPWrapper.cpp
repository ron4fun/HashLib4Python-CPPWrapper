#include "HashLib4CPPWrapper.h"
#include "HashLib4CPP.h"


// ====================== TConverters Implementation ======================
////////////////////
// TConverters
///////////////////

string TConverters::toUpper(const string &a_value)
{
	return Converters::toUpper(a_value);
}

uint32_t TConverters::ReadBytesAsUInt32LE(const HashLibByteArray &a_value, const int32_t a_index)
{
	return Converters::ReadBytesAsUInt32LE(&a_value[0], a_index);
}

uint64_t TConverters::ReadBytesAsUInt64LE(const HashLibByteArray &a_value, const int32_t a_index)
{
	return Converters::ReadBytesAsUInt64LE(&a_value[0], a_index);
}

HashLibByteArray TConverters::ReadUInt32AsBytesLE(const uint32_t a_in)
{
	return Converters::ReadUInt32AsBytesLE(a_in);
}

HashLibByteArray TConverters::ReadUInt64AsBytesLE(const uint64_t a_in)
{
	return Converters::ReadUInt64AsBytesLE(a_in);
}

HashLibByteArray TConverters::ConvertHexStringToBytes(const string &a_in)
{
	return Converters::ConvertHexStringToBytes(a_in);
}

HashLibByteArray TConverters::ConvertStringToBytes(const string &a_in)
{
	return Converters::ConvertStringToBytes(a_in);
}

string TConverters::ConvertBytesToHexString(const HashLibByteArray &a_in, const bool a_group)
{
	return Converters::ConvertBytesToHexString(a_in, a_group);
}


// ====================== THashResult Implementation ======================
////////////////////
// THashResult
///////////////////

THashResult::THashResult()
{
	ptr = nullptr;
}

THashResult::THashResult(IHashResult _ptr)
{
	ptr = ::move(_ptr);
}

THashResult::THashResult(const HashLibByteArray &value)
{
	ptr = make_shared<HashResult>(value);
}

THashResult::THashResult(const THashResult &value)
{
	ptr = ::move(value.ptr);
}

HashLibByteArray THashResult::GetBytes() const
{
	return ptr->GetBytes();
}

uint8_t THashResult::GetUInt8() const
{
	return ptr->GetUInt8();
}

uint16_t THashResult::GetUInt16() const
{
	return ptr->GetUInt16();
}

uint32_t THashResult::GetUInt32() const
{
	return ptr->GetUInt32();
}

int32_t THashResult::GetInt32() const
{
	return ptr->GetInt32();
}

uint64_t THashResult::GetUInt64() const
{
	return ptr->GetUInt64();
}

string THashResult::ToString(const bool a_group) const
{
	return ptr->ToString(a_group);
}

int32_t THashResult::GetHashCode() const
{
	return ptr->GetHashCode();
}

bool THashResult::CompareTo(const THashResult &a_hashResult) const
{
	return ptr->CompareTo(a_hashResult.ptr);
}

bool THashResult::CompareTo(const HashLibByteArray &value) const
{
	return ptr->CompareTo(THashResult(value).ptr);
}

// ====================== THash Implementation ======================
////////////////////
// THash
///////////////////

THash::THash()
{
	ptr = nullptr;
}

THash::THash(IHash _ptr)
{
	ptr = ::move(_ptr);
}

THash::THash(const THash &value)
{
	ptr = ::move(value.ptr);
}

IHash THash::Copy()
{
	return ptr;
}

string THash::GetName() const
{
	return ptr->GetName();
}

int32_t THash::GetBlockSize() const
{
	return ptr->GetBlockSize();
}

int32_t THash::GetHashSize() const
{
	return ptr->GetHashSize();
}

int32_t THash::GetBufferSize() const
{
	return ptr->GetBufferSize();
}

void THash::SetBufferSize(const int32_t value)
{
	ptr->SetBufferSize(value);
}

THash THash::Clone() const
{
	THash hash = THash(ptr->Clone());
	return hash;
}

THashResult THash::ComputeString(const string &a_data)
{
	THashResult result = THashResult(ptr->ComputeString(a_data));
	return result;
}

THashResult THash::ComputeBytes(const HashLibByteArray &a_data)
{
	THashResult result = THashResult(ptr->ComputeBytes(a_data));
	return result;
}

THashResult THash::ComputeFile(const string &a_file_name,
	const int64_t a_from, const int64_t a_length)
{
	THashResult result = THashResult(ptr->ComputeFile(a_file_name, a_from, a_length));
	return result;
}

void THash::Initialize()
{
	ptr->Initialize();
}

void THash::TransformBytes(const HashLibByteArray &a_data, int32_t a_index, int32_t a_length)
{
	ptr->TransformBytes(a_data, a_index, a_length);
}

void THash::TransformBytes(const HashLibByteArray &a_data, const int32_t a_index)
{
	ptr->TransformBytes(a_data, a_index);
}

void THash::TransformBytes(const HashLibByteArray &a_data)
{
	ptr->TransformBytes(a_data);
}

THashResult THash::TransformFinal()
{
	THashResult result = THashResult(ptr->TransformFinal());
	return result;
}

void THash::TransformString(const string &a_data)
{
	ptr->TransformString(a_data);
}

void THash::TransformFile(const string &a_file_name,
	const int64_t a_from, const int64_t a_length)
{
	ptr->TransformFile(a_file_name, a_from, a_length);
}


// ====================== TCRC Implementation ======================
////////////////////
// TCRC
///////////////////

TCRC::TCRC()
{
	ptr = nullptr;
}

TCRC::TCRC(ICRC _ptr)
	:THash(_ptr)
{
	ptr = ::move(_ptr);
}

TCRC::TCRC(const TCRC &value)
	: THash(value.ptr)
{
	ptr = ::move(value.ptr);
}

TCRC TCRC::Clone() const
{
	TCRC hash = TCRC(ptr->CloneCRC());
	return hash;
}

HashLibStringArray TCRC::GetNames() const
{
	return ptr->GetNames();
}

int32_t TCRC::GetWidth() const
{
	return ptr->GetWidth();
}

uint64_t TCRC::GetPolynomial() const
{
	return ptr->GetPolynomial();
}

uint64_t TCRC::GetInit() const
{
	return ptr->GetInit();
}

bool TCRC::GetReflectIn() const
{
	return ptr->GetReflectIn();
}

bool TCRC::GetReflectOut() const
{
	return ptr->GetReflectOut();
}

uint64_t TCRC::GetXOROut() const
{
	return ptr->GetXOROut();
}

uint64_t TCRC::GetCheckValue() const
{
	return ptr->GetCheckValue();
}


// ====================== THashWithKey Implementation ======================
////////////////////
// THashWithKey
///////////////////

THashWithKey::THashWithKey()
{
	ptr = nullptr;
}

THashWithKey::THashWithKey(IHashWithKey _ptr)
	:THash(_ptr)
{
	ptr = ::move(_ptr);
}

THashWithKey::THashWithKey(const THashWithKey &value)
	: THash(value.ptr)
{
	ptr = ::move(value.ptr);
}

THashWithKey THashWithKey::Clone() const
{
	THashWithKey hash = THashWithKey(ptr->CloneHashWithKey());
	return hash;
}

HashLibByteArray THashWithKey::GetKey() const
{
	return ptr->GetKey();
}

void THashWithKey::SetKey(const HashLibByteArray &value)
{
	ptr->SetKey(value);
}

int32_t THashWithKey::GetKeyLength() const
{
	return ptr->GetKeyLength().GetValue();
}


// ====================== THMAC Class ======================
////////////////////
// THMAC Class
///////////////////

THMAC::THMAC()
{
	ptr = nullptr;
}

THMAC::THMAC(THash hash)
{
	ptr = ::move(HashLib4CPP::HMAC::CreateHMAC(hash.Copy()));
}

THMAC::THMAC(const THMAC &value)
{
	ptr = ::move(value.ptr);
}

string THMAC::GetName() const
{
	return ptr->GetName();
}

int32_t THMAC::GetBlockSize() const
{
	return ptr->GetBlockSize();
}

int32_t THMAC::GetHashSize() const
{
	return ptr->GetHashSize();
}

int32_t THMAC::GetBufferSize() const
{
	return ptr->GetBufferSize();
}

void THMAC::SetBufferSize(const int32_t value)
{
	ptr->SetBufferSize(value);
}

THMAC THMAC::Clone() const
{
	THMAC hash = THMAC(ptr->Clone());
	hash.ptr = ptr->CloneHMAC();

	return hash;
}

THash THMAC::CloneTHash() const
{
	THash hash = THash(ptr->Clone());
	return hash;
}

THashResult THMAC::ComputeString(const string &a_data)
{
	THashResult result = THashResult(ptr->ComputeString(a_data));
	return result;
}

THashResult THMAC::ComputeBytes(const HashLibByteArray &a_data)
{
	THashResult result = THashResult(ptr->ComputeBytes(a_data));
	return result;
}

THashResult THMAC::ComputeFile(const string &a_file_name,
	const int64_t a_from, const int64_t a_length)
{
	THashResult result = THashResult(ptr->ComputeFile(a_file_name, a_from, a_length));
	return result;
}

void THMAC::Initialize()
{
	ptr->Initialize();
}

void THMAC::TransformBytes(const HashLibByteArray &a_data, int32_t a_index, int32_t a_length)
{
	ptr->TransformBytes(a_data, a_index, a_length);
}

void THMAC::TransformBytes(const HashLibByteArray &a_data, const int32_t a_index)
{
	ptr->TransformBytes(a_data, a_index);
}

void THMAC::TransformBytes(const HashLibByteArray &a_data)
{
	ptr->TransformBytes(a_data);
}

THashResult THMAC::TransformFinal()
{
	THashResult result = THashResult(ptr->TransformFinal());
	return result;
}

void THMAC::TransformString(const string &a_data)
{
	ptr->TransformString(a_data);
}

void THMAC::TransformFile(const string &a_file_name,
	const int64_t a_from, const int64_t a_length)
{
	ptr->TransformFile(a_file_name, a_from, a_length);
}

HashLibByteArray THMAC::GetKey() const
{
	return ptr->GetKey();
}

void THMAC::SetKey(const HashLibByteArray &value)
{
	ptr->SetKey(value);
}

int32_t THMAC::GetKeyLength() const
{
	return ptr->GetKeyLength().GetValue();
}


// ====================== TPBKDF2_HMAC Class ======================
////////////////////
// TPBKDF2_HMAC Class
///////////////////

TPBKDF2_HMAC::TPBKDF2_HMAC()
{
	ptr = nullptr;
}

TPBKDF2_HMAC::TPBKDF2_HMAC(THash hash, const HashLibByteArray &a_password,
	const HashLibByteArray &a_salt, const uint32_t a_iterations)
{
	ptr = ::move(HashLib4CPP::PBKDF2_HMAC::CreatePBKDF2_HMAC(hash.Copy(), a_password, a_salt, a_iterations));
}

TPBKDF2_HMAC::TPBKDF2_HMAC(const TPBKDF2_HMAC &value)
{
	ptr = ::move(value.ptr);
}

HashLibByteArray TPBKDF2_HMAC::GetBytes(const int32_t bc)
{
	return ptr->GetBytes(bc);
}

// ====================== TBlake2BConfig Implementation ======================
////////////////////
// TBlake2BConfig
///////////////////

TBlake2BConfig::TBlake2BConfig()
{
	ptr = nullptr;
}

TBlake2BConfig::TBlake2BConfig(const int32_t a_hash_size)
{
	IBlake2BConfig config = make_shared<Blake2BConfig>(a_hash_size);
	ptr = ::move(config);
}

TBlake2BConfig::TBlake2BConfig(const TBlake2BConfig &value)
{
	ptr = ::move(value.ptr);
}

IBlake2BConfig TBlake2BConfig::GetConfig() const
{
	return ptr;
}

HashLibByteArray TBlake2BConfig::GetPersonalisation() const
{
	return ptr->GetPersonalisation();
}

void TBlake2BConfig::SetPersonalisation(const HashLibByteArray &value)
{
	ptr->SetPersonalisation(value);
}

HashLibByteArray TBlake2BConfig::GetSalt() const
{
	return ptr->GetSalt();
}

void TBlake2BConfig::SetSalt(const HashLibByteArray &value)
{
	ptr->SetSalt(value);
}

HashLibByteArray TBlake2BConfig::GetKey() const
{
	return ptr->GetKey();
}

void TBlake2BConfig::SetKey(const HashLibByteArray &value)
{
	ptr->SetKey(value);
}

int32_t TBlake2BConfig::GetHashSize() const
{
	return ptr->GetHashSize();
}

void TBlake2BConfig::SetHashSize(const int32_t value)
{
	ptr->SetHashSize(value);
}

// ====================== TBlake2SConfig Implementation ======================
////////////////////
// TBlake2SConfig
///////////////////

TBlake2SConfig::TBlake2SConfig()
{
	ptr = nullptr;
}

TBlake2SConfig::TBlake2SConfig(const int32_t a_hash_size)
{
	IBlake2SConfig config = make_shared<Blake2SConfig>(a_hash_size);
	ptr = ::move(config);
}

TBlake2SConfig::TBlake2SConfig(const TBlake2SConfig &value)
{
	ptr = ::move(value.ptr);
}

IBlake2SConfig TBlake2SConfig::GetConfig() const
{
	return ptr;
}

HashLibByteArray TBlake2SConfig::GetPersonalisation() const
{
	return ptr->GetPersonalisation();
}

void TBlake2SConfig::SetPersonalisation(const HashLibByteArray &value)
{
	ptr->SetPersonalisation(value);
}

HashLibByteArray TBlake2SConfig::GetSalt() const
{
	return ptr->GetSalt();
}

void TBlake2SConfig::SetSalt(const HashLibByteArray &value)
{
	ptr->SetSalt(value);
}

HashLibByteArray TBlake2SConfig::GetKey() const
{
	return ptr->GetKey();
}

void TBlake2SConfig::SetKey(const HashLibByteArray &value)
{
	ptr->SetKey(value);
}

int32_t TBlake2SConfig::GetHashSize() const
{
	return ptr->GetHashSize();
}

void TBlake2SConfig::SetHashSize(const int32_t value)
{
	ptr->SetHashSize(value);
}

// ====================== HashLib4CPPWrapper Implementation ======================
////////////////////
// HashLib4CPPWrapper
///////////////////

// ====================== NullDigest ======================
IHash HashLib4CPPWrapper::CreateNullDigest()
{
	IHash hash = HashLib4CPP::NullDigestFactory::CreateNullDigest();
	return hash;
}

// ====================== Checksum ======================
ICRC HashLib4CPPWrapper::CreateCRC(const CRCStandard &value)
{
	ICRC hash = HashLib4CPP::Checksum::CreateCRC(value);
	return hash;
}

IHash HashLib4CPPWrapper::CreateCRC16_BUYPASS()
{
	IHash hash = HashLib4CPP::Checksum::CreateCRC16_BUYPASS();
	return hash;
}

IHash HashLib4CPPWrapper::CreateCRC32_PKZIP()
{
	IHash hash = HashLib4CPP::Checksum::CreateCRC32_PKZIP();
	return hash;
}

IHash HashLib4CPPWrapper::CreateCRC32_CASTAGNOLI()
{
	IHash hash = HashLib4CPP::Checksum::CreateCRC32_CASTAGNOLI();
	return hash;
}

IHash HashLib4CPPWrapper::CreateCRC64_ECMA()
{
	IHash hash = HashLib4CPP::Checksum::CreateCRC64_ECMA();
	return hash;
}

IHash HashLib4CPPWrapper::CreateAdler32()
{
	IHash hash = HashLib4CPP::Checksum::CreateAdler32();
	return hash;
}

// ====================== Crypto ======================
IHash HashLib4CPPWrapper::CreateBlake2B(const TBlake2BConfig *config)
{
	IHash hash;

	if (config)
		hash = HashLib4CPP::Crypto::CreateBlake2B(config->GetConfig());
	else
		hash = HashLib4CPP::Crypto::CreateBlake2B();

	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2B_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2B_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2B_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2B_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2B_384()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2B_384();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2B_512()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2B_512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2S(const TBlake2SConfig *config)
{
	IHash hash;

	if (config)
		hash = HashLib4CPP::Crypto::CreateBlake2S(config->GetConfig());
	else
		hash = HashLib4CPP::Crypto::CreateBlake2S();

	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2S_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2S_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2S_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2S_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2S_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2S_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBlake2S_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateBlake2S_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateGost()
{
	IHash hash = HashLib4CPP::Crypto::CreateGost();
	return hash;
}

IHash HashLib4CPPWrapper::CreateGOST3411_2012_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateGOST3411_2012_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateGOST3411_2012_512()
{
	IHash hash = HashLib4CPP::Crypto::CreateGOST3411_2012_512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateGrindahl256()
{
	IHash hash = HashLib4CPP::Crypto::CreateGrindahl256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateGrindahl512()
{
	IHash hash = HashLib4CPP::Crypto::CreateGrindahl512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHAS160()
{
	IHash hash = HashLib4CPP::Crypto::CreateHAS160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_3_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_3_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_3_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_3_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_3_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_3_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_3_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_3_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_3_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_3_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_4_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_4_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_4_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_4_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_4_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_4_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_4_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_4_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_4_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_4_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_5_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_5_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_5_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_5_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_5_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_5_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_5_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_5_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateHaval_5_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateHaval_5_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateMD2()
{
	IHash hash = HashLib4CPP::Crypto::CreateMD2();
	return hash;
}

IHash HashLib4CPPWrapper::CreateMD4()
{
	IHash hash = HashLib4CPP::Crypto::CreateMD4();
	return hash;
}

IHash HashLib4CPPWrapper::CreateMD5()
{
	IHash hash = HashLib4CPP::Crypto::CreateMD5();
	return hash;
}

IHash HashLib4CPPWrapper::CreatePanama()
{
	IHash hash = HashLib4CPP::Crypto::CreatePanama();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRIPEMD()
{
	IHash hash = HashLib4CPP::Crypto::CreateRIPEMD();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRIPEMD128()
{
	IHash hash = HashLib4CPP::Crypto::CreateRIPEMD128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRIPEMD160()
{
	IHash hash = HashLib4CPP::Crypto::CreateRIPEMD160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRIPEMD256()
{
	IHash hash = HashLib4CPP::Crypto::CreateRIPEMD256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRIPEMD320()
{
	IHash hash = HashLib4CPP::Crypto::CreateRIPEMD320();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRadioGatun32()
{
	IHash hash = HashLib4CPP::Crypto::CreateRadioGatun32();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRadioGatun64()
{
	IHash hash = HashLib4CPP::Crypto::CreateRadioGatun64();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA0()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA0();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA1()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA1();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_384()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_384();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_512()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_512_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_512_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA2_512_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA2_512_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA3_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA3_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA3_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA3_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA3_384()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA3_384();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSHA3_512()
{
	IHash hash = HashLib4CPP::Crypto::CreateSHA3_512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateKeccak_224()
{
	IHash hash = HashLib4CPP::Crypto::CreateKeccak_224();
	return hash;
}

IHash HashLib4CPPWrapper::CreateKeccak_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateKeccak_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateKeccak_384()
{
	IHash hash = HashLib4CPP::Crypto::CreateKeccak_384();
	return hash;
}

IHash HashLib4CPPWrapper::CreateKeccak_512()
{
	IHash hash = HashLib4CPP::Crypto::CreateKeccak_512();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSnefru_8_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateSnefru_8_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSnefru_8_256()
{
	IHash hash = HashLib4CPP::Crypto::CreateSnefru_8_256();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_3_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_3_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_3_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_3_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_3_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_3_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_4_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_4_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_4_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_4_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_4_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_4_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_5_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_5_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_5_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_5_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger2_5_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger2_5_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_3_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_3_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_3_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_3_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_3_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_3_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_4_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_4_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_4_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_4_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_4_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_4_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_5_128()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_5_128();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_5_160()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_5_160();
	return hash;
}

IHash HashLib4CPPWrapper::CreateTiger_5_192()
{
	IHash hash = HashLib4CPP::Crypto::CreateTiger_5_192();
	return hash;
}

IHash HashLib4CPPWrapper::CreateWhirlPool()
{
	IHash hash = HashLib4CPP::Crypto::CreateWhirlPool();
	return hash;
}

// ====================== Hash32 ======================
IHash HashLib4CPPWrapper::CreateAP()
{
	IHash hash = HashLib4CPP::Hash32::CreateAP();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBernstein()
{
	IHash hash = HashLib4CPP::Hash32::CreateBernstein();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBernstein1()
{
	IHash hash = HashLib4CPP::Hash32::CreateBernstein1();
	return hash;
}

IHash HashLib4CPPWrapper::CreateBKDR()
{
	IHash hash = HashLib4CPP::Hash32::CreateBKDR();
	return hash;
}

IHash HashLib4CPPWrapper::CreateDEK()
{
	IHash hash = HashLib4CPP::Hash32::CreateDEK();
	return hash;
}

IHash HashLib4CPPWrapper::CreateDJB()
{
	IHash hash = HashLib4CPP::Hash32::CreateDJB();
	return hash;
}

IHash HashLib4CPPWrapper::CreateELF()
{
	IHash hash = HashLib4CPP::Hash32::CreateELF();
	return hash;
}

IHash HashLib4CPPWrapper::CreateFNV_32()
{
	IHash hash = HashLib4CPP::Hash32::CreateFNV();
	return hash;
}

IHash HashLib4CPPWrapper::CreateFNV1a_32()
{
	IHash hash = HashLib4CPP::Hash32::CreateFNV1a();
	return hash;
}

IHash HashLib4CPPWrapper::CreateJenkins3()
{
	IHash hash = HashLib4CPP::Hash32::CreateJenkins3();
	return hash;
}

IHash HashLib4CPPWrapper::CreateJS()
{
	IHash hash = HashLib4CPP::Hash32::CreateJS();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateMurmur2_32()
{
	IHashWithKey hash = HashLib4CPP::Hash32::CreateMurmur2();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateMurmurHash3_x86_32()
{
	IHashWithKey hash = HashLib4CPP::Hash32::CreateMurmurHash3_x86_32();
	return hash;
}

IHash HashLib4CPPWrapper::CreateOneAtTime()
{
	IHash hash = HashLib4CPP::Hash32::CreateOneAtTime();
	return hash;
}

IHash HashLib4CPPWrapper::CreatePJW()
{
	IHash hash = HashLib4CPP::Hash32::CreatePJW();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRotating()
{
	IHash hash = HashLib4CPP::Hash32::CreateRotating();
	return hash;
}

IHash HashLib4CPPWrapper::CreateRS()
{
	IHash hash = HashLib4CPP::Hash32::CreateRS();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSDBM()
{
	IHash hash = HashLib4CPP::Hash32::CreateSDBM();
	return hash;
}

IHash HashLib4CPPWrapper::CreateShiftAndXor()
{
	IHash hash = HashLib4CPP::Hash32::CreateShiftAndXor();
	return hash;
}

IHash HashLib4CPPWrapper::CreateSuperFast()
{
	IHash hash = HashLib4CPP::Hash32::CreateSuperFast();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateXXHash32()
{
	IHashWithKey hash = HashLib4CPP::Hash32::CreateXXHash32();
	return hash;
}

// ====================== Hash64 ======================
IHash HashLib4CPPWrapper::CreateFNV_64()
{
	IHash hash = HashLib4CPP::Hash64::CreateFNV();
	return hash;
}

IHash HashLib4CPPWrapper::CreateFNV1a_64()
{
	IHash hash = HashLib4CPP::Hash64::CreateFNV1a();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateMurmur2_64()
{
	IHashWithKey hash = HashLib4CPP::Hash64::CreateMurmur2();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateXXHash64()
{
	IHashWithKey hash = HashLib4CPP::Hash64::CreateXXHash64();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateSipHash2_4()
{
	IHashWithKey hash = HashLib4CPP::Hash64::CreateSipHash2_4();
	return hash;
}

// ====================== Hash128 ======================
IHashWithKey HashLib4CPPWrapper::CreateMurmurHash3_x64_128()
{
	IHashWithKey hash = HashLib4CPP::Hash128::CreateMurmurHash3_x64_128();
	return hash;
}

IHashWithKey HashLib4CPPWrapper::CreateMurmurHash3_x86_128()
{
	IHashWithKey hash = HashLib4CPP::Hash128::CreateMurmurHash3_x86_128();
	return hash;
}

