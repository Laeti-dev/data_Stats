import streamlit as st
import matplotlib.pyplot as plt
import sys

# import external module:
sys.path.insert(0, './')
from function import gaussienne as gauss


st.set_page_config(page_icon="🈺", page_title = "Inferences")
st.markdown("# Display the probability density function")
#st.set_option('deprecation.showPyplotGlobalUse', False) #???
st.markdown('\n')
st.markdown(
        """
This application aims to visualize the area under the curve (or p-value) for a standard deviation of Z. \n
It helps also to visualize an area under the curve's corresponding Z score, for uni or bilaterale situations . \n
""")

# plt.style.use('seaborn-whitegrid') # grid

# Si unilatéral on fait un slider pour Z de -3.5 à 3.5
Z = st.sidebar.slider('Z score',(-3.5),3.5,.0, key="Z")
std = st.sidebar.slider('Std',0.5,3.0,1.0, step=0.1, key="std")
A = st.sidebar.slider('Area',0.0,.99,0.95, key="a")

# On défini une box de sélection avec le choix Unilatéral ou Bilatéral
option = st.sidebar.selectbox('Choose Unilateral ou Bilateral',('Unilateral','Bilateral'))

layout = st.sidebar.columns([1,1])

with layout[0]:
    ba = st.button("Find the area corresponding to Z-score")
        # if unilatéral: using plot_unilatéral_z function

with layout[1]:
    bb = st.button("Find the Z-score corresponding to the area")
        # If unilateral: using plot_unilatéral function

if ba == True and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral_z(Z,std))
elif ba == True and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral_z(Z,std))
elif bb == True and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral(A,std))
elif bb == True and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral(A,std))
