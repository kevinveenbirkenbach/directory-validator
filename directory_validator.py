import argparse
import hashlib
import json
import os
from datetime import datetime

def generate_directory_hash(directory_path):
    if not os.path.exists(directory_path):
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

    print(f"Generated hash for directory: {directory_path}")

    return sha_hash.hexdigest()

def create_stemp_file(path):
    hash_value = generate_directory_hash(path)
    data = {"hash": hash_value, "date": datetime.now().isoformat()}
    with open(os.path.join(path, "directory_stemp.json"), "w") as file:
        json.dump(data, file)
    print("Stamp file created.")

def validate(path):
    stemp_file_path = os.path.join(path, "directory_stemp.json")
    if not os.path.exists(stemp_file_path):
        print("Stamp file not found.")
        return

    with open(stemp_file_path, "r") as file:
        stemp_data = json.load(file)

    current_hash = generate_directory_hash(path)
    if current_hash == stemp_data["hash"]:
        print("Validation successful. The hash value matches.")
        exit(0)
    print("Validation failed. The hash value does not match.")
    exit(1)

def main():
    parser = argparse.ArgumentParser(description='Create and validate a directory stamp.')
    parser.add_argument('path', type=str, help='Path of the directory')
    parser.add_argument('--stamp', action='store_true', help='Create a stamp for the directory')
    parser.add_argument('--validate', action='store_true', help='Validate the directory')

    args = parser.parse_args()

    if args.stamp:
        create_stemp_file(args.path)
    elif args.validate:
        validate(args.path)
    else:
        print("Please use --stamp or --validate")

if __name__ == "__main__":
    main()