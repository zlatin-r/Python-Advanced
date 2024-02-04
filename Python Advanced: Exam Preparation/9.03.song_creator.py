def add_songs(*input_data):
    songs = {}
    result = ""

    for data in input_data:
        song_name, lyrics = data[0], data[1]
        if song_name not in songs:
            songs[song_name] = lyrics
        else:
            if lyrics:
                songs[song_name].extend(lyrics)

    for song, text in songs.items():
        result += f"- {song}\n"

        for line in text:
            result += f"{line}\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
