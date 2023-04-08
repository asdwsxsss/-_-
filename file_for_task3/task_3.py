import os
file_path1 = r'C:\Users\User\Desktop\файлы_дз\file_for_task3\1.txt'
file_path2 = r'C:\Users\User\Desktop\файлы_дз\file_for_task3\2.txt'
file_path3 = r'C:\Users\User\Desktop\файлы_дз\file_for_task3\3.txt'
with open("2.txt", "r", encoding="utf-8") as input:
    with open("4.txt", "w", encoding="utf-8") as output:
        output.writelines(os.path.basename(file_path2) + '\n')
        text = input.read()
        count = text.count('\n') + 1
        output.writelines(str(count) + '\n')
        for line in text.split('\n'):
            output.writelines(line)

with open("1.txt", "r", encoding="utf-8") as input:
    with open("4.txt", "a", encoding="utf-8") as output:
        output.writelines(os.path.basename(file_path1) + '\n')
        text = input.read()
        count = text.count('\n') + 1
        output.writelines(str(count) + '\n')
        for line in text.split('\n'):
            output.writelines(line+'\n')


with open("3.txt", "r", encoding="utf-8") as input:
    with open("4.txt", "a", encoding="utf-8") as output:
        output.writelines(os.path.basename(file_path3) + '\n')
        text = input.read()
        count = text.count('\n')+1
        output.writelines(str(count) + '\n')
        for line in text.split('\n'):
            output.writelines(line+'\n')





