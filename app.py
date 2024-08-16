import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title='Streamlit Training Ground',
    page_icon=':rocket:',
    layout='wide',
    initial_sidebar_state='auto'
)

st.title('Welcome to streamlit training ground :rocket:')
st.write(
    """
    This webpage will learn you all about using streamlit in a fun and interactive way.

    Streamlit is a python library that allows you to create web applications with only a few lines of code.

    """)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('How can you show text in streamlit?')
    st.write('You can use the st.write() function to show text in streamlit')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            st.write('Hello world!')
            """
        )
        st.write('Hello world!')
    
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can you also use emojis?')
    st.write('Yes, you can use emojis in streamlit')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            st.write('Hello world! :smile:')
            """
        )

        st.write('Hello world! :smile:')

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can you also show images?')
    st.write('Yes, you can show images in streamlit by using the st.image() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            from PIL import Image

            image = Image.open('path/to/image.jpg')
            st.image(image, caption='Image caption')
            """
        )

        image = Image.open('./examples/cat.png')
        st.image(image, caption='Image caption')

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can you also show dataframes?')
    st.write('Yes, you can show pandas dataframes in streamlit by using the st.dataframe() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            import pandas as pd

            df = pd.DataFrame({
                'name': ['John', 'Jane', 'Doe'],
                'age': [25, 30, 35]
            })

            st.dataframe(df)
            """
        )

        df = pd.DataFrame({
            'name': ['John', 'Jane', 'Doe'],
            'age': [25, 30, 35]
        })

        st.dataframe(df)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can you also show plots?')
    st.write('Yes, you can show plots in streamlit by using the st.plotly_chart() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            import plotly.express as px

            df = pd.DataFrame({
                'name': ['John', 'Jane', 'Doe'],
                'age': [25, 30, 35]
            })

            fig = px.bar(df, x='name', y='age')
            st.plotly_chart(fig)
            """
        )

        df = pd.DataFrame({
            'name': ['John', 'Jane', 'Doe'],
            'age': [25, 30, 35]
        })

        fig = px.bar(df, x='name', y='age')
        st.plotly_chart(fig)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can you also show videos?')
    st.write('Yes, you can show videos in streamlit by using the st.video() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            st.video('path/to/video.mp4')
            """
        )

        st.video('./examples/video.mp4')

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header('Can I use custom html code?')
    st.write('Yes, you can use custom html code in streamlit by using the st.markdown() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            st.markdown('<h1 style="color: red;">Hello world!</h1>', unsafe_allow_html=True)
            """
        )

        st.markdown('<h1 style="color: red;">Hello world!</h1>', unsafe_allow_html=True)

st.divider()


col1, col2 = st.columns(2)

with col1:
    st.header('Can I make a date picker?')
    st.write('Yes, you can make a date picker in streamlit by using the st.date_input() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            date = st.date_input('Select a date', value=None)
            """
        )

        date = st.date_input('Select a date', value=None)

col1, col2 = st.columns(2)

with col1:
    st.header('Can I use custom css?')
    st.write('Yes, you can use custom css in streamlit by using the st.markdown() function')

with col2:
    with st.expander('Show me the code'):
        st.code(
            """
            st.markdown(
                '''
                <style>
                    h1 {
                        color: red;
                    }
                </style>
                <h1>Hello world!</h1>
                ''', unsafe_allow_html=True
            )
            """
        )

        components.html(
            """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Inspiring Apple-style Buttons</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f5f5f7;
                }
                .container {
                    text-align: center;
                }
                h1 {
                    color: #1d1d1f;
                    font-size: 48px;
                    margin-bottom: 40px;
                }
                .button {
                    display: inline-block;
                    padding: 16px 32px;
                    margin: 0 10px;
                    font-size: 18px;
                    font-weight: 600;
                    text-decoration: none;
                    color: #fff;
                    background-color: #0071e3;
                    border-radius: 980px;
                    transition: all 0.3s ease;
                }
                .button:hover {
                    background-color: #0077ed;
                    transform: scale(1.05);
                }
            </style>
            </head>
            <body>
                <div class="container">
                    <h1>Embrace Your Potential</h1>
                    <a href="#" class="button">Discover More</a>
                    <a href="#" class="button">Start Your Journey</a>
                </div>
            </body>
            </html>
            """, height=500)
