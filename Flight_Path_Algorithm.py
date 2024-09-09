import matplotlib.pyplot as plt

# Function to parse input
def parse_input(input_data):
    flights = []
    for data in input_data:
        flight = [tuple(map(int, coord.split(','))) for coord in data.split()]
        flights.append(flight)
    return flights

# Function to plot flights
def plot_flights(flights):
    for flight in flights:
        x, y = zip(*flight)
        plt.plot(x, y, marker='o')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Flight Paths')
    plt.grid(True)
    plt.show()

# Function to check for intersection
def check_intersection(path1, path2):
    # Simplified check for intersection
    for i in range(len(path1) - 1):
        for j in range(len(path2) - 1):
            if path1[i] == path2[j] or path1[i+1] == path2[j+1]:
                return True
    return False

# Function to adjust paths
def adjust_paths(flights):
    adjusted_flights = []
    for i in range(len(flights)):
        for j in range(i+1, len(flights)):
            if check_intersection(flights[i], flights[j]):
                # Simple adjustment by shifting one of the paths
                flights[j] = [(x+0.1, y+0.1) for x, y in flights[j]]
        adjusted_flights.append(flights[i])
    return adjusted_flights

# Sample Input
input_data = [
    "1,1 2,2 3,3",
    "1,1 2,4 3,2",
    "1,1 4,2 3,4"
]

flights = parse_input(input_data)
adjusted_flights = adjust_paths(flights)
plot_flights(adjusted_flights)
