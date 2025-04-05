# import streamlit as st
# import requests
# from datetime import datetime, date
# import random

# # --- GLOBAL CONSTANTS ---
# BMI_CATEGORIES = {
#     18.5: "Underweight",
#     25: "Normal weight",
#     30: "Overweight",
#     float('inf'): "Obese",
# }

# DIET_PLANS = {
#     "Overweight": [
#         "Focus on whole, unprocessed foods.",
#         "Increase intake of fruits, vegetables, and lean proteins.",
#         "Limit sugary drinks, processed snacks, and high-fat foods.",
#         "Control portion sizes and practice mindful eating.",
#         "Aim for at least 30 minutes of moderate-intensity exercise daily.",
#         "Consider consulting a nutritionist for a personalized plan."
#     ],
#     "Underweight": [
#         "Focus on calorie-dense, nutrient-rich foods.",
#         "Include healthy fats, whole grains, and adequate protein in each meal.",
#         "Eat frequent, smaller meals throughout the day.",
#         "Consider adding healthy snacks between meals.",
#         "Engage in strength training exercises to build muscle mass.",
#         "Consult a nutritionist for personalized guidance."
#     ],
#     "Maintain Shape": [
#         "Maintain a balanced intake of all food groups.",
#         "Prioritize whole foods and limit processed items.",
#         "Engage in regular physical activity that you enjoy.",
#         "Listen to your body's hunger and fullness cues.",
#         "Stay hydrated by drinking enough water throughout the day.",
#         "Ensure you are getting adequate sleep for overall well-being."
#     ]
# }

# MOOD_OPTIONS = ["😊 Happy", "😔 Sad", "😠 Angry", "😌 Relaxed", "😟 Worried", "🥳 Excited", "😴 Tired", "🤔 Confused", "Other"]

# # --- HELPER FUNCTIONS ---
# def get_motivational_quote():
#     try:
#         response = requests.get("https://api.quotable.io/random")
#         response.raise_for_status()  # Raise an exception for bad status codes
#         return response.json().get("content", "Stay strong. You are capable of amazing things.")
#     except requests.exceptions.RequestException as e:
#         st.warning(f"Could not fetch a motivational quote at the moment. Here's one for you: Stay strong. You are capable of amazing things.")
#         return "Stay strong. You are capable of amazing things."

# def convert_currency(amount, from_currency, to_currency):
#     try:
#         url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         rate = data["rates"].get(to_currency.upper())
#         if rate:
#             return amount * rate
#         return None
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error fetching exchange rate: {e}")
#         return None

# def calculate_bmi(weight_kg, height_m):
#     if height_m > 0:
#         return weight_kg / (height_m ** 2)
#     return None

# def get_bmi_category(bmi):
#     if bmi is None:
#         return "N/A"
#     for limit, category in BMI_CATEGORIES.items():
#         if bmi < limit:
#             return category
#     return "Obese"

# def get_diet_plan(goal):
#     return DIET_PLANS.get(goal, ["No specific diet plan found for this goal."])

# def display_diet_plan(plan):
#     st.subheader("🍎 Your Recommended Diet Plan:")
#     for item in plan:
#         st.markdown(f"- {item}")

# def record_activity(activity_type, value, unit, notes=""):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(f"{activity_type}_log.txt", "a") as f:
#         f.write(f"[{timestamp}] {value} {unit} - {notes}\n")
#     st.success(f"{activity_type.capitalize()} recorded successfully!")

# # --- MAIN APP ---
# def run_habit_tracker():
#     # --- CONFIG ---
#     st.set_page_config(page_title="Mindful Momentum: Your Personal Growth Hub", layout="centered", page_icon="✨")

