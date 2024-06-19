import streamlit as st
import congratulation

def show_timeline():
    if 'first_button_clicked' not in st.session_state:
        st.session_state.first_button_clicked = False

    if st.session_state.first_button_clicked:
        st.header("Як все починалось")

        timeline_events = [
                {"emoji": "❤️", "title": "Twitter", "description": "Перший комент про КПІ, починаємо спілкування (-ВИ ТЕЖ З КПІ? - ТЕЖ??? ВИ ТЕЖ????", "year": "5 Червня 2022"},
                {"emoji": "💜", "title": "Telegram", "description": "Блекаути, піздєц, переходимо у тг", "year": "18 листопада 2022"},
                {"emoji": "💚", "title": "Pet's Song", "description": "Перша згадка пса патрона в чаті",
                 "year": "29 листопада 2022"},
                {"emoji": "💛", "title": "First Meet", "description": "Зустрічаємось у Києві, гуляємо, обмінюємось подарунками", "year": "20 червня 2023"},
                {"emoji": "💙", "title": "Anniversary",
                 "description": "Два роки, як ми знайомі", "year": "5 червня 2024"},

            ]

        st.markdown("""
        <style>
            .timeline-container {
                display: flex;
                flex-direction: column;
                align-items: top;
                margin: 0 0;
            }
            .timeline-item {
                display: flex;
                width: 80%;
                margin: 20px 0;
                align-items: center;
            }
            .timeline-item:nth-child(odd) .timeline-content {
                flex-direction: row-reverse;
            }
            .timeline-item:nth-child(odd) .timeline-content::before {
                left: auto;
                right: -20px;
            }
            .timeline-item:nth-child(even) .timeline-content::before {
                left: -20px;
            }
            .timeline-content {
                display: flex;
                align-items: center;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                position: relative;
            }
            .timeline-content::before {
                content: '';
                width: 0;
                height: 0;
                border: 10px solid transparent;
                border-right-color: white;
                position: absolute;
            }
            .timeline-emoji {
                font-size: 2em;
                margin-right: 20px;
            }
            .timeline-info {
                display: flex;
                flex-direction: column;
            }
            .timeline-year {
                font-weight: bold;
                margin-bottom: 5px;
            }
            .timeline-title {
                font-weight: bold;
                margin-bottom: 5px;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
        for event in timeline_events:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-content">
                    <div class="timeline-emoji">{event['emoji']}</div>
                    <div class="timeline-info">
                        <div class="timeline-year">{event['year']}</div>
                        <div class="timeline-title">{event['title']}</div>
                        <div>{event['description']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if 'graph_button_clicked' not in st.session_state:
            st.session_state.graph_button_clicked = False

        if st.session_state.graph_button_clicked:
            congratulation.go()

        else:
            if st.button("Погнали далі"):
                st.session_state.graph_button_clicked = True
                st.experimental_rerun()
    else:
        st.text("я звісно генійка, але не оновлюй сторінку, а то воно злетить нахуй")
        st.snow()
        if st.button("Begin Journey"):
            st.session_state.first_button_clicked = True
            st.experimental_rerun()




show_timeline()

