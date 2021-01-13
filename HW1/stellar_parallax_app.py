#!/usr/bin/python3

import numpy as np
import plotly.graph_objects as go
import streamlit as st



np.random.seed(42)


Nstars = 100

# Background stars
xs = np.random.uniform(-5.0, 5.0, Nstars)
ys = np.random.uniform(-5.0, 5.0, Nstars)
As = np.random.gamma(2.0, 1.0, Nstars)
sigs = np.random.uniform(3, 7, Nstars) #0.02, 0.05


# The star
A = 5.0 #3.0
x0 = 1.0
dx = -0.75 #-0.75
y0 = 0.0
dy = 0.5 #0.5
sig = 10.0


# ==================================================

# ==================================================


# -- Set page config
apptitle = 'Stellar Parallax'

st.set_page_config(page_title=apptitle, page_icon=":sparkles:")

#st.sidebar.markdown("## Foo")

st.markdown("## HW\#1, Part 3: Distance to the Star Alpha Mendacium")

st.markdown("""
On many nights, you go out and make very detailed maps of the stars in different parts of the sky, noting their positions and brightnesses very carefully. Attached are your observations of the bright star Alpha Mendacium (α Med). Using the slider to switch between maps, you need to determine:

1. how far away the star is, and
2. how fast it is moving relative to the Solar System

You remember that your first step in determining both of these is to find the parallax and the proper motion of the star.

Note that while RA is typically given in units of hours, minutes, and seconds, they have been provided to you in degrees, arcminutes, and arcseconds for simplicity.
""")

months = ['March 1830', 'Sept 1830', 'March 1831', 'Sept 1831', 'March 1832', 'Sept 1832', 'March 1833', 'Sept 1833']
slider_val = st.sidebar.select_slider('Select the Observation Time:', options=months)

st.sidebar.markdown(f"""
-----
## Selected observation:
{slider_val}""")

ind = months.index(slider_val)


if ind % 2 == 1:
    px = 0.5
    py = 0.0
else:
    px = 0.0
    py = 0.0


def convert_to_arcsec(arr, offset=0):
    return (arr+5)*3 + offset


fig = go.Figure(data=go.Scatter(
    x = convert_to_arcsec(np.concatenate((xs, [x0+dx*ind+px])), 12),
    y = convert_to_arcsec(np.concatenate((ys, [y0+dy*ind+py])), 28),
    mode='markers',
    marker=dict(
        size=np.concatenate((sigs, [sig])),
        color=np.concatenate((As, [A])),
        colorscale='gray_r'
    )
))





xticks = list(range(15, 45, 5))
yticks = list(range(30, 60, 5))


fig.update_layout(
    width = 600,
    height = 600,
    margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin
    ),
    xaxis_title="RA: 316°30'+X [arcsec]",
    yaxis_title="DEC: 3°44'+Y [arcsec]",
    xaxis=dict(tickvals=xticks, ticktext=list(map(lambda x: "%s''"%x, xticks))),
    yaxis=dict(tickvals=yticks, ticktext=list(map(lambda x: "%s''"%x, yticks))),
    font=dict(size=18,)
)
fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1
  )

#fig.show()




st.plotly_chart(fig)



st.markdown("Written by Michael T. Lam")
