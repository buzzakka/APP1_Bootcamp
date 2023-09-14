#!/bin/sh

echo "Вариант True:"
python3 mfinder.py < tests/m.txt

echo "Вариант False:"
python3 mfinder.py < tests/false1.txt

echo "Вариант False:"
python3 mfinder.py < tests/false2.txt

echo "Вариант False:"
python3 mfinder.py < tests/false2.txt

echo "Вариант Ошибка:"
python3 mfinder.py < tests/error1.txt

echo "Вариант Ошибка:"
python3 mfinder.py < tests/error2.txt

echo "Вариант Ошибка:"
python3 mfinder.py < tests/error3.txt