import streamlit as st
import time
st.set_page_config(page_title="Plotting Demo", page_icon="📈")
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
# CSS 스타일
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4B8BBE;
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        margin: 0.3em;
        font-size: 1.1em;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #306998;
    }
    </style>
""", unsafe_allow_html=True)

# 시간 입력
st.markdown("### ⏰ 타이머 시간 설정")
col1, col2, col3 = st.columns(3)
hours = col1.number_input("🕐 시", min_value=0, max_value=23, value=0, step=1)
minutes = col2.number_input("🕑 분", min_value=0, max_value=59, value=0, step=1)
seconds = col3.number_input("🕒 초", min_value=0, max_value=59, value=5, step=1)

# 총 시간(초) 계산
n = int(hours * 3600 + minutes * 60 + seconds)

# 출력 영역
y = st.empty()
y.markdown("<p style='text-align:center;'>⌛ 시간을 설정하고 아래 버튼을 눌러주세요</p>", unsafe_allow_html=True)

# 버튼 구성
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    start = st.button('▶️ 시작', key="start")
with col_btn2:
    clear = st.button('⏹ 클리어', key="clear")
with col_btn3:
    reset = st.button('🔁 리셋', key="reset")

# 세션 상태 초기화
if "original" not in st.session_state:
    st.session_state.original = n

# 클리어
if clear:
    y.markdown("<h3 style='text-align:center; color:red;'>🛑 타이머가 중지되었습니다.</h3>", unsafe_allow_html=True)

# 리셋
if reset:
    st.session_state.original = n
    y.markdown("<h3 style='text-align:center; color:#F39C12;'>🔄 리셋 완료! 다시 시작을 눌러주세요.</h3>", unsafe_allow_html=True)

# 타이머 실행
if start and n > 0:
    st.session_state.original = n
    with y:
        for i in range(n + 1):
            t = n - i
            h = t // 3600
            m = (t % 3600) // 60
            s = t % 60
            y.markdown(
                f"<h2 style='text-align:center; color:#2ECC71;'>⏳ 남은 시간: {h:02d}:{m:02d}:{s:02d}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(1)
