def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read the entire content of the file
            content = infile.read()

        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()  # You can change this transformation as needed

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Write the modified content to the new file
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'    # Replace with your input file name
output_file = 'output.txt'  # The file where modified content will be saved
modify_file(input_file, output_file)






def read_file():
    # Ask the user for a filename
    filename = input("Please enter the filename you want to read: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content successfully read:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IsADirectoryError:
        print(f"Error: Expected a file, but found a directory instead: '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to read the file
read_file()
