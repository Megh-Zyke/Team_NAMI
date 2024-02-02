
# Virtual Try On by Team Nami

## Overview

This repository contains the implementation of VITON-HD, a high-resolution virtual try-on model that enables realistic and high-quality virtual clothing try-on. It is based on the research paper [VITON-HD: High-Resolution Virtual Try-On via Misalignment-Aware Normalization](https://github.com/shadow2496/VITON-HD).

![Example Image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/92ffb4d9-ce67-4ad0-9319-c573b0f0dbd1)

![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/ac387022-208b-43ad-a3e1-2b91df82f86f)


## Table of Contents

- [Getting Started](#getting-started)
  - [Clone Repository](#clone-repository)
  - [Install Dependencies](#install-dependencies)
- [Dataset](#dataset)
- [Usage](#usage)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Clone Repository

```bash
git clone https://github.com/shadow2496/VITON-HD.git
cd ./HR-VITON/
```

### Install Dependencies

```bash
conda create -n {env_name} python=3.8
conda activate {env_name}
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia
pip install opencv-python torchgeometry Pillow tqdm tensorboardX scikit-image scipy
```

## Dataset

We use the dataset from [VITON-HD: High-Resolution Virtual Try-On via Misalignment-Aware Normalization](https://github.com/shadow2496/VITON-HD).

To download the dataset, please check the [official repository](https://github.com/shadow2496/VITON-HD). Ensure that you have downloaded it into the `./data` directory.

## Usage

### Stuck on what you want to wear ? Well not anymore
  ### Once you find the dress you like, finding out how you look in that dress is just a click away!
Upload the photo of the dress you want to try on and see how one might look based on the pre processed images given below

## Techniques used

  * ### Body part Segmentation
       Body segmentation using deep learning involves training neural networks to identify and delineate human body parts in images or videos. Utilizing architectures like U-Net or Mask R-CNN, these models learn to precisely segment body regions, enabling applications in virtual try-on, pose estimation, and human-computer interaction.
Feel free to customize this template based on the specific details of your project and your preferences. Include additional sections if needed to provide more information about your project.
![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/64f071c2-b91b-42eb-b78f-ca265bd502fa)

* ### Image masking
  In Python, binary image masks are created by thresholding an image, assigning pixel values to either 0 or 1. The OpenCV library is commonly used for this task. For instance, using the `cv2.threshold` function, pixels above a certain threshold become white (1), and those below become black (0). Binary masks are fundamental in image processing, allowing the selective manipulation of specific regions, such as object segmentation or background removal.

  ![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/119fa7aa-3fbc-4bd9-b4e1-ab904b40c804)

  ![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/5cafd5bd-3bc1-4d4b-87e5-92c0eb6df460)



* ### Image Distortions
  In Python, image distortions using binary masks involve applying spatial transformations selectively to regions defined by the mask. The `cv2.warpAffine` or `cv2.warpPerspective` functions in OpenCV allow affine or perspective transformations based on binary masks. By specifying regions to distort, such as rotations or translations, these masks enable precise and localized distortions. This technique is valuable for targeted image manipulations, such as warping specific areas while maintaining the integrity of the rest of the image.
  ![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/efd4b00e-2048-4cf5-8ca9-8f799e1886bd)
![image](https://github.com/Megh-Zyke/Team_NAMI/assets/97515984/2b53e523-84ba-4be9-98e8-23bc92943e27)
