import os
import sys
import subprocess

from fetch_input import fetch_day


filename = sys.argv.pop(1) if len(sys.argv) >= 2 else input('Day to run: ')
day = int(filename.split('.', maxsplit=2)[0])
fetch_day(int(day))

os.chdir('./src')
subprocess.run([sys.executable, f'{filename}.py', *sys.argv[1:]])
os.chdir('..')
