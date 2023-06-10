# Numplate Detection

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![PyTesseract](https://img.shields.io/badge/PyTesseract-4.1%2B-yellow)
![Django](https://img.shields.io/badge/Django-3.0%2B-green)

This project utilizes Python, TensorFlow, PyTesseract, and Django to create a web interface for number plate detection.

## Installation

1. clone the repository, run the following command in your terminal:

    ```shell
        git clone https://github.com/madhavreddy509/smartPlateOCR
2. Create a virtual environment and activate it:

    ```shell
        python -m venv env
        source env/bin/activate # for Linux/macOS
        env\Scripts\activate # for Windows

3. Install the required dependencies:

    ```shell
        pip install -r requirements.txt


4. Download the MobileNetV2 model weights and place them in the `models` directory.

## Usage

1. Start the Django development server:
    
    ```shell
        python manage.py runserver
        

2. Access the web interface by navigating to `http://localhost:8000` in your web browser.

3. Upload an image containing a number plate.

4. The application will detect and extract the number plate from the image, displaying the result on the web interface.

## Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
- ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
- ![PyTesseract](https://img.shields.io/badge/PyTesseract-4.1%2B-yellow)
- ![Django](https://img.shields.io/badge/Django-3.0%2B-green)

## Acknowledgements

- [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381) by Mark Sandler, Andrew Howard, et al.
- [PyTesseract](https://github.com/madmaze/pytesseract): Python wrapper for Tesseract OCR.
- [Django Documentation](https://docs.djangoproject.com/): Official documentation for Django.

## Output 


 <img src="Screenshot (121).png" align="center" />

form to upload a image



  <img src="Screenshot (120).png" align="center" />
form to upload a image

## Note 

- the model is trained on small dataset under 300 images , 

- to incease the bounding box prediction capacity train model 

- under vast inputs to extract the correct output text









