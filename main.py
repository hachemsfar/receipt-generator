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


user_input = "How to cook Tunisian Fricassé Recipe? ingredients and instructions"
response = generate_response(user_input)
print("-------------------------")
print(response)

st.write(response)

