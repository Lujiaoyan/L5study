'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write(':orange[我的电影推荐:]')
    st.write('-------------------------------------------------------------------------------')
    st.write('《泰坦尼克号》')
    st.write('https://www.iqiyi.com/v_1lu8c0ub5bc.html?iqiyi=o&vfm=m_332_bing&fv=8c0aeeff542d8c03')
    st.write('《星球大战》')
    st.write('https://v.qq.com/x/cover/mzc00200s8w4zf7/m0039b67cr9.html')
    st.write(    )
    st.write(':orange[我的书籍推荐：]')
    st.write('---------------------------------------------------------------------------------------')
    st.write('《三体》')

def page2():
    '''图片处理工具'''
    pass

def page3():
    '''智慧词典'''
    pass

def page4():
    '''留言区'''
    pass

if page == '''我的兴趣推荐''':
    page1()

elif page == '''我的图片处理工具''':
    page2()

elif page == '''我的智慧词典''':
    page3()

elif page == '''我的留言区''':
    page4()