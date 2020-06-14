main = []
while True:
    a = input()
    if a == "":
        break
    elif a != "\t\t":
        main.append(a.split("\t"))
with open("dict.txt", "a", encoding="utf-8") as output:
    for gift in main:
        output.write(f'{gift[0]};{gift[2].split(" ")[0]}\n')