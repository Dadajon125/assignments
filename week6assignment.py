listings = [
    ('L101', 'Downtown', 500000, 800),
    ('L205', 'Riverside', 450000, 1000),
    ('L102', 'Downtown', 750000, 1200),
    ('L301', 'Northwood', 350000, 900),
    ('L206', 'Riverside', 600000, 1250)
]



def calculate_price_per_sqft(listing):
    price = 0
    area = 1
    index = 0

    for item in listing:
        if index == 2:
            price = item
        elif index == 3:
            area = item
        index += 1

    return price / area

def find_best_value_listing(listings):
    first_time = True
    best_id = ""
    best_price = 0

    for listing in listings:
        price = calculate_price_per_sqft(listing)
        lid = listing[0]

        if first_time:
            best_price = price
            best_id = lid
            first_time = False
        else:
            if price < best_price:
                best_price = price
                best_id = lid
            elif price == best_price and lid < best_id:
                best_id = lid

    return best_id


def get_listings_in_neighborhood(listings, neighborhood_name):
    result = []
    for listing in listings:
        if listing[1] == neighborhood_name:
            result.append(listing[0])
    result.sort()
    return result

# result = get_listings_in_neighborhood(listings, 'Riverside')

def get_neighborhood_value_summary(listings):
    neighborhoods = []

    for listing in listings:
        name = listing[1]
        if name not in neighborhoods:
            neighborhoods.append(name)

    neighborhoods.sort()
    summary = []

    for name in neighborhoods:
        total_value = 0
        for listing in listings:
            if listing[1] == name:
                total_value += listing[2]
        summary.append((name, total_value))

    return summary

def analyze_listings(listings):
    best_value = find_best_value_listing(listings)
    riverside = get_listings_in_neighborhood(listings, "Riverside")
    summary = get_neighborhood_value_summary(listings)
    return (best_value, riverside, summary)



result = analyze_listings(listings)
print(result)
