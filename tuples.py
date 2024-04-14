names = ("Nancy", "Mary", "Susan", "Martha", "Sharon")
print(names[3])
print(names[1:3])

newNames = list(names)
print(newNames)

newNames.append("Margaret")
print(newNames)

newNames.extend(["Yvonne","Marion"])
print(newNames)

newNames.remove("Yvonne")
print(newNames)

newNames.reverse()
print(newNames)

newNames.pop()
print(newNames)

newNames.sort()
print(newNames)

print(len(newNames))

newNames.insert(3, "Dorothy")
print(newNames)