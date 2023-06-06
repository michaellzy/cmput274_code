words = input().split()
count_num = 0
count_dic = {}
result_list = []
# words is now a list of all strings in the input
# finish the problem!
for word in words:
    count_dic[word] = words.count(word)
count_list = count_dic.values()
max_value = max(count_list)

for key in count_dic.keys():
    if count_dic[key] == max_value:
        result_list.append(key)
    result_list.sort()

# print(count_list)
print("\n".join(result_list))
