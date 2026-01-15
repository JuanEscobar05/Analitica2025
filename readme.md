# 📊 Analitica2025

## 1. Descripción general

**Analitica2025** es un proyecto desarrollado en **Python** enfocado en la simulación, análisis y visualización de datos. El sistema genera listas de datos simulados, los procesa y produce **gráficos** y **reportes en formato HTML**, permitiendo analizar la información de forma clara y estructurada.

Este proyecto está orientado a fines **académicos y formativos**, especialmente para comprender conceptos básicos de analítica de datos, generación de reportes y visualización.

---

## 2. Tecnologías utilizadas

* **Python 3**
* **Matplotlib** (visualización de datos)
* **HTML** (reportes)
* **Listas simuladas de datos**

---

## 3. Estructura del proyecto

```
Analitica2025-main/
│
├── main.py
├── explicación.txt
├── paquetes.txt
├── readme.md
│
├── data/
│   └── listasSimuladas.py
│
├── notebook/
│   ├── generarReportes.py
│   ├── graficarBarras.py
│   └── prueba.html
│
├── reportes/
│   ├── tablaUno.html
│   ├── tablaDos.html
│   ├── tablaTres.html
│   └── tablaCuatro.html
```

---

## 4. Descripción de archivos principales

### 🔹 `main.py`

Archivo principal del proyecto. Se encarga de:

* Ejecutar el flujo general del sistema
* Llamar a las funciones de generación de datos
* Invocar los módulos de gráficos y reportes

---

### 🔹 `data/listasSimuladas.py`

Contiene funciones que generan **listas de datos simulados**, las cuales sirven como base para:

* Análisis estadístico
* Generación de tablas
* Visualización gráfica

Estas listas simulan información real para pruebas y análisis.

---

### 🔹 `notebook/graficarBarras.py`

Módulo encargado de:

* Crear **gráficos de barras**
* Representar visualmente los datos generados
* Facilitar la interpretación de la información

Utiliza librerías de visualización como `matplotlib`.

---

### 🔹 `notebook/generarReportes.py`

Este archivo permite:

* Generar **reportes en formato HTML**
* Construir tablas a partir de los datos
* Guardar los resultados en la carpeta `reportes/`

---

### 🔹 `reportes/`

Contiene los reportes finales generados por el sistema:

* `tablaUno.html`
* `tablaDos.html`
* `tablaTres.html`
* `tablaCuatro.html`

Cada archivo representa una tabla con datos analizados.

---

### 🔹 `paquetes.txt`

Lista de dependencias necesarias para ejecutar el proyecto. Se recomienda instalar los paquetes usando:

```bash
pip install -r paquetes.txt
```

---

### 🔹 `explicación.txt`

Documento de apoyo que explica el objetivo del proyecto y su funcionamiento general.

---

## 5. Ejecución del proyecto

1. Clonar o descargar el repositorio
2. Instalar dependencias:

```bash
pip install -r paquetes.txt
```

3. Ejecutar el archivo principal:

```bash
python main.py
```

4. Revisar los reportes generados en la carpeta `reportes/`

---

## 6. Resultados esperados

* Gráficos estadísticos
* Reportes HTML con tablas de datos
* Visualización clara de información simulada

---

## 7. Posibles mejoras

* Integrar base de datos (MySQL o SQLite)
* Agregar análisis estadístico avanzado
* Exportar reportes en PDF
* Crear interfaz gráfica o web

---

## 8. Autor

Proyecto desarrollado por **Juan Escobar** con fines académicos para el aprendizaje de **Analítica de Datos en Python**.

---
