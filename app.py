
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# Page configuration
# ==========================================

st.set_page_config(
    page_title="IPL Live Winner Prediction",
    page_icon="🏏",
    layout="wide"
)

# ==========================================
# Load model
# ==========================================

model = joblib.load("live_ipl_model.pkl")
ct = joblib.load("live_transform.pkl")
imputer = joblib.load("live_imputer.pkl")

# ==========================================
# Title
# ==========================================

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    ">
        <h1 style="color: white; margin-bottom: 5px;">
            🏏 IPL WINNING TEAM PREDICTION
        </h1>
        <p style="color: #dbeafe; font-size: 18px; margin: 0;">
            AI-powered live match winner prediction
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Enter the current match situation to predict the likely winning team."
)

st.divider()

# ==========================================
# Team list
# ==========================================

teams = [
    "Royal Challengers Bangalore",
    "Punjab Kings",
    "Mumbai Indians",
    "Chennai Super Kings",
    "Kolkata Knight Riders",
    "Rajasthan Royals",
    "Sunrisers Hyderabad",
    "Delhi Capitals",
    "Gujarat Titans",
    "Lucknow Super Giants"
]

# ==========================================
# Match information
# ==========================================

st.markdown(
    """
    <div style="
        background: #f8fafc;
        padding: 12px 18px;
        border-left: 6px solid #2563eb;
        border-radius: 10px;
        margin: 10px 0 15px 0;
    ">
        <h2 style="margin: 0; color: #1e293b;">
            🏏 Match Information
        </h2>
        <p style="margin: 5px 0 0 0; color: #64748b;">
            Select the teams, toss winner and venue
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    team = st.selectbox(
        "Batting Team",
        teams
    )

with col2:
    opponent_options = [
        t for t in teams
        if t != team
    ]

    opponent = st.selectbox(
        "Opponent",
        opponent_options
    )

col3, col4 = st.columns(2)

with col3:
    toss_winner = st.selectbox(
        "Toss Winner",
        [team, opponent]
    )

with col4:
    venue = st.selectbox(
        "Venue",
        [
            "St George's Park",
            "Kingsmead",
            "SuperSport Park",
            "Buffalo Park",
            "New Wanderers Stadium",
            "De Beers Diamond Oval",
            "OUTsurance Oval",
            "Brabourne Stadium",
            "Sardar Patel Stadium, Motera",
            "Barabati Stadium",
            "Vidarbha Cricket Association Stadium, Jamtha",
            "Himachal Pradesh Cricket Association Stadium",
            "Nehru Stadium",
            "Subrata Roy Sahara Stadium",
            "Shaheed Veer Narayan Singh International Stadium",
            "JSCA International Stadium Complex"
        ]
    )

# ==========================================
# City
# ==========================================

city = st.text_input(
    "📍 City",
    "Ahmedabad"
)

st.divider()

# ==========================================
# Live match information
# ==========================================

st.markdown(
    """
    <div style="
        background: #f8fafc;
        padding: 12px 18px;
        border-left: 6px solid #16a34a;
        border-radius: 10px;
        margin: 10px 0 15px 0;
    ">
        <h2 style="margin: 0; color: #1e293b;">
            📊 Live Match Situation
        </h2>
        <p style="margin: 5px 0 0 0; color: #64748b;">
            Enter the current score and match progress
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        display: flex;
        justify-content: space-around;
        background: #0f172a;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    ">
        <div style="text-align:center; color:white; width:33%;">
            <b>🏏 SCORE</b>
        </div>
        <div style="text-align:center; color:white; width:33%;">
            <b>🎯 WICKETS</b>
        </div>
        <div style="text-align:center; color:white; width:33%;">
            <b>⏱️ OVERS</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

with col1:
    score = st.number_input(
        "Current Score",
        min_value=0,
        max_value=300,
        value=120,
        step=1
    )

with col2:
    wickets_lost = st.number_input(
        "Wickets Lost",
        min_value=0,
        max_value=10,
        value=3,
        step=1
    )

with col3:
    overs_completed = st.number_input(
        "Overs Completed",
        min_value=0.0,
        max_value=20.0,
        value=15.0,
        step=0.1
    )

# ==========================================
# Run rate
# ==========================================

if overs_completed > 0:
    calculated_run_rate = score / overs_completed
else:
    calculated_run_rate = 0

st.metric(
    "Current Run Rate",
    f"{calculated_run_rate:.2f}"
)

st.divider()

# ==========================================
# Prediction
# ==========================================

if st.button(
    "🏆 Predict Winner",
    use_container_width=True
):

    if wickets_lost > 10:

        st.error(
            "Wickets cannot be greater than 10."
        )

    elif overs_completed > 20:

        st.error(
            "Overs cannot be greater than 20."
        )

    elif score < 0:

        st.error(
            "Score cannot be negative."
        )

    else:

        match = pd.DataFrame({
            "team": [team],
            "opponent": [opponent],
            "toss_winner": [toss_winner],
            "venue": [venue],
            "city": [city],
            "score": [score],
            "wickets_lost": [wickets_lost],
            "overs_completed": [overs_completed],
            "run_rate": [calculated_run_rate]
        })

        try:

            encoded = ct.transform(match)

            encoded_imputed = imputer.transform(
                encoded
            )

            prediction = model.predict(
                encoded_imputed
            )

            predicted_winner = prediction[0]

            st.success(
                f"🏆 Predicted Winner: {predicted_winner}"
            )

            st.info(
                f"📊 Match Situation: "
                f"{team} {score}/{wickets_lost} "
                f"({overs_completed} overs)"
            )

        except Exception as e:

            st.error(
                "Prediction failed."
            )

            st.exception(e)
            # --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 15px;
        color: #64748b;
        font-size: 14px;
    ">
        🏏 <b>IPL Live Match Winner Prediction</b>
        <br>
        Machine Learning Based Prediction System
        <br>
        <span style="font-size: 12px;">
            Built with Python • Streamlit • Scikit-learn
        </span>
    </div>
    """,
    unsafe_allow_html=True
)