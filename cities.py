from search import romania_map

#initialize origin and destination to empty strings
#defined globally for utilization elsewhere
origin = ""
destination = ""

#function used to get city input 
def get_city_input(prompt):
    global origin, destination

    city = input(prompt).capitalize()
    while city not in romania_map.locations:
        print(f"Could not find {city}, please try again.") #check if valid city
        city = input(prompt).capitalize()
    
    if prompt == "Please enter the origin city: ":
        origin = city #store entered city as origin
    elif prompt == "Please enter the destination city: ":
        destination = city #store entered city as destination

    return city
