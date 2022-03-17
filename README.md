<img src="images/logo.png" height="250" width="350"></img>

![version](https://img.shields.io/badge/version-0.1.0-<COLOR>)
![tests](https://github.com/ericvenarusso/hanabi/actions/workflows/ci.yaml/badge.svg?branch=main)


# What is Hanabi?
Hanabi is a open-source Python framework that automate the creation of music videos with lyrics.

# How to install
To install hanabi, you just need to run:
```
poetry install
```

# How to use
Imagine that you would like to create a music video for Eminem - Lose your self. You can use hanabi cli, as follows:

```
hanabi create-video --music-name "eminem lose your self"
```

When running the code above, hanabi will search for the lyrics, image, music and create the video.

## Additional Options
Hanabi cli has some other arguments such as:

### Image File
Allows you to create the video from the specified image.
```
hanabi create-video --music-name --image-file "eminem.jpg"
```

### Audio File
Allows you to create the video from the specified audio.
```
hanabi create-video --music-name --audio-file "lose_your_self.mp3"
```

### Save Path
Allows you to create the video from the specified path.
```
hanabi create-video --music-name --save-path "eminem_lose_your_self.mp4"
```

## Hanabi API
You can also use the direct API.
``` python
from hanabi.lyrics import Lyrics
from hanabi.audio import Audio
from hanabi.image import Image
from hanabi.video import Video

HANABI_PATH = "/tmp/hanabi"
MUSIC_NAME = "eminem lose your self"

# Get music lyrics
music_lyrics = Lyrics(MUSIC_NAME).get_lyrics()

# Download the image
Image(MUSIC_NAME).download()
image_file = f"{HANABI_PATH}/image/{MUSIC_NAME}/000001.jpg"

# Download the music audio
Audio(MUSIC_NAME).download()
audio_file = f"{HANABI_PATH}/audio/{MUSIC_NAME}.mp3"

# Create the video
video = Video(
    texts=music_lyrics,
    audio=audio_file,
    image=image_file,
)

video.create_video_clip(save_path=f"{MUSIC_NAME}.mp4")
```

# Contributing
To make contributions to the repository, it is necessary to open a PR(Pull Request), which has good code writing and the CI is passing.

