import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data():
    df=pd.read_csv("dataset.csv")
    df.drop(df.columns[0],axis=1,inplace=True)
    df.drop_duplicates(subset="track_id",keep="first",inplace=True)
    df.dropna(inplace=True)
    return df
df=load_data()
features=["danceability","energy","loudness","speechiness","acousticness","instrumentalness","valence","tempo"]
scaler=MinMaxScaler()
df[features]=scaler.fit_transform(df[features])

st.title("🎶Music Recommendation System")
st.write("Get song recommendations based on your mood and preferences!")
genre=st.selectbox("Choose Genre",sorted(df['track_genre'].unique()))
mood=st.selectbox("Choose mood",["Happy","Sad","Energetic","Calm"])
explicit=st.selectbox("Allow Explicit Lyrics?",["Yes","No"])
dance=st.selectbox("Feeling like dancing?",["Yes","No"])

mood_map={
    "Happy":{"valence":(0.6,1.0),"energy":(0.5,1.0)},
    "Sad":{"valence":(0.0,0.4),"energy":(0.0,0.6)},
    "Energetic":{"energy":(0.7,1.0)},
    "Calm":{"energy":(0.0,0.5)},
}

filtered_df=df.copy()
if genre!="":
    filtered_df = filtered_df[filtered_df['track_genre'] == genre]
if dance=="yes":
    filtered_df=filtered_df[filtered_df['danceability']>0.5]
if explicit=="yes":
    filtered_df=filtered_df[filtered_df['explicit']==True]

for key,(low,high) in mood_map[mood].items():
    filtered_df=filtered_df[(filtered_df[key]>=low) & (filtered_df[key]<=high)]

if not filtered_df.empty:
    reference_vector=filtered_df[features].mean().values.reshape(1,-1)
    filtered_df['similarity']=cosine_similarity(filtered_df[features],reference_vector).flatten()
    recommendations=filtered_df.sort_values(by="similarity",ascending=False).head(5)
    st.subheader("🎧Recommended Tracks")
    for idx,row in recommendations.iterrows():
        st.write(f"**{row['track_name']}** by *{row["artists"]}*")
        st.caption(f"Album:{row['album_name']} | Popularity:{row["popularity"]}")
else:
    st.warning("No tracks found for this combination. Try different filters!")