# 📡 **Dashboard de Análisis del Sector Telecomunicaciones en Argentina**

---

## 🌐 **Introducción**

Este proyecto tiene como objetivo analizar la conectividad en Argentina, enfocándose en:
- **📊 Incremento en el Acceso a Internet.**
- **🌐 Expansión de la Cobertura de Fibra Óptica.**
- **💡 Modernización de Infraestructura Tecnológica.**

Utilizando un enfoque basado en datos, hemos diseñado un **Dashboard Interactivo** que proporciona información clave para mejorar el acceso a internet, reducir brechas digitales y fomentar la adopción de tecnologías modernas.

---

## 🎯 **KPIs Principales**

### 1️⃣ **KPI 1: Incremento del Acceso a Internet (+2%)**
- **📌 Objetivo:** Incrementar en un 2% el acceso a Internet por cada 100 hogares en las provincias durante el próximo trimestre.
- **📊 Análisis:** Este KPI evalúa las diferencias de acceso en todo el país, destacando áreas que requieren mayor inversión.

---

### 2️⃣ **KPI 2: Cobertura de Fibra Óptica**
- **📌 Objetivo:** Aumentar la cobertura de fibra óptica en regiones con menor acceso, priorizando áreas rurales.
- **📊 Análisis:** Este indicador muestra desigualdades en la infraestructura tecnológica, resaltando regiones con mayor potencial de mejora.

---

### 3️⃣ **KPI 3: Índice de Modernización**
- **📌 Objetivo:** Medir la transición hacia tecnologías avanzadas como la fibra óptica.
- **📊 Análisis:** El índice identifica provincias líderes y rezagadas en la adopción de tecnologías modernas.

---

## 🛠️ **Estructura del Proyecto**

### 1️⃣ **ETL (Extracción, Transformación y Carga):**
   - Procesamiento de datos desde archivos Parquet.
   - Limpieza y transformación de datos para análisis.

### 2️⃣ **EDA (Exploración de Datos):**
   - Análisis descriptivo para identificar patrones y brechas tecnológicas.

### 3️⃣ **Dashboard Interactivo:**
   - Visualización de los KPIs mediante **Streamlit** con gráficos dinámicos y análisis detallado.

---

## 📈 **Resultados Clave**

### **KPI 1: Incremento del 2% en el Acceso a Internet**
- Regiones como Buenos Aires y CABA lideran, pero provincias del NEA y NOA necesitan mayor inversión.
- **💡 Recomendación:** Dirigir recursos hacia áreas rurales para cerrar brechas digitales.

---

### **KPI 2: Cobertura de Fibra Óptica**
- La cobertura es desigual, con provincias como Catamarca y Tucumán destacando, pero Santiago del Estero y Tierra del Fuego requieren mayor atención.
- **💡 Recomendación:** Implementar estrategias escalonadas para mejorar la infraestructura tecnológica.

---

### **KPI 3: Índice de Modernización**
- Las provincias con mayor adopción de fibra óptica lideran la modernización, pero aún existen regiones con alta dependencia de tecnologías obsoletas.
- **💡 Recomendación:** Fomentar incentivos para acelerar la adopción de fibra óptica.

---

## 🚀 **Ejecución del Proyecto**

### **Requisitos Previos**
- **Python 3.8 o superior.**
- Librerías detalladas en `requirements.txt`.

### **Pasos para Ejecutar:**
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-proyecto.git
   cd tu-proyecto
2. Crear un entorno virtual: 
   ```bash  
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
4. Ejecutar el Dashboard:
    ```bash
   streamlit run main.py


## **🗂️ Estructura del Proyecto**

📁 data

├── 📂 raw                 # Archivos originales en formato Excel/CSV.

├── 📂 processed           # Archivos procesados en formato Parquet.

📁 modulos

├── 📄 kpi_1.py            # Lógica para KPI 1.

├── 📄 kpi_2.py            # Lógica para KPI 2.

├── 📄 kpi_3.py            # Lógica para KPI 3.

├── 📄 cierre.py           # Página de conclusiones.

└── 📄 pagina_principal.py # Página de inicio del Dashboard.

📄 main.py                  # Archivo principal para ejecutar el proyecto.

📄 requirements.txt         # Dependencias del proyecto.

## **📝 Reflexión Final**
Este análisis demuestra la importancia de avanzar hacia una infraestructura moderna y accesible para todos. Aunque las disparidades regionales persisten, estrategias adecuadas pueden fomentar una conectividad más equitativa, mejorando la calidad de vida en Argentina.

## **📚 Fuentes de Datos**
Ente Nacional de Comunicaciones (ENACOM): Datos abiertos sobre conectividad y accesos.
Ministerio de Modernización e Informática.

## **📧 Contacto**
Proyecto desarrollado por Valentin Salgado:

- 📬 Email: valentinsalgado11@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/valentin-salgado-463332301/
