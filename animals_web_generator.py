import json


def load_data(file_path):
    """
    Loads data from json file

    :param file_path: Path to json file
    :return: list of nested dictionaries representing data
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def print_animals_data(animals_data):
    """
    Prints data about animals

    :return: None
    """
    for animal in animals_data:
        name = animal.get("name", "Unknown")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")

        animal_type = characteristics.get("type", "Unknown")

        locations = animal.get("locations")
        location = locations[0] if locations else "Unknown"

        print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n")


# 1. Read the contents of the template, animals_template.html
def read_html_template(template_path):
    """
    Reads an HTML template from a file.

    :param template_path: Path to the HTML template file.
    :return: Content of the template file as a string.
    """
    with open(template_path, "r", encoding='utf-8') as fileobject:
        return fileobject.read()


# 2. Generate a string with the animals’ data
# Use HTML tags & wrap animals in block elements p
def serialize_animals_data(animals_obj):
    """
    Serializes a list of animals into HTML list items.

    :param animals_obj: list of nested dictionaries, each representing an animal.
    :return: A string containing HTML representation of all animals
    """
    output = ""
    for animal in animals_obj:
        #append information to each string
        output += f'    <li class="cards__item">\n'
        output += f'        <div class="card__title">{animal.get("name", "not available")}</div>\n'
        output += f'        <p class="card__text">'

        characteristics = animal.get("characteristics", {})
        output += f'            <strong>Diet</strong>: {characteristics.get("diet", "Not available")}<br>\n'

        locations = animal.get("locations")
        location_str = locations[0] if locations else "Unknown"
        output += f'            <strong>Location</strong>: {location_str}<br>\n'
        output += f'            <strong>Type</strong>: {characteristics.get("type", "Not available")}<br>\n'
        # Bonus fields
        output += f'            <strong>Life-span</strong>: {characteristics.get("lifespan", "Not available")}<br>\n'
        output += f'            <strong>Habitat</strong>: {characteristics.get("habitat", "Not available")}<br>\n'
        output += f'            <strong>Slogan</strong>: {characteristics.get("slogan", "Not available")}<br>\n'
        output += f'            <strong>Color</strong>: {characteristics.get("color", "Not available")}<br>\n'
        output += f'            <strong>Speed</strong>: {characteristics.get("top_speed", "Not available")}<br>\n'
        output += f'            <strong>Temperament</strong>: {characteristics.get("temperament", "Not available")}<br>\n'
        output += f'        </p>\n'
        output += f'    </li>\n'
    return output


# Step 4. Write this new string to the 'new' html file
def write_html_template(html_data):
    """
    Writes the given HTML content (str) to the 'animals.html' file.

    :param html_data: A string containing the full HTML content (str)
    to be written to the file.
    :return: None
    """
    with open("animals.html", "w", encoding='utf-8') as fileobject:
        fileobject.write(html_data)


def main():
    """
    Controls the flow of the program:
    - Loads animal data from JSON
    - Prints animals data to console
    - Reads HTML template
    - Serializes animal data into HTML list items
    - Writes final HTML file to disk

    :return: None
    """
    # Load animal data from json file
    filename = "animals_data.json"
    animals_data = load_data(filename)

    # Print data for console inspection
    print_animals_data(animals_data)

    # Read HTML template
    animals_template_path = "animals_template.html"
    animals_template_html = read_html_template(animals_template_path)

    # Step 3: Replace __REPLACE_ANIMALS_INFO__ with the generated string
    # to serialize animals into HTML
    final_html = animals_template_html.replace(
        "__REPLACE_ANIMALS_INFO__",
        serialize_animals_data(animals_data)
    )

    # Write final HTML to file
    write_html_template(final_html)


if __name__ == "__main__":
    main()