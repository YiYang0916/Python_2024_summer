i = 0
while i < 6:
  print(i)
  i += 2
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

for x in range(20):
  print(x) 

for x in range(2, 30, 3):
  print(x) 
