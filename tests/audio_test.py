import pytest
from unittest.mock import patch

from youtube_dl import YoutubeDL

from hanabi.audio import Audio


@pytest.fixture
def audio():
    return Audio("levan polkka")


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
    audio_url = "http://www.youtube.com"
    mock_return = {"entries": [{"webpage_url": audio_url}]}

    with patch.object(
        YoutubeDL, "extract_info", return_value=mock_return
    ) as mock_method:
        audio_return = audio._get_audio_url()

        mock_method.assert_called_once_with("ytsearch:levan polkka", download=False)
        assert audio_url == audio_return


def test_download():
    get_url_audio_return = "youtube.com"

    with patch.object(Audio, "download") as mock_method:
        mock_method._get_audio_url.return_value = get_url_audio_return
        mock_method.download()

        mock_method.download.assert_called_once()
