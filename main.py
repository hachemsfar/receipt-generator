import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import openai



def get_recipe(dish_name):
    openai.api_key = st.secrets["API"]
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = "How to cook "+str(dish_name)+" ?"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return(response)


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
        st.write(response)



if __name__ == "__main__":
    main()
