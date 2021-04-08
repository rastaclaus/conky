#!/bin/bash
sudo ps -aux | grep conky | grep -v startconky | cut -d' ' -f5 | xargs kill -KILL;

conky -c ~/.conky/rings & # the main conky with rings
conky -c ~/.conky/cpu &
conky -c ~/.conky/mem &
conky -c ~/.conky/todo &
conky -c ~/.conky/notes &
conky -c ~/.conky/news &
# conky -c ~/.conky/calendar &
