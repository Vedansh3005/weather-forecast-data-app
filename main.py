import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Places:")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to veiw:",
                      ("Temprature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filter_data = get_data(place=place, forecast_day=days)
        if option == "Temprature":
            temprature = [dict["main"]["temp"] / 10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=dates, y=temprature, labels={"x": "Dates", "y": "Temprature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            dates = [dict["dt_txt"] for dict in filter_data]
            filter_data = [dict["weather"][0]["main"] for dict in filter_data]
            image_paths = [images[condition] for condition in filter_data]
            st.image(image_paths, caption=dates,  width=115)
    except KeyError:
        st.error("Please enter valid place.")