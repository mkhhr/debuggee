from ctypes import *

#Let's map the Microsoft types to ctypes for clarity
BYTE = c_ubyte
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p
PVOID = c_void_p
LPVOID = c_void_p
UINT_PTR = c_ulong
SIZE_T = c_ulong
LPTHREAD_START_ROUTINE = CFUNCTYPE(DWORD, LPVOID)

# CreateProcess function
#
# Creates a new process and its primary thread. The new
# process runs in the security context of the calling
# process.
#
# If the calling process is impersonating another user,
# the new process uses the token for the calling process,
# not the impersonating token. To run the new process in
# the security context of the user represented by the 
# impersonation token, use the CreateProcessAsUser or
# CreateProcessWithLogonW function.
#
# Syntax
# BOOL WINAPI CreateProcess(
#   _In_opt_ LPCTSTR lpApplicationName,
#   _Inout_opt_ LPTSTR lpCommandLine,
#   _In_opt_ LPSECURITY_ATTRIBUTES lpProcessAttributes,
#   _In_opt_ LPSECURITY_ATTRIBUTES lpThreadAttributes,
#   _In_ BOOL bInheritHandles,
#   _In_ DWORD dwCreationFlags,
#   _In_opt_ LPVOID lpEnvironment,
#   _In_opt_ LPCTSTR lpCurrentDirectory,
#   _In_ LPSTARTUPINFO lpStartupInfo,
#   _Out_ LPPROCESS_INFORMATION lpProcessInformation
# );
#
# Parameters
#
# lpApplicationName [in, optional]
#   The name of the module to be executed. This module can
#   be a Windows-based application. It can be some other 
#   type of module (for example, MS-DOS or OS/2) if the
#   appropriate subsystem is avaliable on the local computer.
#   The string can specify the full path and file name of 
#   the module to execute or it can specify a partial name.
#   In the case of a partial name, the function uses the
#   current drive and current directory to complete the
#   specification. The function will not use the search path.
#   This parameter must include the file name extension; no
#   default extension is assumed.
#   The lpApplicationName parameter can be NULL. In that 
#   case, the module name must be the first white space-
#   delimited token in the lpCommandLine string. If you are
#   using a long file name that contains a space, use quoted
#   strings to indicate where the file name ends and the
#   arguments begin; otherwise, the file name is ambiguous.
#   If the executable module is a 16-bit application,
#   lpApplicationName should be NULL, and the string pointed
#   to by lpCommandLine should specify the executable module
#   as well as its arguments.
#   To run a batch file, you must start the command 
#   interpreter; set lpApplicationName to cmd.exe and set
#   lpCommandLine to the following arguments: /c plus the
#   name of the batch file.
# lpCommandLine [in, out, optional]
#   The command line to be executed. The maximum length of
#   this string is 32768 characters, including the Unicode
#   terminationg null character. If lpApplicationName is
#   NULL, the module name portion of lpCommandLine is
#   limited to MAX_PATH characters.
#   The Unicode version of this function, CreateProcessW,
#   can modify the contents of this string. Therefore, this
#   parameter cannot be a pointer to read-only memory (such
#   as a const variable or a literal string). If this
#   parameter is a constant string, the function may cause
#   an access violation.
#   The lpCommandLine parameter can be NULL. In that case,
#   the function uses the string pointed to by lpApplication
#   Name as the command line.
#   If both lpApplicationName and lpCommandLine are non-NULL,
#   the null-terminated string pointed to by lpApplication-
#   Name specifies the module to execute, and the null-
#   terminated string pointed to by lpCommandLine specifes
#   the command line. The new process can use GetCommandLine
#   to retrieve the entire command line. Console processes
#   written in C can use the argc and argv arguments to parse
#   the command line. Because argv[0] is the module name, C
#   programmers generally repeat the module name as the first
#   token in the command line.
#Constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010
PROCESS_ALL_ACCESS = 0x001F0FFF
INFINITE = 0xFFFFFFFF
DBG_CONTINUE = 0x00010002

