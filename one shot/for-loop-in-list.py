mark = [95, 98, 97, "math", "eng"]
for score in mark:
    print(score)
mark.append(99)
print(mark)
mark.insert(0, 99)
print(mark)
print(99 in mark)
print(93 in mark)
print(len(mark))
i = 0
while i < len(mark):
    print(mark[i])
    i = i + 1
mark.clear()
print(mark)
