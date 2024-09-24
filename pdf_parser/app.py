import re
import argparse
from PyPDF2 import PdfReader

SENTENCE_MULTIPLIERS = {
    'million': 1_000_000,
    'billion': 1_000_000_000,
    'thousand': 1_000,
    'm': 1_000_000,
    'b': 1_000_000_000,
}

# Function to check if a number is in a sentence
def is_in_sentence(text, number_start_pos):
    # Check a window of 50 characters before and after the number for sentence structure
    window_size = 50
    before_text = text[max(0, number_start_pos - window_size):number_start_pos]
    after_text = text[number_start_pos:number_start_pos + window_size]

    # Check for sentence-ending punctuation followed by a capital letter
    if re.search(r'[\.\?!]\s+[A-Z]', before_text):
        return True
    return False

# Function to find numbers in text and apply the current multiplier to them
def find_numbers_in_text(text, multiplier=1):
    numbers = []
    
    # Regex pattern to capture numbers and optional scaling keywords ('million', 'billion', etc.)
    pattern = r'\b(\d{1,3}(?:,\d{3})*(?:\.\d+)?)(?:\s?(M|million|billion|thousand))?\b'

    # Find all numeric values and their possible scale (million, billion, etc.)
    matches = re.finditer(pattern, text, re.IGNORECASE)

    for match in matches:
        num_str, scale = match.groups()
        number_start_pos = match.start()

        # Remove commas from the number and convert to float
        number = float(num_str.replace(',', ''))

        # If the number is part of a sentence, we will not apply the multiplier unless followed by a scale
        if is_in_sentence(text, number_start_pos):
            if scale:
                number *= SENTENCE_MULTIPLIERS.get(scale.lower(), 1)
        else:
            # If it's not part of a sentence, apply the current chart-based multiplier
            number *= multiplier

        numbers.append(number)

    return numbers

# Function to process text and update the multiplier based on keywords like "in millions"
def update_multiplier(text):
    if "$M" in text:
        return 1_000_000
    elif "$B" in text:
        return 1_000_000_000
    if "in millions" in text.lower():
        return 1_000_000
    elif "in billions" in text.lower():
        return 1_000_000_000
    elif "in thousands" in text.lower():
        return 1_000
    else:
        return 1  # Default multiplier if no scaling keyword is found

# Main function to parse the document and apply multipliers to numbers correctly
def find_largest_number_in_pdf(pdf_file):
    largest_number = float('-inf')  # Initialize to a very small number
    page_of_largest = None  # Variable to store the page number of the largest number

    reader = PdfReader(pdf_file)
    
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()

        if text:
            current_multiplier = 1  # Reset multiplier to 1 at the start of each page

            # Process the text line by line
            lines = text.splitlines()
            for line in lines:
                # Check for multiplier changes in the line
                new_multiplier = update_multiplier(line)
                if new_multiplier != 1:
                    current_multiplier = new_multiplier

                # Check if the line contains a sentence boundary to reset the multiplier
                if re.search(r'[\.\?!]\s+[A-Z]', line):
                    current_multiplier = 1

                # Search for numbers in this line and apply the current multiplier
                numbers = find_numbers_in_text(line, multiplier=current_multiplier)
                if numbers:
                    max_number_on_line = max(numbers)
                    if max_number_on_line > largest_number:
                        largest_number = max_number_on_line
                        page_of_largest = page_num + 1  # PyPDF2 uses 0-indexing, so add 1 to display the correct page number

    return largest_number, page_of_largest

# Path to your PDF file
# pdf_file = '/Users/morganmattone/Desktop/FY25AirForceWorkingCapitalFund.pdf'

def main(file_path):
    largest_number, page_of_largest = find_largest_number_in_pdf(file_path)
    if largest_number is not None:
        print(f"The largest number in the document is: {largest_number} (found on page {page_of_largest})")
    else:
        print("No numbers were found in the document.")

# If this script is run directly from the command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the largest number in a PDF.")
    parser.add_argument("file", help="Path to the PDF file")
    args = parser.parse_args()

    main(args.file)