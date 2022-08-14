# pytoimage library is used

from pytoimage import PyImage
from pathlib import Path

def pycode_to_img(file_path = 'main.py'):
    #Get path to a file
    path = Path(file_path)

    #Make a check if file exists
    if not path.is_file():
        return 'Sorry, file is not found :/'

    #Creare an object of PyImage class
    code = PyImage(file_path, background=(255, 255, 255))

    #Create a dictionary with palette
    palette = {
        'line': (255, 0, 255),
        'normal': (0, 0, 0)
    }

    #Apply settings
    code.set_color_palette(palette=palette)

    #Generate image
    code.generate_image()
    img_name = f'{file_path.split(".")[0].png}'
    code.save_image(img_name)
    return f'{img_name} saved successfully'


def main():
    pycode_to_img()
    file_path = input('Please select a file: ')
    print(pycode_to_img(file_path=file_path))


if __name__ == '__name__':
    main()