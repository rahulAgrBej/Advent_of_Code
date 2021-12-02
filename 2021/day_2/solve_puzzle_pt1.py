
f = open('inputs/input.txt', 'r')
commands = f.readlines()
f.close()

commands = [line.rstrip('\n') for line in commands]

final_depth = 0
final_horizontal = 0

for command in commands:
    direction, scale = command.split(' ')
    scale = int(scale)

    if direction == 'forward':
        final_horizontal += scale
    elif direction == 'down':
        final_depth += scale
    elif direction == 'up':
        final_depth -= scale

direction_product = final_horizontal * final_depth
print(f'horizontal * depth = {direction_product}')
