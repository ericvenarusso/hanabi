from moviepy.editor import (
    ImageClip,
    TextClip,
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip,
)


class Video:
    def __init__(self, image, texts, audio):
        self.image = image
        self.texts = texts
        self.audio = audio
        self.image_clip = None
        self.text_clip = None
        self.audio_clip = None

    def set_image_clip(self, image_path):
        self.image_clip = ImageClip(image_path, duration=self.audio_clip.duration)
        self.image_clip.resize((1920, 1080))

    def set_text_clip(self, texts):
        text_clips = []
        for text in texts:
            clip = (
                TextClip(
                    text["lyrics"],
                    font="Antique Olive",
                    fontsize=50,
                    color="yellow",
                    method="caption",
                    size=self.image_clip.size,
                    stroke_width=2,
                    stroke_color="black",
                )
                .set_position("center", "center")
                .set_start(text["seconds"])
                .set_duration(text["duration"])
            )
            text_clips.append(clip)

        self.text_clip = text_clips

    def set_audio_clip(self, audio_path):
        self.audio_clip = AudioFileClip(audio_path)

    def create_video_clip(self, save_path):
        self.set_audio_clip(self.audio)
        self.set_image_clip(self.image)
        self.set_text_clip(self.texts)

        audio_clip = CompositeAudioClip([self.audio_clip])
        video_clip = CompositeVideoClip([self.image_clip] + self.text_clip)

        video_clip.audio = audio_clip

        video_clip.write_videofile(fps=60, codec="png", filename=f"{save_path}.mp4")
