import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import openai

openai.api_key = st.secrets["API"]


def get_recipe(dish_name):
    # Define the prompt
    prompt = f"Please provide the recipe for {dish_name}."

    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the recipe from the response
    recipe = response.choices[0].text.strip()

    return recipe


# Create a Streamlit app
def main():
    # Set the app title
    st.title("Recipe App")

    # Create a text input field for the dish name
    dish_name = st.text_input("Enter the dish name:")

    # Create a button to submit the dish name
    if st.button("Submit"):
        # Call the get_recipe function to get the recipe
        recipe = get_recipe(dish_name)

        # Display the recipe in a text box
        st.text_area("Recipe", recipe)


if __name__ == "__main__":
    main()
