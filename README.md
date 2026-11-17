# MIT-BIH ECG Analyzer

Proyecto académico para analizar señales de electrocardiograma (ECG) de la **MIT-BIH Arrhythmia Database** de PhysioNet. El objetivo es estudiar el efecto de filtros pasa altas y notch en la detección de complejos QRS y en la estimación de frecuencia cardíaca, comparando los resultados con las anotaciones de referencia de la base.

> Los datos de MIT-BIH son señales ECG, no archivos de audio.

## Objetivo del proyecto

El proyecto busca procesar registros ECG reales y evaluar:

- La detección de complejos QRS en señales originales y filtradas.
- La cantidad y ubicación de latidos detectados frente a las anotaciones de MIT-BIH.
- La frecuencia cardíaca estimada a partir de intervalos R–R y mediante autocorrelación.
- El efecto del filtro notch en una señal sin interferencia marcada en su frecuencia de rechazo, observando posibles oscilaciones alrededor de los complejos QRS.

La base MIT-BIH incluye 48 registros de dos canales, de aproximadamente media hora cada uno, muestreados a 360 Hz y acompañados por anotaciones revisadas por especialistas. Las anotaciones se utilizarán como referencia para evaluar la detección; no constituyen un diagnóstico generado por este programa.

## Estado actual

La versión inicial del repositorio es un **Hello, ECG**: descarga los archivos del registro `100`, lee la señal con WFDB e imprime información básica y grafica los primeros cinco segundos del primer canal. Las etapas de filtrado, detección de QRS, autocorrelación y comparación con anotaciones corresponden al desarrollo posterior del proyecto.

## Tecnologías

- **Python 3.10 o posterior:** lenguaje del proyecto.
- **PhysioNet Python tools (`physionet`):** descarga los archivos de la base.
- **WFDB (`wfdb`):** lectura de señales y anotaciones en formato WFDB.
- **NumPy:** manejo de arreglos y operaciones numéricas.
- **SciPy:** filtrado digital y herramientas de procesamiento de señales.
- **Matplotlib:** visualización de señales y resultados.

## Requisitos

- Windows, macOS o Linux.
- Python 3.10 o posterior.
- Conexión a internet para descargar el registro en la primera ejecución.

## Instalación y ejecución

Clona o descarga este repositorio y abre una terminal en su carpeta raíz. En Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python hello_ecg.py
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python hello_ecg.py
```

La primera ejecución descarga `100.hea` y `100.dat` desde PhysioNet. Al terminar, se abre una gráfica del ECG. En ejecuciones posteriores, los archivos descargados pueden recuperarse desde la caché local de PhysioNet.

Si PowerShell impide activar el entorno virtual, permite la activación solo para la ventana actual y vuelve a ejecutar el comando de activación:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Archivos de la base utilizados

- `.hea`: encabezado con metadatos del registro, como frecuencia de muestreo y canales.
- `.dat`: muestras digitales de la señal ECG.
- `.atr`: anotaciones de latidos, ritmos y otros eventos. El ejemplo inicial no las carga; se usarán en la etapa de evaluación del detector.

## Flujo previsto del análisis

1. Seleccionar registros y segmentos, y revisar sus encabezados y anotaciones.
2. Graficar las señales originales y analizar su contenido frecuencial.
3. Aplicar filtros pasa altas y notch con parámetros documentados.
4. Detectar complejos QRS en la señal original y en cada condición filtrada.
5. Comparar detecciones con las anotaciones y calcular medidas de desempeño.
6. Estimar la frecuencia cardíaca mediante intervalos R–R y autocorrelación.
7. Examinar las modificaciones del notch alrededor de los complejos QRS, incluso cuando no haya una interferencia clara que eliminar.

## Fuentes

- Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database*, versión 1.0.0. PhysioNet. https://doi.org/10.13026/C2F305
- Herramientas de PhysioNet para Python: https://github.com/MIT-LCP/physionet
- WFDB para Python: https://github.com/MIT-LCP/wfdb-python
