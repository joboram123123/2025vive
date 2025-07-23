import streamlit as st
import time

st.title("⏱️ Streamlit 타이머")

# 세션 상태 초기화
n = st.number_input("타이머 시간을 초 단위로 입력하세요", min_value=1, max_value=3600, value=5, step=1)

y = st.empty()
y.write('please Click start button')

# 타이머 시작/정지 버튼
c1, c2, c3,_=st.columns([1,1,1,5])
start = c1.button('시작', key=1)
clear = c2.button('클리어', key=2)
c3.button('리셋', key = 3)

if start:
    with y:
        for i in range(n+1):
            t = n-i
            st.write(f'카운트다운 {t} 초')
            time.sleep(1)
