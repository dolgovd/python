# Program allows to convert a file wtih code into a png file
# pytoimage library is used

import os
from pytoimage import PyImage
from pathlib import Path

def pycode_to_img(file_path = 'main.py'):
    #Get path to a file
    path = Path(file_path)

    #Make a check if file exists
    if not path.is_file():
        return 'Sorry, file is not found'

    #Creare an object of PyImage class
    code = PyImage(file_path, background=(0, 0, 0))

    #Create a dictionary with palette
    palette = {
        'line': (105, 105, 105),
        'normal': (255, 255, 255)
    }

    #Apply settings
    code.set_color_palette(palette=palette)

    #Generate image
    code.generate_image()
    img_name = f'{os.path.splitext(file_path)[0]}.png'
    code.save_image(img_name)
    return f'{img_name} saved successfully'


def main():
    pycode_to_img()
    file_path = input('Please select a file: ')
    print(pycode_to_img(file_path = file_path))


if __name__ == '__main__':
    main()