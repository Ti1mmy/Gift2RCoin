"""
Gift Itemization Script
    * Supports 31 gifts per page; will create new pages if N gifts > 31
---
INFO:
    - File structure:
        - Main
            - Test Files
                - EventGifts.conf // Gift file (No IMMs)
            - itemization.py
            - output.conf  // Will be created automatically, no need to create file
    - Change `cooldown` and `shop_name` variables as needed
NB: __MANUALLY ADD INDEX 42 and 43 TO END OF EACH MENU REGARDING MENU NAVIGATION

BUGS:
    - Make sure to double-check gifts for any item with multiple variations per item ID (stained glass, clay, etc)
    - Gift Names with "&" as a part of their name (ie: Sweet&Sour Porkchop) may get messed up
"""
# stacks --> {giftname}stacks
COOLDOWN = 0  # 4h
SHOP_NAME = "regulargiftshop"  # Rename to any string with no spaces. Will append index# for >1 page

dict = {}
toconvert = []
with open("Test Files/inputgifts.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
with open("dict.txt", "r") as File2:
    lines = File2.read().split("\n")
for line in lines:
    elem = line.split(";")
    dict[elem[0].lower()] = float(elem[1])
    toconvert.append(elem[0].lower())
newlist = []
newlistformal = []
newlistitem = []
for thing in file_contents:
    if "displayName=" in thing:
        newlistformal.append(thing.strip())
    elif "itemType=" in thing:
        newlistitem.append(thing.split("=")[1])
    elif thing.startswith(" ") or thing == "}" or thing.startswith("#"):
        pass
    else:
        newlist.append(thing[:-2].lower())
file_contents_new = []
# for i in range(len(file_contents)):
#     if '"' in file_contents[i]:
#         file_contents_new.append(file_contents[i].split('"')[1])
indices_lore = [i for i, x in enumerate(file_contents) if "lores=[" in x]
indices_lore_2 = [i for i, x in enumerate(file_contents) if x.startswith("        ]")]
# print(indices_lore)
# print(indices_lore_2)
# for thing in file_contents:
#     if "lores=[" in thing:
#         pass
lores = []
for i in range(len(indices_lore)):
    lores.append("\n".join(file_contents[indices_lore[i] + 1:indices_lore_2[i]]))
newlores = []
for lore in lores:
    newlores.append(lore)
names = []
for name in newlistformal:
    name = name.replace('"', "")
    names.append(name.split('=')[1])
message = []
for name in newlistformal:
    name = name.replace('"', "")
    message.append(name.split('=')[1])
# for i in range(len(newlist)):
#     print(newlistformal[i][13:-1], newlist[i])
# lores_new = []
# for lore in lores:
#     lores_new.append(lore.strip('"'))
# print(lores_new)
"""
Output code
"""
# main = []
# while True:
#     a = input()
#     if a == "":
#         break
#     elif a != "\t\t":
#         main.append(a.split("\t"))
index = 0
shop = []
main = []
while True:
    a = input()
    if a == "":
        break
    elif a != "\t\t":
        main.append(a.split("\t"))
inputs = []
for thing in main:
    inputs.append(thing[0].lower())
index = 10
if True:
    for gift in inputs:
        shop.append(f'    "{index}"' + ' {')
        shop.append('        action {')
        shop.append('            permission="commands.use"')
        shop.append('            reward {')
        shop.append('                asplayer=true')
        shop.append('                commands=[')
        shop.append(f'                    {gift}stacks')
        shop.append('                ]')
        shop.append('                type=COMMAND')
        shop.append('            }')
        shop.append('            type=REWARD')
        shop.append('        }')
        shop.append('        icon {')
        shop.append(f'            {newlistformal[newlist.index(gift)]}')
        shop.append(f'            itemType={newlistitem[newlist.index(gift)]}')
        shop.append('            lores=[')
        shopname = newlistformal[newlist.index(gift)].split('"')[1]
        shop.append(f'            "&bOpens {shopname} Menu"')
        shop.append('            ]')
        shop.append('        }')
        shop.append('    }')
        if index == 16:
            index += 3
        elif index == 25:
            index += 3
        elif index == 34:
            index += 3
        else:
            index += 1
with open("output.conf", "a", encoding="utf-8") as output:
    for menu in shop:
        output.write(f'{menu}\n')
# for gift in newlist:
#     print(f'        {gift}' + " {\n"
#           '            "0" {\n'
#           f'                reward="COMMAND:giftplayer %p% {gift}"\n'
#           '            }\n'
#           '        }')