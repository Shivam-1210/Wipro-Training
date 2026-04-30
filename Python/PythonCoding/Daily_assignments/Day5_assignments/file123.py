

filename = input("Enter the filename you want to open: ")


try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("File contents:\n")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")