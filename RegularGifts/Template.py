for i in range(45):
    print(f'    "{i}"' + '{')
    print('        action {')
    print('            close=false')
    print('            permission="commands.use"')
    print('            reward="COMMAND:."\n'
          '            type=REWARD\n'
          '        }\n'
          '        icon {\n'
          '            displayName=""\n'
          '            itemType="STAINED_GLASS_PANE"\n'
          '            durability=0\n'
          '            lores=[\n'
          '                ""\n'
          '            ]\n'
          '        }\n'
          '    }')