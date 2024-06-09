# # Part 1 - Coding Exercise: Decoding a Message from a Text File
# In this exercise, you will develop a function named decode(message_file). The message_file argument is a string containing the file path for a .txt file that has an encoded message. When the function is called, it should read the file specified by its argument, decode the message, and return (not print) the decoded message as a string in a specific format, described below.

# Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

# Your function must be able to process an input file with the following format:

# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 i
# 5 you
# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:

#   1
#  2 3
# 4 5 6
# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). The decoded message is formed by taking these words and separating them by individual spaces, with no extra characters. You should ignore all the other words. So for the example input file above, the message words are:

# 1: i
# 3: love
# 6: computers
# and your function would return the string "i love computers".

def decodeMessage(message_file):
    """
    Function to decode a hidden message and return the message as a string
    """
    # The file will have a number followed by a word and the number will correspond to the key in a dictionary and the message will be the value to allow for constant time reading of the answer;
    # The format for the pyramid is to "place" the numbers in a pyramid structure starting from the smallest number and adding 1 to each row of the pyramid until it is complete, then the last number of each row will be necessary keys

    # open file and assign data to variable, message_file is the file path
    data = open(message_file)
    data_list = [d.strip().split(' ') for d in data.readlines()]
    data_dict = {}
    for tuple in data_list:
        if tuple[0] not in data_dict:
            data_dict[tuple[0]] = tuple[1]
        else:
            data_dict[tuple[0]].append(tuple[1])
    





print(decodeMessage('./coding_qual_input.txt'))