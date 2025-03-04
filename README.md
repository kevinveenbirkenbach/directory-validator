# Directory Validator (dirval) 📂✅

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kevinveenbirkenbach/directory-validator.svg?style=social)](https://github.com/kevinveenbirkenbach/directory-validator/stargazers)

Directory Validator is a Python utility that creates and verifies a unique hash stamp for an entire directory. This stamp, saved as a JSON file, represents the directory’s structure and content (excluding the stamp file itself), allowing you to quickly detect any changes.

## 🛠 Features

- **Stamp Creation:** Generate a unique SHA-256 hash for all files and subdirectories.
- **Validation:** Recalculate the hash to determine if any files or directories have changed.
- **Exclusion Handling:** Automatically ignores the stamp file and hidden folders like `.git`.
- **Simple CLI Interface:** Easily create or validate stamps via command-line options.

## 📥 Installation

Install Directory Validator via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `dirval`:

```bash
package-manager install dirval
```

This installs Directory Validator globally so you can run `dirval` in your terminal. 🚀

## 🚀 Usage

### Create a Directory Stamp

Generate a stamp (hash and timestamp) for a directory. The stamp is saved as `directory_stemp.json` inside the directory.

```bash
dirval <path_to_directory> --stamp
```

### Validate a Directory

Compare the current directory state against the stored stamp to check for any modifications.

```bash
dirval <path_to_directory> --validate
```

## 📖 How It Works

- The script recursively walks through the given directory and collects all file and subdirectory paths (ignoring the stamp file and hidden directories like `.git`).
- It sorts the collected paths and computes a cumulative SHA-256 hash.
- The resulting hash, along with the current date and time, is saved in a JSON file (`directory_stemp.json`) within the directory.
- For validation, the script recalculates the current hash and compares it with the stored hash to detect any changes.

## 🧑‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 🌐 [veen.world](https://www.veen.world)

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues if you have suggestions or encounter any problems. Let's improve directory validation together! 😊
