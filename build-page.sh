#!/bin/bash

set -e

FILENAME=$1
TITLE=$(head -n 1 pages/titles/$FILENAME)

mkdir tmp

cat layout/head.html        >  "tmp/$FILENAME.html"
cat pages/content/$FILENAME >> "tmp/$FILENAME.html"
cat layout/bottom.html      >> "tmp/$FILENAME.html"

sed -i "s/{{ TITLE }}/$TITLE/" "tmp/$FILENAME.html"

mv tmp/$FILENAME.html webroot/
rmdir tmp
