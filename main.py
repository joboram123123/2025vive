import streamlit as st
import time

# 세션 상태 초기화
if "count" not in st.session_state:
    st.session_state.count = 5
if "running" not in st.session_state:
    st.session_state.running = False

y = st.empty()
y.write('please Click start button')

# 버튼 구성
c1, c2, c3, _ = st.columns([1, 1, 1, 5])
start = c1.button('시작', key='start')
clear = c2.button('클리어', key='clear')
reset = c3.button('리셋', key='reset')

# 버튼 동작 처리
if start:
    st.session_state.running = True

if clear:
    st.session_state.count = 0
    st.session_state.running = False

if reset:
    st.session_state.count = 5
    st.session_state.running = False

# 타이머 작동
if st.session_state.running and st.session_state.count > 0:
    with y:
        st.write(f'카운트다운 {st.session_state.count} 초')
    time.sleep(1)
    st.session_state.count -= 1
    st.experimental_rerun()  # 여기까지 실행 후 멈춰야 함
    st.stop()  # 이후 코드 실행 막기

# 타이머 종료 메시지
elif st.session_state.count == 0 and st.session_state.running:
    with y:
        st.success("⏰ 타이머 종료!")
    st.session_state.running = False
