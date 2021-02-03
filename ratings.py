"""Restaurant rating lister."""

def rate_a_restaurant(filename):

    restaurants = open(filename)

    restaurant_ratings = {}

    for line in restaurants:
        line = line.rstrip()
        establishment = line.split(':')

        if establishment[0] not in restaurant_ratings:
            restaurant_ratings[establishment[0]] = establishment[1]
    
    sorted_restaurant = sorted(restaurant_ratings)

    for restaurant in sorted_restaurant:
        print(f'{restaurant} is rated at {restaurant_ratings[restaurant]}.')

    return (restaurant_ratings)

rate_a_restaurant("scores.txt")
