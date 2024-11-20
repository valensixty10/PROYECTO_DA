import pandas as pd
import plotly.express as px
import streamlit as st
import warnings

warnings.filterwarnings('ignore')

def display():
    st.title("📊 KPI 1 - Incremento en el Acceso a Internet")
    st.markdown("""
    ### Descripción
    Este KPI mide el crecimiento proyectado del acceso a internet en hogares por provincia, evaluando la meta de un incremento del 2% en el próximo trimestre.
    
    ### Análisis
    - **Acceso Actual**: Representa el número de accesos totales en el último trimestre del año más reciente disponible.
    - **Acceso Proyectado**: Calcula el número de accesos si se logra un incremento del 2% sobre el acceso actual.
    - **Análisis por Región**: Se agrupan las provincias en regiones para observar tendencias y patrones en la conectividad.
    """)

    # Cargar el archivo Parquet de accesos a internet procesado
    accesos_internet = pd.read_parquet('Dashboard/internet_accesos_tecnologia.parquet')

    # Agrupar por provincia y trimestre para obtener la suma de accesos por trimestre en cada provincia
    accesos_provincia = accesos_internet.groupby(['Provincia', 'Año', 'Trimestre'])['Total'].sum().reset_index()

    # Filtrar el último trimestre disponible
    ultimo_ano = accesos_provincia['Año'].max()
    ultimo_trimestre = accesos_provincia[accesos_provincia['Año'] == ultimo_ano]['Trimestre'].max()
    accesos_ultimo_trimestre = accesos_provincia[
        (accesos_provincia['Año'] == ultimo_ano) & (accesos_provincia['Trimestre'] == ultimo_trimestre)
    ].copy()

    # Calcular el acceso proyectado con un incremento del 2%
    accesos_ultimo_trimestre['Nuevo Acceso'] = accesos_ultimo_trimestre['Total'] * 1.02

    # Calcular el KPI de incremento en porcentaje para cada provincia
    accesos_ultimo_trimestre['KPI Incremento (%)'] = ((accesos_ultimo_trimestre['Nuevo Acceso'] - accesos_ultimo_trimestre['Total']) / accesos_ultimo_trimestre['Total']) * 100

    # Ordenar el DataFrame por el número de accesos actuales de menor a mayor
    accesos_ultimo_trimestre_sorted = accesos_ultimo_trimestre.sort_values(by='Total')

    # Gráfico 1: Comparación de Acceso Actual y Proyectado por Provincia
    st.subheader("📊 Comparación por Provincia")
    fig1 = px.bar(
        accesos_ultimo_trimestre_sorted,
        x="Provincia",
        y=["Total", "Nuevo Acceso"],
        labels={"value": "Número de Accesos", "variable": "Tipo de Acceso"},
        barmode="group",
        title="Comparación de Acceso Actual y Proyectado a Internet en Hogares por Provincia"
    )

    # Ajustar la escala del eje Y
    fig1.update_layout(
        yaxis=dict(
            title="Número de Accesos (Escala Logarítmica)",
            type="log",
            range=[5, 8]  # Ajusta los valores para la escala logarítmica
        ),
        xaxis=dict(
            title="Provincia"
        ),
        legend=dict(title="Tipo de Acceso")
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Análisis por región
    st.subheader("📍 Análisis por Región")
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

    # Añadir columna de región al DataFrame
    accesos_ultimo_trimestre_sorted['Región'] = accesos_ultimo_trimestre_sorted['Provincia'].map(provincias_regiones)

    # Calcular el acceso promedio de internet por región
    acceso_promedio_region = accesos_ultimo_trimestre_sorted.groupby('Región')['Total'].mean().reset_index()

    # Gráfico 2: Acceso Promedio de Internet por Región
    fig2 = px.bar(
        acceso_promedio_region,
        x='Región',
        y='Total',
        labels={"Total": "Número Promedio de Accesos", "Región": "Región"},
        title="Acceso Promedio de Internet por Región",
        color='Total',  # Colores basados en el valor
        color_continuous_scale='viridis'  # Cambiar la escala de color
    )

    fig2.update_layout(
        yaxis=dict(
            title="Número Promedio de Accesos (Escala Logarítmica)",
            type="log",
            range=[5, 8]  # Ajustar el rango si es necesario
        ),
        xaxis=dict(
            title="Región"
        )
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Evaluación del KPI
    st.subheader("📈 Evaluación del KPI")
    total_actual = accesos_ultimo_trimestre['Total'].sum()
    total_proyectado = accesos_ultimo_trimestre['Nuevo Acceso'].sum()
    
    if total_actual < total_proyectado:
        st.success(f"✅ El KPI se logró alcanzar con una proyección de {total_proyectado:.2f} accesos.")
    else:
        st.error(f"❌ El KPI no se logró. Accesos actuales: {total_actual:.2f}, Proyectados: {total_proyectado:.2f}.")

    # Explicación adicional
    st.markdown("""
    ### Explicación
    El análisis del KPI 1 nos permite identificar si el objetivo del incremento del 2% en el acceso a internet fue alcanzado. 
    Este objetivo es crucial para evaluar la expansión de la conectividad digital en las provincias. En caso de no lograrse, 
    se recomienda analizar las áreas con menor crecimiento e implementar estrategias específicas para reducir la brecha de acceso.
    """)
