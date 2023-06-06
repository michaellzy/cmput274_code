# Read in the input
word_num = int(input())
# Construct a dictionary mapping binary strings to English words
dic_list = {}
for i in range(word_num):
    input_code_list = input().split()
    dic_list[input_code_list[0]] = input_code_list[1]

decode_str = input()
decode = ""
k = 0
while k < len(decode_str):
    decode += decode_str[k]
    k += 1
    if decode in dic_list:
        # Use the dictionary to decode the binary string
        print(dic_list[decode], end=' ')
        decode = ""

