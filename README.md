# Word Unscrambler

Python script to unscramble words from a scramble word puzzle.

## Overview

This Python script reads a scramble word puzzle from a file (`text_to_find.txt`), unscrambles possible combinations, and checks against a list of valid words (`words.txt`). It outputs two files:
- `unscramble.log`: Logs all unscrambling operations.
- `valid-unscramble.log`: Logs valid words found in `words.txt`.

The default language is English based on `words.txt`, but you can replace `words.txt` with words from any language.

## Requirements

- Python 3.x

## Usage

1. Place your scramble word puzzle inside `text_to_find.txt`.
2. Change the words.txt to suit your language needs (Optional). [Default English](https://github.com/dwyl/english-words.git)
3. Run the script by executing `python word_unscrambler.py` in your terminal or command prompt.

4. The script will perform unscrambling operations and generate two output files:
   - `unscramble.log`: Contains all unscrambled combinations.
   - `valid-unscramble.log`: Contains valid words found in `words.txt`.

## Example

Given the default scramble word puzzle in `text_to_find.txt`, the `valid-unscramble.log` will include valid words like:
- var
- nod
- tag
- tags
- meow
- bus
- map
- mop

## Cons
Line Length Restriction: Ensure that each line in text_to_find.txt has the same length for the script to function correctly.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
