from icrawler.builtin import GoogleImageCrawler


class Image:
    def __init__(self, name):
        self.name = name

    def download(self):
        google_crawler = GoogleImageCrawler(
            storage={"root_dir": f"/tmp/hanabi/image/{self.name}"}
        )

        google_crawler.crawl(
            max_num=1, overwrite=True, keyword=self.name, filters={"size": "large"}
        )
