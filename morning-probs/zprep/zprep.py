# Add your code here
import string
str_input = input().split()

alpha_list = []

str_ele = list("".join(x for x in str_input))
for ele in str_ele:
    if ele not in string.digits:
        alpha_list.append(ele)
print(alpha_list)
