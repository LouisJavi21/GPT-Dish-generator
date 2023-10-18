import json
from csv import writer

# Load in dishes
with open("data/dishes.json", "r") as infile:
    dishes = json.load(infile)


nodes = []
edges = []

unique_ingredients = []

id = 0
for dish in dishes:
    country = dish["country"]
    dish_name = dish["dish"]
    ingredients = dish["ingredients"]

    # Setup nodes as specified as GraphCommons: Node Type, Node name, ID (For personal use)
    country_node = f"country,{country},{str(id)}\n"
    dish_node = f"dish,{dish_name},{str(id)}\n"

    if ingredients:
        unique_ingredients.extend(ingredients)
        # Don't have enough space to put in all ingredients, need a premium GraphCommons account.

        if len(list(set(unique_ingredients))) > 350:
            continue
        # Organize the ingredients as nodes and add the Edge which binds it to the dish
        for ingredient in ingredients:
            ingredient_node = f"ingredient,{ingredient},{str(id)}\n"
            ingredient_dish_edge = f"ingredient,{ingredient},ingredient dish,dish,{dish_name}\n"
            nodes.append(ingredient_node)
            edges.append(ingredient_dish_edge)

    # Bind Country and Dish using an edge: Node Type, Node name, Edge Type, Node Type, Node name
    country_dish_edge = f"dish,{dish_name},dish owned,country,{country}\n"

    # Append the nodes and edges
    nodes.append(country_node)
    nodes.append(dish_node)
    edges.append(country_dish_edge)
    id += 1

# Make sure the edges are unique, limited to size

edges = list(set(edges))
with open("data/nodes.csv", "w+") as outfile:
    csv_writer = writer(outfile)
    outfile.write("Node Type,Name,id\n")
    outfile.writelines(nodes)

with open("data/edges.csv", "w+") as outfile:
    csv_writer = writer(outfile)
    outfile.write("From Type,From Name,Edge Type,To Type,To Name,id\n")
    outfile.writelines(edges)