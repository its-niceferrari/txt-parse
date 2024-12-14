import logging
import os

def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def parse_text_files(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        logging.error("Invalid directory provided.")
        print("Error: Directory does not exist or is not a directory.")
        return

    logging.info("Parsing text files in directory: %s", os.path.abspath(directory))
    total_files = 0
    text_files = 0
    skipped_files = 0

    for root, _, files in os.walk(directory):  # Recursively traverse directories
        for filename in files:
            total_files += 1
            file_path = os.path.join(root, filename)
            print(file_path)

            if filename.endswith('.txt'):
                text_files += 1
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        contents = file.read()
                        logging.info("Processed file: %s", filename)
                        print("\t" + contents)
                except Exception as e:
                    logging.error("Error reading file %s: %s", filename, str(e))
            else:
                skipped_files += 1
                logging.warning("Skipped file: %s (unsupported format)", filename)

    logging.info("Parsing complete. Total files: %d, Text files: %d, Skipped files: %d",
                 total_files, text_files, skipped_files)
    print("Parsing complete. Check the log file for details.")


if __name__ == '__main__':
    directory = input('Input the directory to parse: ')
    log_file = "txt_parse.log"
    setup_logger(log_file)
    parse_text_files(directory)
