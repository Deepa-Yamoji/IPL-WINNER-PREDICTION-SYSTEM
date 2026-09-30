# 🏏 IPL Winning Team Prediction System

A Machine Learning based web application that predicts the **winning team in an IPL match** using match information such as teams, toss result, venue, current score, wickets, overs, and run rate.

## 📌 Project Overview

The **IPL Winning Team Prediction System** uses Machine Learning to analyze cricket match conditions and predict which team has a higher probability of winning.

The project includes a user-friendly **Streamlit web application** where users can enter match details and get a prediction.

## ✨ Features

- 🏏 Predict the likely winning team
- 👥 Select batting team and opponent
- 🪙 Enter toss information
- 🏟️ Select venue and city
- 📊 Enter current score, wickets, and overs
- ⚡ Calculate current run rate
- 🤖 Machine Learning based prediction
- 💻 Simple and interactive Streamlit interface

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Jupyter Notebook**
- **Random Forest Classifier**
- **Pickle**

## 📂 Project Structure

```text
IPL-WINNER-PREDICTION-SYSTEM/
│
├── app.py
├── create_training_data.py
├── ipl_model.pkl
├── imputer.pkl
├── live_imputer.pkl
├── IPL_WINNING_TEAM_PREDICTION.ipynb
├── IPL WINNING TEAM PREDICTION.pdf
├── IPL WINNING TEAM PREDICTION - Made with Clipchamp.mp4
├── .gitignore
└── README.md
```

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for predicting the match winner.

The prediction is based on features such as:

- Team
- Opponent
- Toss Winner
- Venue
- City
- Current Score
- Wickets Lost
- Overs Completed
- Run Rate

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Deepa-Yamoji/IPL-WINNER-PREDICTION-SYSTEM.git
```

### 2. Open the project folder

```bash
cd IPL-WINNER-PREDICTION-SYSTEM
```

### 3. Install the required libraries

```bash
pip install streamlit pandas numpy scikit-learn
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 How It Works

1. Enter the IPL match details.
2. Enter the current match situation.
3. The application calculates the run rate.
4. The trained Machine Learning model processes the information.
5. The application displays the predicted winning team.

## 📚 Project Documentation

The repository also contains:

- 📓 Jupyter Notebook – Machine Learning development
- 📄 PDF – Project documentation
- 🎥 MP4 – Project demonstration video

## ⚠️ Note

The large `live_ipl_model.pkl` file is intentionally not included in the GitHub repository because of GitHub's file-size limitations.

## 🎯 Future Improvements

- Improve prediction accuracy with more IPL match data
- Add real-time IPL match data
- Add prediction probability/percentage
- Add match statistics and visualizations
- Deploy the application online

## 👨‍💻 Author

**Deepa Yamoji**

---

⭐ If you find this project useful, consider giving the repository a star!
