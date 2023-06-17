import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

DATA_URL = (
    "/home/rhyme/Desktop/Project/Motor_Vehicle_Collisions_-_Crashes.csv"
)
st.title("Motor Vehicle Collisions in New York City")

st.markdown("This application is a Streamlit dashboard that can be used to "
"analyze motor vehicle in NYC 🗽💥🚗")


#- ------------------------------------
# Loading motor vehicle collison data
#- ------------------------------------
@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])

    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time':'date/time'}, inplace=True)
    return data

data = load_data(100000)    # load the data
ORIGINAL_DATA = data
#- ------------------------
# Visualizing Data on map
#- ------------------------
st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of people injured in vehicle accident",0,19)
st.map(data.query('injured_persons >= @injured_people')[["latitude", "longitude"]].dropna(how="any"))


#- ------------------------------------
# Filtering Data and interactive Tables
#- ------------------------------------
st.header("how many collisons occur during a given time of day")
# hour = st.selectbox("Hour to look at", range(0,24),1) # enter value in selectbox
# hour = st.sidebar.slider("Hour to look at", 0,23) # slider at sidebar
hour = st.slider("Hour to look at", 0,23)
data = data[data['date/time'].dt.hour==hour]


#- ------------------------------------------
# Plot Filtered Data on a 3D interactive map
#- ------------------------------------------
st.markdown("Vehicle colllisions occured between %i:00 and %i:00" % (hour, (hour+1)%24))
midpoint = (np.average(data['latitude']), np.average(data['longitude']))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state = {
        'latitude': midpoint[0],
        'longitude': midpoint[1],
        'zoom':11,
        "pitch":50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data[['date/time', 'latitude','longitude']],
            get_position = ['longitude', 'latitude'],
            radius=100,
            extruded=True,
            pickable=True,
            elevation_scale=4,
            elevation_range=[0,1000]
        ),
    ],
))

#- -----------------------
# Charts and Histograms
#- -----------------------
st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour+1)%24))
filtered = data[
    (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour+1))
]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0,60))[0]
chard_data = pd.DataFrame({'minute':range(60), 'crashes':hist})
fig = px.bar(chard_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig )

# print(data[['date/time', 'latitude','longitude']])


#- -----------------------------
# Select Data Using Dropdowns
#- -----------------------------
st.header("Top 5 dangerous streets by affected type")
select = st.selectbox("Affected type of people", ['Pedestrians', 'Cyclists', 'Motorists'])
if select == 'Pedestrians':
        st.write(ORIGINAL_DATA.query("injured_pedestrians >= 1")[["on_street_name", "injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how='any'))
elif select == 'Cyclists':
        st.write(ORIGINAL_DATA.query("injured_cyclists >= 1")[["on_street_name", "injured_cyclists"]].sort_values(by=['injured_cyclists'], ascending=False).dropna(how='any'))
else:
        st.write(ORIGINAL_DATA.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how='any'))
# checkbox to show/hide the data
if st.checkbox("Show Raw Data", False):
    # Display the data
    st.subheader('Raw Data')
    st.write(data)
