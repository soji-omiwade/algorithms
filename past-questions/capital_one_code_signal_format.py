'''
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to center"]] and width = 16,
centerNewspaperText(paragraphs, width) = ["******************",
                                          "*  hello world   *",
                                          "*How areYou doing*",
                                          "*  Please look   *",
                                          "*   and align    *",
                                          "*   to center    *",
                                          "******************"]
rem = width = 16                                          
12
5
How areYou doing                                          
#paragraph: "hello world!"
word = world
line = [world]      
res = [hello world]

function buffer_line(line, linewidth)
    rem = width - linewidth
    remleft = remright = rem // 2
    if (width - linewidth) % 2 == 1
        remright += 1
    return remleft + line + remright
     
    
line = []
for paragraph in paragraphs:
    res = []
    rem = width
    for word in paragraph:
        if len(word) <= rem:
            line.append(word)
            rem -= len(word) + 1
        else
            res.append(line)
            buffer_line()
            line = [word]
            rem = width - (len(word) + 1)
    res.append(line)
return res

'''

def buffered_line(line, width):
    spacecount = len(list(1 for word in line)) - 1 # 
    wordareacount = sum(len(word) for word in line)
    linewidth = wordareacount + spacecount
    rem = width - linewidth 
    remleft = remright = rem // 2
    if (width - linewidth) % 2 == 1:
        remright += 1
    return remleft * " " + ' '.join(line) + remright * " "

def centerNewspaperText(paragraphs, width):
    res = []
    res.append((width + 2) * "*")
    for paragraph in paragraphs:
        line = []
        rem = width
        for word in paragraph:
            if len(word) <= rem:
                line.append(word)
                rem -= len(word) + 1
            else:
                res.append("*" + buffered_line(line, width) + "*")
                line = [word]
                rem = width - (len(word) + 1)
        res.append("*" + buffered_line(line, width) + "*")
    res.append((width + 2) * "*")
    return res
    
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to center"]]
width = 16
from pprint import pprint
pprint(centerNewspaperText(paragraphs, width))
'''
centerNewspaperText(paragraphs, width) = ["******************",
                                          "*  hello world   *",
                                          "*How areYou doing*",
                                          "*  Please look   *",
                                          "*   and align    *",
                                          "*   to center    *",
                                          "******************"]
'''