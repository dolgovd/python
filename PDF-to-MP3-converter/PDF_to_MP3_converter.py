# Program will allow to get a PDF file as input and convert it to MP3
# pdfplumber, gTTS, art libraries are used
# Link - https://github.com/jsvine/pdfplumber

from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

# Function accepts 2 parameters: path to a PDF file and used language
def pdf_to_mp3(file_path = 'Test.pdf', language = 'en'):
    
    # Validate is file esxist and it is a PDF
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing ...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            # read text on all pages
            pages = [page.extract_text() for page in pdf.pages]

            # merge all pages together
            text = ''.join(pages)

            # remove EOL symbols. It is needed for getting the target text as one line and eliminating pauses in MP3 file
            text = text.replace('\n', '')

            # generate output MP3 file with gTTS library
            my_audio = gTTS(text=text, lang=language, slow=False)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 has been succesfully created'
    else:
        return 'File does not exist! Please make sure the path and correct'

def main():
    tprint('PDF -> MP3', font='bulbhead')
    file_path = input('\nEnter path to the target PDF file: ')
    language = input('\nEnter language "en" or "ru": ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()

