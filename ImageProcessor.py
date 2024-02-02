from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def imagePreprocess():
    image_path = "cloth_masking/input/shirt.jpg"
    image = Image.open(image_path)

    # Check if the image mode is RGBA
    if image.mode == 'RGBA':
        # Convert RGBA to RGB
        image = image.convert('RGB')

    import numpy as np

    image_resized = image.resize((768, 1024))
    image_array = np.array(image_resized)

    updated_image_path = "datasets/test/cloth/shirt.jpg"
    updated_image = Image.fromarray(image_array.astype(np.uint8))
    updated_image.save(updated_image_path)

def imageMaskPreprocess() :
  image_path  = "datasets/test/cloth-mask/shirt.jpg"
  image = Image.open(image_path)
  import numpy as np
  image_resized = image.resize((768, 1024))
  image_array = np.array(image_resized)
  updated_image_path = "datasets/test/cloth-mask/shirt.jpg"
  updated_image = Image.fromarray(image_array.astype(np.uint8))
  updated_image.save(updated_image_path)


def addImages(): 
  imageMaskPreprocess()
  imagePreprocess()


addImages()