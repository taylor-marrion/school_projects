# StatesDataApp.py
# Author: Taylor Marrion
# Date: 2/2/2020
"""This application displays U.S. states data until the user quits."""

# create a dictionary of state data
# each dictionary key is a state, its value is a list of capital, bird, and flower
# state names stored in all lowercase for string comparison
states_data = {
    "alabama": ["Capital: Montgomery", "State Bird: Yellowhammer", "State Flower: Camellia"],
    "alaska": ["Capital: Juneau", "State Bird: Willow Ptarmigan", "State Flower: Forget Me Not"],
    "arizona": ["Capital: Phoenix", "State Bird: Cactus Wren", "State Flower: Saguaro Cactus Blossom"],
    "arkansas": ["Capital: Little Rock", "State Bird: Mockingbird", "State Flower: Apple Blossom"],
    "california": ["Capital: Sacramento", "State Bird: California Valley Quail", "State Flower: California Poppy"],
    "colorado": ["Capital: Denver", "State Bird: Lark Bunting", "State Flower: White and Lavender Columbine"],
    "connecticut": ["Capital: Hartford", "State Bird: Robin", "State Flower: Mountain Laurel"],
    "delaware": ["Capital: Dover", "State Bird: Blue Hen", "State Flower: Peach Blossom"],
    "florida": ["Capital: Tallahassee", "State Bird: Mockingbird", "State Flower: Orange Blossom"],
    "georgia": ["Capital: Atlanta", "State Bird: Brown Thrasher", "State Flower: Cherokee Rose"],
    "hawaii": ["Capital: Honolulu", "State Bird: Nene", "State Flower: Hibiscus"],
    "idaho": ["Capital: Boise", "State Bird: Mountain Bluebird", "State Flower: Syringa"],
    "illinois": ["Capital: Springfield", "State Bird: Cardinal", "State Flower: Purple Violet"],
    "indiana": ["Capital: Indianapolis", "State Bird: Cardinal", "State Flower: Peony"],
    "iowa": ["Capital: Des Moines", "State Bird: Eastern Goldfinch", "State Flower: Wild Prairie Rose"],
    "kansas": ["Capital: Topeka", "State Bird: Western Meadowlark", "State Flower: Sunflower"],
    "kentucky": ["Capital: Frankfort", "State Bird: Cardinal", "State Flower: Goldenrod"],
    "louisiana": ["Capital: Baton Rouge", "State Bird: Eastern Brown Pelican", "State Flower: Magnolia"],
    "maine": ["Capital: Augusta", "State Bird: Chickadee", "State Flower: White Pine Cone and Tassel"],
    "maryland": ["Capital: Annapolis", "State Bird: Baltimore Oriole", "State Flower: Black-Eyed Susan"],
    "massachusetts": ["Capital: Boston", "State Bird: Chickadee", "State Flower: Mayflower"],
    "michigan": ["Capital: Lansing", "State Bird: Robin", "State Flower: Apple Blossom"],
    "minnesota": ["Capital: Saint Paul", "State Bird: Common Loon", "State Flower: Pink and White Lady Slipper"],
    "mississippi": ["Capital: Jackson", "State Bird: Mockingbird", "State Flower: Magnolia"],
    "missouri": ["Capital: Jefferson City", "State Bird: Bluebird", "State Flower: White Hawthorn Blossom"],
    "montana": ["Capital: Helena", "State Bird: Western Meadowlark", "State Flower: Bitterroot"],
    "nebraska": ["Capital: Lincoln", "State Bird: Western Meadowlark", "State Flower: Goldenrod"],
    "nevada": ["Capital: Carson City", "State Bird: Mountain Bluebird", "State Flower: Sagebrush"],
    "new hampshire": ["Capital: Concord", "State Bird: Purple Finch", "State Flower: Purple Lilac"],
    "new jersey": ["Capital: Trenton", "State Bird: Eastern Goldfinch", "State Flower: Violet"],
    "new mexico": ["Capital: Santa Fe", "State Bird: Roadrunner", "State Flower: Yucca Flower"],
    "new york": ["Capital: Albany", "State Bird: Bluebird", "State Flower: Rose"],
    "north carolina": ["Capital: Raleigh", "State Bird: Cardinal", "State Flower: Dogwood"],
    "north dakota": ["Capital: Bismarck", "State Bird: Western Meadowlark", "State Flower: Wild Prairie Rose"],
    "ohio": ["Capital: Columbus", "State Bird: Cardinal", "State Flower: Scarlet Carnation"],
    "oklahoma": ["Capital: Oklahoma City", "State Bird: Scissor-Tailed Flycatcher", "State Flower: Mistletoe"],
    "oregon": ["Capital: Salem", "State Bird: Western Meadowlark", "State Flower: Oregon Grape"],
    "pennsylvania": ["Capital: Harrisburg", "State Bird: Ruffed Grouse", "State Flower: Mountain Laurel"],
    "rhode island": ["Capital: Providence", "State Bird: Rhode Island Red", "State Flower: Violet"],
    "south carolina": ["Capital: Columbia", "State Bird: Great Carolina Wren", "State Flower: Yellow Jessamine"],
    "south dakota": ["Capital: Pierre", "State Bird: Ring-Necked Pheasant", "State Flower: Pasque Flower"],
    "tennessee": ["Capital: Nashville", "State Bird: Mockingbird", "State Flower: Iris"],
    "texas": ["Capital: Austin", "State Bird: Mockingbird", "State Flower: Bluebonnet"],
    "utah": ["Capital: Salt Lake City", "State Bird: California Seagull", "State Flower: Sego Lily"],
    "vermont": ["Capital: Montpelier", "State Bird: Hermit Thrush", "State Flower: Red Clover"],
    "virginia": ["Capital: Richmond", "State Bird: Cardinal", "State Flower: Dogwood"],
    "washington": ["Capital: Olympia", "State Bird: Willow Goldfinch", "State Flower: Pink Rhododendron"],
    "west virginia": ["Capital: Charleston", "State Bird: Cardinal", "State Flower: Rhododendron"],
    "wisconsin": ["Capital: Madison", "State Bird: Robin", "State Flower: Wood Violet"],
    "wyoming": ["Capital: Cheyenne", "State Bird: Western Meadowlark", "State Flower: Indian Paintbrush"],
    }
