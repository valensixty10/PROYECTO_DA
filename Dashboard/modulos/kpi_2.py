import streamlit as st
import pandas as pd
import plotly.express as px

def display():
    st.title("🌐 KPI 2 - Cobertura de Fibra Óptica por Región")
    st.markdown("""
    ### Descripción
    Este KPI evalúa la cobertura de fibra óptica por región en Argentina. Analizamos qué porcentaje del acceso total a internet en cada región corresponde a conexiones de fibra óptica, identificando las áreas con mayor y menor adopción de esta tecnología avanzada.
    
    ### Metodología
    Los datos se agrupan por región, considerando el porcentaje de accesos de fibra óptica respecto al total de accesos a internet. Esto permite visualizar las disparidades regionales y orientar estrategias de modernización.
    """)

    # Cargar los datos desde archivos Parquet
    accesos_internet = pd.read_parquet('notebooks\data\processed\internet_accesos_tecnologia.parquet')
    mapa_conectividad = pd.read_parquet('notebooks\data\processed\mapa_conectividad.parquet')


    # Preparar el DataFrame de cobertura de fibra óptica
    accesos_fibra_optica = accesos_internet[['Provincia', 'Fibra óptica', 'Total']].copy()
    accesos_fibra_optica['Cobertura Fibra Óptica (%)'] = (accesos_fibra_optica['Fibra óptica'] / accesos_fibra_optica['Total']) * 100

    provincias_regiones = {
        'Buenos Aires': 'Buenos Aires y CABA',
        'CABA': 'Buenos Aires y CABA',
        'Catamarca': 'NOA',
        'Jujuy': 'NOA',
        'La Rioja': 'NOA',
        'Salta': 'NOA',
        'Santiago del Estero': 'NOA',
        'Tucumán': 'NOA',
        'Chaco': 'NEA',
        'Corrientes': 'NEA',
        'Formosa': 'NEA',
        'Misiones': 'NEA',
        'Córdoba': 'Centro',
        'Entre Ríos': 'Centro',
        'Santa Fe': 'Centro',
        'Chubut': 'Patagonia',
        'La Pampa': 'Patagonia',
        'Neuquén': 'Patagonia',
        'Río Negro': 'Patagonia',
        'Santa Cruz': 'Patagonia',
        'Tierra del Fuego': 'Patagonia',
        'Mendoza': 'Cuyo',
        'San Juan': 'Cuyo',
        'San Luis': 'Cuyo'
    }

    # Asignar regiones
    accesos_fibra_optica['Región'] = accesos_fibra_optica['Provincia'].map(provincias_regiones)

    # Calcular cobertura promedio por región
    cobertura_fibra_optica_region = accesos_fibra_optica.groupby('Región')['Cobertura Fibra Óptica (%)'].mean().reset_index()

    # Mostrar la tabla de datos
    st.markdown("### Cobertura de Fibra Óptica por Región")
    st.dataframe(cobertura_fibra_optica_region)

    # Gráfico interactivo de barras con Plotly
    fig = px.bar(
        cobertura_fibra_optica_region,
        x='Región',
        y='Cobertura Fibra Óptica (%)',
        color='Cobertura Fibra Óptica (%)',
        color_continuous_scale='Viridis',
        labels={'Cobertura Fibra Óptica (%)': 'Cobertura (%)'},
        title='Cobertura de Fibra Óptica por Región en Argentina',
        text='Cobertura Fibra Óptica (%)'
    )
    fig.update_layout(
        xaxis_title="Región",
        yaxis_title="Cobertura (%)",
        title_x=0.5,
        title_font_size=20
    )
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

    # Conclusiones
    st.markdown("""
    ### Conclusiones
    - **Región con mayor cobertura:** NOA, destacándose por un alto porcentaje de adopción de fibra óptica.
    - **Región con menor cobertura:** NEA, donde se observa una menor penetración de esta tecnología.
    - Estas disparidades indican la necesidad de estrategias diferenciadas para fomentar la modernización y cerrar la brecha digital.
    """)


