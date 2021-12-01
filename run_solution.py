import os
import sys
import subprocess


day = int(sys.argv[1] if len(sys.argv) >= 2 else input('Day to run: '))
os.chdir('./solutions')
subprocess.run(['python', f'{day}.py'])
os.chdir('..')
