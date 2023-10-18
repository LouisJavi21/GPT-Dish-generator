from csv import reader
import pandas as pd
import json
import re

dishes = []

# Regex pattern to clean up the following:
# Cleans up Units as well.
# Replaces AND words too and :
# Replaces Full stops
ingredients_re =r"\s\(.*\)| and|\.|[Ii]ngredients|[Ii]ngredients:|^[0-9]* tsp$|[0-9]+ml|[0-9]* tbsp|[0-9]+g|[0-9] |:"

with open("responses.csv", "r") as infile:
    csv_reader = reader(infile, delimiter=';')
    for line in csv_reader:

        # Clean up country;dish;ingredients
        if line[0] == "country" and line[1] == "dish" and line[2] == "ingredients":
            continue

        # Sometimes ingredients are separated with a - instead of , Remove for now
        #Lebanon;Shawarma;Ingredients: 
        # - 500g of boneless chicken or beef
        # - 1 tablespoon of olive oil
        # - 1 teaspoon of ground cumin
        # - 1 teaspoon of ground coriander
        # - 1 teaspoon of paprika
        # - 1 teaspoon of turmeric
        # - 1 teaspoon of garlic powder
        # - 1 teaspoon of onion powder
        # - Juice of 1 lemon
        # - Salt and pepper to taste
        # - 4-6 pita bread
        # - Tahini sauce (optional)
        if len(line) < 3:
            continue

        # After exclusion get the ingredients and do basic cleaning
        # This involves: Applying the regex pattern, splitting the ingredients and title casing
        ingredients = line[2]
        ingredients = re.sub(ingredients_re, '', ingredients).title()
        ingredients = ingredients.split(', ')
        cleaned_ingredients = []

        for ingredient in ingredients:
            # Exclude single or double character ingredients. As example: '.', ' ', 'a', Etc.
            if len(ingredient) > 2:
                cleaned_ingredients.append(ingredient.strip())

        line[2] = cleaned_ingredients

        for idx, item in enumerate(line):
            if idx == 2:
                # Do not strip or title case ingredients
                line[idx] = item
            else:
                line[idx] = item.strip().title()
        
        # Organize it into JSON with keys.
        dish = {"country": line[0], "dish": line[1], "ingredients": line[2]}
        dishes.append(dish)

with open("dishes.json", "w+") as outfile:
    outfile.writelines(json.dumps(dishes))

# df = pd.DataFrame.from_dict(dishes)
# print(df.dish.value_counts()[:10].index.tolist())