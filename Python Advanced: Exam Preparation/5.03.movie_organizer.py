def movie_organizer(*info):
    data = {}
    result = ""

    for movie in info:
        name, genre = movie[0], movie[1]

        if genre not in data:
            data[genre] = []
        data[genre].append(name)

    for genre, names in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{genre} - {len(names)}\n"
        for movie in sorted(names):
            result += f"* {movie}\n"

    return result


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
