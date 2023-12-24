{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ee1932f",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install opencv-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab892ae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import urllib.request\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "image_url = \"https://d21zeai4l2a92w.cloudfront.net/wp-content/uploads/2023/01/iStock-1392612588-scaled.jpg\"\n",
    "image_path = \"C:\\\\Users\\\\divya\\\\OneDrive\\\\Desktop\\\\girl_image.jpg\"\n",
    "\n",
    "\n",
    "urllib.request.urlretrieve(image_url, image_path)\n",
    "\n",
    "\n",
    "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "\n",
    "\n",
    "img = cv2.imread(image_path)\n",
    "gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))\n",
    "\n",
    "\n",
    "for (x, y, w, h) in faces:\n",
    "    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)\n",
    "\n",
    "\n",
    "max_dimension = 500\n",
    "height, width, _ = img.shape\n",
    "if height > width:\n",
    "    new_height = max_dimension\n",
    "    new_width = int((max_dimension / height) * width)\n",
    "else:\n",
    "    new_width = max_dimension\n",
    "    new_height = int((max_dimension / width) * height)\n",
    "\n",
    "resized_img = cv2.resize(img, (new_width, new_height))\n",
    "\n",
    "\n",
    "cv2.imshow('Face Detection (Resized)', resized_img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb285a51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
