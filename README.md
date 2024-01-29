# Directory Validator

This Python script provides a simple yet effective way to create a stamp (a unique hash value) for a directory, which can then be used to validate the directory's contents later on. It's designed to detect any changes in the structure or contents of the directory.

## Features

- **Create Stamp**: Generate a unique hash for the entire directory, considering all files and subdirectories, except for the stamp file itself.
- **Validate Directory**: Compare the current state of the directory against the stored hash value to detect any changes.
- **Verbose Output**: Optional detailed output for more insights into the process.

## Usage

First, ensure you have Python installed on your system. Then, use the script from the command line as follows:

To create a stamp for a directory:

```
python directory_validator.py <path_to_directory> --stamp [--verbose]
```

To validate a directory:

```
python directory_validator.py <path_to_directory> --validate [--verbose]
```

## How It Works

- The script walks through the directory, generating a cumulative SHA-256 hash of all file and directory paths.
- The generated hash, along with the current date and time, is stored in a file named `directory_stemp.json` within the directory.
- For validation, the script recalculates the current directory's hash and compares it with the stored hash.

## Author

Kevin Veen-Birkenbach
- Website: [veen.world](https://www.veen.world)

## Repository

This script is maintained at [GitHub](https://github.com/kevinveenbirkenbach/directory-validator).

## Acknowledgments

This script was developed with the assistance of ChatGPT. You can find the conversation that led to this script [here](https://chat.openai.com/share/2ad61078-7190-42f7-8fd5-0d0440cd29db).

---

Feel free to contribute to this project or suggest improvements. For any issues or questions, please open an issue on the GitHub repository.