import streamlit as st 
from streamlit_option_menu import option_menu as opt  
st.set_page_config(page_title="About",page_icon="icon/mainmenu.png",layout='wide')

sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
st.markdown(f"{sty}",unsafe_allow_html=True)

with st.sidebar:
    selected = opt(
        menu_title='About',
        menu_icon='body-text',
        options=['Project','Team']
    )

if selected == 'Project':
    st.write("""
## Product Perspective:
 * The product is a prediction web app that uses machine learning algorithms to predict a student's final semester marks based on their internal marks and other relevant factors. \n
 * The app will be designed to provide accurate and reliable predictions to students, teachers, and institutions. \n
 * The app will be user-friendly and easy to navigate, with clear and concise instructions.\n
## Product Features:

 * User login and registration\n
 * Student page for entering internal marks and other details\n
 * Institution page for entering student data and generating results\n
 * Machine learning algorithms for predicting final semester marks\n
 * Consideration of previous academic performance, attendance, and other relevant factors\n
 * Clear and concise instructions for users\n
 * Ability to export results in an excel/csv file format\n

## User Classes and Characteristics:

 * Students: Students will use the app to predict their final semester marks and get an idea of their academic performance.\n
 * Teachers: Teachers will use the app to monitor their students' academic progress and take appropriate measures to improve their performance.\n
 * Institutions: Institutions will use the app to track their students' academic performance and take appropriate measures to improve their overall performance.\n
 * Administrators: Administrators will manage the app and ensure that it is running smoothly.\n



## Purpose:
 * The purpose of this project is to develop a prediction web app that can accurately predict a student's final semester marks based on their internal marks and other relevant factors. \n
 * The app will help students, teachers, and institutions to get a clear idea of a student's academic performance and take appropriate measures to improve their performance.\n
        """)

if selected == 'Team':
    sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:left;
                }
            </style>
        """
    st.markdown(f"{sty}",unsafe_allow_html=True)
    st.title("Team Details")
    st.header("Team Description :")
    st.write("""
         * Welcome to Savvy! We’re an awesome team of visionaries eager to tackle the issue of student mark prediction. 
         * Our mission is simple: devise a system that accurately predicts grades for students in order to better inform their future decisions of career options. 
         * In order to do this, our group consists of experts from different fields such as statistics, psychology and neuroscience who will use data analysis techniques combined with creativity to come up with innovative solutions. 
         * Through collaboration and brainstorming ideas between all members - no matter how big or small they are- we can create something truly magical together! So let us work harmoniously with each other towards bringing forth tangible results – it’s time for Savvy to shine!     
    """)

    st.subheader("Team members : ")
    st.write("""
         * [Viyasan S - ( Team Leader )](https://www.linkedin.com/in/viyasan-sivaraj-12b14b1a4/)
         * [Shabari K S](https://www.linkedin.com/in/shabari-k-s-56421822a) 
         * [Sathyaram R](https://www.linkedin.com/in/sathyaram-r-592b66227)
         * [Vibav M](https://www.linkedin.com/in/vibav-mahendran-078181228)
    """)

    