#     # --- STYLING ---
#     st.markdown("""
#         <style>
#         body {
#             background-color: #f4f4f4;
#             color: #333;
#             font-family: sans-serif;
#         }
#         .stApp {
#             background-color: #e6e6e6;
#         }
#         .block-container {
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#             background-color: white;
#             border-radius: 10px;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#             padding-left: 20px;
#             padding-right: 20px;
#             margin-bottom: 1em;
#         }
#         .main-title {
#             font-size: 3.0rem;
#             color: #007bff;
#             font-weight: bold;
#             text-align: center;
#             margin-bottom: 1.0em;
#             text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
#         }
#         .section-title {
#             font-size: 2.0rem;
#             color: #28a745;
#             margin-top: 1.5em;
#             margin-bottom: 0.8em;
#             border-bottom: 3px solid #28a745;
#             padding-bottom: 0.3em;
#         }
#         .quote-box {
#             background-color: #f9f9f9;
#             padding: 1.5em;
#             border-radius: 0.5em;
#             margin-top: 1em;
#             border-left: 5px solid #ffc107;
#             box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.05);
#         }
#         .metric-value {
#             font-size: 1.8rem !important;
#             color: #007bff !important;
#         }
#         .metric-label {
#             font-size: 1.1rem !important;
#             color: #6c757d !important;
#         }
#         .st-form {
#             background-color: #f9f9f9;
#             padding: 1.5em;
#             border-radius: 0.5em;
#             box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.05);
#         }
#         .st-selectbox > div > label,
#         .st-number-input > label,
#         .st-text-input > label,
#         .st-date-input > label,
#         .st-text-area > label {
#             color: #555;
#         }
#         .st-button > button {
#             background-color: #007bff;
#             color: white;
#             border: none;
#             border-radius: 0.3em;
#             padding: 0.8em 1.5em;
#             font-size: 1rem;
#             cursor: pointer;
#             transition: background-color 0.3s ease;
#         }
#         .st-button > button:hover {
#             background-color: #0056b3;
#         }
#         .st-success {
#             color: #198754;
#             background-color: #d1e7dd;
#             padding: 0.8em;
#             border-radius: 0.3em;
#             margin-top: 0.5em;
#         }
#         .st-warning {
#             color: #ffc107;
#             background-color: #fff3cd;
#             padding: 0.8em;
#             border-radius: 0.3em;
#             margin-top: 0.5em;
#         }
#         .st-error {
#             color: #dc3545;
#             background-color: #f8d7da;
#             padding: 0.8em;
#             border-radius: 0.3em;
#             margin-top: 0.5em;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # --- TITLE ---
#     st.markdown('<div class="main-title">✨ Mindful Momentum ✨</div>', unsafe_allow_html=True)
#     st.markdown('<p style="text-align: center; color: #777;">Your Personal Growth & Well-being Companion</p>', unsafe_allow_html=True)

#     with st.container():
#         st.markdown('<div class="section-title">🚫 Habit Breaker</div>', unsafe_allow_html=True)
#         with st.form("habit_form", clear_on_submit=True):
#             habit = st.text_input("Habit you want to quit:", placeholder="e.g., Smoking, Junk Food, Late Nights")
#             reason = st.text_area("Why do you want to quit this habit?", height=70)
#             start_date = st.date_input("When did you start quitting?", value=date.today())
#             submitted = st.form_submit_button("Track Progress")

#         if submitted and habit:
#             days_clean = (datetime.now().date() - start_date).days
#             life_gained = round(days_clean * 0.003, 2)  # 3 minutes = 0.003 hours per day

#             col1, col2 = st.columns(2)
#             with col1:
#                 st.metric(label="🧭 Days Clean", value=f"{days_clean} days")
#             with col2:
#                 st.metric(label="💖 Life Gained (approx.)", value=f"{life_gained} hrs")

#             st.markdown(f"### 📝 Reason to Quit:\n> _{reason}_")

#     with st.container():
#         # --- MOTIVATIONAL QUOTE ---
#         st.markdown('<div class="section-title">🌈 Daily Inspiration</div>', unsafe_allow_html=True)
#         quote = get_motivational_quote()
#         st.markdown(f'<div class="quote-box">🗣️ <em>"{quote}"</em></div>', unsafe_allow_html=True)

#     with st.container():
#         # --- CURRENCY CONVERTER ---
#         st.markdown('<div class="section-title">💱 Currency Converter</div>', unsafe_allow_html=True)
#         col3, col4, col5 = st.columns(3)
#         with col3:
#             amount = st.number_input("Amount", value=1.0, min_value=0.0)
#         with col4:
#             from_currency = st.text_input("From", value="USD")
#         with col5:
#             to_currency = st.text_input("To", value="INR")

#         if st.button("Convert"):
#             converted = convert_currency(amount, from_currency, to_currency)
#             if converted:
#                 st.success(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
#             else:
#                 st.error("Currency conversion failed. Please check currency codes.")

#     with st.container():
#         # --- WEIGHT & BMI ---
#         st.markdown('<div class="section-title">⚖️ Body Metrics</div>', unsafe_allow_html=True)
#         weight_kg = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=0.1)
#         height_m = st.number_input("Enter your height (in meters):", min_value=0.5, max_value=3.0, step=0.01)

