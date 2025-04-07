def read_file_with_error_handling():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{filename}'.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Run the function
read_file_with_error_handling()
