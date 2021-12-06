
import pprint

pp = pprint.PrettyPrinter(indent=3)

def find_max_pt(max_pt, pt1, pt2):

    compare_pt = pt1
    if pt2 > compare_pt:
        compare_pt = pt2
    
    if compare_pt > max_pt:
        max_pt = compare_pt

    return max_pt

def create_map(max_x, max_y, marker):

    map = []
    for j in range(max_y):
        map.append([])
        for i in range(max_x):
            map[j].append(marker)
    
    return map

def plot_points(map, start_pt, end_pt):
    pp = pprint.PrettyPrinter(indent=3)

    plot_pts = []

    if start_pt[0] == end_pt[0]: # if vertical line
        print(f'Vertical Line: {start_pt}, {end_pt}')
        if start_pt[1] > end_pt[1]:
            temp = start_pt[1]
            start_pt[1] = end_pt[1]
            end_pt[1] = temp

        x_coord = start_pt[0]
        for i in range(start_pt[1], end_pt[1] + 1):
            map[i][x_coord] += 1

    elif start_pt[1] == end_pt[1]: # if horizontal line
        print(f'Horizontal Line: {start_pt}, {end_pt}')
        if start_pt[0] > end_pt[0]:
            temp = start_pt[0]
            start_pt[0] = end_pt[0]
            end_pt[0] = temp
        
        y_coord = start_pt[1]
        for i in range(start_pt[0], end_pt[0] + 1):
            map[y_coord][i] += 1
    else:
        print(f'Not horizontal or vertical lines: {start_pt} {end_pt}')

    return map

f = open('inputs/input.txt')
lines = f.readlines()
f.close()

lines = [line.rstrip('\n') for line in lines]

max_x = 0
max_y = 0

points = []

# find max points to create a map
for line in lines:
    start_point, arrow, end_point = line.split(' ')
    start_x, start_y = start_point.split(',')
    end_x, end_y = end_point.split(',')

    start_x = int(start_x)
    start_y = int(start_y)
    end_x = int(end_x)
    end_y = int(end_y)

    points.append([[start_x, start_y], [end_x, end_y]])

    max_x = find_max_pt(max_x, start_x, end_x)
    max_y = find_max_pt(max_y, start_y, end_y)

print(f'Max X: {max_x}, Max Y: {max_y}')

map = create_map(max_x + 1, max_y + 1, 0)
#pp.pprint(map)

# fill in map
overlap_counter = 0
for pt in points:
    map = plot_points(map, pt[0], pt[1])
    #pp.pprint(map)

for row in map:
    for cell in row:
        if cell > 1:
            overlap_counter += 1

print(f'Number of overlapping points: {overlap_counter}')