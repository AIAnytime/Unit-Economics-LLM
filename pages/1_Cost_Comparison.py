import streamlit as st 
from PIL import Image
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px

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
            #cost-comparisons-for-llms{padding: 0rem 0px 4rem;}
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
    page_title='Cost Comparison',
    page_icon=img
)

# Add your logo to the sidebar
add_logo("cg_image.png")

# openai
GPT_35_TURBO_PROMPT_COST = 0.0015/1000 
GPT_35_TURBO_COMPLETION_COST = 0.002/1000
GPT4_PROMPT_COST = 0.03/1000
GPT4_COMPLETION_COST = 0.06/1000
###
fif_gpt35 = round((30 * 100 * 80 * GPT_35_TURBO_PROMPT_COST + 30 * 100 * 200 * GPT_35_TURBO_COMPLETION_COST)*30)
hun_gpt35 = round((100 * 250 * 80 * GPT_35_TURBO_PROMPT_COST + 100 * 250 * 200 * GPT_35_TURBO_COMPLETION_COST)*30)
fh_gpt35 = round((500 * 1500 * 80 * GPT_35_TURBO_PROMPT_COST + 500 * 1500 * 200 * GPT_35_TURBO_COMPLETION_COST)*30)
fif_gpt4 = round((30 * 100 * 80 * GPT4_PROMPT_COST + 30 * 100 * 200 * GPT4_COMPLETION_COST)*30)
hun_gpt4 = round((100 * 250 * 80 * GPT4_PROMPT_COST + 100 * 250 * 200 * GPT4_COMPLETION_COST)*30)
fh_gpt4 = round((500 * 1500 * 80 * GPT4_PROMPT_COST + 500 * 1500 * 200 * GPT4_COMPLETION_COST)*30)
# aws
CLAUDEIN_PROMPT_COST = 0.00163/1000
CLAUDEIN_COMPLETION_COST = 0.00551/1000
CLAUDE_PROMPT_COST = 0.01102/1000
CLAUDE_COMPLETION_COST = 0.03268/1000
TITANLT_PROMPT_COST = 0.0003/1000
TITANLT_COMPLETION_COST = 0.0004/1000
TITANEX_PROMPT_COST = 0.0013/1000
TITANEX_COMPLETION_COST = 0.0017/1000
###
fif_ci = round((30 * 100 * 80 * CLAUDEIN_PROMPT_COST + 30 * 100 * 200 * CLAUDEIN_COMPLETION_COST)*30)
hun_ci = round((100 * 250 * 80 * CLAUDEIN_PROMPT_COST + 100 * 250 * 200 * CLAUDEIN_COMPLETION_COST)*30)
fh_ci = round((500 * 1500 * 80 * CLAUDEIN_PROMPT_COST + 500 * 1500 * 200 * CLAUDEIN_COMPLETION_COST)*30)
fif_c = round((30 * 100 * 80 * CLAUDE_PROMPT_COST + 30 * 100 * 200 * CLAUDE_COMPLETION_COST)*30)
hun_c = round((100 * 250 * 80 * CLAUDE_PROMPT_COST + 100 * 250 * 200 * CLAUDE_COMPLETION_COST)*30)
fh_c = round((500 * 1500 * 80 * CLAUDE_PROMPT_COST + 500 * 1500 * 200 * CLAUDE_COMPLETION_COST)*30)
fif_tl = round((30 * 100 * 80 * TITANLT_PROMPT_COST + 30 * 100 * 200 * TITANLT_COMPLETION_COST)*30)
hun_tl = round((100 * 250 * 80 * TITANLT_PROMPT_COST + 100 * 250 * 200 * TITANLT_COMPLETION_COST)*30)
fh_tl = round((500 * 1500 * 80 * TITANLT_PROMPT_COST + 500 * 1500 * 200 * TITANLT_COMPLETION_COST)*30)
fif_tx = round((30 * 100 * 80 * TITANEX_PROMPT_COST + 30 * 100 * 200 * TITANEX_COMPLETION_COST)*30)
hun_tx = round((100 * 250 * 80 * TITANEX_PROMPT_COST + 100 * 250 * 200 * TITANEX_COMPLETION_COST)*30)
fh_tx = round((500 * 1500 * 80 * TITANEX_PROMPT_COST + 500 * 1500 * 200 * TITANEX_COMPLETION_COST)*30)
# gcp
BISON_PROMPT_COST = 0.0005/1000
BISON_COMPLETION_COST= 0.0005/1000
###
fif_bis = round((30 * 100 * 80 * BISON_PROMPT_COST + 30 * 100 * 200 * BISON_COMPLETION_COST)*30)
hun_bis = round((100 * 250 * 80 * BISON_PROMPT_COST + 100 * 250 * 200 * BISON_COMPLETION_COST)*30)
fh_bis = round((500 * 1500 * 80 * BISON_PROMPT_COST + 500 * 1500 * 200 * BISON_COMPLETION_COST)*30)

