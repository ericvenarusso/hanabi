import pytest
from unittest.mock import patch

from hanabi.audio import Audio


@pytest.fixture
def audio():
    return Audio(name="levan polkka")


def test_init_youtube_downloader(audio):
    mock_youtube_params = {
        "format": "bestaudio/best",
        "nocheckcertificate": False,
        "outtmpl": "/tmp/hanabi/audio/levan polkka.mp3",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    assert mock_youtube_params == audio.youtube.params


def test_get_audio_url(audio):
    return_url = "youtube.com"
    with patch.object(Audio, "_get_audio_url", return_value = return_url) as mock_method:
        audio._get_audio_url()

        mock_method.assert_called_once()
        mock_method.return_value == return_url

def test_donwload(audio):
    with patch.object(Audio, "download") as mock_method:
        audio.download()
        mock_method.assert_called_once()
