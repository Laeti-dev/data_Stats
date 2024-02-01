import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time
from IPython.display import HTML
# plt.style.use('seaborn')

st.set_page_config(page_icon="🔢", page_title = "Learnings", initial_sidebar_state = "collapsed")

st.markdown('''# Large numbers law illustrated !
#### Choose how many time you'd like to throw a 6 faces dice, then observe what faces you are getting the most!''')

#####################
n = st.slider("How many trhows ?", 5, 100, 5, step=5)
t = st.radio(
     "Speed between animation(s)",
     (.01, .1, .5, 1), index = 0, horizontal = True)
#####################

fig, ax = plt.subplots()
data = []

def animate(i):
    d1 = np.random.randint(1,7)
    d2 = np.random.randint(1,7)
    s = d1+d2
    data.append(s)

    figure.pyplot(fig)

    counts, edges, bars = ax.hist(data,
        bins = np.array(range(2,14)),
        align = "left",
        lw=1,
        ec="black",
        fc="#ffcc00")

    ax.set_ylim(top=6+(i//6))
    ax.set_xticks(range(2,13))
    ax.set_title(i+1)

## By clicking the button
if st.button("Throw the dice", key="launch"):

    figure = st.pyplot(fig)

    for i in range(n+1):
        animate(i)

        time.sleep(t)
