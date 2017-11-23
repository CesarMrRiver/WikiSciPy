
#Importamos la librería
import scipy.linalg as ln
import numpy as np

#Creamos una matriz aleatoria de 3x3
ran = np.random.rand(3,3)

#Imprimimos la matriz generada
print ran

#Imprimimos la inversa de la matriz original
print "\n"
print ln.inv(ran)

#Imprimimos el seno de la matriz original
print "\n"
print ln.sinm(ran)

#Imprimimos el coseno
print "\n"
print ln.cosm(ran)

#Imprimimos la tangente
print "\n"
print ln.tanm(ran)

#Imprimimos el logaritmo
print "\n"
print ln.logm(ran)

