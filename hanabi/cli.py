import click

from hanabi import __version__
from hanabi.lyrics import Lyrics
from hanabi.audio import Audio
from hanabi.image import Image
from hanabi.video import Video


HANABI_PATH = "/tmp/hanabi"


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-V", "--version")
@click.argument("create-video", required=True)
@click.option(
    "--music-name", required=True, help="Name of the Music to build the video."
)
@click.option(
    "--image-file",
    required=False,
    type=click.Path(exists=True),
    help="Image file to build the video.",
)
@click.option(
    "--audio-file",
    required=False,
    type=click.Path(exists=True),
    help="Audio file to build the video.",
)
@click.option("--save-path", required=False, help="Path to save the video")
def create_video(create_video, music_name, image_file, audio_file, save_path):
    """Framework to create music lyrics video."""
    music_lyrics = Lyrics(music_name).get_lyrics()

    if not image_file:
        Image(music_name).download()
        image_file = f"{HANABI_PATH}/image/{music_name}/000001.jpg"

    if not audio_file:
        Audio(music_name).download()
        audio_file = f"{HANABI_PATH}/audio/{music_name}.mp3"

    video = Video(
        texts=music_lyrics,
        audio=audio_file,
        image=image_file,
    )

    music_name = f"{music_name}.mp4"
    if save_path:
        music_name = save_path

    video.create_video_clip(save_path=music_name)


if __name__ == "__main__":
    create_video()
