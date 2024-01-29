import argparse
import hashlib
import json
import os
from datetime import datetime

def generate_directory_hash(directory_path):
    if not os.path.exists(directory_path):
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

    return sha_hash.hexdigest()

def create_stemp_file(path):
    hash_value = generate_directory_hash(path)
    data = {"hash": hash_value, "date": datetime.now().isoformat()}
    with open(os.path.join(path, "directory_stemp.json"), "w") as file:
        json.dump(data, file)
    print("Stempel-File erstellt.")

def validate(path):
    stemp_file_path = os.path.join(path, "directory_stemp.json")
    if not os.path.exists(stemp_file_path):
        print("Stempel-File nicht gefunden.")
        return

    with open(stemp_file_path, "r") as file:
        stemp_data = json.load(file)

    current_hash = generate_directory_hash(path)
    if current_hash == stemp_data["hash"]:
        print("Validierung erfolgreich. Der Hashwert stimmt überein.")
    else:
        print("Validierung fehlgeschlagen. Der Hashwert stimmt nicht überein.")

def main():
    parser = argparse.ArgumentParser(description='Erstellen und Validieren eines Directory-Stempels.')
    parser.add_argument('path', type=str, help='Pfad des Verzeichnisses')
    parser.add_argument('--stamp', action='store_true', help='Erstelle einen Stempel für das Verzeichnis')
    parser.add_argument('--validate', action='store_true', help='Validiere das Verzeichnis')

    args = parser.parse_args()

    if args.stamp:
        create_stemp_file(args.path)
    elif args.validate:
        validate(args.path)
    else:
        print("Bitte verwenden Sie --stamp oder --validate")

if __name__ == "__main__":
    main()
