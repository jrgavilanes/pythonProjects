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

    def __init__(self, name: str = "", enchantments=[]):
        self.name = name
        self.enchantments = enchantments

    def __str__(self):
        enchantments = ""
        curated_enchantments = sorted(set(self.enchantments), key=lambda x: x.id_name)
        # items[item].enchantments = sorted(set(items[item].enchantments), key=lambda x: x.id_name)
        # items[item].enchantments = list(set(items[item].enchantments))
        for item in curated_enchantments:
            enchantments += f"\n  [{item.max_level}] {item.id_name}"

        title = self.name.replace("_", " ")
        return f"{title.title()}: " + enchantments


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
                    items = list(map(lambda x: x.replace('fishing rod', 'fishing_rod'), items))

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
                items[item] = Item(item, [data[key_enchantment]])
            else:
                items[item].enchantments.append(data[key_enchantment])
                # items[item].enchantments = sorted(set(items[item].enchantments), key=lambda x: x.id_name)
                # items[item].enchantments = list(set(items[item].enchantments))

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

# solution provided
# from collections import defaultdict
# from dataclasses import dataclass, field
# from functools import total_ordering
# import os
# from pathlib import Path
# from re import compile, search
# from typing import Any, DefaultDict, List
# from urllib.request import urlretrieve
#
# from bs4 import BeautifulSoup as Soup
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# HTML_FILE = TMP / "enchantment_list_pc.html"
#
# # source:
# # https://www.digminecraft.com/lists/enchantment_list_pc.php
# URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
#        "minecraft-enchantment.html")
#
# ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}
#
#
# @dataclass
# @total_ordering
# class Enchantment:
#     """Minecraft enchantment"""
#
#     id_name: str
#     name: str
#     max_level: int
#     description: str
#     items: List[str] = field(default_factory=list)
#
#     def __str__(self):
#         return f"{self.name} ({self.max_level}): {self.description}"
#
#     def __lt__(self, other):
#         return self.id_name < other.id_name
#
#
# @dataclass
# class Item:
#     """Minecraft enchantable item"""
#
#     name: str
#     enchantments: List[Enchantment] = field(default_factory=list)
#
#     def __str__(self):
#         enchants = sorted(self.enchantments)
#         enc_list = [f"\n  [{enc.max_level}] {enc.id_name}" for enc in enchants]
#         return f"{self.name.title()}: {''.join(enc_list)}"
#
#
# def clean_up_names(item_names):
#     """Cleans up item names
#
#     :param item_names: String of item names
#     :return: String of cleaned up item names
#     """
#     unwanted = (".png", "_sm", "iron_", "enchanted_")
#
#     if "fishing_rod" in item_names:
#         item_names = item_names.replace("fishing_rod", "fishingrod")
#
#     for chars in unwanted:
#         if chars in item_names:
#             item_names = item_names.replace(chars, "")
#
#     item_names = item_names.split("_")
#     item_names = [
#         "fishing_rod" if item == "fishingrod" else item for item in item_names
#     ]
#
#     return " ".join(item_names)
#
#
# def enchantable_items(soup):
#     """Scrapes BeautifulSoup object for items
#
#     :param soup: BeautifulSoup object
#     :return: List of enchantable items lists
#     """
#     table = soup.find("table", {"id": "minecraft_items"})
#     items = [
#         clean_up_names(img["data-src"].split("/")[-1]).split()
#         for img in table.find_all("img")
#     ]
#
#     return items
#
#
# def generate_enchantments(soup):
#     """Generates a dictionary of Enchantment objects
#
#     :param soup: BeautifulSoup object
#     :return: DefaultDict of Enchantment objects
#     """
#     item_list = enchantable_items(soup)
#     data = parse_html(soup)
#     enchant_data: DefaultDict[Any, Enchantment] = defaultdict(Enchantment)
#
#     for i, row in enumerate(data):
#         id_name, name = split_title(row[0])
#         max_level = ROMAN[row[1]]
#         description = row[2]
#         items = item_list[i]
#         enchant = Enchantment(id_name, name, max_level, description, items)
#         enchant_data[id_name] = enchant
#
#     return enchant_data
#
#
# def generate_items(data):
#     """Generates a dictionary of Item objects
#
#     :param data: DefaultDict of Enchantment objects
#     :return: DefaultDict of Item objects
#     """
#     mc_items: DefaultDict[Any, Item] = defaultdict(Item)
#     unique_items = gen_item_set(data)
#
#     for item in unique_items:
#         mc_items[item] = Item(item.replace("_", " "))
#
#     for enchant in data:
#         for item in data[enchant].items:
#             mc_items[item].enchantments.append(data[enchant])
#
#     return mc_items
#
#
# def gen_item_set(data):
#     """Returns a set of item names
#
#     :param data: Dictionary of Enchantment objects
#     :return: Set of sorted item object name strings
#     """
#     mc_items = set()
#     for enchantment in data.keys():
#         for item in data[enchantment].items:
#             mc_items.add(item)
#
#     return sorted(mc_items)
#
#
# def get_soup(file=HTML_FILE):
#     """Retrieves source HTML and returns a BeautifulSoup object
#
#     :param file: Path file object
#     :return: BeautifulSoup object
#     """
#     if isinstance(file, Path):
#         if not file.is_file():
#             urlretrieve(URL, file)
#
#         with file.open() as html_source:
#             soup = Soup(html_source, "html.parser")
#     else:
#         soup = Soup(file, "html.parser")
#
#     return soup
#
#
# def main():
#     """This function is here to help you test your final code"""
#     soup = get_soup()
#     enchantment_data = generate_enchantments(soup)
#     minecraft_items = generate_items(enchantment_data)
#     for item in minecraft_items:
#         print(minecraft_items[item], "\n")
#
#
# def parse_html(soup):
#     """Parses BeautifulSoup object and returns the table
#
#     :param soup: BeautifulSoup object
#     :return: List of the rows that make up the table
#     """
#     table = soup.find("table", {"id": "minecraft_items"})
#     data = [
#         [td.get_text() for td in row.find_all("td")] for row in table.find_all("tr")
#     ]
#
#     return data[1:]
#
#
# def split_title(title):
#     """
#     Splits the title string
#
#     :param title: String of the enchantment title
#     :return: Tuple(id_names, names)
#     """
#     pattern = compile(r"(.*)\((.*)\)")
#     names, id_names = search(pattern, title).groups()
#     return id_names, names
#
#
# if __name__ == "__main__":
#     main()