import streamlit as st
import pandas as pd 

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