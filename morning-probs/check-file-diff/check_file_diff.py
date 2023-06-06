from collections import Counter
label_path = "/Users/zlu6/Downloads/detect_res.txt"

label_reader = open(label_path, "r")
label_datas = label_reader.readlines()
label_image_name = []
for cur_line_data in label_datas:
    cur_line_splits = cur_line_data.strip().split(",")
    cur_image_name = cur_line_splits[0]
    label_image_name.append(cur_image_name)

print(len(label_image_name))

b = dict(Counter(label_image_name))
print({key: value for key, value in b.items() if value > 1})