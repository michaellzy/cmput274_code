import sys

# this will read in every line until the end of file
# caution: the newline at the end of a line is not automatically stripped!
char_list = []
convert_char = []
str_ele = ""
new_str = ""
count = 0
try:
    for line in sys.stdin:
        if line == "\n":
            convert_char.append("\n")
            continue

        else:
            for char in line:
                char_list.append(char)

            str_ele = "".join(char_list)
        char_list = []
        new_str = str_ele.replace("X", "1").replace(".", "0")
        convert_char.append(chr(int(new_str, 2)))
except:
    pass
if convert_char[len(convert_char) - 1] == "\n":
    convert_char.pop()
print("".join(convert_char).strip("\n"))
