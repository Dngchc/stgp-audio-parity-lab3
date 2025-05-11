import hashlib

def generate_hash(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            file_content = f.read()

        sha256_hash = hashlib.sha256(file_content).hexdigest()

        with open(output_file, 'w') as f:
            f.write(sha256_hash)

        print(f"Hash has been created and saved to {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the input file path: ")
    output_file = input("Enter the output file name: ")

    generate_hash(input_file, output_file)

