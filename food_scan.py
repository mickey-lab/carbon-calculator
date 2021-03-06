import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def detect(src):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(src)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

# for label in labels:
#     print(label.description)


def calc_emissions_pic(labels): #017082884022 05100023355
    datadict = {'Wheat & Rye (Bread)': 0.6, 'Maize (Meal)': 0.4, 'Barley (Beer)': 0.2, 'Oatmeal': 0.9, 'Rice': 1.2, 'Potatoes': 0.6, 'Cassava': 1.4, 'Cane Sugar': 3.2, 'Beet Sugar': 1.8, 'Other Pulses': 0.8, 'Peas': 0.4, 'Nuts': 0.3, 'Groundnuts': 1.2, 'Soymilk': 1.0, 'Tofu': 2.0, 'Soybean Oil': 6.3, 'Palm Oil': 7.3, 'Sunflower Oil': 3.6, 'Rapeseed Oil': 3.8, 'Olive Oil': 5.4, 'Tomatoes': 2.1, 'Onions & Leeks': 0.5, 'Root Vegetables': 0.4, 'Brassicas': 0.5, 'Other Vegetables': 0.5, 'Citrus Fruit': 0.4, 'Bananas': 0.9, 'Apples': 0.4, 'Berries & Grapes': 1.5, 'Wine': 0.1, 'Other Fruit': 1.1, 'Coffee': 0.4, 'Dark Chocolate': 2.3, 'Bovine Meat (beef herd)': 50.0, 'Bovine Meat (dairy herd)': 17.0, 'Lamb & Mutton': 20.0, 'Pig Meat': 7.6, 'Poultry Meat': 5.7, 'Milk': 3.2, 'Cheese': 11.0, 'Eggs': 4.2, 'Fish (farmed)': 6.0, 'Crustaceans (farmed)': 18.0}
    foods = {'Rice': ['Rice', 1000], 'Oatmeal': ['Oatmeal', 1000], 'Potatoes': ['Potatoes', 1000], 'Beef': ['Bovine Meat (beef herd)', 400], 'Bread': ['Wheat & Rye (Bread)', 1000], 'Fish': ['Fish (farmed)', 400], 'Egg': ['Eggs', 400], 'Cheese': ['Cheese', 400], 'Milk': ['Milk', 624], 'Chicken': ['Poultry Meat', 400], 'Turkey': ['Poultry Meat', 400], 'Bacon': ['Pig Meat', 400], 'Ham': ['Pig Meat', 400], 'Pork': ['Pig Meat', 400], 'Lamb': ['Lamb & Mutton', 400], 'Mutton': ['Lamb & Mutton', 400], 'Banana': ['Bananas', 890], 'Apple': ['Apples', 520], 'Olive Oil': ['Olive Oil', 8048], 'Nut': ['Nuts', 400], 'Pea': ['Peas', 810], 'Tofu': ['Tofu', 400], 'Tomato': ['Tomatoes', 180], 'Berries': ['Berries & Grapes', 330], 'Shrimp': ['Crustaceans (farmed)', 400], 'Pasta': ['Wheat & Rye (Bread)', 1000]} #key is search item, value is [table item, NU factor]

    footprint = 'Unknown'

    for label in labels:
        for food in foods:
            if label.description.find(food) != -1: #ie food found in description
                footprint = datadict[foods[food][0]]*700/foods[food][1] #guess average portion 700kcal
                return footprint, food


# print(calc_emissions_pic(labels))