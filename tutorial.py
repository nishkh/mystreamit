import streamlit as st
st.set_page_config(page_title = 'MyStreamlit')
mymenu = st.sidebar.selectbox('My Menu',('Home','Fill Form','Download'))
st.title('onlei tech')
st.header("hi")
st.image('https://www.python.org/static/img/python-logo.png')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html = True)
elif(mymenu=='Fill Form'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("Choose DOB")
        marks=st.slider('Choose Marks')
        k=st.form_submit_form("Submit Form")
        if k:
            st.write('Name',name,'dob:',dob,'Marks:',marks)
elif(mymenu=='Download'):
    st.header("Download")
    st.download_button('Download Now','hello there','onlie.txt')
