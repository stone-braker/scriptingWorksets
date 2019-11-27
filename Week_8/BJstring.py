
def countString(xstr):
    counter = 0
    for char in xstr:
        counter += 1
    return counter


strizing = 'hello i am a string'

num = countString(strizing)
# print(num)


def stripWhite(xstr):
    xstr = ''.join(xstr.split())
    return xstr


print(stripWhite(strizing))
# print(strizing.split())
print(strizing.split())

spcless = ''.join(strizing.split())
listSpc = list(spcless)
print(listSpc)
