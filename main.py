import streamlit as st
import time

st.title("⏱️ 시간·분·초 입력 카운트다운 타이머")

# 사용자 입력: 시간, 분, 초
col1, col2, col3 = st.columns(3)
hours = col1.number_input("시간", min_value=0, max_value=23, value=0, step=1)
minutes = col2.number_input("분", min_value=0, max_value=59, value=0, step=1)
seconds = col3.number_input("초", min_value=0, max_value=59, value=5, step=1)

# 전체 초로 변환
n = int(hours * 3600 + minutes * 60 + seconds)

# 안내 영역
y = st.empty()
y.write('⌛ 시간을 설정하고 [시작]을 눌러주세요')

# 버튼 구성
c1, c2, c3, _ = st.columns([1, 1, 1, 5])
start = c1.button('▶️ 시작', key=1)
clear = c2.button('⏹ 클리어', key=2)
reset = c3.button('🔁 리셋', key=3)

# 세션 상태 초기화
if "original" not in st.session_state:
    st.session_state.original = n

# 클리어 동작
if clear:
    y.write("🛑 타이머가 클리어되었습니다.")

# 리셋 동작
if reset:
    st.session_state.original = n
    y.write("🔄 리셋되었습니다. [시작] 버튼을 다시 눌러주세요.")

# 타이머 시작
if start and n > 0:
    st.session_state.original = n
    with y:
        for i in range(n + 1):
            t = n - i
            h = t // 3600
            m = (t % 3600) // 60
            s = t % 60
            st.write(f'⏳ 남은 시간: **{h:02d}:{m:02d}:{s:02d}**')
            time.sleep(1)
