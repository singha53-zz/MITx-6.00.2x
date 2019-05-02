###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if len(cows) == 0:
        return []
    tmpcows = cows.copy()
    weights = sorted(tmpcows.items(), key=lambda x: x[1] , reverse=True)
    trips = []
    while sum(tmpcows.values()) > 0:
        total = 0
        trip = []
        for cow, weight in weights:
            if tmpcows[cow] != 0 and weight + total <= limit:
                trip.append(cow)
                total += weight
                tmpcows[cow] = 0
        trips.append(trip)
    return trips
        
cows = {'Louis': 45, 'Milkshake': 75, 'Clover': 5, 'Lotus': 10, 'MooMoo': 85, 'Muscles': 65, 'Patches': 60, 'Polaris': 20, 'Miss Bella': 15, 'Horns': 50}
limit = 100
greedy_cow_transport(cows,limit)

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    allPartitions = sorted(get_partitions(cows), key = len)
    # Note that this returns a list of names (strings), and we will need to do
    # dictionary lookup later
    # Now time to filter the power list:
    result = []
    for i in allPartitions:
        trip = []
        for j in i:
            weights = []
            for k in j:
                weights.append(cows[k])
            trip.append(sum(weights))
        if all(d <= limit for d in trip):
            result.append(i)
    rm_result = []
    for k in result:
        if k not in rm_result:
            rm_result.append(k)
    # now find the minimum list length:
    min_list_len = min(map(len, rm_result))
    for l in rm_result:
        if len(l) == min_list_len:
            return l

cows = {'Miss Bella': 25, 'Horns': 25, 'Lotus': 40, 'MooMoo': 50, 'Milkshake': 40, 'Boo': 20}
limit = 100
brute_force_cow_transport(cows,limit)
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


