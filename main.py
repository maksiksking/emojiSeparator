import re

input_string = " test ♣️ ⚾️ 💛 🌧 🐆 🌒 🐂 🎖 test 🌀 🚞 ⤵️ 🈸 ⛎"

m = re.compile(r'[a-zA-Z0-9()_/., ]*$')
if m.match(input_string):
    print("Uh oh, contains text only")
else:
    blankPrompt = []
    for i in input_string:
        print(i)
        doAppend = True
        if re.search(r'[^a-zA-Z0-9()_/., ]', i):
            print("safe")
        else:
            print("unsafe")
            doAppend = False
        if doAppend:
            blankPrompt.append(i)
    beautifiedPrompt = ''.join(str(p) for p in blankPrompt)
    print(beautifiedPrompt)
