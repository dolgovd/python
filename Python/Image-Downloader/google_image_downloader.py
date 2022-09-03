# Program allows to download images from the Internet based on provided parameters as resolution, type of license, etc.
# icrawler library is used for the project
# Library documentation is available here https://icrawler.readthedocs.io/en/latest/builtin.html
# google engine does not work at this moment (3rd Sep 2022) :(

from icrawler.builtin import GoogleImageCrawler

def google_image_downloader():
    filters = dict(
        type = 'photo', # photo, face, clipart, etc.
        color = 'blackandwhite',
        size = 'large', # large, icon, 1024x1024
        license = 'noncommercial',
        date = 'pastweek' # date when image was published 
    )
    # create an object of the class
    crawler =  GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.session.verify = False
    crawler.crawl(
        keyword='mr.robot',
        max_num=5,
        filters = filters,
        file_idx_offset='auto'
        )
    
def main():
    google_image_downloader()

if __name__ == '__main__':
    main()