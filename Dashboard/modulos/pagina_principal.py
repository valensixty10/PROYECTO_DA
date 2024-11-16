import streamlit as st

def display():
    # Título y subtítulo del Dashboard
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 3.5rem;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.4rem;
            color: #b0b0b0;
            text-align: center;
            margin-bottom: 30px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="main-title">🛰️Telecomunicaciones en Argentina🛰️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Análisis de Acceso a Internet, Modernización y Cobertura Regional</div>', unsafe_allow_html=True)

    # Diseño de las tarjetas KPI
    st.markdown(
        """
        <style>
        .card {
            background: linear-gradient(135deg, #1f77b4, #2c3e50);
            padding: 20px;
            margin: 10px;
            border-radius: 15px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.5);
        }
        .card h3 {
            color: #ffffff;
            font-size: 22px;
            margin: 0 0 10px;
        }
        .card p {
            color: #ecf0f1;
            font-size: 18px;
        }
        .card strong {
            font-size: 40px;
            color: #ffffff;
        }
        .icon {
            font-size: 60px;
            color: #1abc9c;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

            # Tarjetas con columnas
    col1, col2, col3 = st.columns(3)

    # Primera tarjeta: Acceso a Internet
    with col1:
        if st.button("📊 Acceso a Internet"):
            st.session_state['selected_page'] = "KPI 1 - Acceso a Internet"
        st.markdown(
            """
            <div class="card">
                <div class="icon">📶</div>
                <h3>Acceso a Internet</h3>
                <strong>+2%</strong>
                <p>Aumento proyectado trimestral</p>
            </div>
            """, unsafe_allow_html=True
        )

    # Segunda tarjeta: Fibra Óptica por region
    with col2:
        if st.button("🌐 Fibra Óptica por region"):
            st.session_state['selected_page'] = "KPI 2 - Fibra Óptica por region"
        st.markdown(
            """
            <div class="card">
                <div class="icon">🌐</div>
                <h3>Fibra Óptica por region</h3>
                <strong>24%</strong>
                <p>Provincias con menor cobertura</p>
            </div>
            """, unsafe_allow_html=True
        )

    # Tercera tarjeta: Modernización de Infraestructura
    with col3:
        if st.button("📈 Modernización de Infraestructura"):
            st.session_state['selected_page'] = "KPI 3 - Modernización de Infraestructura"
        st.markdown(
            """
            <div class="card">
                <div class="icon">📈</div>
                <h3>Modernización de Infraestructura</h3>
                <strong>+15%</strong>
                <p>Crecimiento anual en modernización</p>
            </div>
            """, unsafe_allow_html=True
        )


    # Explicación de los KPIs
    st.markdown(
        """
        <style>
        .kpi-section {
            font-size: 1.2rem;
            line-height: 1.8;
            color: #ecf0f1;
            margin-top: 60px;
        }
        .kpi-section h4 {
            font-size: 1.5rem;
            color: #1abc9c;
            margin-top: 60px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="kpi-section">', unsafe_allow_html=True)
    st.markdown("### Que analizan los KPIs?", unsafe_allow_html=True)
    st.markdown(
        """
        - 📶 **Acceso a Internet**: Se proyecta un aumento del 2% en el acceso a internet por cada 100 hogares en las provincias.
        - 🌐 **Fibra Óptica por region**: 24% de las provincias con acceso limitado están adoptando tecnologías avanzadas.
        - 📈 **Modernización de Infraestructura**: Incremento del 15% en usuarios que migran a tecnologías modernas como fibra óptica.
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Navegación a las secciones de KPIs
    st.markdown(
        """
        <style>
        .nav-button {
            display: inline-block;
            background-color: #ffffff;
            color: white;
            padding: 12px 30px;
            margin: 15px 10px;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            font-size: 1.2rem;
            transition: background-color 0.3s, transform 0.2s;
        }
        .nav-button:hover {
            background-color: #2980b9;
            transform: scale(1.1);
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div style="text-align: center; margin-top: 40px;">', unsafe_allow_html=True)
    st.markdown('<a class="nav-button" href="#kpi-1">📊 KPI 1 - Acceso a Internet</a>', unsafe_allow_html=True)
    st.markdown('<a class="nav-button" href="#kpi-2">🌐 KPI 2 - Fibra Óptica por region</a>', unsafe_allow_html=True)
    st.markdown('<a class="nav-button" href="#kpi-3">📈 KPI 3 - Modernización</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Pie de página
    st.markdown(
        """
        <hr style="margin-top: 50px; margin-bottom: 20px; border-color: #95a5a6;">
        <div style="text-align: center; font-size: 0.9rem; color: #7f8c8d;">
            Creado por <b>Equipo de Análisis</b>. Basado en datos del período 2023-2024.<br>
            📚 Fuente de datos: <i>Ministerio de Modernización</i>.
        </div>
        """, unsafe_allow_html=True
    )

