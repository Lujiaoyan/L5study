import streamlit as st


page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区"])

def page1():
    '''兴趣推荐'''
    st.write("我的书籍推荐")
    st.image("书籍.jpg")
    st.write("-----------------------------")
    st.write("我的游戏推荐")
    st.image("游戏.jpg")
    st.write("-----------------------------")
    st.write("我的旅游地推荐")
    st.image("旅游地.jpg")
    st.write("-----------------------------")
    st.write("我的电影推荐")
    st.image("电影.jpg")
    st.write("-----------------------------")
    st.write("我的动漫推荐")
    st.image("动漫.jpg")
    st.write("-----------------------------")

def page2():
    '''图片处理工具'''
    pass

def page3():
    '''智慧词典'''
    pass

def page4():
    '''留言区'''


if page=='我的兴趣推荐':
    page1()
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()