# storing values
azure_data = {
    "GPT-4": {"Cost": [fif_gpt4, hun_gpt4, fh_gpt4]},
    "GPT-35-Turbo": {"Cost": [fif_gpt35, hun_gpt35, fh_gpt35]}
}

aws_data = {
    "Anthropic Claude": {"Cost": [fif_c, hun_c, fh_c]},
    "Anthropic Claude-Instant": {"Cost": [fif_ci, hun_ci, fh_ci]},
    "Titan Lite": {"Cost": [fif_tl, hun_tl, fh_tl]},
    "Titan Express": {"Cost": [fif_tx, hun_tx, fh_tx]}
}

gcp_data = {
    "Text Bison": {"Cost": [fif_bis, hun_bis, fh_bis]}
}

# Function to create a new trace for each selection
def create_traces(data, selected_options):
    traces = []
    for option in selected_options:
        trace = go.Scatter(x=[1, 2, 3, 4], y=data[option]["Cost"], mode='lines', name=option)
        traces.append(trace)
    return traces

def main():
    st.markdown("<h1 style='text-align: center; color: #12ABDB;'>Cost Comparisons for LLMs</h1>", unsafe_allow_html=True)
    st.info("Please Select all the available options in the dropdown menu for the complete cost analysis!")
    service = st.selectbox('Select a Service Provider:', ('Azure OpenAI', 'AWS Bedrock', 'GCP VertexAI'))

    if service == "Azure OpenAI":
        selected_options = st.multiselect("Select LLMs (You can select multiple LLMs from the dropdown)", list(azure_data.keys()))
        if not selected_options:
            st.warning('Please select LLMs for insights.')
        else:
            traces = create_traces(azure_data, selected_options)
            st.divider()
            st.write('**Scale for this graph: 1 Unit = 1$ ')
            fig = go.Figure(data=traces)
            fig.update_xaxes(showticklabels=False)  # Hide x-axis labels
            fig.update_yaxes(title_text="Cost")  # Set y-axis title
            st.plotly_chart(fig, use_container_width=True)

    elif service == "AWS Bedrock":
        selected_options = st.multiselect("Select LLMs (You can select multiple LLMs from the dropdown)", list(aws_data.keys()))
        if not selected_options:
            st.warning('Please select LLMs for insights.')
        else:
            traces = create_traces(aws_data, selected_options)
            st.divider()
            st.write('**Scale for this graph: 1 Unit = 1$ ')
            fig = go.Figure(data=traces)
            fig.update_xaxes(showticklabels=False)  # Hide x-axis labels
            fig.update_yaxes(title_text="Cost")  # Set y-axis title
            st.plotly_chart(fig, use_container_width=True)

    elif service == "GCP VertexAI":
        selected_options = st.multiselect("Select LLMs (You can select multiple LLMs from the dropdown)", list(gcp_data.keys()))
        if not selected_options:
            st.warning('Please select LLMs for insights.')
        else:
            traces = create_traces(gcp_data, selected_options)
            st.divider()
            st.write('**Scale for this graph: 1 Unit = 1$ ')
            fig = go.Figure(data=traces)
            fig.update_xaxes(showticklabels=False)  # Hide x-axis labels
            fig.update_yaxes(title_text="Cost")  # Set y-axis title
            st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader('Here are the parameters considered for the above plot (If there is any!)')
    

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write('Point 1:')
        st.info('Number of Employees: 30  \nNumber of Prompt Frequency: 100  \nPrompt Tokens Length: 80  \nCompletions Tokens Length: 200')
        if service == "Azure OpenAI" and selected_options == ["GPT-4", "GPT-35-Turbo"]:
            gpt_35_cost_30 = fif_gpt35
            gpt_4_cost_30 = fif_gpt4
            st.write('Cost for GPT-4: ', gpt_4_cost_30, "$")
            st.write('Cost for GPT-3.5 Turbo: ', gpt_35_cost_30, "$")
        elif service == "AWS Bedrock" and selected_options == ["Anthropic Claude", "Anthropic Claude-Instant", "Titan Lite", "Titan Express"]:
            st.write('Cost for Anthropic Claude: ', fif_c, "$")
            st.write('Cost for Anthropic Claude-Instant: ', fif_ci, "$")
            st.write('Cost for Titan Lite: ', fif_tl, "$")
            st.write('Cost for Titan Express: ', fif_tx, "$")
        elif service == "GCP VertexAI" and selected_options == ["Text Bison"]:
            st.write('Cost for Text Bison: ', fif_bis, "$")
    with col2:
        st.write('Point 2:')
        st.info('Number of Employees: 100  \nNumber of Prompt Frequency: 250  \nPrompt Tokens Length: 80  \nCompletions Tokens Length: 200')
        if service == "Azure OpenAI" and selected_options == ["GPT-4", "GPT-35-Turbo"]:
            gpt_35_cost_100 = hun_gpt35
            gpt_4_cost_100 = hun_gpt4
            st.write('Cost for GPT-4: ', gpt_4_cost_100, "$")
            st.write('Cost for GPT-3.5 Turbo: ', gpt_35_cost_100, "$")
        elif service == "AWS Bedrock" and selected_options == ["Anthropic Claude", "Anthropic Claude-Instant", "Titan Lite", "Titan Express"]:
            st.write('Cost for Anthropic Claude: ', hun_c, "$")
            st.write('Cost for Anthropic Claude-Instant: ', hun_ci, "$")
            st.write('Cost for Titan Lite: ', hun_tl, "$")
            st.write('Cost for Titan Express: ', hun_tx, "$")
        elif service == "GCP VertexAI" and selected_options == ["Text Bison"]:
            st.write('Cost for Text Bison: ', hun_bis, "$")
    with col3:
        st.write('Point 3:')
        st.info('Number of Employees: 500  \nNumber of Prompt Frequency: 1500  \nPrompt Tokens Length: 80  \nCompletions Tokens Length: 200')
        if service == "Azure OpenAI" and selected_options == ["GPT-4", "GPT-35-Turbo"]:
            st.write('Cost for GPT-4: ', fh_gpt4, "$")
            st.write('Cost for GPT-3.5 Turbo: ', fh_gpt35, "$")
        elif service == "AWS Bedrock" and selected_options == ["Anthropic Claude", "Anthropic Claude-Instant", "Titan Lite", "Titan Express"]:
            st.write('Cost for Anthropic Claude: ', fh_c, "$")
            st.write('Cost for Anthropic Claude-Instant: ', fh_ci, "$")
            st.write('Cost for Titan Lite: ', fh_tl, "$")
            st.write('Cost for Titan Express: ', fh_tx, "$")
        elif service == "GCP VertexAI" and selected_options == ["Text Bison"]:
            st.write('Cost for Text Bison: ', fh_bis, "$")




if __name__ == "__main__":
    main()