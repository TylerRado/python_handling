# File Read & Write Challenge 🖋️
# Create a program that reads a file and writes a modified version to a new file.

def modify_file(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_file}' was successfully modified and saved as '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_file = 'input.txt'   # Replace with your input file
    output_file = 'output.txt' # Replace with your desired output file
    modify_file(input_file, output_file)




    # Error Handling Lab : 
    # Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ").strip()
        
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\n File Content:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"\n Error: The file '{filename}' does not exist. Please check the name and try again.")
    
    except PermissionError:
        print(f"\n Error: You don't have permission to read the file '{filename}'.")
    
    except IsADirectoryError:
        print(f"\n Error: '{filename}' is a directory, not a file.")
    
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")


# Run the file reader
if __name__ == "__main__":
    read_file()

