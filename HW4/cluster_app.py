#!/usr/bin/python3

import numpy as np
import plotly.graph_objects as go
import streamlit as st
from load_data import *


# ==================================================

# ==================================================


# -- Set page config
apptitle = 'Star Clusters'

st.set_page_config(page_title=apptitle, page_icon=":sparkles:")


st.markdown("## HW\#4: The Age of Stellar Clusters")

st.markdown("""
Theoretical models of stellar evolution can predict the color index and absolute magnitude of a star of a given mass during its lifetime on the main sequence and beyond. A star remains on the main sequence for a relatively long time in a state of stability; other phases in a star's lifetime are more rapid. Ignoring the very rapid early stages of the star's life before it reaches the main sequence, we can consider the color-magnitude main sequence established by theoretical models along with observations as the *zero-age main sequence*, or ZAMS. This tells us the color and magnitude of a star right as it is born. A time scale can be associated with the ZAMS, this "age" is the length of time a star of a given mass will remain in its stable main sequence phase before it evolves off the ZAMS, i.e., the "lifetime" of the star.

Using the tools to the left, you can

1. select a cluster to analyze,
2. toggle the ZAMS on or off, and
3. shift the ZAMS by a certain magnitude. A shift of 0 means that the apparent magnitude equals the absolute magnitude.

When hovering over the panel below, in the top right toolbar, you may find it useful to click "toggle spike lines" to help guide your eye to the axes, though hovering over a data point will also show its x and y values. If you select "compare data on hover" then the x value of your mouse cursor will be shown on the x axis.
""")

M5 = "Aethon Cluster [M5]"# Globular Cluster in Serpens
M45 = "Hawking Eta Cluster [M45]" #Pleiades
M67 = "Artemis Tau Cluster [M67]"# open cluster, fairly red

clusters = [M5, M45, M67]
cluster_choice = st.sidebar.radio("Cluster Selection:", clusters)
zams_on = st.sidebar.checkbox("Display Zero-Age Main Sequence (ZAMS)")

shift = st.sidebar.slider("Shift ZAMS Magnitude", min_value=0.0, max_value=20.0, step=0.1)


if cluster_choice == M5:
    V, I = loadM5()
    xtick = 1.0
    ytick = 2.0
elif cluster_choice == M45:
    V, I = loadM45()
    xtick = 1.0
    ytick = 2.0
elif cluster_choice == M67:
    V, I = loadM67()
    xtick = 0.5
    ytick = 1.0

V_ZAMS, I_ZAMS = loadZAMS()

VmI = V - I

XMIN = min(VmI)-0.75
XMAX = max(VmI)+0.75
YMIN = min(V)-0.75 #invert later
YMAX = max(V)+0.75

fig = go.Figure(data=go.Scatter(
    x = VmI,
    y = V,
    mode='markers',
    marker=dict(
        colorscale='gray_r'
    ),
    name = 'Stellar Data'
))

if zams_on:
    fig.add_trace(go.Scatter(
        x = V_ZAMS-I_ZAMS,
        y = V_ZAMS+shift,
        mode='lines',
        name = 'ZAMS'
    ))

fig.update_xaxes(range=[XMIN, XMAX])
fig.update_yaxes(range=[YMAX, YMIN]) #inverted

fig.update_layout(
    width = 600,
    height = 600,
    margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin
    ),
    #yaxis = dict(autorange="reversed"),
    # broken?
    #xaxis_title=r'$m_V - m_I$',
    #yaxis_title=r"$m_V$",
    xaxis_title="<i>m</i><sub>V</sub> - <i>m</i><sub>I</sub> ",
    yaxis_title="<i>m</i><sub>V</sub>",
    #xaxis=dict(tickvals=xticks, ticktext=list(map(lambda x: "%s''"%x, xticks))),
    #yaxis=dict(tickvals=yticks, ticktext=list(map(lambda x: "%s''"%x, yticks))),
    font=dict(size=18,),
    xaxis = dict(dtick=xtick),
    yaxis = dict(dtick=ytick),
    showlegend=False
)


st.plotly_chart(fig)

st.markdown("Written by Michael T. Lam, original Java applet by Terry Herter et al. See data files for paper references.")
