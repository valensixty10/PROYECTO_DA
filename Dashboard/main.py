import streamlit as st
from modulos import pagina_principal, kpi_1, kpi_2, kpi_3, cierre

# Configuración global
st.set_page_config(
    page_title="Dashboard de Análisis de Internet",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS personalizado para la barra lateral
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        color: white;
        font-family: Arial, sans-serif;
        font-size: 1rem;
    }
    [data-testid="stSidebar"] h2 {
        color: #ecf0f1;
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 20px;
    }
    [data-testid="stSidebar"] .css-1e5imcs {
        color: #ecf0f1;
        font-weight: bold;
        font-size: 1.1rem;
        margin: 10px 0;
    }
    [data-testid="stSidebar"] .css-1e5imcs:hover {
        background-color: #3498db;
        border-radius: 5px;
        padding: 5px;
    }
    [data-testid="stSidebar"] input[type="radio"]:checked + label {
        background-color: #1abc9c;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Diccionario de navegación
pages = {
    "Página Principal": pagina_principal,
    "KPI 1 - Acceso a Internet": kpi_1,
    "KPI 2 - Cobertura de Fibra Óptica": kpi_2,
    "KPI 3 - Modernización de Infraestructura": kpi_3,
    "Conclusiones": cierre,
}

# Título personalizado para la barra lateral
st.sidebar.markdown('<h2 style="text-align: center; color: #ecf0f1;">📊 Navegación</h2>', unsafe_allow_html=True)

# Pestaña de selección en la barra lateral
selection = st.sidebar.selectbox(
    "Selecciona una sección:",
    list(pages.keys())
)

# Determinar la página a mostrar
page = pages[selection]
page.display()
