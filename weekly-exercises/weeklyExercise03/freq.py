# ————————————————————————————————
#   Name: Zhiyuan Lu
#   ID: 1579058
#   CMPUT 274, Fall 2018
#
#   Weekly Exercise #3: Word Frequency
# --------------------------------

# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!
import sys
import string


def read_whole_file(file_name):
    """ Read the contents of the file, find all the
    words(individual, space-separated) in the text.

    :param
        file_name: an input file which contains texts.
    :return:
        word_text: return a list of words from the texts
    """
    word_text = []
    # open and read the input file, find all the words
    # separated by the whitespace. Append these words
    # in word_text list.
    try:
        file = open(file_name)
        word_lines = file.readlines()
        for word in word_lines:
            word = word.strip(string.whitespace)
            word_text.extend(word.split())
        file.close()
    # If the user enter the wrong
    # file name, a warning message would prompt.
    except IOError as err:
        print("File Error:" + str(err))
        sys.exit(3)
    return word_text


def word_count(words_list):
    """ count number of times each words appear in the
        input file's texts

    :param
        words_list: a list of words from the text

    :return:
        word_dic: return a dictionary which contains each words and
        the number of times each words appears in the text
    """
    # create a dictionary for each words
    # <key>: word in the text
    # <value>: the number of times each words appears in the text
    word_dic = {}
    # find all the words(non-repeated) in words_list.
    for i in set(words_list):
        word_dic[i] = words_list.count(i)
    return word_dic


def draw_freq_table(word_dic):
    """ count each words' relative frequency

    :param
        word_dic: a word dictionary which contains
        <key> :words in the text
        <value>: number of words appears
    :return:
        result_list: return the final result
        in this format:
        word count freq
    """
    word_length = 0
    # sort the word_dic in alphabetical order
    word_dic_sort = sorted(word_dic.items(), key=lambda item: item[0], reverse=False)
    # find total words in the text
    for i in word_dic:
        word_length += word_dic.get(i)

    new_sorted_list = []
    result_list = []
    # find relative frequency of each words, append
    # first element: word
    # second element: number of each words appear in the text
    # third element: relative frequency of each words
    # in new_sorted_list
    for item in word_dic_sort:
        relative_freq = round(item[1] / word_length, 3)
        new_sorted_list.append((item[0], item[1], relative_freq))
    # convert list-tuple type to list
    for word in new_sorted_list:
        word_line = " ".join(str(x) for x in word)
        print(word_line)
        result_list.append(word_line + "\n")
    return result_list


def write_result(file_out_name, result_list):
    """output the result in a new plain-text file

    :param file_out_name: output file's name
    :param result_list: word count result
    """
    with open(file_out_name, "w+") as f:
        f.writelines(result_list)


def main():
    # check the user's command inputs
    # show a warning message if the user does not input filename or
    # enter more command-line arguments
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) < 2:
        print("There are too few command-line arguments, please input \n**python3 freq.py <input_file_name>**")
        sys.exit(1)
    else:
        print("There are too many command-line arguments, please input \n**python3 freq.py <input_file_name>**")
        sys.exit(2)
    word_dictionary = word_count(read_whole_file(file_name))
    draw_result = draw_freq_table(word_dictionary)
    file_out = file_name + ".out"
    write_result(file_out, draw_result)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    # file_open = read_whole_file("sample1")
    # print(file_open)
    main()
