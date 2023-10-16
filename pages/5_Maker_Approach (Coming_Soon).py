import streamlit as st 
from PIL import Image
import base64

# gcp
BISON_train = 0.218499
BISON_PROMPT_COST = 0.0005/1000
BISON_COMPLETION_COST= 0.0005/1000
# openai
GPT_35_train = 0.0080/1000
GPT_35_TURBO_PROMPT_COST = 0.0120/1000 
GPT_35_TURBO_COMPLETION_COST = 0.0160/1000

@st.cache_data()
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="10%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("data:image/png;base64,%s");
                background-repeat: no-repeat;
                background-position: %s;
                margin-top: %s;
                background-size: %s %s;
            }
            [data-testid="stToolbar"] {
                visibility: hidden;
            }
            [data-testid="stDecoration"] {
                visibility: hidden;
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #maker-approach{padding: 0rem 0px 4rem;}
        </style>
    """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )

def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

# Load your logo image
img = Image.open('favicon_img.png')

# Set the page configuration
st.set_page_config(
    layout="wide",
    page_title='Taker Approach',
    page_icon=img
)

# Add your logo to the sidebar
add_logo("cg_image.png")

def main():

    st.markdown("<h1 style='text-align: center; color: #12ABDB;'>Maker Approach</h1>", unsafe_allow_html=True)
    st.warning('Coming Soon...')
    # col1, col2 = st.columns([1,1])
    # with col1:
    #     st.subheader('Start with selecting an LLM')
    #     llm_option = st.selectbox('Select an LLM:', ('GPT-35-Turbo', 'Text Bison'))
    #     input_nos = st.number_input("Your total tokens length", value=10000, placeholder="Type your length of tokens...")
    #     if llm_option == "GPT-35-Turbo":
    #         llm_cost = GPT_35_train * input_nos
    #         st.success(" $" + str(round(llm_cost, 2)))
            
            

if __name__ == "__main__":
    main()