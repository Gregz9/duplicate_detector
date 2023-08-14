f = open("random1.txt", "r")
file_content = f.read()

sentences = file_content.split(". ")

for sentence in sentences:
    # print(sentence, "\n")
    sentence

with open("random_data1.txt", "r") as f:
    print(f.read())
