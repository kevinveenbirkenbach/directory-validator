import argparse
import subprocess
import hashlib
import json
from datetime import datetime

def run_tree(level):
    command = ["tree"]
    if level is not None:
        command += ["-L", str(level)]
    return subprocess.check_output(command).decode()

def hash_output(output):
    return hashlib.sha256(output.encode()).hexdigest()

def create_json_file(hash_value, level, filename="directory_stemp.json"):
    data = {
        "hash": hash_value,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": level if level is not None else 0
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def validate_directory(level, expected_hash):
    output = run_tree(level)
    current_hash = hash_output(output)
    return current_hash == expected_hash

def main():
    parser = argparse.ArgumentParser(description="Directory Structure Tool")
    parser.add_argument("--level", type=int, help="Level of directory depth")
    parser.add_argument("--file", action="store_true", help="Create a JSON file")
    parser.add_argument("--stemp", action="store_true", help="Stamp the directory")
    parser.add_argument("--validate", action="store_true", help="Validate directory")
    parser.add_argument("--hash", help="Hash value for validation")

    args = parser.parse_args()

    if args.stemp:
        output = run_tree(args.level)
        hash_value = hash_output(output)
        print(f"Directory Hash: {hash_value}")
        if args.file:
            create_json_file(hash_value, args.level)

    if args.validate:
        if args.hash is None:
            print("Error: No hash value provided for validation.")
        else:
            is_valid = validate_directory(args.level, args.hash)
            print("Directory is valid." if is_valid else "Directory is not valid.")

if __name__ == "__main__":
    main()
