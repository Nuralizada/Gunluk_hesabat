import streamlit as st

# İstifadəçi məlumatlarını saxlayan bir dict (fayl yerinə)
USER_DATA = {
    "Natiq.Rasulzada": "gunluk123",  # İstifadəçi ID: parol
    "Gulchin.Nuralizada.ADY": "gunluk2501",
    "Lalezar.Hanifayeva": "gunluk0303",
    "Lala.Rzayeva.ADY": "gunlukhesabat123",
    "Adil.Movsumov": "Pilotboeing737"
}

# Session State-də identifikasiya vəziyyətini və istifadəçi ID-ni yoxlamaq
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_id = None

if not st.session_state.authenticated:
    st.title("Tətbiqə Giriş")
    
    # İstifadəçidən ID və parol tələb olunur
    user_id = st.text_input("ID:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Giriş"):
        # İstifadəçi ID və parol yoxlanılır
        if user_id in USER_DATA and USER_DATA[user_id] == password:
            st.session_state.authenticated = True
            st.session_state.user_id = user_id
            st.success(f"Giriş uğurlu oldu! Xoş gəldiniz, {user_id}.")
        else:
            st.error("Yanlış istifadəçi ID və ya parol.")
else: 
