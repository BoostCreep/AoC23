def extract_first_and_last_digit(line):
    # Extract the first and last characters if they are digits
    digits = [char for char in line if char.isdigit()]
    
    if len(digits) == 1:
        # Duplicate the digit if there is only one on the line
        return digits[0], digits[0]
    elif len(digits) >= 2:
        return digits[0], digits[-1]
    else:
        return None, None

def process_and_print(file_path):
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Extract first and last digits from each line, duplicate if needed, and display modified lines
            for line_number, line in enumerate(lines, start=1):
                first_digit, last_digit = extract_first_and_last_digit(line)

                if first_digit is not None and last_digit is not None:
                    combined_number = int(f"{first_digit}{last_digit}")
                    print(f"Line {line_number}: {first_digit}{last_digit} (Combined: {combined_number})")
                    total_sum += combined_number

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"\nTotal Sum of Combined Numbers: {total_sum}")

# Replace 'Y:\\AoC23\\input.txt' with the actual path to your input text file
file_path = 'Y:\\AoC23\\input.txt'
process_and_print(file_path)
