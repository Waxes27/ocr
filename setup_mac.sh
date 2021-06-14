#!/bin/bash
mkdir -p "$HOME/Desktop/OCR"
mkdir -p "$HOME/Desktop/OCR/redo"
brew install tesseract

read -p "Start scanning now?[y/n]: " prompt

if [ $prompt == 'y' ]; then
rm -rf pictures/.DS_Sto*
./run.sh

fi