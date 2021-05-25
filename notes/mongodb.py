import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']

## luke = db.characters.find_one({"name": "Luke Skywalker"})
# luke = db.characters.find({"name": "Luke Skywalker"})
#
# for char in luke:
#     print(char)


# Print the names of all the droids
# droids = db.characters.find({"species.name": "Droid"})
#
# for char in droids:
#     print(char["name"])


# Find the height of Darth Vader, only return results for the name and the height

# dar_vader = db.characters.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0})
# print(dar_vader)
#
# dar_vader = db.characters.find_one({"name": {"$regex": "Vader"}}, {"name": 1, "height": 1, "_id": 0})
# print(dar_vader)


# Find all characters with yellow eyes, only return results for the names of the characters

# yel_eyes = db.characters.find({"eye_color": "yellow"}, {"name": 1, "eye_color": 1, "_id": 0})
#
# for char in yel_eyes:
#     print(char)


# Find male characters, return the first three

# male_char = db.characters.find({"gender": "male"}, {"name": 1, "gender": 1, "_id": 0}).limit(3)
#
# for char in male_char:
#     print(char)


# Find the names of all the humans whose homeworld is Alderaan
#
# human_ald = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"}, {"name": 1, "_id": 0})
#
# for char in human_ald:
#     print(char)


#  What is the average height of female characters
#
# avg_female_char = db.chardemo.aggregate([
#     {"$match": {"gender": "female", "height": {"$ne": float("nan")}}},
#     {"$group": {"_id": "$gender", "Avg_height": {"$avg": "$height"}}}
# ])
# print(avg_female_char.next())


# Which character is the tallest?
#
# max_char = db.chardemo.aggregate([
#     {"$group": {"_id": None, "max_height": {"$max": "$height"}}}
# ]).next()["max_height"]
#
# for tallest in db.chardemo.find({"height": max_char}):
#     print(tallest["name"], tallest["height"])


