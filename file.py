def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content (example: converting text to uppercase)
        modified_content = content.upper()  # Modify the content (you can customize this)

        # Write the modified content to the new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File processed successfully! The modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the filename
input_filename = input("Please enter the filename to read: ")
output_filename = input("Please enter the filename to write the modified content: ")

# Call the function to read, modify, and write to the new file
read_and_modify_file(input_filename, output_filename)
