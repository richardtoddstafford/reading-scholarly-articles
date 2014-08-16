#!/bin/bash

set -e

# Clean up first
clean.sh
mkdir -p tmp
mkdir -p webroot

for page in pages/content/*
do

  FILENAME=$(echo $page | sed 's/[^/]*\/[^/]*\///')
  TITLE=$(head -n 1 pages/titles/$FILENAME)

  cat layout/head.html        >  "tmp/$FILENAME.html"
  cat pages/content/$FILENAME >> "tmp/$FILENAME.html"
  cat layout/foot.html        >> "tmp/$FILENAME.html"

  sed -i "s|{{ TITLE }}|$TITLE|" "tmp/$FILENAME.html"

  mv tmp/$FILENAME.html webroot/

done

rmdir tmp

cp -r static webroot/
cp -r assets webroot/
