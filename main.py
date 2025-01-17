
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

