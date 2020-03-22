import base64


def bin_decode(bin_string):
    normal_str = ""
    for i in range((len(bin_string) // 8)):
        normal_str += chr(int(bin_string[8 * i:8 * (i + 1)], 2))
    return normal_str


input_string = "MDEwMDAwMTAwMTEwMTAwMTAxMTEwMTAwMDEwMDExMDEwMTEwMTExMTAxMTEwMDEwMDExMDAxMDE="
output_string = ""

input_string = base64.b64decode(input_string)

output_string = bin_decode(input_string)
print(output_string)
