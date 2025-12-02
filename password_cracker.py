pos = 50
count = 0
with open('input.txt') as f:
    for line in f:
        d = int(line[1:])
        pos = (pos - d) % 100 if line[0].upper() == 'L' else (pos + d) % 100
        if pos == 0:
            count += 1
print(count)
