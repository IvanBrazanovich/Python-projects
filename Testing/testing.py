  
import numpy as np
           import matplotlib.pyplot as plt

  
def sinc(x):
    return np.sin(x) / x

def d_sinc(x):
    "derivative of sinc-function"
    return np.cos(x)/x - np.sin(x)/x**2
# evaluate functions at 1000 points evenly spaced in [-15, 15]
x = np.linspace(-15, 15, 1000)
f = sinc(x)
df = d_sinc(x)
# plot the sinc-function and its derivative
fig, ax = plt.subplots()
ax.plot(x, f, color="red", label=r"$sinc(x)$")
ax.plot(x, df, color="blue", ls="--", label=r"$\frac{d(sinc(x))}{dx}$")


ax.set_title("Example Notebook Plot")
ax.set_xlabel(r"$x$ [radians]")

ax.grid(True)
ax.legend();

plt.show()