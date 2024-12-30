import hashlib
import os
import json

# Function to calculate the hash of a file
def calculate_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Function to save hash values to a JSON file
def save_hashes(directory, output_file):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    with open(output_file, 'w') as f:
        json.dump(file_hashes, f, indent=4)
    print(f"Hashes saved to {output_file}")

# Function to check for changes in files
def check_integrity(directory, hash_file):
    with open(hash_file, 'r') as f:
        stored_hashes = json.load(f)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            stored_hash = stored_hashes.get(file_path)
            
            if not stored_hash:
                print(f"NEW FILE: {file_path}")
            elif current_hash != stored_hash:
                print(f"MODIFIED FILE: {file_path}")
            else:
                print(f"UNCHANGED FILE: {file_path}")

    # Check for deleted files
    for file_path in stored_hashes:
        if not os.path.exists(file_path):
            print(f"DELETED FILE: {file_path}")

# Main function
def main():
    print("1. Save hashes")
    print("2. Check integrity")
    choice = input("Enter your choice: ")
    directory = input("Enter the directory path: ")
    hash_file = "file_hashes.json"

    if choice == '1':
        save_hashes(directory, hash_file)
    elif choice == '2':
        if os.path.exists(hash_file):
            check_integrity(directory, hash_file)
        else:
            print(f"{hash_file} not found! Please save hashes first.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
