#!/usr/bin/env python
# This script is a custom wc – word, line, character, and byte count command line tool
import sys
import os
import locale


def count_bytes_file(filename):
    file_size = os.stat(filename).st_size
    return file_size

def count_bytes_stdin(text):
    return len(text.encode('utf-8'))

def count_lines(text):
    return text.count('\n')


def count_words(text):
    return len(text.split())


def count_chars(text):
    return len(text)


def process_file(filename, options):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory")
        sys.exit(1)

    results = []
    if not options or 'l' in options:
        results.append(str(count_lines(text)))
    if not options or 'w' in options:
        results.append(str(count_words(text)))
    if not options or 'c' in options:
        results.append(str(count_bytes_file(filename)))
    if 'm' in options:
        results.append(str(count_chars(text)))

    results.append(filename)
    print('\t'.join(results))


def process_stdin(options):
    text = sys.stdin.read()
    results = []
    if 'l' in options:
        results.append(str(count_lines(text)))
    if 'w' in options:
        results.append(str(count_words(text)))
    if 'c' in options:
        results.append(str(count_bytes_stdin(text)))
    if 'm' in options:
        results.append(str(count_chars(text)))

    print('\t'.join(results))


def main():
    if len(sys.argv) == 1:
        process_stdin('lwc')
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith('-'):
            process_stdin(sys.argv[1][1:])
        else:
            process_file(sys.argv[1], '')
    elif len(sys.argv) == 3:
        if sys.argv[1].startswith('-'):
            process_file(sys.argv[2], sys.argv[1][1:])
        else:
            process_file(sys.argv[1], sys.argv[2][1:])
    else:
        print("Usage: ccwc [-clwm] [file]")
        sys.exit(1)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    main()
