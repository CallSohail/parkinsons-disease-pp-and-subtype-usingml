import streamlit as st
import warnings
import logging
from MachineLearningStreamlitBase.multiapp import MultiApp
from MachineLearningStreamlitBase.apps import streamlit_prediction_component_multiclass, streamlit_shapley_component
from MachineLearningStreamlitBase.apps import parkinson
from apps import topological_space, select
import gc

st.set_option('deprecation.showPyplotGlobalUse', False)

warnings.filterwarnings("ignore")

logger = logging.getLogger()
logger.disabled = True

# add any app you like in apps directory


app = MultiApp()
max_width = 15000
padding_top = 10
padding_right = 10
padding_left = 10
padding_bottom = 10
COLOR = 'black'
BACKGROUND_COLOR = 'white'
st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
    unsafe_allow_html=True,
)

gc.enable()

# Define the sidebar layout

# st.sidebar.title(
#     ":orange[Identification & Prediction Of :blue[_Parkinson Disease_] Subtypes & Progression Using Machine Learning]"
# )
st.sidebar.markdown(
    "<h1 style='color: orange; font-size: 25px; font-family: monospace;'>Identification & Prediction Of <span "
    "style='color: Cyan;'>Parkinson Disease</span> Subtypes & Progression Using Machine Learning</h1>",
    unsafe_allow_html=True
)


st.sidebar.markdown("___")

# Define the app selection menu

app_selection = st.sidebar.selectbox(
    ":green[**Select App**]",
    (
        "Home 🏘️",
        "Predict Patient PD Subtype 👨‍⚕️",
        "Predict Parkinson's Disease 🏥",
        "Scientific background 👨‍🔬",
        "Explore the PD subtype topological space 👾"

    ))

# Add the apps based on the selected option

if app_selection == "Home 🏘️":
    app.add_app("Home", select.app)
elif app_selection == "Scientific background 👨‍🔬":
    app.add_app("Scientific background", streamlit_shapley_component.app)
elif app_selection == "Predict Patient PD Subtype 👨‍⚕️":
    app.add_app("Predict Patient PD Subtype", streamlit_prediction_component_multiclass.app)
elif app_selection == "Explore the PD subtype topological space 👾":
    app.add_app("Explore the PD subtype topological space", topological_space.app)
elif app_selection == "Predict Parkinson's Disease 🏥":
    app.add_app("Predict Parkinson's Disease", parkinson.app)

# Define the main content layout

st.markdown(

    """
    <style>
        .reportview-container .main {
            max-width: 1200px;
            padding: 1rem;
        }
    </style>
    """
    ,
    unsafe_allow_html=
    True
    ,
)

# Render the app
app.run()
