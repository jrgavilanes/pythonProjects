import os
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
HTML_FILE = TMP / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")

enchantment_data = None


class Enchantment:
    """Minecraft enchantment class

    Implements the following: 
        id_name, name, max_level, description, items
    """

    def __init__(self, id_name, name, max_level, description, items=[]):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items

    def __repr__(self):
        # return f"[{self.max_level}] {self.id_name}"
        return f"{self.name} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class

    Implements the following: 
        name, enchantments
    """

    def __init__(self, name: str = "", items=[]):
        self.name = name
        self.items = items

    def __str__(self):
        global enchantment_data
        enchantments = ""
        for e in self.items:
            if e in enchantment_data:
                enchantments += f"\n  {enchantment_data[e]}"
                # enchantments += f"\n  {e}"

        return f"{self.name.capitalize()}:" + enchantments



def _roman_to_digit(roman_value: str) -> int:
    roman_value = roman_value.strip()
    if roman_value == "I":
        return 1
    elif roman_value == "II":
        return 2
    elif roman_value == "III":
        return 3
    elif roman_value == "IV":
        return 4
    elif roman_value == "V":
        return 5

    return 0


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects

    With the key being the id_name of the enchantment.
    """
    enchantments = {}
    table_rows = soup.select("table.std_table tr")
    for row in table_rows[1:]:
        id_name = ""
        name = ""
        max_level = ""
        description = ""
        items = ""
        for index, col in enumerate(row):
            if index == 1:
                id_name = col.find("em")
                id_name = id_name.text
                name = col.find("a")
                if name:
                    name = name.text
            elif index == 3:
                max_level = _roman_to_digit(col.text)
            elif index == 5:
                description = col.text
            elif index == 9:
                imgs = col.find_all("img")
                for img in imgs:
                    items = img["data-src"]
                    items = items.split("/")[-1]
                    items = items.replace("_sm.png", "")
                    items = items.replace("enchanted", "")
                    items = items.replace("iron", "")
                    items = items.replace(".png", "")
                    items = items.replace("fishing_rod", "fishing rod")
                    items = items.split("_")

        # print(f"id_name: {id_name}")
        # print(f"name: {name}")
        # print(f"max_level: {max_level}")
        # print(f"description: {description}")
        # print(f"items: {items}")
        # print("-------")
        enchantments[id_name] = Enchantment(id_name, name, max_level, description, items)

    # print(enchantments)
    return enchantments


def generate_items(data):
    """Generates a dictionary of Item objects

    With the key being the item name.
    """
    all_items = []
    items = {}
    for key_enchantment in data:
        for item in data[key_enchantment].items:
            all_items.append(item)
            if item not in items:
                items[item] = Item(item, [key_enchantment])
            else:
                items[item].items.append(key_enchantment)
                items[item].items = sorted(set(items[item].items))

    del items['']
    sorted_keys = sorted(items.keys())
    result = {key: items[key] for key in sorted_keys}
    return result


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not file.is_file():
            urlretrieve(URL, file)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.

    Once complete, the print out should match what's at the bottom of this file"""
    global enchantment_data
    get_soup()
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
