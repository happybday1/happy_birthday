import pandas as pd
import streamlit as st

import final


def test_page():

    st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        position: relative;
    }
    .balloons {
        position: absolute;
        top: -50px;
        right: -50px;
        width: 150px;
    }
    .balloons-left {
        position: absolute;
        top: -50px;
        left: -50px;
        width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main">
        <img src="https://i.imgur.com/tOsCI3u.jpeg" class="balloons">
        <img src="https://i.imgur.com/mmlJICx.jpeg" class="balloons-left">
        <h1><center>Тут буде тестік!</center></h1>
        <h3>В тебе звісно міліон спроб, але вперед:</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.form("test_form"):
        answers = []
        questions = pd.read_csv("questions.csv")
        for index, row in questions.iterrows():
            st.markdown(f"#### {index + 1}. {row['question']}")
            options = [row['option1'], row['option2'], row['option3'], row['option4']]
            answer = st.radio(f"Обирай:", options, key=f"answer_{index}")
            answers.append(answer)

        submitted = st.form_submit_button("Submit")
    if 'final_button' not in st.session_state:
        st.session_state.final_button = False

    if st.session_state.final_button:
        final.final()


    if submitted:
        correct_answers = questions['correct_answer'].tolist()
        if answers == correct_answers:
            st.session_state.final_button = True
            st.session_state['test_completed'] = True
        else:
            st.error("Ь")
