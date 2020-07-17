with open("Test Files/menusPortingShop.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
newlist = []
cooldowns = []
for i in range(len(file_contents)):
    if "cooldown=itemization" in file_contents[i]:
        if file_contents[i+1][-1] == '"':
            cooldown_name = file_contents[i + 1].split(":")[1][:-1]
        else:
            cooldown_name = file_contents[i+1].split(":")[1]
        cooldowns.append(f'{cooldown_name}itemization=0') # Increase int as required
        newlist.append(f'            cooldown={cooldown_name}itemization')
    else:
        newlist.append(file_contents[i])
with open("outputnewPortingShop.conf", "a", encoding="utf-8") as output:
    for line in newlist:
        output.write(f'{line}\n')
with open("outputcooldowns.conf", "a", encoding="utf-8") as output:
    for cooldown in cooldowns:
        output.write(f'{cooldown}\n')