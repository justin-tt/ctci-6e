# https://stackoverflow.com/questions/9141830/explain-the-use-of-a-bit-vector-for-determining-if-all-characters-are-unique

def has_unique_chars(string): 
    ''' 
    assuming only lower case a-z are in strings.
    a - z flags are stored via bit positions,
    where the position is the dictionary key
    '''
    bit_dictionary = bin(0)
    for c in string:
        bit_key = get_bit_key(c)
        if is_in_bit_dictionary(bit_dictionary, bit_key):
            return False
        bit_dictionary = update_bit_dictionary(bit_dictionary, bit_key)
    return True

def get_bit_key(char):
    return bin(1 << (ord(char) - 97))

def update_bit_dictionary(bit_dictionary, bit_char):
    return bin(int(bit_dictionary,2) | int(bit_char,2))

def is_in_bit_dictionary(bit_dictionary, bit_char):
    if (int(bit_dictionary,2) & int(bit_char,2) > 0):
        return True
    else:
        return False

assert(get_bit_key("a") == bin(1 << 0))
assert(get_bit_key("z") == bin(1 << 25))

test_bit_dictionary = bin(0)
test_bit_char = get_bit_key("a")
test_bit_dictionary = update_bit_dictionary(test_bit_dictionary, test_bit_char)
assert(test_bit_dictionary == bin(1))
test_bit_char2 = get_bit_key("z")
test_bit_dictionary = update_bit_dictionary(test_bit_dictionary, test_bit_char2)
assert(test_bit_dictionary == bin(1 << 0 | 1 << 25))

test_bit_dictionary = bin(0)
test_bit_char = get_bit_key("a")
test_bit_char2 = get_bit_key("z")
test_bit_dictionary = update_bit_dictionary(test_bit_dictionary, test_bit_char)
assert(is_in_bit_dictionary(test_bit_dictionary, test_bit_char) == True)
assert(is_in_bit_dictionary(test_bit_dictionary, test_bit_char2) == False)
test_bit_dictionary = update_bit_dictionary(test_bit_dictionary, test_bit_char2)
assert(is_in_bit_dictionary(test_bit_dictionary, test_bit_char2) == True)

assert(has_unique_chars("abcdz") == True)
assert(has_unique_chars("abcda") == False)

