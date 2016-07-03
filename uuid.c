// uuid.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <Rpc.h>

#pragma comment (lib, "Rpcrt4.lib")

char *uuidtostring(GUID guid)
{
	char buf[64] = { 0 };
	sprintf_s(buf, sizeof(buf), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X}",
		guid.Data1, guid.Data2, guid.Data3,
		guid.Data4[0], guid.Data4[1],
		guid.Data4[2], guid.Data4[3],
		guid.Data4[4], guid.Data4[5],
		guid.Data4[6], guid.Data4[7]);
	return buf;
}

int main(){   
	UUID uuid;
	char uuid_s[64];
	UuidCreate(&uuid);
	uuid_s = uuidtostring(uuid);
	puts(uuid_s);
	system("pause");


	return 0;
}

