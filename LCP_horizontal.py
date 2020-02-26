#horizontal greedy approach
#this works
#LCP(string)= LCP(LCP(string1, string2), string3)

def LCP(str):
    new = ""
    prefix = str[0]
    print(prefix)
    for x in str:
        new = find(prefix, x)
        if new == "":
            print ("No LCP")
            quit()
        prefix = new
    return prefix


def find(str1, str2):
    newstring = ""
    for i, j in zip(str1, str2):
        if i is j:
            newstring = newstring + i
        else:
            break
    return newstring

words = ["flower", "flow", "flight"]
lcp = LCP(words)
if (len(lcp)):
    print("Longest common prefix:" , lcp)
else:
    print("No LCP")
