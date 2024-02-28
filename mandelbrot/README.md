# Mandelbrot

The Mandelbrot set is a set of complex numbers defined by a simple iterative algorithm.


```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

may need
```bash
sudo apt install libxcb-cursor0
```


#

another ver

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install numpy matplotlib
```

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

width, height = 800, 800
image = np.zeros((height, width))

for x in range(width):
    for y in range(height):
        c = complex(x - width/2, y - height/2) / width * 3
        image[y, x] = mandelbrot(c, 50)

plt.imshow(image, cmap='rainbow', interpolation='none')
plt.show()
```