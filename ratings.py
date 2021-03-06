"""Restaurant rating lister."""

def add_ratings():
    """ Reads file and retuns dictionary with resturant names and ratings """

    restaurants = open("scores.txt")

    restaurant_ratings = {}

    for line in restaurants:
        line = line.rstrip()
        establishment = line.split(':')

        if establishment[0] not in restaurant_ratings:
            restaurant_ratings[establishment[0]] = establishment[1]

    return restaurant_ratings

def add_restaurant(restaurant_ratings):
    """ Adds a restaurant and rating to existing restaurants and ratings """

    print("Add a rating for a restaurant!")
    restaurant_name = input("Restaurant name > ").title()
    restaurant_score = int(input("Restaurant rating > "))

    restaurant_ratings[restaurant_name] = restaurant_score


def sorted_scores(restaurant_ratings):
    """ Prints all restaurants and ratings sorted in alphabetical order """

    sorted_restaurant = sorted(restaurant_ratings)

    for restaurant in sorted_restaurant:
        print(f'{restaurant} is rated at {restaurant_ratings[restaurant]}.')

    return (restaurant_ratings)


# will process existing restaurants and ratings from file
restaurant_ratings = add_ratings()

# prompts user to add a restaurant and rating
add_restaurant(restaurant_ratings)

#prints all rated restaurants and ratings in alaphabetical order
sorted_scores(restaurant_ratings)
