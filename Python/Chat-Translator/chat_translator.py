# Program allows to translate messages automatically
# googletrans 3.1.0 library is used

from googletrans import Translator

def text_translator(text='Hello', src='en', dest='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text
    except Exception as ex:
        return ex

def main():
    print(text_translator(text='Hello', src='en', dest='fr'))

if __name__ == '__main__':
    main()
