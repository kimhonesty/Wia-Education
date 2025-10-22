import streamlit as st
from datetime import date

st.set_page_config(page_title="나만의 업무 체크리스트", page_icon="📅")

st.title("📅 업무 체크리스트 with 일정 & 담당자")

# Session state 초기화
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 업무 추가 폼
with st.form("add_task", clear_on_submit=True):
    cols = st.columns([2,2,2])
    with cols[0]:
        task_name = st.text_input("업무명", "")
    with cols[1]:
        deadline = st.date_input("마감일", value=date.today())
    with cols[2]:
        partner = st.text_input("담당자(카운트파트너)", "")
    submitted = st.form_submit_button("📝 업무 추가")
    if submitted and task_name and partner:
        st.session_state.tasks.append({
            "name": task_name,
            "deadline": str(deadline),
            "partner": partner,
            "done": False
        })

st.divider()
st.markdown("### 오늘의 업무 현황")

if not st.session_state.tasks:
    st.info("업무를 추가하세요! 👆")
else:
    for idx, task in enumerate(st.session_state.tasks):
        col_a, col_b, col_c, col_d = st.columns([3,2,2,1])
        with col_a:
            checked = st.checkbox(
                f"{task['name']}", value=task["done"], key=f"done_{idx}")
            st.session_state.tasks[idx]["done"] = checked
        with col_b:
            st.write(f"⏰ `{task['deadline']}`")
        with col_c:
            st.write(f"🧑 {task['partner']}")
        with col_d:
            if st.button("❌ 삭제", key=f"delete_{idx}"):
                st.session_state.tasks.pop(idx)
                st.experimental_rerun()

    # 완료된 업무 한번에 삭제
    if st.button("✅ 완료된 업무 모두 삭제"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["done"]]
        st.experimental_rerun()

st.divider()
st.text_area("📒 오늘의 업무 메모", key="memo", height=80)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Streamlit 업무 체크리스트 예시 by ChatGPT 🔥")
