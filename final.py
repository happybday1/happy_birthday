import streamlit as st
import pydeck as pdk

def final():

    st.title("Фінішна пряма")

    st.text("На жаль, я не змогла приїхати, але я дуже хотіла зробити \n подарунок сюрпризом, тому фінальна чатсина квесту буде очно")
    st.text("Login: [@neilm111er](https://t.me/neilm111er)")

    st.text("Забирати тут:")


    latitude = 50.44758169171687
    longitude = 30.45285419941046
    # Define the layer for the red marker
    marker_layer = pdk.Layer(
        'ScatterplotLayer',
        data=[{'coordinates': [longitude, latitude]}],
        get_position='coordinates',
        get_color='[200, 30, 64, 160]',
        get_radius=5,
    )

    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state={
            "latitude": latitude,
            "longitude": longitude,
            "zoom": 19,
            "pitch": 150,
        },
        layers=[marker_layer]
    )

    st.pydeck_chart(map)
