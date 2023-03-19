import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit

import openai

openai.api_key = st.secrets["API"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.8,
        max_tokens=100,
        n=1,
        stop="\n"
    )

    return(response.choices[0].text.strip())


user_input = "How to cook Tunisian Fricassé Recipe? ingredients and instructions"
response = generate_response(user_input)
print("-------------------------")
print(response)

st.write(response)

