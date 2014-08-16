#!/bin/bash

set -e

# Clean up first
rm -f webroot/*.html
mkdir -p tmp

for page in pages/content/*
do

  FILENAME=$(echo $page | sed 's/[^/]*\/[^/]*\///')
  TITLE=$(head -n 1 pages/titles/$FILENAME)

  cat layout/head.html        >  "tmp/$FILENAME.html"
  cat pages/content/$FILENAME >> "tmp/$FILENAME.html"
  cat layout/bottom.html      >> "tmp/$FILENAME.html"

  sed -i "s|{{ TITLE }}|$TITLE|" "tmp/$FILENAME.html"

  mv tmp/$FILENAME.html webroot/

done

rmdir tmp
