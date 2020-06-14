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
COOLDOWN = 14400  # 4h
SHOP_NAME = "EventgiftShop"  # Rename to any string with no spaces. Will append index# for >1 page


with open("Test Files/EventRCoinShopGifts.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
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
        newlist.append(thing[:-2])
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
    lores.append("\\n".join(file_contents[indices_lore[i] + 1:indices_lore_2[i]]))
newlores = []
for lore in lores:
    lore = lore.replace('"', '')
    lore = lore.replace("            ", '')
    lore = lore.replace("&", "§")
    newlores.append(lore)
names = []
for name in newlistformal:
    name = name.replace("&", "§")
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
print(newlist[0])
index = 0
shop = []
for i in range((len(newlistformal) // 31)):
    if True:
        shop.append([f'{SHOP_NAME}{i}' + " {"])
        for k in range(31):
            shop[i].append(f'	"{index % 31}"' + " {", )
            shop[i].append("		action {")
            shop[i].append(f"			cooldown={COOLDOWN}")
            print(index)
            shop[i].append(f'			commodity="WRAPPED_GIFT:{newlist[index]}:1"')
            shop[i].append(f'			"cost_sell"="CURRENCY:rcoin:2"')
            shop[i].append(f'			message="&4Enjoy!"')
            shop[i].append('			permission="commands.use"')
            shop[i].append("			type=TRADE")
            shop[i].append("		}")
            shop[i].append("		icon {")
            shop[i].append(f'			{newlistformal[index]}')
            shop[i].append(f'			itemType={newlistitem[index]}')
            shop[i].append('			lores=[')
            shop[i].append(f'				"&bSell: 2 RCoins &7Left-click"')
            shop[i].append('			]')
            shop[i].append('		}')
            shop[i].append('	}')
            index += 1
            print(shop)
        for o in range(5):
            shop[i].append(f'    "{31 + o}"' + "{")
            shop[i].append("        action {")
            shop[i].append('            permission="commands.use"')
            shop[i].append('            reward="COMMAND:."')
            shop[i].append('            type=REWARD')
            shop[i].append('        }')
            shop[i].append('        icon {')
            shop[i].append('            displayName=""')
            shop[i].append('            itemType="STAINED_GLASS_PANE"')
            shop[i].append('			durability=7')
            shop[i].append('            lores=[')
            shop[i].append('                ""')
            shop[i].append('            ]')
            shop[i].append('        }')
            shop[i].append('    }')
        shop[i].append('	"menu_title"="&6Event Shop!"')
        shop[i].append('}')
    else:
        shop.append([f'{SHOP_NAME}{i}' + " {"])
        for k in range(31):
            shop[i].append(f'	"{index % 31}"' + " {", )
            shop[i].append("		action {")
            shop[i].append(f"			cooldown={COOLDOWN}")
            shop[i].append(f'			commodity="WRAPPED_GIFT:{newlist[index]}:1"')
            shop[i].append(f'			"cost_sell"="CURRENCY:rcoin:2"')
            shop[i].append(f'			message="&4Enjoy!"')
            shop[i].append('			permission="commands.use"')
            shop[i].append("			type=TRADE")
            shop[i].append("		}")
            shop[i].append("		icon {")
            shop[i].append(f'			{newlistformal[index]}')
            shop[i].append(f'			itemType={newlistitem[index]}')
            shop[i].append('			lores=[')
            shop[i].append(f'				"&bSell: 2 RCoins &7Left-click"')
            shop[i].append('			]')
            shop[i].append('		}')
            shop[i].append('	}')
            index += 1
        for o in range(5):
            shop[i].append(f'    "{31 + o}"' + "{")
            shop[i].append("        action {")
            shop[i].append('            permission="commands.use"')
            shop[i].append('            reward="COMMAND:."')
            shop[i].append('            type=REWARD')
            shop[i].append('        }')
            shop[i].append('        icon {')
            shop[i].append('            displayName=""')
            shop[i].append('            itemType="STAINED_GLASS_PANE"')
            shop[i].append('			durability=7')
            shop[i].append('            lores=[')
            shop[i].append('                ""')
            shop[i].append('            ]')
            shop[i].append('        }')
            shop[i].append('    }')
        shop[i].append('	"menu_title"="&6Event Shop!"')
        shop[i].append('}')
with open("output.conf", "a", encoding="utf-8") as output:
    for menu in shop:
        for line in menu:
            output.write(f'{line}\n')
# for gift in newlist:
#     print(f'        {gift}' + " {\n"
#           '            "0" {\n'
#           f'                reward="COMMAND:giftplayer %p% {gift}"\n'
#           '            }\n'
#           '        }')