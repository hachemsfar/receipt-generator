import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit

import openai

openai.api_key = st.secrets["API"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature = 0.7,
        max_tokens = 1024,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0.5
    )

    return response.choices[0].text.strip()


user_input = "How to cook Tunisian Fricassé? I need the answer in HTML"
response = generate_response(user_input)
print(response)

# Render the h1 block, contained in a frame of size 200x200.
components.html(response, width=200, height=200)
