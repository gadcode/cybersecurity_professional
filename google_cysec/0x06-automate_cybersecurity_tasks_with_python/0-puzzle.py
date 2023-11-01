# ------------------------------------------------------------
# This program contains the solution to a puzzle
# given in the first week and module of this course - Automate
# Cybersecurity Tasks with Python).
#
# Here is the binary representation of an ASCII
# charcter given to us to translate to plane text:
# """
# 01100110 01101001 01101110 01100100 00101110 01100110\
# 01101111 01101111 00101111 00110010 00110000 00110010\
# 00110011 01000111 01101111 01101100 01100101 01000011\
# 01100101 01110010 01110100 01110011
# """
# ------------------------------------------------------------

binary_sequence = "01100110 01101001 01101110 01100100 00101110\
        01100110 01101111 01101111 00101111 00110010 00110000\
        00110010 00110011 01000111 01101111 01101100 01100101\
        01000011 01100101 01110010 01110100 01110011"

# Split the binary sequence into individual binary numbers
binary_numbers = binary_sequence.split()

# Convert each binary number to its decimal representation and
# then to its ASCII character
text = ''.join([chr(int(binary, 2)) for binary in binary_numbers])

print(text)

# => OUTPUTS:
# find.foo/2023GoleCerts
