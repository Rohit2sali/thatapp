import streamlit as st


def login_screen():
    st.header("this app is private")
    st.subheader("please log in")
    # st.button("login with google", on_click=st.login("google"))
    if st.button("Login with google"):
        st.login("google")

# login_screen() 


if not st.user.is_logged_in:
    login_screen()
else:
    # st.user()
    st.header(f"welcome {st.user} !")
    if st.button("Log out"):
        st.logout()

# https://docs.streamlit.io/develop/tutorials/authentication/google
# https://console.cloud.google.com/auth/clients/261962590474-67q8ju493lave85s124o1qcb9u80ljep.apps.googleusercontent.com?project=firstproject-482516&supportedpurview=project


# C:\machine learning\firstapp\app.py
# C:\machine learning\firstapp\streamlittut.streamlit\secrets.toml