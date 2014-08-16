#!/bin/bash

set -e

for page in pages/content/*
do

  id=$(echo $page | sed 's/[^/]*\/[^/]*\///')
  build-page.sh $id

done
