import numpy as np

a = np.array([1,2,3,4,5]) # np.array() convierte datos (listas u otros) en un arreglo de NumPy (ndarray).
print("Array a")
print(a.shape)
print(a)

print("_____________________________________________________________________________________________________________")

b = np.array([[1,2],[3,4]])
print("Array b")
print(b.shape)
print(b)

print("_____________________________________________________________________________________________________________")
print("Array c")
c = np.array([[1,2],[3,4],[5,6]])
print(c.shape)
print(c)

print("_____________________________________________________________________________________________________________")
print("_____________________________________________________________________________________________________________")

#Indexación
print("Indexación")
print("a = " + str(a[0,]))
print("b = " + str(b[0,1]))
print("b = " + str(b[1,1]))
print("c = " + str(c[0,1]))

print("_____________________________________________________________________________________________________________")
print("_____________________________________________________________________________________________________________")

#Creación de arrays
print("Creación de arrays")
d = np.zeros((2,3))
print("Array d")
print(d.shape)
print(d)

e = np.ones((4,2))
print("Array e")
print(e.shape)
print(e)

f = np.full((2,2),9)
print("Array f")
print(f.shape)
print(f)

g = np.random.random((3,3))
print("Array g")
print(g.shape)
print(g)

print("_____________________________________________________________________________________________________________")
print("_____________________________________________________________________________________________________________")
#Promedios
print("Promedios")
print(np.mean(a))
print(np.mean(b))
print(np.mean(c))
print(np.mean(d))
print(np.mean(e))
print(np.mean(f))
print(np.mean(g))

print("____________________________________________________________ \n"
      "____________________________________________________________")