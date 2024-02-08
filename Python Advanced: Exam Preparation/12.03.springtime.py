def start_spring(**kwargs):
    collections = {}
    result = ""

    for object_name, object_type in kwargs.items():
        if object_type not in collections:
            collections[object_type] = []
        collections[object_type].append(object_name)

    sorted_collections = sorted(collections.items(), key=lambda x: (-len(x[1]), x[0]))

    for k, v in sorted_collections:
        result += f"{k}:\n"
        for value in sorted(v):
            result += f"-{value}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
