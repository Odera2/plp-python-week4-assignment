def read_and_write_file():
    # File names
    input_filename = "FilehandlingAndErrorLab/input.txt"
    output_filename = "FilehandlingAndErrorLab/output.txt"

    try:
        # Open input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
read_and_write_file()
