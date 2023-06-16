# Nombre: Geometria.py

# Descripcion: Script para el cálculo y graficación de propiedades de la sección transversal de un canal trapezoidal compuesto.
# Requerimientos: Python 3.10

## INICIO SCRIPT

## Importar librerias
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Ingresar información geometrica de la sección
b=10  #main channel width, b(m)
bv=20 #entire channel width, b(m)
ym=3  #main channel depth, ym(m)
z1=1  #main channel section slope
z2=0.5 #entire channel section slope
yi=5  #total channel depth, y(m)

T1=b+2*ym*z1  #Ancho del cauce principal T(m)
T2=bv+2*(yi-ym)*z2   #Ancho total del canal T(m)

# Gráfica de la sección transversal compuesta
Gx=[0,z2*(yi-ym),z2*(yi-ym)+(bv-T1)/2,z2*(yi-ym)+(bv-T1)/2+ym*z1,z2*(yi-ym)+(bv-T1)/2+ym*z1+b,z2*(yi-ym)+(bv-T1)/2+T1,T2-z2*(yi-ym),T2]
Gy=[yi,ym,ym,0,0,ym, ym,yi]

plt.figure(figsize=(15,12))
plt.subplot(511)
plt.plot(Gx,Gy,'b')
plt.grid(True)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('Channel Section')

# Cálculo del área hidráulica
def Ar1(b, ym, z1): return (b * ym) + ((ym ** 2) * z1)
def Ar2(b, bv, ym, z1, z2, yi): return ((b * ym) + ((ym ** 2) * z1))+(bv*(yi-ym)+((yi-ym)**2)*z2)

y1 = np.arange(0.0, ym + 0.01, 0.01)
y2 = np.arange(ym, yi + 0.01, 0.01)
Area1 = Ar1(b, y1, z1)
Area2 = Ar2(b, bv, ym, z1, z2, y2)

# Gráfica del área hidráulica
plt.subplot(513)
plt.plot(Area1,y1,'r')
plt.plot(Area2,y2,'r')
plt.xlabel('Area, $(m^2)$')
plt.ylabel('Depth, y(m)')
plt.title('Area of a Coumpund Channel')
plt.grid(True)

# Cálculo del radio hidráulico
def Pm1(b, ym, z1): return b+2*((ym**2+(ym*z1))**0.5)
def Pm2(b,bv,yi,ym,z1,z2,T1): return (b+2*((ym**2+(ym*z1))**0.5))+((bv-T1)+2*(((yi-ym)**2+((yi-ym)*z2))**0.5))

Rh1 = Ar1(b, y1, z1)/Pm1(b,y1,z1)
Rh2 = Ar2(b, bv, ym, z1, z2, y2)/Pm2(b, bv, y2,ym, z1, z2, T1)

# Gráfica del radio hidráulico
plt.subplot(515)
plt.plot(Rh1,y1,'r')
plt.plot(Rh2,y2,'r')
plt.xlabel('Hydraulic radio, (m)')
plt.ylabel('Depth, y(m)')
plt.title('Hydraulic radio of a Coumpund Channel')
plt.grid(True)