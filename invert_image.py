from PIL import Image, ImageOps
import sys

def invert_image(input_path, output_path):
    try:
        image = Image.open(input_path)
        inverted_image = ImageOps.invert(image.convert('RGB'))
        inverted_image.save(output_path)
        print(f'Inverted image saved to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python invert_image.py <input_image> <output_image>')
    else:
        invert_image(sys.argv[1], sys.argv[2])
