import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import openai
import requests
from io import BytesIO
from PIL import Image

st.markdown(
    """<style>
	.entities {
	     line-height: 2; 
	}

	[data-entity] {
	     padding: 0.25em 0.35em;
	     margin: 0px 0.25em;
	     line-height: 1;
	     display: inline-block;
	     border-radius: 0.25em;
	     border: 1px solid; 
	}

	[data-entity]::after {
	     box-sizing: border-box;
	     content: attr(data-entity);
	     font-size: 0.6em;
	     line-height: 1;
	     padding: 0.35em;
	     border-radius: 0.35em;
	     text-transform: uppercase;
	     display: inline-block;
	     vertical-align: middle;
	     margin: 0px 0px 0.1rem 0.5rem; 
	}

	[data-entity][data-entity="ingredient"] {
	     background: rgba(166, 226, 45, 0.2);
	     border-color: rgb(166, 226, 45); 
	}

	[data-entity][data-entity="ingredient"]::after {
	     background: rgb(166, 226, 45); 
	}

	body {
	    padding: 25px 50px;
	    font: 18px Helvetica, Arial, sans-serif;
	}
        </style>""",
    unsafe_allow_html=True,
)

def generate_image(prompt):
    openai.api_key = st.secrets["API"]
    response = openai.Image.create(
	    prompt=prompt,
	    n=1,
	    size="512x512"
	)

    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    st.image(image)
    return("")

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
    #st.write(response)

    API_URL = "https://api-inference.huggingface.co/models/edwardjross/xlm-roberta-base-finetuned-recipe-all"
    API_TOKEN= st.secrets["API_TOKEN"]
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
                   
    def query(payload):
	    response = requests.post(API_URL, headers=headers, json=payload)
	    return response.json()
               
    output = query({
        "inputs": str(response),
    })
    #st.write(output)
	
    new_text=""
    k=0
    receipt=False
    for i in output:
        if(i['entity_group']=="NAME"):
            new_text=new_text+response[k:i['start']]
            new_text=new_text+str("<mark data-entity=\"ingredient\">"+str(response[i['start']:i['end']])+"</mark>")
            k=i['end']
            receipt=True
		
    if(receipt==True):
        st.subheader("How to make "+str(dish_name))
        new_text=new_text+response[k:]
        st.markdown(new_text,unsafe_allow_html=True)
	
# Create a Streamlit app
def main():
    # Set the app title
    st.title("Recipe Generator")

    # Create a text input field for the dish name
    dish_name = st.text_input("Enter the dish name:")

    # Create a button to submit the dish name
    if st.button("Submit"):
	image = generate_image(dish_name)
        recipe = get_recipe(dish_name)

    ingredient = st.text_input("Enter the ingredient name:")
    if st.button("Get Photo"):
        image = generate_image(ingredient)
	    
	



if __name__ == "__main__":
    main()
