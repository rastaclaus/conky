#!/bin/bash

cat ~/todo.txt | sed 's/^/ \${color #ddddff}x  \$color /g'
