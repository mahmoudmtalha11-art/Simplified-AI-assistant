import streamlit as st

st.title("موقعي الأول للذكاء الاصطناعي 🤖")
st.write("أهلاً بك! هذا الموقع يعمل بالذكاء الاصطناعي ومصمم بالكامل مجاناً.")

user_input = st.text_input("اسألني أي شيء:")

if st.button("إرسال"):
    if user_input:
        st.success(f"لقد قلت: '{user_input}'. أهلاً بك في عالم البرمجة!")
    else:
        st.warning("الرجاء كتابة سؤال أولاً!")
