def encode_string(input_string):
    if len(input_string) < 1:
        return input_string
    result = ""
    counter = 1
    for i in range(1, len(input_string)):
        if input_string[i-1] == input_string[i]:
            counter += 1
        else:
            result += f"{counter}{input_string[i-1]}"
            counter = 1
    result += f"{counter}{input_string[-1]}"
    return result


if __name__ == '__main__':
    assert encode_string('aaabbbccc') == '3a3b3c'
    assert encode_string('bcbcbcb') == '1b1c1b1c1b1c1b'
    assert encode_string('a') == '1a'
    assert encode_string('') == ''
    print('All tests has passed!')
