#!/bin/bash
# полный путь до скрипта
ABSOLUTE_FILENAME=`readlink -e "$0"`
# каталог в котором лежит скрипт
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

conky -c $DIRECTORY/rings & # the main conky with rings
conky -c $DIRECTORY/cpu &
conky -c $DIRECTORY/mem &
conky -c $DIRECTORY/notes &
