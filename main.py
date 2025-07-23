import streamlit as st
import time

y = st.empty()
y.write('please Click start button')

c1, c2, c3,_=st.columns([1,1,1,5])
start = c1.button('시작', key=1)
clear = c2.button('클리어', key=2)
c3.button('리셋', key = 3)

if start:
    with y:
        for i in range(6):
            t = 5-i
            st.write(f'카운트다운 {t} 초')
            time.sleep(1)
