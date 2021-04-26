# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


fun = []
M = 22


def get_file(name):
    f = open(name, 'r')
    content = f.read()
    f.close()
    return content


def is_correct_init_state(st):
    if len(st) != 23:
        return False

    return all(((ch == '0') or (ch == '1')) for ch in st)


def find_xor_sum(s):
    bits_array = [int(c, base=2) for c in s]
    xor_sum = (bits_array[0] * fun[0]) ^ (bits_array[1] * fun[1])
    for i in range(2, len(s)):
        xor_sum ^= bits_array[i] * fun[i]

    return xor_sum


def shift(s):
    b_extra = find_xor_sum(s)
    s = s[1:] + s[:1]
    s_list = list(s)
    s_list[22] = str(b_extra)
    return "".join(s_list)


def create_key(init_st, count):
    s = init_st
    str_key = ""
    while len(str_key) != count:
        str_key += s[0]
        s = shift(s)

    return str_key


def count_bits(msg):
    count = 0
    for c in msg:
        number = ord(c)
        count += len(bin(number)[2:])

    return len(msg) * 8


def encode(msg, k):
    enc_msg = ""
    for i in range(len(msg)):
        val = ord(msg[i]) ^ int(k[i * 8: i * 8 + 8], base=2)
        enc_msg += chr(val)
        print(val)

    return enc_msg


# MAIN
# x^23 + x^5 + 1
fun = [0] * (M + 1)
fun[22] = 1
fun[4] = 1
fun[0] = 1

file_name = input("Enter the file name: ")
init_state = input("Enter the register initial state(length must be 23): ")
while not is_correct_init_state(init_state):
    init_state = input("Enter the register initial state(length must be 23): ")

message = get_file(file_name)
key = create_key(init_state, count_bits(message))
print(key)
encoded_message = encode(message, key)
print(encoded_message)