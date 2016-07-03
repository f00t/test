#include <windows.h>
#include <stdio.h>

char* execmd(WCHAR *cmd)
{
	HANDLE stdout_r, stdout_w, stderr_r, stderr_w;
	SECURITY_ATTRIBUTES sa;
	sa.nLength = sizeof(SECURITY_ATTRIBUTES);
	sa.bInheritHandle = TRUE;
	sa.lpSecurityDescriptor = NULL;

	CreatePipe(&stderr_r, &stderr_w, &sa, 0);
	SetHandleInformation(stderr_r, HANDLE_FLAG_INHERIT, 0);
	CreatePipe(&stdout_r, &stdout_w, &sa, 0);
	SetHandleInformation(stdout_r, HANDLE_FLAG_INHERIT, 0);

	PROCESS_INFORMATION pi;
	STARTUPINFO si;
	ZeroMemory(&pi, sizeof(PROCESS_INFORMATION));
	ZeroMemory(&si, sizeof(STARTUPINFO));

	si.cb = sizeof(STARTUPINFO);
	si.hStdError = stderr_w;
	si.hStdOutput = stdout_w;
	si.dwFlags |= STARTF_USESTDHANDLES;
	
	CreateProcess(NULL, cmd, NULL, NULL, TRUE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi);

	CloseHandle(stderr_w);
	CloseHandle(stdout_w);

	DWORD dwRead;
	char buf[BUFFSIZE *10];
	char out[BUFFSIZE *5] = "";
	char err[BUFFSIZE *5] = "";
	BOOL bSuccess = FALSE;

	while(true) {
		bSuccess = ReadFile(stdout_r, out, BUFFSIZE *4, &dwRead, NULL);
		if(!bSuccess || dwRead == 0)
			break;
	}

	dwRead = 0;
	while (true) {
		bSuccess = ReadFile(stderr_r, err, BUFFSIZE *4, &dwRead, NULL);
		if(!bSuccess || dwRead == 0)
			break;
	}

	return strcat(strcat(buf,out),err);
}

