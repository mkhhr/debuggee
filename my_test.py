import my_debugger
debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.detach()
#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
