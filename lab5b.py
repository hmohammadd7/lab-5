#!/usr/bin/env python3
# Author ID: hmohammad7


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string

    file = open(file_name, 'r')
    content = file.read()
    file.close()

    return content


def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters

    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    new_lines = []

    for line in lines:
        new_lines.append(line.strip())

    return new_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))



def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file

    file = open(file_name, 'a')
    file.write(string_of_lines)
    file.close()


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line

    file = open(file_name, 'w')

    for line in list_of_lines:
        file.write(line + '\n')

    file.close()


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

    file_read = open(file_name_read, 'r')
    file_write = open(file_name_write, 'w')
    line_number = 1

    for line in file_read:
        file_write.write(str(line_number) + ':' + line)
        line_number += 1

    file_read.close()
    file_write.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