# Debug event constants
EXCEPTION_DEBUG_EVENT = 0x1
CREATE_THREAD_DEBUG_EVENT = 0x2
CREATE_PROCESS_DEBUG_EVENT = 0x3
EXIT_THREAD_DEBUG_EVENT = 0x4
EXIT_PROCESS_DEBUG_EVENT = 0x5
LOAD_DLL_DEBUG_EVENT = 0x6
UNLOAD_DLL_DEBUG_EVENT = 0x7
OUTPUT_DEBUG_STRING_EVENT = 0x8
RIP_EVENT = 0x9

# Constants of ExceptionCode for struct EXCEPTION_REOCRD
EXCEPTION_GUARD_PAGE = 0x80000001
EXCEPTION_ACCESS_VIOLATION = 0xc0000005
EXCEPTION_ARRAY_BOUNDS_EXCEEDED = 0xc000008c
EXCEPTION_BREAKPOINT = 0x80000003
EXCEPTION_DATATYPE_MISALIGNMENT = 0x80000002
EXCEPTION_FLT_DENORMAL_OPERAND = 0xC000008D
EXCEPTION_FLT_DIVIDE_BY_ZERO = 0xC000008E
EXCEPTION_FLT_INVALID_OPERATION = 0xC0000090
EXCEPTION_FLT_OVERFLOW = 0xC0000091
EXCEPTION_FLT_STACK_CHECK = 0xC0000092
EXCEPTION_FLT_UNDERFLOW = 0xC0000093
EXCEPTION_ILLEGAL_INSTRUCTION = 0xC000001D
EXCEPTION_IN_PAGE_ERROR = 0xC0000006
EXCEPTION_INT_DIVIDE_BY_ZERO = 0xC0000094
EXCEPTION_INT_OVERFLOW = 0xC0000095
EXCEPTION_INVALID_DISPOSITION = 0xC0000026
EXCEPTION_NONCONTINUABLE_EXCEPTION = 0xC0000025
EXCEPTION_PRIV_INSTRUCTION = 0xC0000096
EXCEPTION_SINGLE_STEP = 0x80000004
EXCEPTION_STACK_OVERFLOW = 0xC00000FD

#Structrures for CreateProcessA() function
class STARTUPINFO(Structure):
	_fields_ = [
		('cb', DWORD),
		('lpReserved', LPTSTR),
		('lpDesktop', LPTSTR),
		('lpTitle', LPTSTR),
		('dwX', DWORD),
		('dwY', DWORD),
		('dwXSize', DWORD),
		('dwYSize', DWORD),
		('dwXCountChars', DWORD),
		('dwYCountChars', DWORD),
		('dwFillAttribute', DWORD),
		('dwFlags', DWORD),
		('wShowWindow', WORD),
		('cbReserved2', WORD),
		('lpReserved2', LPBYTE),
		('hStdInput', HANDLE),
		('hStdOutput', HANDLE),
		('hStdError', HANDLE),
		]

class PROCESS_INFORMATION(Structure):
	_fields_ = [
		('hProcess', HANDLE),
		('hThread', HANDLE),
		('dwProcessId', DWORD),
		('dwThreadId', DWORD),
		]

class EXCEPTION_RECORD(Structure):
	pass

EXCEPTION_RECORD._fields_ = [
			('ExceptionCode', DWORD),
			('ExceptionFlags', DWORD),
			('ExceptionRecord', POINTER(EXCEPTION_RECORD)),
			('ExceptionAddress', PVOID),
			('NumberParameters', DWORD),
			('ExceptionInformation', UINT_PTR * 15),
			]

class EXCEPTION_DEBUG_INFO(Structure):
	_fields_ = [
			('ExceptionRecord', EXCEPTION_RECORD),
			('dwFirstChance', DWORD)
			]