# end states_data dictionary

def get_selection():
    """prompts user for selection or to quit"""
    while True: # int type input validation
        try:
            print ('Select from the following menu:')
            print ('1. Display all U.S. States in Alphabetical order along with Capital, State Bird, and State Flower')
            print ('2. Search for a specific state and display the appropriate Capital, Bird, and Flower')
            print ('3. Update a Bird for a specific state')
            print ('4. Exit the Application')
            selection = int(input('Enter your selection: '))
            return (selection)
        except ValueError:
            print (' Invalid option! Please enter an Integer between 1-4!')
# end get_selection

def display_all_states():
    """Displays all U.S. states in Alphabetical order along with Capital, State Bird, and State Flower."""
    for state, data in states_data.items():
        print (f'{state.title()}:  {data}')
# end display_all_states

def find_state(state):
    """Search for a specific state and display the appropriate Capital, Bird, and Flower."""
    if (state in states_data):
        print (f'%s: %s' % (state.title(), states_data[state]))
    else:
        print ('Invalid state! Check your spelling.')
# end find_state

def update_bird(state):
    """Update a Bird for a specific state."""
    if (state in states_data):
        new_bird = input((f"Enter %s's new State Bird:") % state.title())
        states_data[state][1] = (f'State Bird: %s' % new_bird)
        print (f'New entry for %s follows:' % state.title())
        print (f'%s: %s' % (state.title(), states_data[state]))
    else:
        print ('Invalid state! Check your spelling.')
# end update_bird

def generate_output(selection):
    """Generates output based on user selection."""
    if selection == 1:
        display_all_states()
    elif selection == 2:
        state = input('Please enter a state: ')
        print ('Your choice: ' + state)
        find_state(state.lower())
    elif selection == 3:
        state = input('Please enter a state: ')
        print ('Your choice: ' + state)
        update_bird(state.lower())
    else: # range check input validation
        print (' Invalid option! Please enter an Integer between 1-3!')
    # end if-elif-else block
# end generate_output

# start main body of code
# print welcome message
print ('**** Welcome to the States data application! ****')

# prompt user for selection with sentinel-controlled iteration
selection = get_selection()
exit_int = 4
while selection != exit_int:
    generate_output(selection)
    selection = get_selection()
# end while loop
print ('You selected %d to quit.' % exit_int)

# print goodbye message
print ('Thanks for trying the States data Application!')
print ('*********************************************************')