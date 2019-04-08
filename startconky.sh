#!/bin/bash
conky -c ~/.conky/rings & # the main conky with rings
conky -c ~/.conky/cpu &
conky -c ~/.conky/mem &
conky -c ~/.conky/notes &
conky -c ~/.conky/calendar &
