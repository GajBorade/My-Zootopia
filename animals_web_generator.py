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

# 1. Read the contents of the template, animals_template.html
# As html template is in the same folder no need to specify
# path hence no os import required.

with open("animals_template.html", "r", encoding='utf-8') as fileobject:
    animals_template = fileobject.read()


# 2. Generate a string with the animals’ data
# Use break tags & wrap animals in block elements p
output: str = "" # define empty string
for animal in animals_data:
    #append information to each string
    output += f"    <li>\n"
    output += f"    <p>Name: {animal.get('name', 'not available')}<br>\n"
    output += f"    Diet: {animal['characteristics'].get('diet', 'Not available')}<br>\n"
    locations = animal.get("locations")
    location_str = locations[0] if locations else "Unknown"
    output += f"    Location: {location_str}<br>\n"
    output += f"    Type: {animal.get('type', 'Not available')}<br></p>\n"
    output += f"    </li>\n"

print(output)

# Step 3. Replace __REPLACE_ANIMALS_INFO__ with the generated string

html_data = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4. Write this new string to the 'new' html file
with open("animals.html", "w", encoding='utf-8') as fileobject:
    fileobject.write(html_data)