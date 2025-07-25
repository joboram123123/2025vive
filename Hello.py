import streamlit as st
import requests
from datetime import datetime, timedelta
import time
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")
st.markdown(
    """
    <style>
    .go-button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition-duration: 0.3s;
    }
    .go-button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<a href="https://2025vive-kjfajmxkrrc22dg89w9bu3.streamlit.app/" target="_blank">'
    '<button class="go-button">타이머 페이지로 가기</button></a>',
    unsafe_allow_html=True
)

# worldtimeapi에서 서울시간 불러오기
@st.cache_data(ttl=60)  # 60초마다 새로고침
def get_seoul_time():
    try:
        res = requests.get("http://worldtimeapi.org/api/timezone/Asia/Seoul")
        res.raise_for_status()
        data = res.json()
        datetime_str = data["datetime"]
        # ISO 형식 datetime 문자열 -> datetime 객체 (타임존 제거)
        dt = datetime.fromisoformat(datetime_str[:-6])
        return dt
    except Exception as e:
        st.error(f"서버 시간 불러오기 실패: {e}")
        return None

server_now = get_seoul_time()
if server_now is None:
    st.stop()

st.write(f"서버 기준 현재 서울 시간: {server_now.strftime('%Y-%m-%d %H:%M:%S')}")

# 사용자 입력: 카운트다운 지속 시간 (초)
duration = st.number_input("몇 초 동안 카운트다운 할까요?", min_value=1, max_value=3600, value=10, step=1)

start = st.button("▶️ 서버 시간 기준 타이머 시작")

if start:
    end_time = server_now + timedelta(seconds=duration)
    while True:
        now = get_seoul_time()
        if now is None:
            break
        remaining = (end_time - now).total_seconds()
        if remaining <= 0:
            st.success("⏰ 타이머 종료!")
            break
        hours = int(remaining // 3600)
        minutes = int((remaining % 3600) // 60)
        seconds = int(remaining % 60)
        st.write(f"남은 시간: {hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        st.experimental_rerun()
