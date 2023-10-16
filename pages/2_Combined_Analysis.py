import streamlit as st 
from PIL import Image
import plotly.figure_factory as ff
import plotly.subplots as sp
import plotly.graph_objs as go
import base64

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
            #combined-analysis{padding: 0rem 0px 4rem;}
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
    page_title='Combined Analysis',
    page_icon=img
)

# Add your logo to the sidebar
add_logo("cg_image.png")

# data = {
#     "100 Users": {
#         "Azure OpenAI":['2', '2', '2', '2', '2'],
#         "GCP VertexAI":['2', '0.6', '1', '2', '2'],
#         "AWS Bedrock":['6.4', '1.1', '0.6', '14.5', '0.1']
#     },
#     "500 Users":{
#         "Azure OpenAI":['2', '2', '2', '2', '2'],
#         "GCP VertexAI":['2', '2', '2', '2', '2'],
#         "AWS Bedrock":['32', '5.7', '1', '25', '0.5']
#     },
#     "1000 Users":{
#         "Azure OpenAI":['2', '2', '2', '2', '2'],
#         "GCP VertexAI":['2', '2', '2', '2', '2'],
#         "AWS Bedrock":['94', '12.5', '1.2', '33.5', '0.6']
#     }
# }
data = {
    "100 Users": {
        "Azure OpenAI":['2', '2', '2'],
        "GCP VertexAI":['2', '0.6', '1'],
        "AWS Bedrock":['6.4', '1.1', '0.6']
    },
    "500 Users":{
        "Azure OpenAI":['2', '2', '2'],
        "GCP VertexAI":['10', '3', '5'],
        "AWS Bedrock":['32', '5.7', '1']
    },
    "1000 Users":{
        "Azure OpenAI":['2', '2', '2'],
        "GCP VertexAI":['20', '6', '10'],
        "AWS Bedrock":['94', '12.5', '1.2']
    }
}


colors = {
    "Azure OpenAI":"Dark blue",
    "GCP VertexAI":"yellowgreen",
    "AWS Bedrock":"orange"
}

def main():
    st.markdown("<h1 style='text-align: center; color: #12ABDB;'>Combined Analysis</h1>", unsafe_allow_html=True)

    # Radio buttons for selecting the number of users
    num_users = st.radio("Select the number of users:", list(data.keys()))
    st.divider()
    st.write('**Scale for this graph: 1 Unit = 1000$')

    if num_users:
    # Create a Plotly bar chart
        sectors = list(data[num_users].keys())
        values = [data[num_users][sector] for sector in sectors]

        fig = sp.make_subplots(rows=1, cols=1)
        sector_totals = {}  # To store sector totals

        for sector, values in data[num_users].items():
            values = [float(val) for val in values]  # Convert strings to floats
            # fig.add_trace(go.Bar(x=['ML Platform', 'GenAI Services', 'Storage', 'Serverless Computing', 'Serving Services (UI)'], y=values, name=sector, marker_color=colors[sector]))
            fig.add_trace(go.Bar(x=['ML Platform', 'GenAI Services', 'Storage'], y=values, name=sector, marker_color=colors[sector]))
            sector_totals[sector] = sum(values)

        fig.update_layout(barmode="group", xaxis_title="Services", yaxis_title="Cost")

        # Plot the chart
        st.plotly_chart(fig, use_container_width=True)

        st.divider()
        # Display sector totals
        st.subheader("Total Cost by each service provider:")

        # Create a Markdown table
        table_data = "| Sector | Total Cost ( in $) |\n"
        table_data += "|--------|------------|\n"

        for sector, total in sector_totals.items():
            table_data += f"| {sector} | {total:.2f} |\n"

        st.markdown(table_data)


if __name__ == "__main__":
    main()