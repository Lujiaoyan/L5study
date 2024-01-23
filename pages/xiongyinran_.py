'''我的主页'''
import streamlit as st
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
def page1():
    '''兴趣推荐'''
    with open('经典通用天气预报片头背景配乐.mp3','rb') as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write('我的电影推荐')
    st.write('《流浪地球》《流浪地球2》')
    st.image('流浪地球.png')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('“我的世界”、“原神”、“崩坏：星穹铁道”')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('《中华上下五千年》《海底两万里》《骆驼祥子》')
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('《点金卷》')
    st.write('-----------------------------')
def page2():
    '''图片处理工具'''
    pass
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass
if page=='我的兴趣推荐':
    page1()
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()