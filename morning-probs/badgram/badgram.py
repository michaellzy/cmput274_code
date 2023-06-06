import sys
word_list = []
letter_list = []
bad_list = []
result_list = []
bad_letter = 'vkjxqz'

for line in sys.stdin:
    # be mindful that line may have a trailing \n character
    if line != "\n":
        word_list.append(line)
        letter_list = list("".join(x for x in word_list).lower())
        for ele in bad_letter:
            while ele in letter_list:
                bad_list.append(ele)
                break
        bad_length = len(bad_list)
        word_list = []
        bad_list = []
        if bad_length > 4:
            result_list.append("BAD"+"\n")
        elif bad_length <= 4:
            result_list.append("OK"+"\n")
    elif line == "\n":
        continue

print("".join(result_list).strip("\n"))





