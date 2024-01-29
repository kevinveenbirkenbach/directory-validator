import argparse
import hashlib
import json
import os
from datetime import datetime

def generate_directory_hash(directory_path, verbose):
    if not os.path.exists(directory_path):
        if verbose:
            print("Directory does not exist.")
        return -1

    sha_hash = hashlib.sha256()
    paths = []

    for root, dirs, files in os.walk(directory_path):
        dirs.sort()
        files.sort()
        for name in dirs + files:
            if root == directory_path and name == 'directory_stemp.json':
                continue

            rel_path = os.path.relpath(os.path.join(root, name), directory_path)
            paths.append(rel_path)

    for path in sorted(paths):
        sha_hash.update(path.encode('utf-8'))

    if verbose:
        print(f"Generated hash for directory: {directory_path}")

    return sha_hash.hexdigest()

def create_stemp_file(path, verbose=False):
    hash_value = generate_directory_hash(path, verbose)
    data = {"hash": hash_value, "date": datetime.now().isoformat()}
    with open(os.path.join(path, "directory_stemp.json"), "w") as file:
        json.dump(data, file)
    if verbose:
        print("Stamp file created.")

def validate(path, verbose=False):
    stemp_file_path = os.path.join(path, "directory_stemp.json")
    if not os.path.exists(stemp_file_path):
        if verbose:
            print("Stamp file not found.")
        return

    with open(stemp_file_path, "r") as file:
        stemp_data = json.load(file)

    current_hash = generate_directory_hash(path, verbose)
    if current_hash == stemp_data["hash"]:
        if verbose:
            print("Validation successful. The hash value matches.")
        else:
            print("Validation failed. The hash value does not match.")

def main():
    parser = argparse.ArgumentParser(description='Create and validate a directory stamp.')
    parser.add_argument('path', type=str, help='Path of the directory')
    parser.add_argument('--stamp', action='store_true', help='Create a stamp for the directory')
    parser.add_argument('--validate', action='store_true', help='Validate the directory')
    parser.add_argument('--verbose', action='store_true', help='Provide detailed information about the steps')

    args = parser.parse_args()

    if args.stamp:
        create_stemp_file(args.path, args.verbose)
    elif args.validate:
        validate(args.path, args.verbose)
    else:
        print("Please use --stamp or --validate")

if __name__ == "__main__":
    main()