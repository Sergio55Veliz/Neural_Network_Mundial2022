# Neural_Network_Mundial2022

Esta es una práctica de uso de redes neuronales con Tensorflow y Keras.

En este proyecto se hizo uso de *web scrapping* para la obtención del dataset y *TensorFlow* para la creación de redes neuronales.

<br/>
<hr/> 

## DataSet
El dataset fue extraido en del siguiente link: https://www.losmundialesdefutbol.com/selecciones.php

En este link se nos presenta cada uno de los paises que en algún momento jugaron en un mundial, por lo que incluso podríamos toparnos con paises que actualmente no existen, como la Alemania oriental.

De esta fuente, hay dos secciones de la que hemos sacado información:
  - Mundial por mundial: Información por orden cronológico de la participación del país en el mundial por año. La información aquí es un mero resumen, no da información especifica sobre un determinado partido, para acceder a ello debemos de revisar la secciónd e Resultados.
  - Resultados: Aquí nos encontramos con los partidos que ha jugado dicho país. clasificada por mundial. De aquí extraemos la información de:
    - Nombre de equipo contrario
    - Fecha (para identificar el año del mundial)
    - Goles de cada equipo. Aquí hay que resaltar un pequeño detalle, la página si da información sobre los goles de tiempo extra (en caso de haber quedado empate), pero en este proyecto eso lo hemos ignorado y solo consideramos lo desarrollado dentro de los 90 minutos, no lo que se desarrlló en el tiempo extra.


## Web Scrapping

#### **XPath**
Para explorar en la página y verificar que nuestro xpath sea el correcto se usó una extensión que permitía el ingreso del xpath y resaltaba lo que el xpath indicaba. Si manejas Chrome, te recomiento usar **XPath Helper Wizard** https://chrome.google.com/webstore/detail/xpath-helper-wizard/jadhpggafkbmpdpmpgigopmodldgfcki?hl=es


#### **Consideraciones** que tienes que tener para usar la librería de **Selenium**:

  - En este proyecto se trabajó específicamente con el driver de Chrom de Selenium, si deseas trabajar con algún otro navegador te recomiendo revisar la lista de drivers en el siguiente link -> https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference

  - El driver de selenium para chrome se puede descargar en -> https://chromedriver.chromium.org/downloads

  - Si quieres revisar opciones para otros navegadores revisar -> https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference

  - Antes de descargar el driver, revisar la version de tu navegador
    
    La version de Chrome la puedes ver en -> chrome://settings/help
    
    En mi caso, mi version de Chrome es la 107.

<br/>
<hr/> 

## Modelo de IA
Nuestra red neuronal creada es una fully-connected y va a servir para clasificar, si el partido fue ganado por el equipo de "izquierda" o el de la "derecha" o hubo un "empate". Por lo tanto, con esto sabemos que deben de haber 3 neuronas en la capa de salida. Además, como la red debe de hacer una clasificación entre más de 2 opciones, la función de activación de la capa de salida es la "softmax".



