import os
from pathlib import Path
import textwrap


HOME = os.getenv('HOME')
NOTES_PATH = Path(HOME) / 'notes.txt'


def main(notes_path=NOTES_PATH):
    with open(notes_path) as notes_file:
        for line in notes_file:
            for wrapped in textwrap.wrap(line, 40):
                print(wrapped)
            print()


if __name__ == '__main__':
    main()
