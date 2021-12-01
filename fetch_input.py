import os
import sys

import dotenv
import requests


dotenv.load_dotenv()

day = int(sys.argv[1] if len(sys.argv) >= 2 else input('Day to fetch: '))

print(f'✔ Request being made for Day {day}')

AOC_SESSION = os.getenv('AOC_SESSION')
r = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers={
    'cookie': f'session={AOC_SESSION}'
})

print(f'✔ File {day}.txt fetched')

infile_path = f'solutions/in/{day}.txt'
with open(infile_path, 'w') as f:
    f.write(r.text)
    print(f'✔ File saved as {infile_path}')
