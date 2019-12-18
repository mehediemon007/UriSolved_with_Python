text = input()

textTolist = list(text)

print(id(text))


for i in range(len(textTolist)):
    if ord(textTolist[i]) >=65 and ord(textTolist[i]) <=90:
          if ord(textTolist[i])-13 <65:
              textTolist[i] = chr(91+(ord(textTolist[i])-65)-13)

          else:
              textTolist[i] = chr(ord(textTolist[i])-13)

    elif ord(textTolist[i]) >=97 and ord(textTolist[i]) <=122:
          if ord(textTolist[i]) - 13 < 97:
             textTolist[i] = chr(123-13+(ord(textTolist[i])-97))

          else:
             textTolist[i] = chr(ord(textTolist[i]) - 13)

    else:
         textTolist[i] = textTolist[i]


text = "".join(textTolist)
print(id(text))
print(text)