def cookbook(*args):
    data = {}
    result = ""

    for arg in args:
        recipie, cuisine, ingredients = arg

        if cuisine not in data:
            data[cuisine] = {}
        data[cuisine][recipie] = ingredients

    sorted_data = sorted(data.items(), key=lambda item: (-len(item[1]), item))

    for k, v in sorted_data:
        result += f"{k} cuisine contains {len(v)} recipes:\n"
        for recipe, ingredients in sorted(v.items()):
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
    ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
    ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
    ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
