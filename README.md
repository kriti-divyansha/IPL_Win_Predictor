**IPL Win Predictor - Machine Learning Project**

Live Demo:
👉 [Click here to try the app]([https://ipl-win-predictor.streamlit.app](https://iplwinpredictor-6hlvnmcpxnqydv8cejzyfh.streamlit.app/)

This project is an interactive web application that uses machine learning to predict the win probability of an IPL team in real time during a match. Built using Streamlit for deployment and UI, this project showcases how data science can bring insights into live sports.

📊 Overview

The IPL Win Predictor takes live match conditions as input and predicts the likelihood of a team winning. The model is trained using historical IPL data and considers several match-specific parameters to give accurate, probabilistic outcomes.

🔍 Key Features:

-Predicts win probabilities for the batting and bowling teams.

Updates dynamically based on:

-Runs remaining

-Balls left

-Wickets in hand

-Current run rate

-Required run rate

-Simple and intuitive interface using Streamlit

-Fast, real-time predictions using a trained ML model

| Component        | Technology               |
| ---------------- | ------------------------ |
| Machine Learning | Scikit-learn, Pandas     |
| Model Deployment | Streamlit                |
| UI               | HTML/CSS (via Streamlit) |
| Hosting          | Streamlit Cloud          |

🧠 How It Works

Input Features: The user provides match context (e.g., target score, current score, overs left, wickets).

Data Preprocessing: Input is transformed using label encoding and numerical scaling.

Prediction Model: A pre-trained classification model (e.g., Logistic Regression) processes the input.

Output: The model returns a percentage-based win probability for both teams, visualized in an engaging way.
