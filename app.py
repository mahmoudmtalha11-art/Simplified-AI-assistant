import streamlit as st
from groq import Groq

st.set_page_config(page_title="موقعي للذكاء الاصطناعي", page_icon="🤖")

st.title("موقعي للذكاء الاصطناعي 🤖")
st.write("أهلاً بك! هذا الموقع متصل بنموذج ذكاء اصطناعي حقيقي ويجيب على أي سؤال في العالم.")

api_key = st.secrets.get("GROQ_API_KEY") or st.text_input("أدخل مفتاح Groq API الخاص بك:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        user_input = st.text_input("اسألني عن أي شيء في العالم:")
        
        if st.button("إرسال"):
            if user_input:
                with st.spinner("جاري التفكير والتوليد..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": user_input,
                            }
                        ],
                        model="llama-3.1-8b-instant",
                    )
                    answer = chat_completion.choices[0].message.content
                    st.success(answer)
            else:
                st.warning("الرجاء كتابة سؤال أولاً!")
                
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
else:
    st.info("الرجاء إدخال مفتاح الـ API أعلاه للبدء في طرح الأسئلة.")
