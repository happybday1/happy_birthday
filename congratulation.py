import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import test_page


# Function to plot the implicit equation (x^2 + y^2 - t)^3 - t * x^2 * y^3 = 0
def plot_implicit_equation():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    t = 21  # Choose a specific t value for plotting



    fig, ax = plt.subplots()
    F = (X ** 2 + Y ** 2 - t) ** 3 - t * X ** 2 * Y ** 3
    ax.contour(X, Y, F, levels=[0], colors='b')
    F = (X ** 2 + Y ** 2 - 3) ** 3 - t * X ** 2 * Y ** 3
    ax.contour(X, Y, F, levels=[0], colors='pink')
    F = (X ** 2 + Y ** 2 - 9) ** 3 - t * X ** 2 * Y ** 3
    ax.contour(X, Y, F, levels=[0], colors='purple')
    ax.set_aspect('equal')
    st.pyplot(fig)

# Function to check user inputs
def check_inputs(input_ys):
    correct_ys = [1, 3, 5]

    if np.allclose(input_ys, correct_ys, atol=1e-6):
        st.success("Ага")
        st.session_state.values_button = True
        st.experimental_rerun()

    else:
        st.error("Нєа")
def go():
    st.title("А я віддам тобі своє сердечко...")

    st.header("Маленький графічок)")

    plot_implicit_equation()

    st.write("А тепер намалюй його в [Desmos](https://www.desmos.com/calculator) : `(x^2 + y^2 - t)^3 - t * x^2 * y^3 = 0` with t=?. think about it:)")

    st.write("І спробуй знайти пароль для ось цих х-ів (5.33, 6.35, 6.71):")

    input_y1 = st.number_input("y для x=5.33", min_value=1, max_value=5)
    input_y2 = st.number_input("у для x=6.35", min_value=1, max_value=5)
    input_y3 = st.number_input("y для x=6.71", min_value=1, max_value=5)


    if 'values_button' not in st.session_state:
        st.session_state.values_button = False

    if st.session_state.values_button:
        st.balloons()

        test_page.test_page()

    else:
        if st.button("Перевірити"):
            user_inputs = [input_y1, input_y2, input_y3]
            check_inputs(user_inputs)



