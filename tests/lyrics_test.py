import json
import pytest
from unittest.mock import Mock, patch

import requests

from hanabi.lyrics import Lyrics


@pytest.fixture
def lyrics():
    return Lyrics("levan polkka")


@pytest.fixture
def lyrics_text():
    return [
        {"seconds": 3, "text": "Black Hole Sun"},
        {"seconds": 4, "text": "Wont you come"},
    ]


def test_duration(lyrics, lyrics_text):
    mock_duration = [1, 3]

    lyrics._add_duration(lyrics_text)
    duration_list = [duration["duration"] for duration in lyrics_text]

    assert mock_duration == duration_list


def test_get_lyrics(lyrics, lyrics_text):
    mock_response = Mock()
    mock_response.text = json.dumps(lyrics_text)

    with patch.object(requests, "get", return_value=mock_response) as mock_method:
        lyrics_return = lyrics.get_lyrics()

        mock_method.assert_called_once_with(
            "https://api.textyl.co/api/lyrics", params={"q": lyrics.name}
        )

        lyrics_text[0]["duration"] = 1
        lyrics_text[1]["duration"] = 3

        lyrics_return == lyrics_text
