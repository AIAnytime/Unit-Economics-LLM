import streamlit as st
import base64
from PIL import Image


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
            #introduction{padding: 0rem 0px 4rem;}
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
    st.markdown(logo_markup, unsafe_allow_html=True)

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .main {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Load your logo image
img = Image.open('favicon_img.png')

# Set the page configuration
st.set_page_config(
    layout="wide",
    page_title='Unit Economics',
    page_icon=img
)

# Add your logo to the sidebar
add_logo("cg_image.png")

# Set the background image
# set_png_as_page_bg("bg-cost.png")


    
    

def about_us():
    st.markdown("<h1 style='text-align: center; color: #12ABDB; pb:4'>Unit Economics of LLMs</h1>", unsafe_allow_html=True)
    st.title("About the App")

    st.write("""
    Welcome to the "Unit Economics of LLMs" application! 

    Our mission is to provide enterprises with the tools they need to make informed decisions about the financial aspects of their GenAI initiatives. With the increasing adoption of large language models (LLMs) like GPT-4, Text Bison, etc. It's crucial to have a clear understanding of the unit economics involved in building GenAI projects.

    **Key Features:**
    - Calculate the cost associated with your GenAI projects on multiple hyperscalers.
    - Compare costs and performance across different platforms.
    - Gain insights into the financial aspects of your AI projects.

    Whether you're an AI Engineer, a project manager, or an executive, our application is designed to help you optimize your GenAI projects and maximize your return on investment.

    **How to Use the App:**
    1. Use the navigation bar on the left to access different sections of the app.
    2. Input your project details and hyperscaler choices.
    3. Let our app do the heavy lifting and provide you with cost estimates and insights.

    **Contact Us:**
    Have questions, feedback, or suggestions? We'd love to hear from you! 

    Thank you for choosing "Unit Economics of LLMs" for your GenAI cost assessment needs. We're excited to be part of your GenAI journey!
    """)

# Main Streamlit code
if __name__ == "__main__":
    about_us()

