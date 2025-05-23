import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import base64


teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Guwahati']

pipe = pickle.load(open('pipe.pkl','rb'))
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image file name
add_bg_from_local("background.jpg")  # Change this to your image file name

st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',teams)
with col2:
    bowling_team = st.selectbox('Select the bowling team',teams)

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict probability'):
    runs_left = target - score
    balls_left =120 - (overs*6)
    wickets = 10- wickets
    crr = score/overs
    rrr = runs_left*6/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                             'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],
                             'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + " - " + str(round(win*100))+ "%")
    st.header(bowling_team + " - " + str(round(loss*100)) + "%")

    # Pie Chart
    fig, ax = plt.subplots()
    ax.pie([win, loss], labels=[batting_team, bowling_team], autopct='%1.1f%%', startangle=70,
           colors=['#1f77b4', '#ff7f0e'])
    ax.axis('equal')
    st.pyplot(fig)