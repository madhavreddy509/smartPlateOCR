import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pytesseract as pt

model = tf.keras.models.load_model('./static/models2/object_detection.h5')

def object_detection(path,filename):
    # read image
    image = load_img(path) # PIL object
    image = np.array(image,dtype=np.uint8) # 8 bit array (0,255)
    image1 = load_img(path,target_size=(224,224))
    # data preprocessing
    image_arr_224 = img_to_array(image1)/255.0  # convert into array and get the normalized output
    h,w,d = image.shape
    test_arr = image_arr_224.reshape(1,224,224,3)
    # make predictions
    coords = model.predict(test_arr)
    # denormalize the values
    denorm = np.array([w,w,h,h])
    coords = coords * denorm
    coords = coords.astype(np.int32)
    # draw bounding on top the image
    xmin, xmax,ymin,ymax = coords[0]
    pt1 =(xmin,ymin)
    pt2 =(xmax,ymax)
    print(pt1, pt2)
    cv2.rectangle(image,pt1,pt2,(0,255,0),3)
    # convert into bgr
    image_bgr = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('./static/predict/{}'.format(filename),image_bgr)
    return coords

def OCR(path,filename):
    img = np.array(load_img(path))
    cods = object_detection(path,filename)
    xmin ,xmax,ymin,ymax = cods[0]
    roi = img[ymin:ymax,xmin:xmax]
    roi_bgr = cv2.cvtColor(roi,cv2.COLOR_RGB2BGR)
    cv2.imwrite('./static/roi/{}'.format(filename),roi_bgr)
    text = pt.image_to_string(roi)
    print("-------------------------------=====================")
    print("text",text)
    return text