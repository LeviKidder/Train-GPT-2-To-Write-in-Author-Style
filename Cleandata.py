import os
import re
with open("merged_books.txt",'r', encoding = "utf8") as f:
    string = f.read()


    def clean_text(string):
        pattern = '(page|PAGE|Page)(\s+\|\s+)([0-9]+)(.*)$'
        output_cleaned = re.sub('\s$', '', string, flags=re.MULTILINE)
        p = re.compile(pattern, re.MULTILINE)
        output_cleaned = p.sub(" ", output_cleaned)
        return output_cleaned


    check = clean_text(string)

    with open("output_cleaned.txt", 'w', encoding = "utf8") as f:
        f.writelines(check)

train_doc =[]
val_doc =[]



with open("output_cleaned.txt",'r', encoding = "utf8") as f:
    file_input=f.readlines()

file_input

count = 0
for cnt, line in enumerate(file_input):
#         print(cnt)
        if cnt <= len(file_input)*0.90:
            train_doc.append(line)
        else:
            val_doc.append(line)


len(train_doc)

## Write to file
f = open('val.txt', "w+",  encoding = "utf8")
count = 0
for line in val_doc:
    count = count + 1
    f.write(str(line))
    f.write("\n")

## Write to file
f = open('train.txt', "w+", encoding = "utf8")
count = 0
for line in train_doc:
    count = count + 1
    f.write(str(line))
    f.write("\n")

f.close()
print(count)

f.close()
print(count)

