from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_picture = current_dir / "assets" / "Profile picture.png"



PAGE_TITLE = "Digital CV | Jeyaraman"
PAGE_ICON = "👨‍💻"
NAME = "Jeyaraman"
DESCRIPTION = """ Emerging Machine learning developer,Eager to learn to new stuff all day """

EMAIL = "jeyaramanjr7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jeyaraman-r-1368ab1a1/",
    "Github" : "https://github.com/RoboJunior"
}
PROJECTS = {
    "🎯 Text to image using Dall-E2" : "https://github.com/RoboJunior/dall-e2-image-model",
    "🎯 Pdf-Reader Using Langchain Openai" : "https://github.com/RoboJunior/Pdf_bot",
    "🎯 Sentiment analysis Using Vader python" : "https://github.com/RoboJunior/sentiment_analysis_using_amazon_review_dataset"
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html = True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_picture)


col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧",EMAIL)



    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index,(plaform,link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{plaform}]({link})")


    st.write("#")
    st.subheader("Experience & Qualifications")
    st.write(
        """ 
        - ✅ Strong Knowledge and hands on experience on python and machine learning 
        - ✅ Good understanding of models algorithm and how they work
        - ✅ Quick learner and a good team player  
           """
    )

    st.write("#")
    st.subheader("Skills")
    st.write(""" 
        - 👨‍💻 Programming : Python (Scikit-learn, Pandas),Sql
        - 📊 Data Visulization : Plotly,Matplotlib
        - 📚 Modeling : Logisitc regression , linear regression , Decision Tree , Deep learning , Reinforcement learning
        - 📄 Databases : Postgres , Mongodb , Mysql
      """
             
    )


    st.write("#")
    st.subheader("Projects")
    for project,link in PROJECTS.items():
        st.write(f"[{project}]({link})")
    