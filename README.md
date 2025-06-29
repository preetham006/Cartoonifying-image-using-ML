# Cartoonifying Images Using Machine Learning

This repository contains a Python application that transforms regular images into cartoon-style images using image processing techniques implemented with OpenCV and a user-friendly GUI built with Tkinter. The cartoonification process applies edge detection and color smoothing to achieve a stylized, cartoon-like effect.

Repository: [https://github.com/preetham006/Image-upscaling-using-Generative-Adversarial-Network](https://github.com/preetham006/Image-upscaling-using-Generative-Adversarial-Network)

## Project Overview

The Cartoonifier application uses OpenCV's image processing capabilities to convert images into a cartoon-like style. It employs **adaptive thresholding** for edge detection and **bilateral filtering** for color smoothing, creating a stylized effect. The Tkinter-based GUI allows users to upload images, apply the cartoon effect, and save the results, with an additional feature to randomly select images from a directory.

## Features

- **Cartoon Effect**: Applies edge detection and color smoothing to create a cartoon-like appearance.
- **Interactive GUI**: Built with Tkinter for easy image uploading, processing, and saving.
- **Random Image Selection**: Allows users to select a random image from a directory for cartoonification.
- **Cross-Platform**: Runs on any system with Python, OpenCV, and Tkinter installed.
- **Customizable**: Easily extendable for additional image processing effects.

## Installation

### Prerequisites

- Python 3.8+
- OpenCV (`opencv-python`)
- Pillow (`Pillow`)
- Tkinter (included with standard Python installations)
- NumPy (dependency for OpenCV)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/preetham006/Image-upscaling-using-Generative-Adversarial-Network.git
   cd Image-upscaling-using-Generative-Adversarial-Network
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install opencv-python pillow numpy
   ```

## Usage

### Running the Application

1. **Run the Script**:
   Execute the main script to launch the GUI:
   ```bash
   python cartoonifier.py
   ```

2. **Upload an Image**:
   - Click the "Upload an image" button to select an image file (`.jpg`, `.jpeg`, or `.png`).
   - The selected image will be displayed on the left side of the GUI.

3. **Apply Cartoon Effect**:
   - Click the "Cartoonify me" button to process the image.
   - The cartoonified image will appear on the right side of the GUI.

4. **Save the Result**:
   - Click the "Save to computer" button to save the cartoonified image to your desired location.

5. **Random Image Selection**:
   - (Optional) Modify the script to enable the random image selection feature by uncommenting the relevant function call or adding a button for it.

### Example

To cartoonify an image:
```bash
python cartoonifier.py
```
- Select an image (e.g., `sample.jpg`) via the GUI.
- Click "Cartoonify me" to process the image.
- Save the cartoonified image as `cartoon_sample.jpg`.

## Repository Structure

```
Image-upscaling-using-Generative-Adversarial-Network/
├── cartoonifier.py       # Main script with cartoonification logic and GUI
├── samples/              # Directory for sample input/output images (optional)
├── README.md             # This file
└── requirements.txt      # Dependencies
```

## Requirements

See the `requirements.txt` file for a complete list of dependencies:
```
opencv-python>=4.5.0
pillow>=9.0.0
numpy>=1.24.0
```

Install them using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the PEP 8 style guide and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using [OpenCV](https://opencv.org/) for image processing and [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- Inspired by cartoonification techniques described in various computer vision tutorials.

## Contact

For questions or suggestions, please open an issue on the [GitHub repository](https://github.com/preetham006/Image-upscaling-using-Generative-Adversarial-Network) or contact the maintainer at 
[preethamkarthik7386@gmail.com].

