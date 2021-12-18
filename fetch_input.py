import os
import sys

import dotenv
import requests


dotenv.load_dotenv()
AOC_SESSION = os.getenv('AOC_SESSION')

def fetch_day(day: int, force: bool=False):
    infile_path = f'src/in/{day}.txt'

    if not force and os.path.exists(infile_path):
        return

    print(f'✔ Request being made for Day {day}')

    r = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers={
        'cookie': f'session={AOC_SESSION}'
    })

    if r.status_code != 200:
        raise RuntimeError(r.status_code, r.text)

    print(f'✔ File {day}.txt fetched')

    with open(infile_path, 'w') as f:
        f.write(r.text)
        print(f'✔ File saved as {infile_path}')


if __name__ == '__main__':
    day = int(sys.argv[1] if len(sys.argv) >= 2 else input('Day to fetch: '))
    fetch_day(day)
