from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

def image_downloader():
    # bing crawler
    filters = dict(
        type = 'photo', # photo, face, clipart, etc.
        color = 'blackandwhite',
        size = 'large', # large, icon, 1024x1024
        # license = 'noncommercial',
        # date = 'pastweek' # date when image was published
    )
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': './img'})
    bing_crawler.crawl(
        keyword='mr.robot',
        filters=filters,
        offset=0,
        max_num=10)
    
def main():
    image_downloader()

if __name__ == '__main__':
    main()