import streamlit as st
import random

# 맛집 리스트
restaurants = [
    "창원돼지국밥",
    "노랑통닭 창원성주점",
    "최춘복참치",
    "명륜진사갈비 창원중앙점",
    "롯데리아 창원중앙점",
    "초심쭈꾸미",
    "왕돈까스",
    "맹호칼국수",
    "부산아지매국밥",
    "미소반 챔피언",
    "대공주삼계탕",
    "미소닭갈비",
    "한솥도시락 창원중앙점",
    "도향반점",
    "이화갈비",
    "광덕왕족발",
    "두꺼비횟집",
    "원조누룽지통닭",
    "스타일커피",
    "전설의떡복이"
]

st.title("창원 현대위아 근처 회식장소 랜덤 추천기")

st.write("아래 버튼을 누르면 랜덤한 회식 맛집을 추천해드려요!")

if st.button("회식장소 추천받기"):
    choice = random.choice(restaurants)
    st.success(f"오늘의 회식 추천 장소: **{choice}**")

st.write("---")
st.write("리스트 안의 모든 맛집:")
for i, r in enumerate(restaurants, 1):
    st.write(f"{i}. {r}")
import streamlit as st
import random
import time

restaurants = [
    "창원돼지국밥",
    "노랑통닭 창원성주점",
    "최춘복참치",
    "명륜진사갈비 창원중앙점",
    "롯데리아 창원중앙점",
    "초심쭈꾸미",
    "왕돈까스",
    "맹호칼국수",
    "부산아지매국밥",
    "미소반 챔피언",
    "대공주삼계탕",
    "미소닭갈비",
    "한솥도시락 창원중앙점",
    "도향반점",
    "이화갈비",
    "광덕왕족발",
    "두꺼비횟집",
    "원조누룽지통닭",
    "스타일커피",
    "전설의떡복이"
]

st.title("창원 현대위아 근처 회식장소 랜덤 추천기")
st.write("버튼을 누르면 스피너 효과와 함께 오늘의 회식 장소를 추천해드려요!")

if st.button("회식장소 추천받기"):
    spinning_box = st.empty()
    spin_time = 3      # 총 스피너 시간(초)
    spin_interval = 0.05 # 스피너가 음식점을 바꾸는 간격(초)
    end_time = time.time() + spin_time

    while time.time() < end_time:
        name = random.choice(restaurants)
        spinning_box.markdown(f"🎰 **{name}**")
        time.sleep(spin_interval)

    final_choice = random.choice(restaurants)
    spinning_box.success(f"오늘의 회식 추천 장소: **{final_choice}**")

st.write("---")
st.write("전체 음식점 리스트:")
for i, r in enumerate(restaurants, 1):
    st.write(f"{i}. {r}")
