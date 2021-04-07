import subprocess as sp
import json
from pprint import pformat
from textwrap import wrap

NOTES_COMMAND = ['joplin', 'ls', '-l', '-t', 'n', '--format', 'json']


def get_note_ids():
    res = sp.run(NOTES_COMMAND, stdout=sp.PIPE, encoding='utf-8')
    data = json.loads(res.stdout)
    for entry in data:
        yield entry['id']


def print_note_text(note_text):
    lines = note_text.split('\n')
    header = lines[0]
    if len(lines) > 2:
        header += ':'
    print(header)
    text = ' '.join(lines[1:])
    for line in wrap(text, 38):
        print(line)


def get_note_text(note_id):
    command = ['joplin', 'cat', note_id, '--format', 'json']
    res = sp.run(command, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    return res.stdout


def print_note(note_id):
    note_text = get_note_text(note_id)
    print_note_text(note_text)


def main():
    for note_id in get_note_ids():
        print_note(note_id)
        print()


if __name__ == '__main__':
    main()
