import pytest
from unittest.mock import patch

from icrawler.builtin import GoogleImageCrawler

from hanabi.image import Image


@pytest.fixture
def image():
    return Image("levan polkka")


def test_download(image):
    with patch.object(GoogleImageCrawler, "crawl") as mock_method:
        image.download()

        mock_method.assert_called_once_with(
            max_num=1, overwrite=True, keyword=image.name, filters={"size": "large"}
        )
