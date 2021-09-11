import wmi

ti = 0
name = 'vlc.exe'
f = wmi.WMI()

for process in f.Win32_Process():

    if process.name == name:
        process.Terminate()
        ti += 1

if ti == 0:
    print("process not found")
else:
    print("Process found!")
