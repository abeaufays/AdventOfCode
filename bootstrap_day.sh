#!/bin/bash
if [ $# -ne 2 ]; 
    then echo "Need to input years and day indicator (i.e $0 25 02)"
fi
mkdir -p -- y"$1"/d"$2"
echo "def answer(filename:str) -> int:
    return 0" > y"$1"/d"$2"/part1.py
echo "import y"$1".d"$2".part1 as part1

def test_answer():
    assert part1.answer(\"y"$1"/d"$2"/test\") == -1 # TO FILL" > y"$1"/d"$2"/test_part1.py

touch y"$1"/d"$2"/test
touch y"$1"/d"$2"/data
