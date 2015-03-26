#!/bin/bash


set -e


# Clean up first
echo "Cleaning build directory."
./clean.sh
mkdir -p tmp
mkdir -p webroot
mkdir -p webroot/json


echo "Copying static files into webroot."
cp -r static webroot/

echo "Building articles."
for article in pages/articles/*
do

  echo "Operating on $article."

  echo "  Generating asset filenames."
  ID=$(echo $article | sed 's/[^/]*\/[^/]*\///' )
  TITLE_FILE="pages/articles/$ID/title.txt"
  ARTICLE_FILE="pages/articles/$ID/article.html"
  OVERVIEW_FILE="pages/articles/$ID/overview.html"
  COPYRIGHT_FILE="pages/articles/$ID/copyright.html"
  ANNOTATIONS_FILE="pages/articles/$ID/annotations.json"
  CREATOR_FILE="pages/articles/$ID/creator.html"

  echo "  Checking file presence."
  if [ ! -f $TITLE_FILE ]; then echo "No file $TITLE_FILE found.  Exiting."; exit; fi
  if [ ! -f $OVERVIEW_FILE ]; then echo "No file $OVERVIEW_FILE found.  Exiting."; exit; fi
  if [ ! -f $ARTICLE_FILE ]; then echo "No file $ARTICLE_FILE found.  Exiting."; exit; fi
  if [ ! -f $CREATOR_FILE ]; then echo "No file $CREATOR_FILE found. Exiting."; exit; fi
  if [ ! -f $COPYRIGHT_FILE ]; then echo "No file $COPYRIGHT_FILE found.  Exiting."; exit; fi
  if [ ! -f $ANNOTATIONS_FILE ]; then echo "No file $ANNOTATIONS_FILE found.  Exiting."; exit; fi

  echo "  Reading data."
  TITLE=$( cat $TITLE_FILE )
  ARTICLE=$( cat $ARTICLE_FILE )
  OVERVIEW=$( cat $OVERVIEW_FILE )
  COPYRIGHT=$( cat $COPYRIGHT_FILE )
  CREATOR=$( cat $CREATOR_FILE )
  
  echo "  Generating template."
  cat layout/head.html    >  "tmp/$ID.html"
  cat layout/article.html >> "tmp/$ID.html"
  cat layout/foot.html    >> "tmp/$ID.html"

  echo "  Populating template with data."
  sed -i -e "s|{{ TITLE }}|$TITLE|" \
         -e "s|{{ ID }}|$(echo $ID)|" \
         -e "s|{{ COPYRIGHT }}|$(echo $COPYRIGHT)|" \
         -e "s|{{ OVERVIEW }}|$(echo $OVERVIEW)|" \
         -e "s|{{ ARTICLE }}|$(echo $ARTICLE)|" \
         -e "s|{{ CREATOR }}|$(echo $CREATOR)|" \
         "tmp/$ID.html"

  echo "  Moving into webroot."
  mv "tmp/$ID.html" webroot/
  cp $ANNOTATIONS_FILE "webroot/json/$ID.json"

  ASSETS="pages/articles/$ID/assets"
  if [ -e $ASSETS ]
  then

    echo "  Copying over assets."
    mkdir -p "webroot/assets/$ID"
    cp -r $ASSETS/* "webroot/assets/$ID"

  fi

done



echo "Building site pages."
for page in pages/site/*
do

  echo "Operating on $page."

  echo "  Generating asset filenames."
  ID=$(echo $page | sed 's/[^/]*\/[^/]*\///' )
  TITLE_FILE="pages/site/$ID/title.txt"
  BODY_FILE="pages/site/$ID/body.html"
 
  
  echo "  Checking file presence."
  if [ ! -f $TITLE_FILE ]; then echo "No file $TITLE_FILE found.  Exiting."; exit; fi
  if [ ! -f $BODY_FILE ]; then echo "No file $BODY_FILE found.  Exiting."; exit; fi
 

  echo "  Reading data."
  TITLE=$( cat $TITLE_FILE )
  BODY=$( cat $BODY_FILE )
  

  echo "  Generating template."
  cat layout/head.html >  "tmp/$ID.html"
  cat $BODY_FILE       >> "tmp/$ID.html"
  cat layout/foot.html >> "tmp/$ID.html"

  echo "  Populating template with data."
  sed -i -e "s|{{ TITLE }}|$TITLE|"  \
	"tmp/$ID.html"

	echo "  Removing copyright placeholder in help file."
	sed -i -e "/{{ COPYRIGHT }}/d" \
	   "tmp/$ID.html"
	
	echo "  Removing creator placeholder in help file."
	sed -i -e "/{{ CREATOR }}/d" \
	   "tmp/$ID.html"
	
  echo "  Moving into webroot."
  mv "tmp/$ID.html" webroot/

done


echo "Cleaning up."
rmdir tmp
