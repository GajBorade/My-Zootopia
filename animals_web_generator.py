import json


def load_data(file_path):
    """
    Loads data from json file

    :param file_path: Path to json file
    :return: list of nested dictionaries representing data
    """
    with open(file_path) as handle:
        return json.load(handle)


filename = "animals_data.json"
animals_data = load_data(filename)

for animal in animals_data:
    name = animal.get("name", "Unknown")

    diet = animal["characteristics"].get("diet", "Unknown")

    animal_type = animal["characteristics"].get("type", "Unknown")

    # location = ", ".join(animal['locations']) # for all locations
    locations = animal.get("locations")
    location = locations[0] if locations else "Unknown"

    print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n")
