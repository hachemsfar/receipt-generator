import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import openai
import requests



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
    st.write(response)

    API_URL = "https://api-inference.huggingface.co/models/edwardjross/xlm-roberta-base-finetuned-recipe-all"
    API_TOKEN= st.secrets["API_TOKEN"]
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
                   
    def query(payload):
	    response = requests.post(API_URL, headers=headers, json=payload)
	    return response.json()
               
    output = query({
        "inputs": str(response),
    })
    st.write(output)
	
    new_text=""
    k=0
    for i in output:
        if(i['entity_group']=="NAME"):
            new_text=new_text+response[k:i['start']]
            new_text=new_text+str("<span style=\"background-color: yellow\">"+str(response[i['start']:i['end']])+"</span>")
            k=i['end']
		
    new_text=new_text+response[i['end']:]
    st.write(new_text)
	
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

if __name__ == "__main__":
    main()
