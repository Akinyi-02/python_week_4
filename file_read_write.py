# File Read & Write Challenge

def read_and_write_file():
    # Ask for the filename to read
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the new filename to write to: ")

    try:
        #Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()
            #Modify the content
            modified_content = content.upper()

        # Write the modified content to the new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read or write the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_and_write_file()
