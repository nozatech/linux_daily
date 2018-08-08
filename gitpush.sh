#!/bin/bash

echo "Checking if there is any changes...."
git status
sleep 3
echo
echo

echo "Newly changed files are adding to the stage...."
git add .
echo 
echo

echo "Committing to Stage...."
git commit -m "update"
echo
echo

echo "Uploading to Github...."
git push
echo 
echo

echo "All files are uploaded to Gibhub." 
echo "Check your new files on the Gibhub."
