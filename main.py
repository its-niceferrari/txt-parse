import os

def parse_text_files(directory):
    f = open("txt_parse.log", "x")
    # Iterate through all files in the directory
    f.write("[INFO] Parsing for text documents in the following directory: " + os.path.abspath(directory) + "\n\n")
    for filename in os.listdir(directory):
        # Print the filename to the terminal
        f.write(filename + "\n")
        # Check if the file is a text file
        if filename.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory, filename), 'r') as file:
                contents = file.read()
                # Print the contents of the file to the terminal
                f.write(contents + "\n")
        else: f.write("[WARNING]: " + filename + " is not a supported file format.\n\n")
    f.write("[INFO] Parsing complete.")


if __name__ == '__main__':
    directory = input('Input the directory to parse: ')
    parse_text_files(directory)