#         if st.button("Calculate BMI"):
#             bmi = calculate_bmi(weight_kg, height_m)
#             bmi_category = get_bmi_category(bmi)
#             if bmi:
#                 st.metric("Your BMI", value=f"{bmi:.2f}", delta=bmi_category)
#             else:
#                 st.warning("Please enter a valid height.")

#     with st.container():
#         # --- DIET PLAN ---
#         st.markdown('<div class="section-title">🍎 Personalized Diet Guidance</div>', unsafe_allow_html=True)
#         goal = st.selectbox("What is your primary health goal?", ["Maintain Shape", "Overweight", "Underweight"])
#         if st.button("Show Diet Plan"):
#             plan = get_diet_plan(goal)
#             display_diet_plan(plan)

#     with st.container():
#         # --- CALORIE TRACKER ---
#         st.markdown('<div class="section-title">🔥 Calorie Journal</div>', unsafe_allow_html=True)
#         col_c1, col_c2 = st.columns(2)
#         with col_c1:
#             calories_consumed = st.number_input("Calories Consumed:", min_value=0)
#             food_notes = st.text_area("Notes on consumed food (optional):", height=70)
#             if st.button("Log Consumed", key="log_consumed"):
#                 record_activity("calories_consumed", calories_consumed, "kcal", food_notes)
#         with col_c2:
#             calories_burnt = st.number_input("Calories Burnt:", min_value=0)
#             exercise_notes = st.text_area("Notes on exercise (optional):", height=70)
#             if st.button("Log Burnt", key="log_burnt"):
#                 record_activity("calories_burnt", calories_burnt, "kcal", exercise_notes)

#     with st.container():
#         # --- SLEEP TRACKER ---
#         st.markdown('<div class="section-title">😴 Sleep Log</div>', unsafe_allow_html=True)
#         sleep_hours = st.number_input("Hours of sleep last night:", min_value=0.0, max_value=15.0, step=0.5)
#         sleep_notes = st.text_area("Notes on your sleep (optional):", height=70)
#         if st.button("Log Sleep"):
#             record_activity("sleep", sleep_hours, "hours", sleep_notes)

#     with st.container():
#         # --- MOOD TRACKER ---
#         st.markdown('<div class="section-title">😊 Mood Diary</div>', unsafe_allow_html=True)
#         mood = st.selectbox("How are you feeling today?", MOOD_OPTIONS)
#         mood_notes = st.text_area("Notes on your mood (optional):", height=70)
#         if st.button("Log Mood"):
#             record_activity("mood", mood, "", mood_notes)

#     with st.container():
#         # --- REFLECTION JOURNAL ---
#         st.markdown('<div class="section-title">🧠 Daily Reflection</div>', unsafe_allow_html=True)
#         reflection = st.text_area("What's on your mind today?", height=150, placeholder="Write your thoughts, struggles, or wins...")
#         if st.button("Save Reflection"):
#             with open("habit_journal.txt", "a") as f:
#                 f.write(f"\n[{datetime.now()}]\n{reflection}\n")
#             st.success("Your reflection has been saved.")

#             st.progress(min(streak / 30, 1.0), text=f"Streak Goal: {streak}/30 days")


#     # --- FOOTER ---
#     st.markdown("""---""")
#     st.caption("🛠️ Built with Streamlit · ❤️ Empowering your journey to well-being.")

# if __name__ == "__main__":
#     run_habit_tracker()




# import random
# import streamlit as st
# import requests
# from datetime import datetime, date

# # --- PAGE CONFIG ---
# st.set_page_config(page_title="Sanctuary of Self: A habit tracker", layout="centered", page_icon="❄️")

