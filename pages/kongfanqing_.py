import streamlit as st  

page = st.sidebar.radio("我的首页",['我的兴趣推荐',"我的图片处理工具","我的智慧词典","我的留言区"])

def page1():
    st.write('我的电影推荐')
    st.write('------------------------------')
    st.write('我的图片处理工具推荐')
    st.write('------------------------------')
    st.write('我的智慧词典推荐')
    st.write('------------------------------')
    st.write('我的留言推荐')
    st.write('------------------------------')

def page2():
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')

def page3():
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')

def page4():
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')
    st.write('pass')
    st.write('------------------------------')

if page == "我的兴趣推荐":
    page1()
if page == "我的图片处理工具":
    page2()
if page == "我的智慧词典":
    page3()
if page == "我的留言区":
    page4()
