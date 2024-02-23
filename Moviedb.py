from requests import *
import streamlit as st


def findmovie(movie_name):
    api_key = "xxxx"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
    data = get(url).json()
    try:
        m_name = data["Title"]
        m_dir = "Directed By : " + data["Director"]
        m_release = "Released : " + data["Released"]
        m_genre = "Genre : " + data["Genre"]
        m_lang = "Language : " + data["Language"]
        m_cast = "Cast : " + data["Actors"]
        m_plot = "Plot :" + data["Plot"]
        m_poster = data["Poster"]

    except KeyError:
        st.write("Movie Details Not Available")
    return m_name, m_dir, m_release, m_genre, m_lang, m_cast, m_plot, m_poster


def main():
    st.title("Movie DB")
    movie_name = st.text_input(label=" Which Movie Do You Wanna Search ?", placeholder="Enter Movie Name").lower()
    if st.button("Search"):
        m_name, m_dir, m_release, m_genre, m_lang, m_cast, m_plot, m_poster = findmovie(movie_name)
        col_1, col_2 = st.columns(2)
        with col_2:
            st.title(m_name)
            st.write(m_dir)
            st.write(m_genre)
            st.write(m_lang)
            st.write(m_release)
            st.write(m_cast)
            st.write(m_plot)
        with col_1:
            st.image(m_poster)


if __name__ == "__main__":
    main()
