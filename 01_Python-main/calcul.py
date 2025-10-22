import streamlit as st

st.set_page_config(page_title="🌟 화려한 스트림릿 계산기", page_icon="🧮")

st.markdown("<h1 style='text-align:center; color:#FFD700;'>🧮 화려한 계산기</h1>", unsafe_allow_html=True)
st.write("## 원하는 연산을 선택해주세요!")

# 컬럼 나누기
col1, col2, col3 = st.columns([2,1,2])

with col1:
    st.markdown("#### 🔢 첫 번째 숫자")
    num1 = st.number_input("", value=0.0, key="num1", format="%.2f")

with col3:
    st.markdown("#### 🔢 두 번째 숫자")
    num2 = st.number_input("", value=0.0, key="num2", format="%.2f")

st.divider()

# 버튼 스타일 바꾸기
st.markdown("""
<style>
div.stButton > button {
    color: #fff;
    background-color: #FF5722;
    border-radius: 8px;
    height: 45px;
    font-size: 1.2em;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

# 이모지 포함 연산 버튼
operation = st.selectbox("**💡 연산자 선택**", [
    "➕ 덧셈 (+)", "➖ 뺄셈 (-)", "✖️ 곱셈 (×)", "➗ 나눗셈 (÷)"
])

if st.button("✨ 계산하기"):
    with st.container():
        st.markdown("### 🎲 결과는?")
        result = None
        if operation == "➕ 덧셈 (+)":
            result = num1 + num2
            st.success(f"🟢 **{num1} + {num2} = `{result}`**")
        elif operation == "➖ 뺄셈 (-)":
            result = num1 - num2
            st.success(f"🟣 **{num1} - {num2} = `{result}`**")
        elif operation == "✖️ 곱셈 (×)":
            result = num1 * num2
            st.success(f"🟠 **{num1} × {num2} = `{result}`**")
        elif operation == "➗ 나눗셈 (÷)":
            if num2 != 0:
                result = num1 / num2
                st.success(f"🔵 **{num1} ÷ {num2} = `{result}`**")
            else:
                st.error("🛑 0으로 나눌 수 없습니다!")

# 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888;font-size:13px;'>by Streamlit ✨ | 화려한 계산기 예시</p>", unsafe_allow_html=True)
