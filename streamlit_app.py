import streamlit as st
import numpy as np
import pandas as pd
import time

# Write a data frame
"""
Here's our first attempt at using data to create a table:
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df


st.write("Here's our second attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("Here's our first attempt at using data to create a interactive table:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("Here's our first attempt at using data to create a static table:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


# line chart
st.write("Here's a line chart:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Model-a', 'Model-b', 'Model-c'])
st.line_chart(chart_data)


# Map
st.write("Here's a map")
df=pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon'])
st.map(df)

st.write("Here's a map with slidebar")
st.sidebar.title("streamlit :red[Tutorial]")
st.sidebar.header(":blue[Introduction to Databases]")
st.sidebar.subheader("Web Applications")
df=pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon'])
st.map(df)


# Widgets: st.slider(), st.button() or st.selectbox()
st.write("Here are some widgets:")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option


# Layout
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


# Show Progress
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
