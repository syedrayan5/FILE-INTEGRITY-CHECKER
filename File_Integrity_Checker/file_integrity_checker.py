import hashlib
import os
import json

class FileIntegrityChecker:
    def __init__(self, hash_algorithm='sha256', hash_file='file_hashes.json'):
        self.hash_algorithm = hash_algorithm
        self.hash_file = hash_file

    def calculate_hash(self, file_path):
        """
        Calculates the hash of a file using the specified hashing algorithm.
        """
        hash_func = hashlib.new(self.hash_algorithm)
        try:
            with open(file_path, 'rb') as file:
                while chunk := file.read(8192):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None

    def save_hashes(self, directory):
        """
        Scans the directory, calculates hashes for all files, and saves them to a JSON file.
        """
        file_hashes = {}
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hashes[file_path] = self.calculate_hash(file_path)
        with open(self.hash_file, 'w') as f:
            json.dump(file_hashes, f, indent=4)
        print(f"File hashes saved to {self.hash_file}")

    def check_integrity(self, directory):
        """
        Compares the current hashes of files in the directory with the saved hashes.
        """
        if not os.path.exists(self.hash_file):
            print(f"Hash file {self.hash_file} not found. Please save hashes first.")
            return

        with open(self.hash_file, 'r') as f:
            saved_hashes = json.load(f)

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                current_hash = self.calculate_hash(file_path)
                saved_hash = saved_hashes.get(file_path)

                if saved_hash is None:
                    print(f"NEW FILE: {file_path}")
                elif current_hash != saved_hash:
                    print(f"MODIFIED FILE: {file_path}")
                else:
                    print(f"UNCHANGED FILE: {file_path}")

        # Check for deleted files
        for file_path in saved_hashes:
            if not os.path.exists(file_path):
                print(f"DELETED FILE: {file_path}")

if __name__ == "__main__":
    print("File Integrity Checker")
    print("1. Save file hashes")
    print("2. Check file integrity")
    choice = input("Enter your choice (1 or 2): ")

    directory = input("Enter the directory to monitor: ")
    checker = FileIntegrityChecker()

    if choice == '1':
        checker.save_hashes(directory)
    elif choice == '2':
        checker.check_integrity(directory)
    else:
        print("Invalid choice.")
