import streamlit as st

def display():
    # Estilos personalizados
    st.markdown(
        """
        <style>
        .page-title {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #2ecc71;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #3498db;
            margin-top: 40px;
        }
        .highlight-box {
            background-color: #000000;
            border-left: 5px solid #3498db;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            font-size: 1.2rem; /* Tamaño general del texto */
        }
        .highlight-box:hover {
            transform: scale(1.03);
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        }
        .recommendation-card {
            background-color: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .recommendation-card:hover {
            transform: scale(1.05);
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        }
        .recommendation-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2c3e50;
        }
        .recommendation-text {
            color: #34495e;
            font-size: 1rem;
            margin-top: 5px;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #7f8c8d;
            margin-top: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Título principal
    st.markdown('<div class="page-title">✅ Conclusiones</div>', unsafe_allow_html=True)

    # Resumen de hallazgos
    st.markdown('<div class="section-title">📊 Resumen de Hallazgos</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="highlight-box">
        <ul>
        <li><b>KPI 1:</b> El incremento del 2% en el acceso a internet genera un impacto significativo en provincias con mayor infraestructura y acceso.</li>
        <li><b>KPI 2:</b> Existe una desigualdad notable en la cobertura de fibra óptica entre regiones, con oportunidades claras de mejora en áreas rurales.</li>
        <li><b>KPI 3:</b> El índice de modernización demuestra una transición hacia tecnologías avanzadas como fibra óptica, especialmente en provincias con menor dependencia de tecnologías tradicionales.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Recomendaciones
    st.markdown('<div class="section-title">💡 Recomendaciones</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="recommendation-card">
                <div class="recommendation-title">1️⃣ Priorizar inversión en áreas rurales</div>
                <div class="recommendation-text">Ampliar la infraestructura en regiones con menor acceso a internet para cerrar la brecha digital.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="recommendation-card">
                <div class="recommendation-title">2️⃣ Promover la transición hacia fibra óptica</div>
                <div class="recommendation-text">Impulsar incentivos y subsidios para fomentar la adopción de tecnologías modernas en áreas urbanas y rurales.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="recommendation-card">
                <div class="recommendation-title">3️⃣ Monitorear el índice de modernización</div>
                <div class="recommendation-text">Establecer sistemas de seguimiento para evaluar el impacto de las inversiones en infraestructura digital.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="recommendation-card">
                <div class="recommendation-title">4️⃣ Colaboración público-privada</div>
                <div class="recommendation-text">Fomentar alianzas estratégicas para maximizar los recursos y garantizar conectividad inclusiva y sostenible.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Reflexión final
    st.markdown('<div class="section-title">🔍 Reflexión Final</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="highlight-box">
        Este análisis demuestra la importancia de avanzar hacia una infraestructura moderna y accesible para todos. 
        Las disparidades regionales aún persisten, pero con las estrategias adecuadas, es posible fomentar una conectividad más equitativa y eficiente, mejorando la calidad de vida de los ciudadanos.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Pie de página
    st.markdown(
        """
        <div class="footer">
        Creado por el <b>Equipo de Análisis</b>.  
        Basado en datos del período 2023-2024.  
        Fuente de datos: <i>Ministerio de Modernización e Informática</i>.
        </div>
        """,
        unsafe_allow_html=True,
    )
