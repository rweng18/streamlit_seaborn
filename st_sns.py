# ---------------------------------------------------------------------------- #
# HELPFUL SOURCES
# ---------------------------------------------------------------------------- #

# http://seaborn.pydata.org/index.html
# https://discuss.streamlit.io/t/rendering-matplotlib-axessubplots-in-streamlit/5662/5
# https://stackoverflow.com/questions/45569592/saving-plot-from-seaborn?rq=1
# https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another
# https://www.datacamp.com/community/blog/seaborn-cheat-sheet-python
# https://www.kdnuggets.com/2019/04/data-visualization-python-matplotlib-seaborn.html
# https://seaborn.pydata.org/tutorial/axis_grids.html (axis grids)

# ---------------------------------------------------------------------------- #
# IMPORT PACKAGES
# ---------------------------------------------------------------------------- #

import streamlit as st
import seaborn as sns

# ---------------------------------------------------------------------------- #

st.title('Integrating Seaborn and Streamlit')
st.subheader('Rebecca Weng | Dec. 2020')

fig_type = st.selectbox('Plot Type', ('Histogram', 'Lineplot',
                                      'Scatterplot', 'Boxplot'))

# ---------------------------------------------------------------------------- #

# Adapted from "Stacked histogram on a log scale" from seaborn.pydata.org
if fig_type == 'Histogram':

    diamonds = sns.load_dataset("diamonds")

    # Workaround for displaying categorical variables
    st.write(diamonds.astype('object'))

    sns.set_theme(style="darkgrid")

    plt = sns.histplot(diamonds[diamonds['cut'] == 'Ideal'], x="price",
                       edgecolor="0.3", linewidth=.5,
                       log_scale=True) # AxesSubplot Object
    plt.set_title("Histogram of Price of Ideal Cut Diamonds")

    # Necessary line of code to get underlying plot's object
    fig = plt.get_figure() # Figure object

    st.pyplot(fig) # produces graph, same as st.write(fig)

    # Clears figure so you can plot the next without retaining first plot
    fig.clf()

    plt2 = sns.histplot(diamonds, x="price", hue="cut", multiple="stack",
                       palette="light:m_r", edgecolor=".3", linewidth=.5,
                       log_scale=True) # AxesSubplot Object

    plt2.set_title("Stacked Histogram of Diamond Price by Cut")

    fig2 = plt2.get_figure()

    st.pyplot(fig2)

# ---------------------------------------------------------------------------- #

# Adapted from "Timseries plot with error bands" from seaborn.pydata.org
elif fig_type == 'Lineplot':

    sns.set_theme(style="darkgrid")

    # Load an example dataset with long-form data
    fmri = sns.load_dataset("fmri")

    # Plot the responses for different events and regions
    plt3 = sns.lineplot(x="timepoint", y="signal",
                        hue="region", style="event", data=fmri)

    fig3 = plt3.get_figure()

    st.pyplot(fig3)

# ---------------------------------------------------------------------------- #

# Adapted from "Scatterplot with multiple semantics" from seaborn.pydata.org
elif fig_type == 'Scatterplot':

    # Load the example diamonds dataset
    diamonds = sns.load_dataset("diamonds")

    # Draw a scatterplot while assigning point colors and sizes to different
    # variables in the dataset
    clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

    plt4 = sns.scatterplot(x="carat", y="price",
                           hue="clarity", hue_order=clarity_ranking,
                           palette="ch:r=-.2,d=.3_r", size="depth",
                           sizes=(1, 8), linewidth=0,
                           data=diamonds)
    plt4.legend(fontsize = 'small')

    fig4 = plt4.get_figure()

    st.pyplot(fig4)


# ---------------------------------------------------------------------------- #

# Adapted from "Scatterplot with multiple semantics" from seaborn.pydata.org
elif fig_type == 'Boxplot':

    # Load the example tips dataset
    tips = sns.load_dataset("tips")

    # Draw a nested boxplot to show bills by day and time
    plt5 = sns.boxplot(x="day", y="total_bill",
                       hue="smoker", data=tips)

    plt5.legend(fontsize = 'small')
    plt5.set_xlabel("Total Bill")
    plt5.set_ylabel("Day of the Week")

    fig5 = plt5.get_figure()

    st.pyplot(fig5)
