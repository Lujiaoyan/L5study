"'我的主页'"
import streamlit as st
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言'])
def page1 ():
    '我的兴趣推荐'
    st.write('我的电影推荐')
    st.write('---<<长津湖>>')
    st.write('我的电视剧推荐')
    st.write('---<<三体>>')
    st.write('我的书籍推荐')
    st.write('---<<鲁宾孙漂流记>>')
def page2 ():
    '我的图片处理工具'
    pass
def page3 ():
    '我的智慧词典'
    pass
def page4 ():
    '我的留言'
    pass
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言':
    page4()
#'python -m streamlit run C:\Users\Administrator\Desktop\我的网络\myhome.py'    