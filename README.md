
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

[Provide instructions on how to use or run your project.]

## References

- [VITON-HD Paper](https://github.com/shadow2496/VITON-HD)
- [Original Repository](https://github.com/shadow2496/VITON-HD)

## Contributing

[Include information about how others can contribute to your project.]

## License

[Specify the license under which your project is distributed.]

---

Feel free to customize this template based on the specific details of your project and your preferences. Include additional sections if needed to provide more information about your project.
