import os
import streamlit as st
import requests
from PIL import Image

img = Image.open("app/orange-chill.png")
st.set_page_config(page_title="Cats", page_icon=img, layout="centered")
col1, col2 = st.columns(2)

with col1:
    st.title("Cat Collection")
with col2:
    st.image(img, width=50)


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Base URL for the FastAPI backend
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8001")

header1, header2 = st.columns(2)

with header1:
    with st.expander("Add a new cat", expanded=True):
        with st.form("adopt_form"):
            col1, col2 = st.columns(2)
            with col1:
                cat_name = st.text_input("Name", placeholder="Mia", help="Mandatory")
                colour = st.text_input("Colour", placeholder="black/white/orange...")
            with col2:
                age = st.number_input("Age", min_value=0, step=1, value=None, placeholder="ex: 2")
                fav_toy = st.text_input("Favourite Toy", placeholder="ball", help="Mandatory")

            submitted = st.form_submit_button("Save")
            if submitted:
                payload: dict[str, object] = {}
                if cat_name:
                    payload["cat_name"] = cat_name
                if fav_toy:
                    payload["fav_toy"] = fav_toy
                if colour:
                    payload["colour"] = colour
                if age is not None:
                    payload["age"] = int(age)

                if "cat_name" not in payload or "fav_toy" not in payload:
                    st.error("'Name' and 'Favourite Toy' are mandatory.")
                else:
                    try:
                        r = requests.post(f"{API_BASE_URL}/cats/", json=payload, timeout=10)
                        if r.status_code == 200:
                            st.success("Cat added!")
                        else:
                            st.error(f"Error while saving: {r.status_code} - {r.text}")
                    except Exception as e:
                        st.error(f"Error in api request: {e}")

with header2:
    st.subheader("Cat list")
    try:
        response = requests.get(f"{API_BASE_URL}/cats/", timeout=10)
    except Exception as e:
        st.error(f"Error with backend: {e}")
        response = None

    if response and response.status_code == 200:
        cats = response.json()
        if not cats:
            st.info("No cat was added yet.")
        else:
            for cat in cats:
                age_txt = f"{cat.get('age')} years old" if cat.get("age") is not None else "age not added"
                colour_txt = cat.get("colour") or "colour not added"
                st.write(f"• {cat['cat_name']} — {age_txt} — {colour_txt} — toy: {cat['fav_toy']}")
    elif response is not None:
        st.error(f"Error in get cats: {response.status_code}")
