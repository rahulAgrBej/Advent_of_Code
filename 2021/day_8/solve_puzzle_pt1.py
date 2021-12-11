
f = open('inputs/input.txt')
lines = f.readlines()
f.close()

# separate signals from outputs
num_easy_digits = 0
for line in lines:
    signals, outputs = line.rstrip('\n').split(' | ')
    signals = signals.split(' ')
    outputs = outputs.split(' ')

    for output in outputs:
        if (len(output) == 2) or (len(output) == 4) or (len(output) == 3) or (len(output) == 7):
            num_easy_digits += 1

print(f'Number of Easy Digits: {num_easy_digits}')