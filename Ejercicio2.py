#-*- encoding: utf-8 -*-
#Importamos la librería para integrar SciPy (mejor sólo un sub-módulo que Scipy entero)
import scipy.integrate as integ

#Creamos dos variables para generar la respuesta y el margen de error
respuesta, error = integ.quad(lambda x: x**2, 0, 2)

#Imprimimos ambos resultados!
print respuesta
print error

#Para integrales dobles, triples, o más grandes aún, tenemos también esta serie de funciones:
'''
integ.dblquad()
integ.tplquad()
integ.nquad()
'''