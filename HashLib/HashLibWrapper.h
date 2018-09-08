#ifndef HASHLIBWRAPPER_H
#define HASHLIBWRAPPER_H

#include <wchar.h>
#include "Utils\HlpHashLibTypes.h"

enum MODE 
{ 
	a_STRING = 0,
	a_FILE
}; // end enum MODE

enum HASH
{
	a_NORMAL = 0,
	a_HMAC,
	a_PBKDF
}; // end enum HASH

class HashFactoryWrapper
{
public:
	// ====================== Checksum ====================== 
	static string CreateCRC(const CRCStandard &, const string &, const MODE &);
	static string CreateCRC16_BUYPASS(const string &, const MODE &);
	static string CreateCRC32_PKZIP(const string &, const MODE &);
	static string CreateCRC32_CASTAGNOLI(const string &, const MODE &);
	static string CreateCRC64_ECMA(const string &, const MODE &);
	static string CreateAdler32(const string &, const MODE &);

	// ====================== Crypto ======================
	static string CreateGost(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateGrindahl256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateGrindahl512(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHAS160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_3_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_3_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_3_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_3_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_3_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_4_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_4_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_4_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_4_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_4_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_5_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_5_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_5_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_5_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateHaval_5_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateMD2(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateMD4(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateMD5(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreatePanama(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRIPEMD(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRIPEMD128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRIPEMD160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRIPEMD256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRIPEMD320(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRadioGatun32(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateRadioGatun64(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA0(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA1(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_384(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_512(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_512_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA2_512_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA3_224(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA3_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA3_384(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSHA3_512(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSnefru_8_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateSnefru_8_256(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_3_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_3_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_3_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_4_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_4_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_4_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_5_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_5_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger2_5_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_3_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_3_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_3_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_4_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_4_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_4_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_5_128(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_5_160(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateTiger_5_192(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);
	static string CreateWhirlPool(const string &, const MODE &, const string & = "", const HASH & = HASH::a_NORMAL, const string & = "", const uint32_t = 1000, const int32_t = 32);

	// ====================== Hash32 ======================
	static string CreateAP(const string &, const MODE &);
	static string CreateBernstein(const string &, const MODE &);
	static string CreateBernstein1(const string &, const MODE &);
	static string CreateBKDR(const string &, const MODE &);
	static string CreateDEK(const string &, const MODE &);
	static string CreateDJB(const string &, const MODE &);
	static string CreateELF(const string &, const MODE &);
	static string CreateFNV_32(const string &, const MODE &);
	static string CreateFNV1a_32(const string &, const MODE &);
	static string CreateJenkins3(const string &, const MODE &);
	static string CreateJS(const string &, const MODE &);
	static string CreateMurmur2_32(const string &, const MODE &, const uint32_t=0x0);
	static string CreateMurmurHash3_x86_32(const string &, const MODE &, const uint32_t = 0x0);
	static string CreateOneAtTime(const string &, const MODE &);
	static string CreatePJW(const string &, const MODE &);
	static string CreateRotating(const string &, const MODE &);
	static string CreateRS(const string &, const MODE &);
	static string CreateSDBM(const string &, const MODE &);
	static string CreateShiftAndXor(const string &, const MODE &);
	static string CreateSuperFast(const string &, const MODE &);
	static string CreateXXHash32(const string &, const MODE &, const uint32_t = 0x0);

	// ====================== Hash64 ======================
	static string CreateFNV_64(const string &, const MODE &);
	static string CreateFNV1a_64(const string &, const MODE &);
	static string CreateMurmur2_64(const string &, const MODE &, const uint32_t = 0x0);
	static string CreateXXHash64(const string &, const MODE &, const uint64_t = 0x0);
	static string CreateSipHash2_4(const string &, const MODE &, const uint64_t = 0x0001020304050607, const uint64_t = 0x08090A0B0C0D0E0F);

	// ====================== Hash128 ======================
	static string CreateMurmurHash3_x64_128(const string &, const MODE &, const uint32_t = 0x0);
	static string CreateMurmurHash3_x86_128(const string &, const MODE &, const uint32_t = 0x0);
};


#endif // !HASHLIBWRAPPER_H