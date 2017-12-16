def decode(string):
    string_decoded = ''
    temp_num_string = ''

    for char in string:
        if char.isnumeric():
            temp_num_string += char
        elif temp_num_string:
            string_decoded += char * int(temp_num_string)
            temp_num_string = ''
        else:
            string_decoded += char

    return string_decoded


def encode(string):
    string_length = len(string)

    if string_length == 0:
        return string

    string_encoded = ''
    count = 0

    for i in range(1, string_length):
        if string[i] == string[i - 1]:
            count += 1
        elif not count:
            string_encoded += string[i - 1]
        else:
            string_encoded += str(count + 1) + string[i - 1]
            count = 0

    if not count:
        string_encoded += string[-1]
    else:
        string_encoded += str(count + 1) + string[-1]

    return string_encoded