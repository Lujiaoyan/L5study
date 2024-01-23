'''我的主页'''
import streamlit as st

with open('轻松获胜.wav', 'rb') as f:
    mymp3 = f.read()
st.audio(mymp3, format='audio/wav', start_time=0)



page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    '''我的兴趣推荐'''
    st.write('我最喜欢的电影推荐')
    st.write('唐人街探案、流浪地球、我和我的祖国')
    st.write('我最喜欢的游戏推荐')
    st.write('outlast(逃生)、buckshot roulette(俄罗斯轮盘赌)、迷你世界')
    st.write('我最喜欢的书籍推荐')
    st.write('童年、爱的教育、鲁滨逊漂流记')







def page2():
    '''我的图片处理工具'''
    pass

def page3():
    '''我的智慧词典'''
    pass

def page4():
    '''我的留言区'''
    pass

if page == '''我的兴趣推荐''':
    page1()

if page == '''我的图片处理工具''':
    page2()

if page == '''我的智慧词典''':
    page3()

if page == '''我的留言区''':
    page4()



