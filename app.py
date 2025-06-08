import streamlit as st
import json

# Estilo customizado
st.set_page_config(page_title="ODS Radar", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Título e subtítulo
st.markdown("<h1>📡 ODS Radar</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>Notícias que transformam o mundo – com base nos Objetivos de Desenvolvimento Sustentável.</p>", unsafe_allow_html=True)

# Carrega as notícias simuladas
with open("noticias.json", "r", encoding="utf-8") as f:
    noticias = json.load(f)

# Lista de ODS disponíveis
ods_opcoes = sorted(set(n["ods"] for n in noticias))
ods_escolhido = st.selectbox("🔎 Escolha um ODS", ["Todos"] + ods_opcoes)

# Filtro de notícias
for noticia in noticias:
    if ods_escolhido == "Todos" or noticia["ods"] == ods_escolhido:
        description = noticia.get("descricao", noticia.get("resumo", "Descrição não disponível"))
        st.markdown(f"""
        <div class='card'>
            <h2>{noticia["titulo"]}</h2>
            <p><strong>Fonte:</strong> {noticia["fonte"]}</p>
            <p>{description}</p>
            <a href="{noticia["link"]}" target="_blank">🔗 Leia mais</a>
        </div>
        """, unsafe_allow_html=True)