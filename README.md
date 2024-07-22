# ccwc - Custom Unix-Style wc Command Line Tool

`ccwc` is a Python script that mimics the functionality of the Unix `wc` command. It can count the number of bytes, lines, words, and characters in a file or from standard input.

## Features

- Count bytes in a file with the `-c` option.
- Count lines in a file with the `-l` option.
- Count words in a file with the `-w` option.
- Count characters in a file with the `-m` option.
- Default behavior counts lines, words, and bytes if no options are provided.
- Supports reading from standard input if no filename is specified.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ccwc.git
    ```

2. Navigate to the project directory:
    ```sh
    cd ccwc
    ```

3. Make the script executable (optional):
    ```sh
    chmod +x ccwc.py
    ```

## Usage Example

### Count Bytes

```sh
python ccwc.py -c test.txt

Output:
342190 test.txt
```

##Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

##Acknowledgments
Inspired by the Unix wc command.
Thank you to the Coding Challenges community for the idea.
