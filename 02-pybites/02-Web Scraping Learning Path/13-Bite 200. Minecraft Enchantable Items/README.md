# Bite 200. 🥳 Minecraft Enchantable Items

https://codechalleng.es/bites/200/

My kids love Minecraft and they always want me to play with them. At times gathering resources can get boring so I
sometimes deck them out with some enchanted items so that we can take on some pillager strongholds. Although typing in
the commands is relatively simple, they can get pretty long and unwieldy!

After doing it a few times, I decided to turn to my favorite tool, Python! This bite is actually my first step in
creating a command line utility that generates the commands for me. I've already done this but I thought it would be
great to see how others would tackle the same problem. Your challenge here is to scrape digminecraft.com for a list of
enchantable items and create a couple of classes from the information gathered.

What I'm looking for is a dictionary of Minecraft items. The page only contains information on the enchantments so that
is all we'll be focusing on. If done correctly the main() function should print the following results:

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

    Tasks to complete:
    Enchantment class

        id_name: Internal name of the enchantment
        name: User friendly name of the enchantment
        max_level: Enchantment level. Original is in Roman numerals; they need to be converted to integers
        description: Summary of what the enchantment does
        items: List of item names that are typically enchanted with this enchantment.

    If, for example, the mending instance is printed, it should look like this:

    Mending (1): Uses xp to mend your tools, weapons and armor

    NOTE: Notice that the name is title cased, max_level is surrounded by parenthesis, which is followed by the description.

    If you print its items, it would look like this:

    ['sword', 'chestplate', 'pickaxe', 'fishing_rod']

    NOTE: Notice that the items are not in alphabetical order! They are stored in the order in which they are parsed from the html and are only alphabetized when the instance in printed.
    Item class

        name: Name of the item
        enchantments: List of the enchantment instances.

    If, for example, the fishing_rod object is printed, it should look like this:

    Fishing Rod: 
      [3] luck_of_the_sea
      [3] lure
      [1] mending
      [3] unbreaking
      [1] vanishing_curse

    NOTE: Notice that the name is title cased and that the _ has been replaced with a space!

    If you were to print each enchantment belonging to the fishing_rod, it would look like this:

    Curse of Vanishing (1): Cursed item will disappear after player dies
    Luck of the Sea (3): Increases chances of catching valuable items
    Lure (3): Increases the rate of fish biting your hook
    Mending (1): Uses xp to mend your tools, weapons and armor
    Unbreaking (3): Increases durability of item

    NOTE: Notice that this output is exactly like the one for the Enchantment objects, because that's what they are.
    The following functions are what you will need to complete:
    generate_enchantments

        This function is responsible for generating a dictionary of the Enchantment objects.

    generate_items

        This function is responsible for generating a dictionary of the Item objects.

    Some helpful tips:

    Each of the enchantments has an image in place of actual item names. The best thing that I could come up with was to clean up the image name and extract the information from them. Removing the following from the names will do the job: ".", "_", "enchanted", "iron", "png", and "sm"

    For example, vanishing_curse has this image:

    https://www.digminecraft.com/enchantments/images/sword_chestplate_pickaxe_fishing_rod_sm.png

    Which would be scraped as ["sword", "chestplate", "pickaxe", "fishing_rod"] for that enchantment.

    NOTE: Caution must be taken here since fishing_rod is a valid item name that must be maintained!

    The titles will need some work as well. In it's raw form the titles are listed as Aqua Affinity(aqua_affinity). You'll have to separate the two and assign them to their correct variables: name and id_name, where the latter is the one in parenthesis.
    Final Note

    Pay attention to that output above. Not only are the items sorted, but also each of the item's enchantments! Don't try and modify the output from main() as that is not used in the testing.
