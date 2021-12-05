import os
import sys
import subprocess


day = sys.argv[1] if len(sys.argv) >= 2 else input('Day to run: ')

os.chdir('./src')
subprocess.run(['python', f'{day}.py'] + sys.argv[2:])
os.chdir('..')
