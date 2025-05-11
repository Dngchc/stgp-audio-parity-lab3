def read_hash_from_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"[Error] File not found: {filepath}")
        return None

def main():
    file1 = input("Enter path to the first hash file: ").strip()
    file2 = input("Enter path to the second hash file: ").strip()

    hash1 = read_hash_from_file(file1)
    hash2 = read_hash_from_file(file2)

    if hash1 is None or hash2 is None:
        print("Cannot continue comparison due to missing file(s).")
        return

    print(f"\nHash from {file1}: {hash1}")
    print(f"Hash from {file2}: {hash2}")

    if hash1 == hash2:
        print("\nMatch: The two hash values are identical. (PASS)")
    else:
        print("\nMismatch: The two hash values are different. (FAIL)")

if __name__ == "__main__":
    main()

