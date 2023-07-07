# Nombre: VelocutyProfile.py

# Descripcion: Script para el cálculo y graficación del perfil de velocidades en un canal trapezoidal.
# Requerimientos: Python 3.10

## INICIO SCRIPT

## Importar librerias
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Ingresar información geometrica de la sección

b=0.5       # ancho base del canal, b(m)
y=2.0         # profundidad de flujo, y(m)
z=0.25      # pendiente de los taludes laterales
Q=1         # flujo volumétrico, Q(m3/s)
ks=0.36     # rugosidad absoluta, ks(mm)
n=0.013     # coeficientes de rugosidad de Manning
ρ=998       # densidad de liquido, ρ(kg/m3)
ν=1.1e-6    # viscosidad cinemática, ν(m2/s)

# Cálculo de características geométricas

A=b*y+z*y**2                    # Área de flujo
P=b+2*np.sqrt(y**2+(z*y)**2)    # Perímetro mojado
Rh=A/P                          # Radio hidráulico
T=b+2*y*z                       # Ancho del cauce principal T(m)

# Cálculo de velocidad media, Vm (m/s)
Vm=Q/A

# Cálculo de condiciones de flujo
Vc=Vm*n*(9.806**0.5)/(Rh**(1/6))   # Velocidad de corte, V* (m/s)
Rer=Vc*ks/ν/1000                  # Reynolds asociado a la rugosidad

# Gráfica de la sección transversal
Gx=[0,y*z,y*z+b,T]
Gy=[y,0,0,y]

plt.figure(figsize=(10,12))
plt.subplot(211)
plt.plot(Gx,Gy,'b')
plt.grid(True)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('Gráfica de la sección transversal')

# Gráfica del perfil de velocidades
h=np.linspace(0.1,y,100)   # lista con valores de altura en el flujo 'h'

# evaluación de la condición de flujo y definición de la función
if Rer<5:
    cond="hidráulicamente lisa."
    def v(h): return Vc*np.log(9.025*Vc*h/ν)/0.4
else:
    if Rer<70:
        cond="hidráulicamente en transición."
        def v(h): return Vc*np.log((h*1000/ks)/((1/(9.025*Rer))+(np.exp(-10.78/Rer)/30)))/0.4
    else:
        cond="hidráulicamente rugosa."
        def v(h): return Vc*np.log(30000*h/ks)/0.4

print ("El número de reynolds asociado a la rugosidad del flujo es de "+ str(Rer)+" por lo tanto, la superficie se clasifica como "+cond)

plt.subplot(212)
plt.plot(v(h),h,'r')
plt.grid(True)
plt.xlabel('Velocidad, v(m/s)')
plt.ylabel('h(m)')
plt.title('Perfil de velocidades')
plt.show()