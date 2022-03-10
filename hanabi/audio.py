import youtube_dl


class Audio:
    def __init__(self, name):
        self.name = name
        self.youtube = self.__open_youtube_downloader()

    def __open_youtube_downloader(self):
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"/tmp/hanabi/audio/{self.name}.mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        return youtube_dl.YoutubeDL(options)

    def __get_audio_url(self):
        video_info = self.youtube.extract_info(f"ytsearch:{self.name}", download=False)

        return video_info["entries"][0]["webpage_url"]

    def download(self):
        video_url = self.__get_audio_url()
        self.youtube.download([video_url])
