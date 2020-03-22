input_string = "010110100110010101110010011011110101001101110100011000010110011101100101"
output_string = ""
for i in range((len(input_string)//8)):
    output_string += chr(int(input_string[8*i:8*(i+1)], 2))
print(output_string)
