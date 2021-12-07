#     --- Day 5: Hydrothermal Venture ---
#     https://adventofcode.com/2021/day/5

# Read input from file as "data = [[(x1, y1), (x2, y2)], etc...]"
with open("input5.txt", 'r') as file:
    data = [[tuple(int(value) for value in tuple(coord_pair.strip().split(','))) for coord_pair in line.strip().split('->')] for line in file]

example = [
    [(0, 9), (5, 9)],
    [(8, 0), (0, 8)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(6, 4), (2, 0)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
    [(0, 0), (8, 8)],
    [(5, 5), (8, 2)],
]

class Vent:  
    def __init__(self, start_coord, end_coord):
        self.start_coord = start_coord
        self.end_coord = end_coord
        self.locations = []

    def __str__(self) -> str:
        return f'Start: {self.start_coord}  End: {self.end_coord}'

    def get_locations(self) -> list:
        return self.locations

    def get_x_large(self) -> int:
        return max(self.start_coord[0], self.end_coord[0])
    
    def get_y_large(self) -> int:
        return max(self.start_coord[1], self.end_coord[1])

    def connect_vents(self):
        x1 = self.start_coord[0]
        y1 = self.start_coord[1]
        x2 = self.end_coord[0]
        y2 = self.end_coord[1]        
        x_diff = abs(x2 - x1)
        y_diff = abs(y2 - y1)
        
        if x_diff == 0 or y_diff == 0:
            if x1 == x2:              
                self.locations = [(x1, min(y1, y2) + idx) for idx in range(y_diff+1)]
            elif y1 == y2:
                self.locations = [(min(x1, x2) + idx, y1) for idx in range(x_diff+1)]
        # For part 2
        else:
            if (x1 < x2):
                if (y1 < y2):
                    self.locations = [((x1+idx),(y1+idx)) for idx in range(x_diff+1)]
                elif (y2 < y1):
                    self.locations = [((x1+idx),(y1-idx)) for idx in range(x_diff+1)]
            elif (x2 < x1):
                if (y1 < y2):
                    self.locations = [((x1-idx),(y1+idx)) for idx in range(x_diff+1)]
                elif (y2 < y1):
                    self.locations = [((x1-idx),(y1-idx)) for idx in range(x_diff+1)]
# Setup
def part_one(data):  
    # Create the list of vertical and horizontal vents
    vents = [Vent(line[0], line[1]) for line in data]
    for vent in vents:
        vent.connect_vents()

    # Create the diagram of the ocean vents
    grid_size = get_grid_size(vents)
    rows = grid_size[0] + 1
    cols = grid_size[1] + 1
    diagram = [[0 for _ in range(cols)] for _ in range(rows)]
    danger_zones = 0  

    for vent in vents:
        if len(vent.get_locations()) > 0:
            for coord in vent.get_locations():
                update_diagram(coord, diagram)
                
    for row in diagram:
        for cell in row:
            if cell > 1:
                danger_zones += 1
    return danger_zones

def display_map(diagram):
    for row in diagram:
        print(row)
    print("\n")

def update_diagram(coord, diagram):
    diagram[coord[0]][coord[1]] += 1
    
def get_grid_size(vents) -> list:  
    x_values = [vent.get_x_large() for vent in vents]
    y_values = [vent.get_y_large() for vent in vents]
    return [max(x_values), max(y_values)]


print(f"Part 2: {part_one(data)}")