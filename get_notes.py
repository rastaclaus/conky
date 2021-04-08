# pylint: disable=invalid-name,missing-docstring
import os
from pathlib import Path
from textwrap import fill

import configparser as cpr

import simplenote as snapi


HOME = os.getenv('HOME')
SNCONFIG = Path(HOME) / '.snclirc'
NOTE_WIDTH = 46
TODO_INDENT = 6


def get_credentials(fname):
    config = cpr.ConfigParser()
    config.read(fname)
    return (
        config['sncli']['cfg_sn_username'],
        config['sncli']['cfg_sn_password']
    )


def get_notes_list():
    uname, pwd = get_credentials(SNCONFIG)
    sn = snapi.Simplenote(uname, pwd)
    notes, status = sn.get_note_list()
    if status != 0:
        raise RuntimeError("cannot sync with server")

    notes = filter(lambda n: not n['deleted'], notes)
    return list(notes)


def print_note(note):
    for line in note['content'].split('\n'):
        indent = " " * TODO_INDENT if line.startswith('-') else ""
        print(fill(line, NOTE_WIDTH, subsequent_indent=indent))
    print()


def main():
    notes_list = get_notes_list()
    for note in notes_list:
        print_note(note)


if __name__ == '__main__':
    main()
