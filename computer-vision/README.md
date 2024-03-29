<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Computer Vision

#### _Let's Code!_

- Detecção de rostos (_Face Detection_)
    - Utilizando `haarcascade`.
    - Contador de rostos utilizando `dlib`.
- Medindo objetos (_Object size measurement_)
    - [Medindo o tamanho de objetos em uma imagem com `OpenCV`.](https://github.com/JoseMateusCamargo/python/tree/main/computer-vision/object-size-measurement)
- **OpenCV** exemplos de como usar
    - Iniciando camera `OpenCV` frame.
    - [Contorno OpenCV usando `APPROX_NONE`.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/cv2-master/contour_detection_approx_none.py)
    - [Contorno OpenCV usando `APPROX_SIMPLE`.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/cv2-master/contour_detection_approx_simple.py)
    - Detecção de cores usando `HSV`.
    - [Script simples para abrir imagem, acessar pixel, fazer retângulo e definir texto na imagem.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/cv2-master/cv2_make_rectangle.py)
    - [Exemplo de círculo HSV para RGB.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/cv2-master/circle_HSV2RGB.py)

---

## Detecção de rostos (_Face Detection_)

**_Face Detection_ utilizando `haarcascade`.**

A detecção de rosto usando cascatas Haar é uma abordagem baseada em aprendizado de máquina em que uma função em
cascata é treinada com um conjunto de dados de entrada. O OpenCV já contém muitos classificadores pré-treinados
para rosto, olhos, sorrisos, etc.

* [Face Detection com `haarcascade` em 17 linhas.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/face-detection-haarcascade/haarcascade_face_detection.py)
* [Face Detection com `haarcascade` aplicado em uma imagem.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/face-detection-haarcascade/haarcascade_face_detection_img.py)

**_Face Detection_ condator de rostos utilizando `dlib`.**

[Dlib](http://dlib.net/) tem crescido, principalmente por ter a capacidade de unir Machine Learning ou Aprendizado de
Máquina e Visão Computacional, sendo muito mais simples e intuitivo construir classificadores e
assim detectar o objeto ou pessoa em diferentes imagens e vídeos

* [Condador de rostos utilizando `dlib`.](https://github.com/JoseMateusCamargo/python/blob/master/computer-vision/face-detection-haarcascade/haarcascade_face_detection.py)

---

## OpenCV exemplos de como usar

**Iniciando camera `OpenCV` frame**

```python
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):  # q -> to close
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

**Detecção de cores usando `HSV`**

```python
import cv2
import numpy as np


def circle_HSV2RGB(frame, radius):
    img = np.ones((frame, frame, 3), np.float32)
    ll, cc = np.indices((frame, frame))
    circle = (ll - frame / 2) ** 2 + (cc - frame / 2) ** 2

    arc_tan_ll = (ll.astype(np.float32) - frame / 2)
    arc_tan_cc = (cc.astype(np.float32) - frame / 2)

    hue = np.rad2deg(np.arctan2(arc_tan_ll, arc_tan_cc))
    saturation = (circle.astype(np.float32)) / radius ** 2

    img[:, :, 0] = hue
    img[:, :, 1] = saturation

    img[circle > radius ** 2] = [0, 0, 0]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    cv2.imshow("CircleHSV2RGB", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


circle_HSV2RGB(400, 180)
```