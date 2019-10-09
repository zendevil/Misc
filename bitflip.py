## The code is a fun exercise in Python that flips random bits of binaries and then runs those binaries and computes the probability of them crashing. 

import subprocess
import os
import time
linuxdir = '/mnt/c/Users/Prikshet/Desktop/flipped/linked'
run = 0
noRun = 0
def check_pid(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

for file in os.listdir(linuxdir):
    print('Executing file', file)
    
    proc = subprocess.Popen(linuxdir+'/'+file)
    time.sleep(5)
    if check_pid(proc.pid):
        run += 1
        proc.kill()
        print("run=",run)
    else:
        noRun += 1
        print("noRun=", noRun)

print("noRun=", noRun)
print("run=", run)


