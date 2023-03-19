import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import openai

openai.api_key = st.secrets["API"]


# Define the GPT-3 prompt
def generate_recipe(dish_name):
    prompt = f"Generate a recipe for {dish_name}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recipe = response.choices[0].text.strip()
    return recipe

# Define the Streamlit app
def app():
    st.title("Recipe Generator")

    # Get user input
    dish_name = st.text_input("Enter the name of a dish:")
    if not dish_name:
        return

    # Generate recipe
    recipe = generate_recipe(dish_name)

    # Display results
    st.header("Ingredients:")
    ingredients = recipe.split("Instructions:")[0]
    st.write(ingredients)

    st.header("Instructions:")
    instructions = recipe.split("Instructions:")[1]
    st.write(instructions)

if __name__ == "__main__":
    app()
