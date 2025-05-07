import matplotlib
import matplotlib.pyplot as plt

print (matplotlib.__version__)
x=[1,2,3,4,5]	
y=[2,4,6,8,10]
nombre_linea="linea1"
plt.plot(x,y,label=nombre_linea,color="blue")

#agregar parametros
plt.title("primer grafico")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.legend()
plt.show()