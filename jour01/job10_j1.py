import string

alphabet = string.ascii_lowercase
line_length = 1  # Initialize line_length to 1 for the first line

for i in range(14):
    # Extract the characters for the current line
    line = alphabet[:line_length]
    # Print the line
    print(line)
    # Increment line length for the next iteration
    line_length += 2
