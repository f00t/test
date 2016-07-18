// rc4.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string.h>

typedef unsigned long ULONG;
void rc4_init(unsigned char *s, unsigned char *key, unsigned long Len);
void rc4_crypt(unsigned char *s, unsigned char *Data, unsigned long Len);


void rc4_init(unsigned char *s, unsigned char *key, unsigned long Len) //init
{
	int i = 0, j = 0;
	char k[256] = { 0 };
	unsigned char tmp = 0;
	for (i = 0;i<256;i++) {
		s[i] = i;
		k[i] = key[i%Len];
	}
	for (i = 0; i<256; i++) {
		j = (j + s[i] + k[i]) % 256;
		tmp = s[i];
		s[i] = s[j]; //exchange s[i]和s[j]
		s[j] = tmp;
	}
}

void rc4_crypt(unsigned char *s, unsigned char *Data, unsigned long Len) //rc4
{
	int i = 0, j = 0, t = 0;
	unsigned long k = 0;
	unsigned char tmp;
	for (k = 0;k<Len;k++) {
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;
		tmp = s[i];
		s[i] = s[j]; //exchange s[x]和s[y]
		s[j] = tmp;
		t = (s[i] + s[j]) % 256;
		Data[k] ^= s[t];
	}
}

int main()
{
	unsigned char s[256] = { 0 }; //S-box
	char key[256] = { "AbHGlhg1123214234352UOr134rt4t31t42fr33r321rrrrrrrrdfas3er1232fja32423g4rfqerf21GYGTk9sdfan4222r44122fnsadh21q234234wewqreqwer234123432148978HKJNJ"};
	char pData[512] = {0};
	gets_s(pData,512 );
	ULONG len = strlen(pData);
	printf("key : %s\n", key);
	printf("raw : %s\n", pData);

	rc4_init(s, (unsigned char *)key, strlen(key)); 
	rc4_crypt(s, (unsigned char *)pData, len);//encode
	printf("encrypt  : %s\n", pData);
	rc4_init(s, (unsigned char *)key, strlen(key)); //init key
	rc4_crypt(s, (unsigned char *)pData, len);//decode
	printf("decrypt  : %s\n", pData);
	system("pause");
	return 0;
}
