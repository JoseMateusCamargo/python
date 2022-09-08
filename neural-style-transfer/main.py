# Neural Style Transfer é um processo que usa redes neurais para aplicar o estilo artístico de uma imagem para outra.

import tensorflow_hub as hub  # pip install --upgrade tensorflow-hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

# Fast arbitrary image style transfer.
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


# Preprocess Image and Load
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


# Visualize Output
content_image = load_image('img/profile.png')
style_image = load_image('img/salvador_dali.jpg')

content_image.shape

plt.imshow(np.squeeze(style_image))
plt.show()

# Stylize Image
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
plt.imshow(np.squeeze(stylized_image))
plt.show()

cv2.imwrite('generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_BGR2RGB))
