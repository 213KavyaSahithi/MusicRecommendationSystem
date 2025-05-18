# 🎶 Music Recommendation System

A personalized music recommendation web app built using **Python**, **Streamlit**, and **scikit-learn**. This app helps users discover music based on their **mood**, **genre**, and **listening preferences** like danceability and explicit content.

🌐 **Live App**: [Click here to try it out!](https://213kavyasahithi-musicrecommendationsystem-app-6iqk3b.streamlit.app/)

---

## 📌 Features

- 🔍 Filter music by **genre**
- 😊 Select your current **mood** – Happy, Sad, Energetic, or Calm
- 💃 Enable **danceability** filter
- 🚫 Option to **exclude explicit lyrics**
- 📊 Uses **cosine similarity** on scaled audio features to recommend songs

---

## 📂 Dataset

The app expects a `dataset.csv` file with the following columns:

- `track_id`, `track_name`, `artists`, `album_name`, `track_genre`, `popularity`, `explicit`
- Audio features: `danceability`, `energy`, `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `valence`, `tempo`

---

## 🧠 How It Works
- The dataset is loaded and cleaned on app start.
- Selected audio features are scaled using MinMaxScaler.
- Based on the user's selected mood (e.g., "Happy"), a corresponding feature range (like high valence) is applied.
- Cosine similarity compares the songs' feature vectors against the average mood vector.
- The top 5 most similar tracks are recommended to the user.
