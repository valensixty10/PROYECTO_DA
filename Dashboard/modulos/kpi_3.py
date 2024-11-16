import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def display():
    # Título y descripción
    st.title("📈 KPI 3 - Modernización de Infraestructura")
    st.markdown("""
    ### Descripción
    Este KPI mide el grado de modernización de la infraestructura de acceso a internet en cada provincia. 
    Se calcula como la proporción de accesos mediante **fibra óptica** respecto al total de accesos tradicionales (ADSL, Cablemódem y Fibra Óptica). 
    El objetivo es identificar regiones con mayor adopción de tecnologías avanzadas y evaluar disparidades regionales.
    """)

    # Cargar el archivo Parquet
    accesos_internet = pd.read_parquet('notebooks\data\processed\internet_accesos_tecnologia.parquet')

    # Calcular el índice de modernización en porcentaje
    accesos_internet['Índice de Modernización (%)'] = (
        accesos_internet['Fibra óptica'] / 
        (accesos_internet['ADSL'] + accesos_internet['Cablemodem'] + accesos_internet['Fibra óptica'])
    ) * 100

    # Agrupar por provincia y calcular el promedio del índice de modernización
    indice_modernizacion_provincia = accesos_internet.groupby('Provincia')['Índice de Modernización (%)'].mean().reset_index()

    # Ordenar los datos de mayor a menor índice de modernización
    indice_modernizacion_provincia = indice_modernizacion_provincia.sort_values(by='Índice de Modernización (%)', ascending=False)

    # Gráfico 1: Índice de Modernización por Provincia
    st.subheader("🌟 Índice de Modernización por Provincia")
    st.markdown("""
    #### Análisis
    - Las provincias con mayor adopción de tecnologías avanzadas (fibra óptica) son **Catamarca**, **Tucumán** y **Mendoza**, con índices superiores al 20%.
    - Por otro lado, provincias como **Santiago del Estero** y **Tierra del Fuego** tienen índices significativamente bajos, lo que indica una baja modernización de infraestructura.
    - Este análisis permite priorizar políticas de inversión en regiones con menor desarrollo tecnológico.
    """)
    fig1 = px.bar(
        indice_modernizacion_provincia,
        x="Provincia",
        y="Índice de Modernización (%)",
        labels={"Provincia": "Provincia", "Índice de Modernización (%)": "Índice de Modernización (%)"},
        title="Índice de Modernización Promedio por Provincia",
        color="Índice de Modernización (%)",
        color_continuous_scale="Blues"
    )
    fig1.update_layout(
        xaxis=dict(title="Provincia", tickangle=45),
        yaxis=dict(title="Índice de Modernización (%)", tickformat=".1f"),
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Calcular proporciones de tecnologías por provincia
    accesos_internet_provincia = accesos_internet.groupby('Provincia')[['ADSL', 'Cablemodem', 'Fibra óptica']].sum()
    accesos_internet_provincia_percent = accesos_internet_provincia.div(accesos_internet_provincia.sum(axis=1), axis=0) * 100

    # Ordenar por proporción de fibra óptica
    accesos_internet_provincia_percent = accesos_internet_provincia_percent.sort_values(by='Fibra óptica', ascending=False)

    # Gráfico 2: Distribución de Accesos por Tecnología
    st.subheader("📊 Distribución de Accesos por Tecnología")
    st.markdown("""
    #### Análisis
    - La tecnología **fibra óptica** está presente en un porcentaje mayor en provincias como **Catamarca** y **Tucumán**, mientras que **ADSL** sigue siendo predominante en muchas otras regiones.
    - **Cablemodem** se mantiene como una tecnología intermedia, con buena presencia en provincias como **Buenos Aires** y **Córdoba**.
    - Este gráfico destaca la heterogeneidad en la adopción tecnológica a nivel provincial.
    """)
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=accesos_internet_provincia_percent.index,
        y=accesos_internet_provincia_percent['ADSL'],
        name='ADSL',
        marker_color='#FFB6C1'  # Rosa claro
    ))
    fig2.add_trace(go.Bar(
        x=accesos_internet_provincia_percent.index,
        y=accesos_internet_provincia_percent['Cablemodem'],
        name='Cablemodem',
        marker_color='#ADD8E6'  # Azul claro
    ))
    fig2.add_trace(go.Bar(
        x=accesos_internet_provincia_percent.index,
        y=accesos_internet_provincia_percent['Fibra óptica'],
        name='Fibra Óptica',
        marker_color='#98FB98'  # Verde claro
    ))
    fig2.update_layout(
        barmode='stack',
        title="Distribución de Accesos por Tipo de Tecnología en cada Provincia (Proporciones)",
        xaxis=dict(title="Provincia", tickangle=45),
        yaxis=dict(title="Porcentaje de Acceso", tickformat=".1f"),
        legend=dict(title="Tecnología")
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Conclusiones
    st.markdown("""
    ### Conclusiones
    - Las provincias con mayor índice de modernización coinciden con aquellas que tienen un porcentaje significativo de acceso mediante **fibra óptica**.
    - Existen disparidades importantes entre provincias en cuanto al nivel de adopción de tecnologías avanzadas.
    - Este análisis puede servir como base para diseñar políticas públicas que promuevan la modernización de la infraestructura en las provincias con menor índice.
    """)
