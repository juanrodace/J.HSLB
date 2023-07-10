## Distribución de presiones <a href="../.Slides/HSLB-4-Velocidades-Presiones.pdf" target="_blank"><img src="../../.icons/Slides_Icon.png" width="25" border="0" /></a>

Keywords: `Hydraulics` `Open channel flow` `Pressuure distribution` `Uniform flow`

<div align="center">
<img alt="J.HRAS" src="Graph/Arroyo_LasAnimas.jpg" width="100%">
</div>

> Arroyo Las Ánimas, Cesar, Col. _Fuente propia_

En canales o conductos con flujo a superficie libre es común asumir la distribución vertical de presiones como hidrostática, dependiendo únicamente del peso del líquido o en términos prácticos de la densidad y la profundidad del flujo. Sin embargo, es importante conocer que existen factores que pueden cambiar dicha distribución hidrostática, como es el caso de la curvatura del fondo o los canales alta pendiente. Considerar adecuadamente la presión es importante al momento de utilizar la ecuación fundamental del _momentum_.

### Presiones en canal con pendiente baja y fondo recto 
En el caso de los canales con pendiente baja (S<sub>o</sub> < 0.1), puede considerarse que el valor del $\cos \theta$ se aproxima a $\approx 1$. Así mismo, al no tener curvatura en el fondo, no se tendrán efectos por la aceleración normal al flujo o fuerzas centrífugas. Por lo tanto, para un flujo **paralelo** es válido aplicar la ley hidrostática a la distribución vertical de presiones y su expresión se puede considerar como:

$$P=\gamma h$$

### Presiones en canal con pendiente baja y fondo curvo 
Como se describió anteriormente, para canales con pendiente baja se puede considerar el valor de $\cos \theta \approx 1$. Sin embargo, cuando se tiene curvatura en el fondo existen efectos por la aceleración normal al flujo o las fuerzas centrífugas. A partir de la ecuación de euler




___
### Preguntas
1. ¿Qué es la hipótesis de fluido ideal?
2. ¿Qué es una sección de control?
2. Determine y grafique el perfil de velocidades de un canal muy ancho (b = 600 m) con una profundidad media de y = 10 m y un caudal de 5000 $\frac{m^{3}}{s}$. Considere una densidad relativa de 1.05, una viscosidad de 1.15e<sup>-6</sup> $\frac{m^{2}}{s}$, una rugosidad absoluta del fondo de 14 mm y un coeficiente de Manning n=0.04.
3. Estime los coeficientes de Coriolis y Boussinesq para el flujo presentado en el ejemplo 2.
___

### Referencias
- The Hydraulics of Channel Flow: An Introduction. Chanson H. 2nd Ed.,Elsevier Butterworth-Heinemann. 2004.
- Open Channel Hydraulics. Chow, Ven Te. 2nd Ed., Blackburn Press. 2009.
- Open Channel Flow. Chaudry, M. H. 2ed., Springer, 2008.
- Open Channel Flow. Osman Akan, A. Elsevier Ltd., 2006.
- Introducción a la hidráulica de canales. Duarte A. Carlos A. 4a Ed., Editorial Universidad Nacional de Colombia. 2016.
- Flow in open channels. Subramanya K. 3th Ed., Tata McGraw-Hill Publishing. 2009.
- Hidráulica de canales. Sotelo A., Gilberto. UNAM México, Facultad de Ingeniería. 2002.

### Control de versiones

| Versión | Descripción                                                    |                    Autor                    | Horas |
|:-------:|:---------------------------------------------------------------|:-------------------------------------------:|:-----:|
| 2023.07 | Versión inicial, definición de estructura general y contenido. | [juanrodace](https://github.com/juanrodace) |  1.0  |
| 2023.07 | Inclusión de conceptos, esquemas y ejemplos.                   | [juanrodace](https://github.com/juanrodace) |  1.0  |

| [:arrow_backward:Anterior](Clasificacion.md) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/juanrodace/J.HSLB/discussions) | [Siguiente:arrow_forward:](Presiones.md) |
|----------------------------------------------|-----------------------------------|----------------------------------------------------------------------|------------------------------------------|

_J.HSLB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../License.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._


[^1]: Introduction to Fluid Mechanics. Fox and McDonald's. 8th Ed., Jhon Wilwy & Sons, Inc. 2011.