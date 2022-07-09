import os
countries = ["mondstadt", "liyue", "inazuma"]

def get_num_classes():
    num_classes = 0
    for country in countries:
        characters = os.listdir(country)
        for character in characters:
            character_dir = f"{country}/{character}"
            if os.path.isdir(character_dir):
                num_classes += 1
    return num_classes