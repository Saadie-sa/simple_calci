import streamlit as st 
st.title('HI DADDY')
st.write('HI dadday how are you? I hope your safe with your mommy. i know your fully safe daddy bcuz i know your mom')
calci=st.sidebar.radio('CALCULATORS',options=['simple','advanced'])
st.markdown('<h1>OHMS CALUCALATOR</h1>',unsafe_allow_html=True)
state=st.radio('Choose the operator',options=['voltage','Current','Resistance'])
if state == 'voltage':
    I=st.number_input('enter the current value:')
    R=st.number_input('enter the resistance value:')
    V=I*R
    st.write('the voltage is:',V)
if state == 'Current':
    V=st.number_input('enter the voltage value:')
    R=st.number_input('enter the resistance value:')
    if R!=0:
        I=V/R
        st.write('the current is:',I)
if state == 'Resistance':
    V=st.number_input('enter the voltage value:')
    I=st.number_input('enter the current value:')
    if I!=0:
        R=V/I
        st.write('the resistance is:',R)
    
#with st.form('form2'):
    