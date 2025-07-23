import streamlit as st
import time

st.title("⏱️ Streamlit 타이머")

# 세션 상태 초기화
n = st.number_input("타이머 시간을 초 단위로 입력하세요", min_value=1, max_value=3600, value=5, step=1)

y = st.empty()
y.write('please Click start button')

# 타이머 시작/정지 버튼
def toggle_timer():
    if not st.session_state.running:
        st.session_state.start_time = time.time()
        st.session_state.running = True
    else:
        st.session_state.running = False

if st.button("▶️ 타이머 시작 / 일시정지", on_click=toggle_timer):
    pass

# 타이머 표시
if st.session_state.running:
    with y:
        for i in range(n):
            t=n-i
            st.wirte('남은 시간 : {t}초')
            time.sleep(1)
