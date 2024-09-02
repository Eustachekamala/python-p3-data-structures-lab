spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #returns a list of strings with the names of each spicy food.
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    #returns a list of dictionaries where the heat level of the food is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        ''' A string of chili peppers based on the heat level '''
        peppers = "🌶" * heat_level
        
        ''' Format the output string '''
        output = f"{name} ({cuisine}) | Heat Level: {peppers}"
        
        print(output)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    '''Returns a dictionary of the spicy food whose cuisine matches the given cuisine.'''
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower(): return food
    return None # Return None if no food is found
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            
            ''' A string of chili peppers based on the heat level '''
            peppers = "🌶" * heat_level
            
            ''' Format the output string '''
            output = f"{name} ({cuisine}) | Heat Level: {peppers}"
            
            print(output)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        # Handle the case where the list is empty
        return 0
    
    # Calculate the total heat level
    total_heat = sum([food["heat_level"] for food in spicy_foods])
    
    # Calculate the number of elements in the list
    num_foods = len(spicy_foods)
    
    # Compute the average heat level
    average_heat_level = total_heat // num_foods
    
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    
    # Create a new dictionary for the spicy food
    new_food = {
        "name": spicy_food["name"],
        "cuisine": spicy_food["cuisine"],
        "heat_level": spicy_food["heat_level"],
    }
    
    # Add the new food to the list of spicy foods
    spicy_foods.append(new_food)
    
    return spicy_foods
