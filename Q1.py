text = open("input.txt", "r")

dic = dict()

for line in text:

    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
for key in list(dic.keys()):
    print(key, ":", dic[key],end=",")