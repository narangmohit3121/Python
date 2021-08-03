# with open('JabberWocky.txt', 'r') as jabber:
#     for line in jabber:
#         print(line, end='')

# jabber = open('JabberWocky.txt')

# for line in jabber:
#     print(line,end='')
#
# jabber.close()

with open('JabberWocky.txt') as jabber:
    lines = jabber.readlines()
    for line in lines:
        if line.upper().find("JABBER") != -1:
            print(line)