# # --- CUSTOM STYLING ---
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(to bottom, #1a1a1a, #2e3b47);
#         color: #e0f2f7;
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
#     .main-title {
#         font-size: 3rem;
#         color: #8ab4f8;
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .section-title {
#         font-size: 2rem;
#         color: #a7ffeb;
#         margin-top: 2rem;
#         border-bottom: 2px solid #a7ffeb;
#         padding-bottom: 0.5rem;
#     }
#     .quote-box {
#         background-color: rgba(255, 255, 255, 0.05);
#         padding: 1.2em;
#         border-radius: 0.5em;
#         margin-top: 1em;
#         border-left: 4px solid #b3e5fc;
#         font-style: italic;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- MOCK HELPER FUNCTIONS ---
# def calculate_bmi(weight, height):
#     if height > 0:
#         return weight / (height ** 2)
#     return None

# def get_bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif bmi < 25:
#         return "Normal weight"
#     elif bmi < 30:
#         return "Overweight"
#     else:
#         return "Obese"

# def get_exercise_suggestion(category):
#     suggestions = {
#         "Underweight": "Focus on strength training and a calorie-rich diet.",
#         "Normal weight": "Maintain with regular cardio and strength sessions.",
#         "Overweight": "Include moderate cardio and light resistance workouts.",
#         "Obese": "Begin with low-impact cardio like walking or swimming."
#     }
#     return suggestions.get(category, "Stay active and listen to your body.")

# def get_diet_plan(goal):
#     plans = {
#         "Maintain Shape": ["Balanced meals", "Stay hydrated", "Eat regularly"],
#         "Overweight": ["Reduce sugar intake", "More vegetables", "Lean proteins"],
#         "Underweight": ["High-calorie snacks", "More frequent meals", "Protein shakes"]
#     }
#     return plans.get(goal, [])

# def display_diet_plan(plan):
#     st.subheader("🥗 Suggested Diet Plan:")
#     for item in plan:
#         st.markdown(f"- {item}")

# def record_activity(category, value, unit, notes):
#     st.success(f"Logged {value} {unit} for {category.replace('_', ' ').title()}.")
#     if notes:
#         st.markdown(f"📝 Notes: _{notes}_")

# def get_motivational_quote():
#     quotes = [
#         "Stay strong. Your habits don’t define you — your commitment does.",
#         "You’re doing better than you think.",
#         "Progress is progress, no matter how small.",
#         "Let go of the old you to become the new you.",
#     ]
#     return random.choice(quotes)

# def convert_currency(amount, from_currency, to_currency):
#     try:
#         url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
#         response = requests.get(url)
#         data = response.json()
#         rate = data['rates'][to_currency.upper()]
#         return amount * rate
#     except Exception:
#         return None

# # --- MAIN APP ---
# def run_habit_tracker():
#     st.markdown('<div class="main-title">❄️ Sanctuary of Self ❄️</div>', unsafe_allow_html=True)
#     st.markdown('<p style="text-align: center; color: #dcedc8;">A Chillingly Calm Chronicle of Your Well-being</p>', unsafe_allow_html=True)

#     # --- HABIT TRACKING ---
#     st.markdown('<div class="section-title">🧊 Habit Alleviation</div>', unsafe_allow_html=True)
#     with st.form("habit_form", clear_on_submit=True):
#         habit = st.text_input("Habit you seek to release:", placeholder="e.g., Late-night scrolling, Sugary cravings")
#         reason = st.text_area("Reflect on your motivation to relinquish this habit:", height=80)
#         start_date = st.date_input("Date of commencement:", value=date.today())
#         submitted = st.form_submit_button("Track Your Tranquil Progress")

#     if submitted and habit:
#         days_clean = (datetime.now().date() - start_date).days
#         life_gained = round(days_clean * 0.003, 2)
#         col1, col2 = st.columns(2)
#         with col1:
#             st.metric(label="🧊 Days of Clarity", value=f"{days_clean} days")
#         with col2:
#             st.metric(label="⏳ Estimated Time Reclaimed", value=f"{life_gained} hrs")
#         st.markdown(f"### 📜 Reason for Release:\n> _{reason}_")

#     st.markdown('<div class="section-title">⚖️ Icy Metrics & Movement</div>', unsafe_allow_html=True)
#     weight_kg = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=300.0, step=0.1)
#     height_m = st.number_input("Enter your height (meters):", min_value=0.5, max_value=3.0, step=0.01)

#     if st.button("Calculate & Seek Movement Wisdom"):
#         bmi = calculate_bmi(weight_kg, height_m)
#         if bmi:
#             bmi_category = get_bmi_category(bmi)
#             st.metric("Your BMI", value=f"{bmi:.2f}", delta=bmi_category)
#             exercise_tip = get_exercise_suggestion(bmi_category)
#             st.info(f"💡 Movement Guidance: {exercise_tip}")
#         else:
#             st.warning("Please provide a valid height for calculation.")

#     # --- DIET PLAN ---
#     st.markdown('<div class="section-title">🍎 Crystalized Nutritional Insights</div>', unsafe_allow_html=True)
#     goal = st.selectbox("Your primary wellness aspiration:", ["Maintain Shape", "Overweight", "Underweight"])
#     if st.button("Reveal Nutritional Path"):
#         plan = get_diet_plan(goal)
#         display_diet_plan(plan)

#     # --- CALORIE TRACKER ---
#     st.markdown('<div class="section-title">🔥 Embers of Energy Journal</div>', unsafe_allow_html=True)
#     col_c1, col_c2 = st.columns(2)
#     with col_c1:
#         calories_consumed = st.number_input("Calories Consumed:", min_value=0)
#         food_notes = st.text_area("Notes on nourishment (optional):", height=80)
#         if st.button("Log Intake", key="log_consumed"):
#             record_activity("calories_consumed", calories_consumed, "kcal", food_notes)
#     with col_c2:
#         calories_burnt = st.number_input("Calories Expended:", min_value=0)
#         exercise_notes = st.text_area("Notes on exertion (optional):", height=80)
#         if st.button("Log Expenditure", key="log_burnt"):
#             record_activity("calories_burnt", calories_burnt, "kcal", exercise_notes)

#     # --- MOTIVATION ---
#     st.markdown('<div class="quote-box">❄️ ' + get_motivational_quote() + "</div>", unsafe_allow_html=True)













import random
import streamlit as st
import requests
from datetime import datetime, date, timedelta
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sanctuary of Self: A habit tracker", layout="centered", page_icon="🧘")

# --- SESSION STATE INIT ---
if 'habits' not in st.session_state:
    st.session_state.habits = []
if 'mood_log' not in st.session_state:
    st.session_state.mood_log = []
if 'sleep_log' not in st.session_state:
    st.session_state.sleep_log = []
if 'streaks' not in st.session_state:
    st.session_state.streaks = {}

# --- STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic&display=swap');
    .stApp {
        background: linear-gradient(to bottom, #f1f8e9, #e8f5e9);
        color: #37474f;
        font-family: 'Zen Maru Gothic', sans-serif;
    }
    .main-title {
        font-size: 3rem;
        text-align: center;
        color: #4caf50;
        text-shadow: 2px 2px 6px rgba(76, 175, 80, 0.3);
        margin-bottom: 0.5rem;
        padding-top: 0.5rem;
    }
    .section-title {
        font-size: 1.75rem;
        color: #66bb6a;
        margin-top: 2.5rem;
        border-bottom: 2px solid #a5d6a7;
        padding-bottom: 0.5rem;
        text-shadow: 1px 1px 3px rgba(102, 187, 106, 0.3);
    }
    .quote-box {
        background: rgba(255, 255, 255, 0.7);
        padding: 1.2em;
        border-left: 5px solid #c5e1a5;
        font-style: italic;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.15);
        transition: box-shadow 0.3s ease-in-out;
    }
    .quote-box:hover {
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
    }
    .stButton>button {
        background-color: #a5d6a7 !important;
        color: #2e7d32 !important;
        border: none;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(165, 214, 167, 0.3);
    }
    .stButton>button:hover {
        background-color: #81c784 !important;
        box-shadow: 0 6px 15px rgba(129, 199, 132, 0.4);
        transform: scale(1.02);
    }
    .pulse-circle {
        width: 20px;
        height: 20px;
        background: #81c784;
        border-radius: 50%;
        margin: 0 auto;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.5); opacity: 0.5; }
      100% { transform: scale(1); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Optional ambient audio
with st.sidebar:
    if st.checkbox("🔊 Play Zen Garden Music"):
        st.markdown("""
            <audio autoplay loop>
              <source src="https://dl.sndup.net/xhxq/ZEN-Ambient-Stream.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)

# --- HELPERS ---
def calculate_bmi(weight, height):
    return weight / (height ** 2) if height > 0 else None

def get_bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal weight"
    elif bmi < 30: return "Overweight"
    else: return "Obese"

def get_exercise_suggestion(category):
    return {
        "Underweight": "Focus on strength training and a calorie-rich diet.",
        "Normal weight": "Maintain with regular cardio and strength sessions.",
        "Overweight": "Include moderate cardio and light resistance workouts.",
        "Obese": "Begin with low-impact cardio like walking or swimming."
    }.get(category, "Stay active and listen to your body.")

def get_diet_plan(goal):
    return {
        "Maintain Shape": ["Balanced meals", "Stay hydrated", "Eat regularly"],
        "Overweight": ["Reduce sugar intake", "More vegetables", "Lean proteins"],
        "Underweight": ["High-calorie snacks", "More frequent meals", "Protein shakes"]
    }.get(goal, [])

def display_diet_plan(plan):
    st.subheader("🥗 Suggested Diet Plan:")
    for item in plan:
        st.markdown(f"- {item}")

def get_motivational_quote():
    quotes = [
        "Breathe in calm, breathe out stress.",
        "Your journey is your own, take it one mindful step at a time.",
        "In stillness, we find strength.",
        "Let each small act of care ripple into inner peace."
    ]
    return random.choice(quotes)

def update_streak(habit, start_date):
    today = datetime.now().date()
    if habit not in st.session_state.streaks:
        st.session_state.streaks[habit] = 0
    last_date = start_date
    if (today - last_date).days == 1:
        st.session_state.streaks[habit] += 1
    elif (today - last_date).days > 1:
        st.session_state.streaks[habit] = 1
    return st.session_state.streaks[habit]

# --- MAIN APP ---
def run_habit_tracker():
    st.markdown('<div class="main-title">🧘 Sanctuary of Self 🧘</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #689f38;">A Serene Journey into Well-being</p>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🌿 Habit Reflection</div>', unsafe_allow_html=True)
    with st.form("habit_form", clear_on_submit=True):
        habit = st.text_input("Habit you seek to release:", placeholder="e.g., Late-night scrolling")
        reason = st.text_area("Reflect on your motivation:", height=80)
        start_date = st.date_input("Date of commencement:", value=date.today())
        reminder_time = st.time_input("Reminder Time")
        submitted = st.form_submit_button("Track Your Tranquil Progress")

    if submitted and habit:
        days_clean = (datetime.now().date() - start_date).days
        life_gained = round(days_clean * 0.003, 2)
        streak = update_streak(habit, start_date)
        st.session_state.habits.append((habit, start_date))

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🌼 Days of Mindfulness", f"{days_clean} days")
        with col2:
            st.metric("⏳ Time Reclaimed", f"{life_gained} hrs")
        with col3:
            st.metric("🌸 Current Streak", f"{streak} days")

        st.markdown(f"### 📜 Reason:\n> _{reason}_")
        st.info(f"⏰ Reminder set for {reminder_time.strftime('%I:%M %p')}")

    st.markdown('<div class="section-title">📅 Calendar Overview</div>', unsafe_allow_html=True)
    if st.session_state.habits:
        data = {"Habit": [h[0] for h in st.session_state.habits],
                "Date": [h[1] for h in st.session_state.habits]}
        fig = px.timeline(x_start=data["Date"], x_end=[d + timedelta(days=1) for d in data["Date"]],
                          y=data["Habit"], color=data["Habit"])
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">🪷 Mood Tracker</div>', unsafe_allow_html=True)
    mood = st.selectbox("How are you feeling today?", ["🙂 Good", "😐 Okay", "🙁 Bad"])
    if st.button("Log Mood"):
        st.session_state.mood_log.append((datetime.now().date(), mood))
        st.success(f"Mood logged: {mood}")

    st.markdown('<div class="section-title">🌙 Sleep Tracker</div>', unsafe_allow_html=True)
    sleep_hours = st.slider("How many hours did you sleep last night?", 0, 12, 7)
    if st.button("Log Sleep"):
        st.session_state.sleep_log.append((datetime.now().date(), sleep_hours))
        st.success(f"Logged {sleep_hours} hours of sleep")

    st.markdown('<div class="section-title">🌬️ Breathing Exercise</div>', unsafe_allow_html=True)
    if st.button("Begin Breathing Exercise"):
        st.markdown('<div class="pulse-circle"></div>', unsafe_allow_html=True)
        st.info("Inhale... Hold... Exhale... Feel the peace wash over you.")

    st.markdown('<div class="section-title">🍵 Diet Plan</div>', unsafe_allow_html=True)
    goal = st.selectbox("Your primary wellness aspiration:", ["Maintain Shape", "Overweight", "Underweight"])
    if st.button("Reveal Diet"):
        plan = get_diet_plan(goal)
        display_diet_plan(plan)

    with st.expander("🌱 Daily Zen Thought"):
        st.markdown("> “The quieter you become, the more you can hear.” — Ram Dass")

    st.markdown('<div class="quote-box">🧘 ' + get_motivational_quote() + "</div>", unsafe_allow_html=True)

run_habit_tracker()
