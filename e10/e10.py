import subprocess
command = "powershell -ExecutionPolicy ByPass -File power.ps1"
print(command)
powerShellResult = subprocess.run(command)
