import streamlit as st
import pandas as pd
import dhlab as dh
import re
from config import corpus_dict
from utils import load_corpus, gh_button


def main():
    
    st.set_page_config(
        layout="wide",
        page_title="Norn korpus",
        page_icon="📚",
        initial_sidebar_state="expanded",
    )
    
    
    
    # Add favicon stylesheet
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([4, 1])
    col1.title("Norn")

    link = "https://github.com/nationallibraryofnorway/NORN"

    col2.markdown(
        f"""<div style="float: right;">
        <a href="{link}" target="_blank">
            <i class="fab fa-github fa-2x" style="margin-right: 10px;"></i>
        </a>
        <a href="https://www.nb.no/dh-lab/kontakt/" target="_blank">
            <i class="fas fa-envelope fa-2x"></i>
        </a>
    </div>""",
        unsafe_allow_html=True,
    )

    st.write("### Korpusanalyse")
    st.write("Velg mellom konkordanser og kollokasjoner i menyen til venstre.")
    st.write("Inspiser korpusene ved å velge det i menyen til under.")

    corpus_options = corpus_dict.keys()
    selected_corpus = st.selectbox("Select a Corpus:", corpus_options)

    c = load_corpus(corpus_dict[selected_corpus])

    df = c.frame

    st.dataframe(df)


if __name__ == "__main__":
    main()
