
shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

total_items = 0

print(f"Lista zakupów")
for shop, items in shopping_dict.items():
    shop = shop.capitalize()
    items_capitalized = [item.capitalize() for item in items]
    print(f"Idę do {shop}, kupuję tu następujące reczy: {items_capitalized}.")
    total_items += len(items)


print(f"W sumie kupuję {total_items} produktów.")

##THE END

price1 = 12.50
price2 = 11.24

total_price = price1 + price2

print(total_price)


### POZDROWIENIA !!!!


print(" POZDROWIENIA !!!! ")


"""
 P.S. Właśnie przyczytałem, że zgodnie z najlepszą praktyką i konwencją nazewnictwa
 branch'y na GitHub powinno sie stosować małe litery, ale już za późno...
 
"""
