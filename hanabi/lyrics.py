import ast

import requests


class Lyrics:
    def __init__(self, name):
        self.name = name
        self.lyrics_endpoint = "https://api.textyl.co/api/lyrics"

    @staticmethod
    def _add_duration(lyrics):
        position = 0
        list_len = len(lyrics)

        while position < list_len:
            actual_element = lyrics[position]

            next_index = position + 1
            if next_index == list_len:
                actual_element["duration"] = 3
                break

            next_element = lyrics[next_index]

            duration = next_element["seconds"] - actual_element["seconds"]
            actual_element["duration"] = duration

            position += 1

        return lyrics

    def get_lyrics(self) -> list:
        response = requests.get(self.lyrics_endpoint, params={"q": self.name})
        response_list = ast.literal_eval(response.text)
        lyrics = self._add_duration(response_list)

        return lyrics
