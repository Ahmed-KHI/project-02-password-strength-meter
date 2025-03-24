import streamlit as st
import re
import random
import string

# styling
st.markdown("""
    <style>
        /* Global Styles */
        body {
            background: #1B1B1B; /* Dark background for a futuristic, metallic look */
            font-family: 'Roboto', sans-serif;
            color: #E0E0E0; /* Light gray for text */
        }

        /* Header Styles */
        h1 {
            text-align: center;
            color: #FF0000; /* Transformers Red */
            font-size: 50px;
            font-weight: 800;
            margin-top: 50px;
            text-transform: uppercase;
        }

        /* Password input field */
        .stTextInput input {
            font-size: 18px;
            padding: 12px;
            border-radius: 15px;
            border: 2px solid #0A74DA; /* Cyber blue border */
            background-color: #2A2A2A;
            color: #E0E0E0;
            width: 75%;
            margin: 0 auto;
            display: block;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }

        .stTextInput input:focus {
            border-color: #FF0000; /* Red border when focused */
            outline: none;
        }

        /* Button Styles */
        .stButton button {
            background-color: #0A74DA; /* Cyber blue */
            color: white;
            padding: 12px 25px;
            border-radius: 50px; /* Round edges for futuristic look */
            font-size: 16px;
            font-weight: 700;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
            margin: 15px;
            display: inline-block;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }

        .stButton button:hover {
            background-color: #005A7C; /* Darker blue on hover */
            transform: scale(1.05);
        }

        /* Password strength display */
        .strength-indicator {
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            color: #FFDD00; /* Yellow similar to Transformers */
            margin-top: 30px;
        }

        .strength-indicator.strong {
            color: #2E8B57; /* Green for strong */
        }

        .strength-indicator.medium {
            color: #FFD700; /* Gold for medium */
        }

        .strength-indicator.weak {
            color: #FF4500; /* Red for weak */
        }

        /* Suggestions */
        .suggestions {
            font-size: 16px;
            color: #FFFFFF;
            background-color: rgba(0, 0, 0, 0.7); /* Dark background */
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: left;
        }

        .suggestions ul {
            list-style-type: none;
            padding-left: 0;
        }

        .suggestions li {
            margin: 8px 0;
            font-weight: 600;
        }

        /* Strong password display */
        .strong-password {
            background-color: #333333; /* Metallic gray */
            color: #FFDD00; /* Yellow text */
            padding: 18px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 40px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        }

        /* Flex container for side-by-side buttons */
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }

        /* Button spacing */
        .button-container .stButton {
            margin-right: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚙️ Password Strength Meter</h1>", unsafe_allow_html=True)


password = st.text_input("Enter your password:", type="password", placeholder="Enter a secure password...")

# Password strength checker function
def check_strength(password):
    length_criteria = len(password) >= 12
    lower_case = bool(re.search(r"[a-z]", password))
    upper_case = bool(re.search(r"[A-Z]", password))
    digit = bool(re.search(r"\d", password))
    special_char = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    strength = sum([length_criteria, lower_case, upper_case, digit, special_char])

    suggestions = []
    if not length_criteria:
        suggestions.append("🔹 Use at least 12 characters for better security.")
    if not lower_case:
        suggestions.append("🔹 Add lowercase letters (a-z).")
    if not upper_case:
        suggestions.append("🔹 Include uppercase letters (A-Z).")
    if not digit:
        suggestions.append("🔹 Add numbers (0-9).")
    if not special_char:
        suggestions.append("🔹 Use special characters like (!@#$%^&*).")

    if strength == 5:
        return "🟢 Strong", suggestions
    elif strength >= 3:
        return "🟡 Medium", suggestions
    else:
        return "🔴 Weak", suggestions

# Strong password generator function
def generate_strong_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(16))  # Increased length for stronger passwords

# Display strength and suggestions
if password:
    strength, suggestions = check_strength(password)
    st.markdown(f"<div class='strength-indicator {strength.lower()}'>{strength} Password</div>", unsafe_allow_html=True)

    if suggestions:
        st.markdown("<div class='suggestions'><strong>💡 Suggestions to Improve Your Password:</strong><ul>", unsafe_allow_html=True)
        for suggestion in suggestions:
            st.markdown(f"<li>{suggestion}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

# Generate a strong password with a button
with st.container():
    # Button actions
    st.markdown("""
        
    """, unsafe_allow_html=True)

    # Button actions
    if st.button("🔑 Check Password Strength"):
        st.write("Checking your password strength...")
    
    if st.button("✨ Generate Strong Password"):
        strong_password = generate_strong_password()
        st.markdown(f"<div class='strong-password'>💪 Your Strong Password: {strong_password}</div>", unsafe_allow_html=True)
