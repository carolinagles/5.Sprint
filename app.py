import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title='Vehicle Advertisement Listings (US)', page_icon='🏁', layout='wide')

# Load the DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Application title
st.title('🏁  Vehicle Advertisement Listings (US)')

# Introductory description
st.markdown("""
This application allows you to explore a dataset of vehicle sales ads in the US.\n          
You can create histograms and scatter plots to analyze trends in prices and other variables.
""")

# Show data option
with st.expander("Show dataset"):
    st.write(car_data)

# Sidebar checkboxes for selecting plots
st.sidebar.header("Plot Options")
hist_check = st.sidebar.checkbox('Create Histogram')
scatter_check = st.sidebar.checkbox('Create Scatter Plot')

# Histogram parameters
if hist_check:
    st.subheader('Price Histogram')
    # Column selection for histogram
    col_hist = st.selectbox('Select column for histogram:',
                            car_data.columns, index=car_data.columns.get_loc('price'))
    # Slider for number of bins
    num_bins = st.slider('Select number of bins:',
                         min_value=10, max_value=100, value=30)

    try:
        st.write(
            f'Creating a histogram for the selected column: **{col_hist}**')
        # Create histogram
        fig = px.histogram(car_data, x=col_hist, nbins=num_bins,
                           title=f'Histogram of {col_hist}',
                           color_discrete_sequence=['#abcdde']
                           )
        # Show histogram
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating the histogram: {e}")

# Scatter plot parameters
if scatter_check:
    st.subheader('Scatter Plot')
    # Column selection for axes
    col_x = st.selectbox('Select column for X-axis:', car_data.columns,
                         index=car_data.columns.get_loc('model_year'))
    col_y = st.selectbox('Select column for Y-axis:',
                         car_data.columns, index=car_data.columns.get_loc('price'))

    try:
        st.write(f'Creating a scatter plot for **{col_x}** vs **{col_y}**')
        # Create scatter plot
        fig = px.scatter(car_data, x=col_x, y=col_y, title=f'{
                         col_x} vs {col_y}', trendline='ols')

        # Show scatter plot
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating the scatter plot: {e}")
