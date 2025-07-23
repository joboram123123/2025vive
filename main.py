import streamlit as st
import time

st.title("⏱️ Streamlit 타이머")

# 세션 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "running" not in st.session_state:
    st.session_state.running = False

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
    elapsed = int(time.time() - st.session_state.start_time)
    st.write(f"⏳ 경과 시간: **{elapsed}초**")
    time.sleep(1)
    st.experimental_rerun()
elif st.session_state.start_time:
    elapsed = int(time.time() - st.session_state.start_time)
    st.write(f"⏹️ 멈춤 - 마지막 시간: **{elapsed}초**")
