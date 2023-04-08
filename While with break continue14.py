# Example using break with a while loop
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
# Example using continue with a while loop
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
# Example using pass with a while loop
i = 0
while i < 10:
    if i == 5:
        pass
    print(i)
    i += 1
