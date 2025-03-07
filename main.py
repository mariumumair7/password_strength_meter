import re
import random
import streamlit as st
import pandas as pd

SPECIAL_CHARACTERS = "!@#$%^&*"

def check_password_strength(password):
    """Evaluates password strength and provides feedback."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(rf"[{re.escape(SPECIAL_CHARACTERS)}]", password):
        score += 1
    else:
        feedback.append(f"❌ Include at least one special character ({SPECIAL_CHARACTERS}).")

    return score, feedback

def generate_strong_password(length=12):
    """Generates a strong random password."""
    uppercase = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = random.choice("abcdefghijklmnopqrstuvwxyz")
    digit = random.choice("0123456789")
    special_char = random.choice(SPECIAL_CHARACTERS)

    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + SPECIAL_CHARACTERS
    remaining_chars = "".join(random.choices(all_chars, k=length - 4))

    password_list = list(uppercase + lowercase + digit + special_char + remaining_chars)
    random.shuffle(password_list)

    return "".join(password_list)

st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength and get suggestions.")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password! 🚀")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        for msg in feedback:
            st.write(msg)

        if score < 4:
            st.write(f"💡 Suggested Strong Password: **{generate_strong_password()}**")
    else:
        st.warning("⚠️ Please enter a password.")

df = pd.DataFrame({
    "Criteria": ["Length (>=8)", "Upper & Lowercase", "Digit (0-9)", "Special Character"],
    "Required": ["✔", "✔", "✔", "✔"]
})
st.write("### Password Strength Criteria:")
st.dataframe(df, hide_index=True)

