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
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            return
        
        if not os.path.isdir(directory):
            print(f"Error: '{directory}' is not a directory.")
            return

        file_hashes = {}
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.abspath(os.path.join(root, file))
                
                # Skip hidden/system files (optional)
                if file.startswith('.'):
                    continue  

                file_hash = self.calculate_hash(file_path)
                if file_hash:
                    file_hashes[file_path] = file_hash

        if not file_hashes:
            print("Error: No valid files found to save hashes.")
            return

        with open(self.hash_file, 'w') as f:
            json.dump(file_hashes, f, indent=4)
        print(f"File hashes saved to {self.hash_file}")

    def check_integrity(self, directory):
        """
        Compares the current hashes of files in the directory with the saved hashes.
        """
        if not os.path.exists(self.hash_file):
            print(f"Error: Hash file '{self.hash_file}' not found. Please save hashes first.")
            return

        try:
            with open(self.hash_file, 'r') as f:
                saved_hashes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: Hash file is empty or corrupt.")
            return

        if not saved_hashes:
            print("Error: No hashes found in the file. Please save hashes first.")
            return

        found_changes = False

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.abspath(os.path.join(root, file))
                
                # Skip hidden/system files (optional)
                if file.startswith('.'):
                    continue  

                current_hash = self.calculate_hash(file_path)
                saved_hash = saved_hashes.get(file_path)

                if saved_hash is None:
                    print(f"NEW FILE: {file_path}")
                    found_changes = True
                elif current_hash != saved_hash:
                    print(f"MODIFIED FILE: {file_path}")
                    found_changes = True
                else:
                    print(f"UNCHANGED FILE: {file_path}")

        # Check for deleted files
        for file_path in saved_hashes:
            if not os.path.exists(file_path):
                print(f"DELETED FILE: {file_path}")
                found_changes = True

        if not found_changes:
            print("No changes detected.")

if __name__ == "__main__":
    print("File Integrity Checker")
    print("1. Save file hashes")
    print("2. Check file integrity")
    choice = input("Enter your choice (1 or 2): ")

    directory = input("Enter the directory to monitor: ").strip()
    checker = FileIntegrityChecker()

    if choice == '1':
        checker.save_hashes(directory)
    elif choice == '2':
        checker.check_integrity(directory)
    else:
        print("Invalid choice.")
