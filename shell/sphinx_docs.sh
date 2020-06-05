#!/bin/bash


cd ./docs
make html
git add .
git commit -m "test"
git push