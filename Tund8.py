import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,1) #-10,-9,-8....10 linspace(-10,10,100)
#punktide arv
y=2*x**2-4+5
plt.figure(facecolor="yellow")
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("y=2*x**2-4*x+5")
plt.title("Graafik")
plt.grid()
plt.savefig("graafik.png")
plt.show()

x=[1, 2 ,3 ,4 , 5]
y=[10, 20, 25, 30, 35]

# plt.plot(x, y, linestyle="--", marker="D",markersize=10, color="red")
# plt.xlabel("X-telg")
# plt.ylabel("Y-telg")
# plt.title("Lihtne graafik")
# plt.show()

# plt.scatter(x,y,color="lightblue", label="Punktidest diagramm")
# plt.show()

# plt.bar(x,y,color="orange", label="Tulpidiagramm")
# plt.legend()
# plt.show()

plt.pie(x,y)
plt.show()

plt.hist(x,y,color="green", label="Histodiagramm")
plt.show()
