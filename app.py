# app.py
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="🤰 Maternal Health Tracker", layout="centered")
st.title("🤰 Maternal Health Tracker")
st.markdown("Track your pregnancy week and stay healthy!")

st.subheader("📅 Last Menstrual Period (LMP)")
lmp = st.date_input("Select the first day of your last period:", value=None)

if lmp is None:
    st.info("Please select your LMP to begin.")
    st.stop()

today = datetime.now().date()
days_pregnant = (today - lmp).days

if days_pregnant > 280:
    st.error("⚠️ You're past 40 weeks! Please consult a doctor.")
    st.stop()
elif days_pregnant < 0:
    st.warning("⚠️ LMP cannot be in the future.")
    st.stop()

current_week = (days_pregnant // 7) + 1
due_date = lmp + timedelta(days=280)

st.metric("Current Week", f"Week {current_week}")
st.metric("Due Date", due_date.strftime("%b %d, %Y"))
st.metric("Remaining Days", (due_date - today).days)

if current_week <= 12:
    st.success("**First Trimester Tips**")
    st.markdown("- Take folic acid\n- Avoid smoking/alcohol\n- Get first checkup")
elif current_week <= 28:
    st.success("**Second Trimester Tips**")
    st.markdown("- Eat iron-rich foods\n- Start pelvic exercises\n- Monitor weight")
else:
    st.success("**Third Trimester Tips**")
    st.markdown("- Pack hospital bag\n- Watch for danger signs\n- Attend classes")

st.warning("🚨 **Danger Signs**: Severe headache, bleeding, swelling, reduced baby movement")
