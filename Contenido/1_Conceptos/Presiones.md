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
Como se describió anteriormente, para canales con pendiente baja se puede considerar el valor de $\cos \theta \approx 1$. Sin embargo, cuando se tiene curvatura en el fondo existen efectos por la aceleración normal al flujo o las fuerzas centrífugas. A partir de la ecuación de euler se puede demostrar que el gradiente de presiones en la dirección normal depende de la aceleración y esta aceleración puede aproximarse a $a_{n}=v^{2}/r$, donde $v$ es la velocidad de flujo y $r$ el radio de curvatura.  Este flujo curvilíneo puede ser cóncavo o convexo. En el primero, las fuerzas centrífugas apuntan hacia abajo haciendo que la presión en un punto sea mayor que la hidrostática. Caso contrario ocurre con las curvas convexas, donde las fuerzas centrífugas o la aceleración apunta hacia arriba, disminuyendo el efecto de la gravedad y disminuyendo la presión con respecto a la hidrostática. 

Si se asume que la **aceleración** es constante, la distribución vertical de presiones puede expresarse en función de la aceleración **a<sub>n</sub>** y del radio de curvatura **r**:

P=\gamma h (1+\frac{a_{n}}{g})\approx \gamma h (1+\frac{v^{2}}{gr})\rightarrow {\color{DarkBlue} 'C. Cóncavas'}
P=\gamma h (1-\frac{a_{n}}{g})\approx \gamma h (1-\frac{v^{2}}{gr})\rightarrow {\color{DarkBlue} 'C. Convexas'}

Si se considera la variación de la **aceleración, a<sub>n</sub>**, la presión dependerá de la condición del perfil de velocidades **v<sub>h</sub>** y se puede generalizar como:

$$P=\gamma h\pm \rho \int \frac{v_{h}^{2}}{r}$$

### Presiones en canal con pendiente alta

En el caso de los canales con pendiente alta (S<sub>o</sub> > 0.1), es necesario considerar el ángulo de inclinación **θ** al momento de realizar el análisis dinámico. Así mismo, si se quiere expresar la altura de presión en términos de la profundidad de flujo **y**, se deberá considerar que **y=d cos θ**. Por lo tanto, la distribución vertical de presiones puede expresarse como:

$$P=\gamma h\cos\theta = \gamma y\cos^{2}\theta$$

Si el canal con pendiente alta tiene un perfil longitudinal con curvatura apreciable, la presión debe ser también corregida por el efecto de la curvatura o fuerzas centrífugas.

___
### Preguntas
1. ¿Describa que es un flujo paralelo?
2. ¿Cómo se debe considerar la distribución de presiones en un flujo rápidamente variado?
3. Determine y grafique la distribución de presiones de un tramo de canal con perfil curvo convexo, que transporta aguas negras (DR=1.03) a un ritmo de 7 m<sup>3</sup>/s. La sección transversal del canal es rectangular con un ancho de 3 metros y la profundidad de flujo es de 2 metros. El radio de curvatura hasta el fondo del canal es de 20 metros.  Compare el resultado con la distribución de presiones hidrostática.
4. Estime la fuerza debida a la presión en la sección transversal del punto anterior.         
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
| 2023.07 | Inclusión de conceptos, esquemas y ejemplos.                   | [juanrodace](https://github.com/juanrodace) |  2.0  |

| [:arrow_backward:Anterior](Velocidades.md) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/juanrodace/J.HSLB/discussions) | [Siguiente:arrow_forward:](../2_Energia/Energia.md) |
|--------------------------------------------|-----------------------------------|----------------------------------------------------------------------|-----------------------------------------------------|

_J.HSLB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../License.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [juanrodace](https://github.com/juanrodace) en GitHub._