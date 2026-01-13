import streamlit as st
import pandas as pd

st.title("🎬 Любими филми – анкета")

# Данни: жанр -> филми
movies = {
    "Екшън": [
        "Джон Уик",
        "Лудият Макс",
        "Умирай трудно",
        "Гладиатор",
        "Черният рицар"
    ],
    "Ужаси": [
        "Заклинанието",
        "То",
        "Предизвестена смърт",
        "Коварен",
        "Кошмар на Елм стрийт"
    ],
    "Комедия": [
        "Сам вкъщи",
        "Ергенският запой",
        "От глупав по-глупав",
        "Мистър Бийн",
        "Големи момчета"
    ]
}

# Памет за статистика
if "genre_votes" not in st.session_state:
    st.session_state.genre_votes = {g: 0 for g in movies.keys()}

if "movie_votes" not in st.session_state:
    st.session_state.movie_votes = {
        movie: 0 for films in movies.values() for movie in films
    }

# Избор
genre = st.selectbox("🎭 Избери жанр:", list(movies.keys()))
movie = st.selectbox("🎥 Избери филм:", movies[genre])

# Бутон
if st.button("Запази избора"):
    st.session_state.genre_votes[genre] += 1
    st.session_state.movie_votes[movie] += 1
    st.success("Изборът е записан!")

st.divider()
st.subheader("📊 Статистика")

# Най-избирани
top_genre = max(st.session_state.genre_votes, key=st.session_state.genre_votes.get)
top_movie = max(st.session_state.movie_votes, key=st.session_state.movie_votes.get)

st.write("🏆 Най-избиран жанр:", top_genre)
st.write("🎬 Най-избиран филм:", top_movie)

# Графики
genre_df = pd.DataFrame.from_dict(
    st.session_state.genre_votes, orient="index", columns=["Брой"]
)
movie_df = pd.DataFrame.from_dict(
    st.session_state.movie_votes, orient="index", columns=["Брой"]
)

st.bar_chart(genre_df)
st.bar_chart(movie_df)

