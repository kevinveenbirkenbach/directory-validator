import hashlib
import json
import os
import sys
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
    """Erstelle ein Stempel-File mit dem Hashwert und dem Datum."""
    hash_value = generate_directory_hash(path)
    data = {
        "hash": hash_value,
        "date": datetime.now().isoformat()
    }
    with open("directory_stemp.json", "w") as file:
        json.dump(data, file)
    print("Stempel-File erstellt.")

def validate(path):
    """Validiere den Hashwert des Pfades mit dem im Stempel-File."""
    if not os.path.exists("directory_stemp.json"):
        print("Stempel-File nicht gefunden.")
        return

    with open("directory_stemp.json", "r") as file:
        stemp_data = json.load(file)

    current_hash = generate_directory_hash(path)

    if current_hash == stemp_data["hash"]:
        print("Validierung erfolgreich. Der Hashwert stimmt überein.")
    else:
        print("Validierung fehlgeschlagen. Der Hashwert stimmt nicht überein.")

def main():
    if "--stamp" in sys.argv:
        # Nehmen Sie an, dass der Pfad das aktuelle Verzeichnis ist
        create_stemp_file(os.getcwd())
    elif "--validate" in sys.argv:
        validate(os.getcwd())
    else:
        print("Bitte verwenden Sie --stamp oder --validate")

if __name__ == "__main__":
    main()
