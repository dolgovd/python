# Program allows to download images from the Internet based on provided parameters as resolution, type of licence, etc.
# icrawler library is used for the project

from icrawler.builtin import GoogleImageCrawler

def google_image_downloader():
    # create an object of the class
    crawler =  GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword='mr.robot', max_num=5)

def main():
    google_image_downloader()

if __name__ == '__main__':
    main()