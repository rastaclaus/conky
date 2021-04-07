import subprocess as sp
import json
from pprint import pformat

NOTES_COMMAND = ['joplin', 'ls', '-l', '-t', 't', '--format', 'json']


def get_todo_ids():
    res = sp.run(NOTES_COMMAND, stdout=sp.PIPE, encoding='utf-8')
    data = json.loads(res.stdout)
    for entry in data:
        yield (entry['id'], entry['todo_completed'])


def print_todo_text(todo_text):
    lines = todo_text.split('\n')
    header = lines[0]
    if len(lines) > 2:
        header += '...'
    print(header)


def get_todo_text(todo_id):
    command = ['joplin', 'cat', todo_id, '--format', 'json']
    res = sp.run(command, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    return res.stdout


def print_todo(todo_id, todo_completed):
    cmp_char = "x" if todo_completed else " "
    todo_text = f"[{cmp_char}] " + get_todo_text(todo_id)
    print_todo_text(todo_text)


def main():
    for todo_id, todo_completed in get_todo_ids():
        print_todo(todo_id, todo_completed)


if __name__ == '__main__':
    main()
