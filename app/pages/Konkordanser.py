import streamlit as st
import sys
sys.path.append('..')
from utils import load_corpus
from config import corpus_dict


def main():
    
    st.set_page_config(
        layout="wide",
        page_title="Norn konkordanser",
        page_icon="📚",
        initial_sidebar_state="expanded",
    )
    
    st.title('Konkordanser')
    st.write('### Velg korpus')
    
    col1, col2 = st.columns([1, 4])
    
    corpus_options = corpus_dict.keys()
    selected_corpus = col1.selectbox("Velg et korpus:", corpus_options)
        
    c = load_corpus(corpus_dict[selected_corpus])

    user_input = col2.text_input("Input tekst")
    
    
    if user_input is not "":        
        conc = c.conc(user_input)
        df = conc.frame

        
        html_table = df.to_html(escape=False)
        st.markdown(html_table, unsafe_allow_html=True)
        
        #st.dataframe(df)
    

    st.write('Konkordanser vises her.')


if __name__ == "__main__":
    main()