class CREATE_THREAD_DEBUG_INFO(Structure):
	_fields_ = [
			('hThread', HANDLE),
			('lpThreadLocalBase', LPVOID),
			('lpStartAddress', LPTHREAD_START_ROUTINE),
			]

class CREATE_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [
			('hFile', HANDLE),
			('hProcess', HANDLE),
			('hThread', HANDLE),
			('lpBaseOfImage', LPVOID),
			('dwDebugInfoFileOffset', DWORD),
			('nDebugInfoSize', DWORD),
			('lpThreadLocalBase', LPVOID),
			('lpStartAddress', LPTHREAD_START_ROUTINE),
			('lpImageName', LPVOID),
			('fUnicode', WORD),
			]

class EXIT_THREAD_DEBUG_INFO(Structure):
	_fields_ = [('dwExitCode', DWORD)]

class EXIT_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [('dwExitCode', DWORD)]

class LOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [
			('hFile', HANDLE),
			('lpBaseOfDll', LPVOID),
			('dwDebugInfoFileOffset', DWORD),
			('nDebugInfoSize', DWORD),
			('lpImageName', LPVOID),
			('fUnicode', WORD),
			]

class UNLOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [('lpBaseOfDll', LPVOID)]

class OUTPUT_DEBUG_STRING_INFO(Structure):
	_fields_ = [
			('lpDebugStringData', LPTSTR),
			('fUnicode', WORD),
			('nDebugStringLength', WORD),
			]

class RIP_INFO(Structure):
	_fields_ = [
			('dwError', DWORD),
			('dwType', DWORD),
			]

class DEBUG_EVENT_UNION(Union):
	_fields_ = [
			('Exception', EXCEPTION_DEBUG_INFO),
			('CreateThread', CREATE_THREAD_DEBUG_INFO),
			('CreateProcessInfo', CREATE_PROCESS_DEBUG_INFO),
			('ExitThread', EXIT_THREAD_DEBUG_INFO),
			('ExitProcess', EXIT_PROCESS_DEBUG_INFO),
			('LoadDll', LOAD_DLL_DEBUG_INFO),
			('UnloadDll', UNLOAD_DLL_DEBUG_INFO),
			('DebugString', OUTPUT_DEBUG_STRING_INFO),
			('RipInfo', RIP_INFO),
			]

class DEBUG_EVENT(Structure):
	_fields_ = [
			('dwDebugEventCode', DWORD),
			('dwProcessId', DWORD),
			('dwThreadId', DWORD),
			('u', DEBUG_EVENT_UNION),
			]

# dwType: Any additional information about the type of error that
# caused the RIP debug event.
SLE_ERROR = 0x00000001
SLE_MINORERROR = 0x00000002
SLE_WARNING = 0x00000003

# dwContinueStatus[in]
# The options to continue the thread that reported the debugging event

# If the thread specified by the dwThreadId parameter previously reported an 
# EXCEPTION_DEBGU_EVENT debugging event, the function stops all exception and
# processing and continues the thread. For any other debugging event, this flag
# simply continues the thread.
DBG_CONTINUE = 0x00010002

# If the thread specified by the dwThreadId previously reported and 
# EXCEPTION_DEBUG_EVENT degugging event, the function continues
# exception processing. If this is a first-chance exception event,
# the search and dispatch logic of the structured exception handler
# is used; otherwise, the process is terminated. For any other debugging
# event, this flag simply continues the thread.
DBG_EXCEPTION_NOT_HANDLED = 0x80010001

# BOOL WINAPI DebugActiveProcessStop(
#   _In_ DWORD dwProcessId
# );
# Stops the debugger from debugging the specified process.
# dwProcessId [in] 
#     The identifier of the process to stop debugging.
# If the function succeed, the return value is nonzero.
# If the function fails, the return value is zero. To get extended error
#    information, call GetLastError.
