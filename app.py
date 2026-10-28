import streamlit as st
from groq import Groq

st.set_page_config(page_title="موقعي للذكاء الاصطناعي", page_icon="🤖")

st.title("موقعي للذكاء الاصطناعي 🤖")
st.write("أهلاً بك! هذا الموقع متصل بنموذج ذكاء اصطناعي حقيقي ويجيب على أي سؤال في العالم.")

api_key = st.secrets.get("GROQ_API_KEY") or st.text_input("أدخل مفتاح Groq API الخاص بك:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # جلب قائمة النماذج الفعالة حالياً في حسابك واختيار نموذج صالح تلقائياً
        models = client.models.list()
        active_model = None
        for m in models.data:
            if "llama" in m.id:
                active_model = m.id
                break
        
        # إذا لم يجد لاما، يأخذ أول نموذج متاح
        if not active_model and models.data:
            active_model = models.data[0].id
        else:
            active_model = "llama-3.1-8b-instant"

        user_input = st.text_input("اسألني عن أي شيء في العالم:")
        
        if st.button("إرسال"):
            if user_input:
                with st.spinner("جاري التفكير والتوليد..."):
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "أنت مساعد ذكي. أجب على الأسئلة بدقة ووضوح باللغة العربية."
                            },
                            {
                                "role": "user",
                                "content": user_input,
                            }
                        ],
                        model=active_model,
                    )
                    answer = chat_completion.choices[0].message.content
                    st.success(answer)
            else:
                st.warning("الرجاء كتابة سؤال أولاً!")
                
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
else:
    st.info("الرجاء إدخال مفتاح الـ API أعلاه للبدء في طرح الأسئلة.")
