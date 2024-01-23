"""我的主页"""
import streamlit as st
import pandas as pd

with open("wa.mp3","rb") as h:
    mp31=h.read()
with open("We.mp3","rb") as j:
    mp32=j.read()
with open("oh.mp3","rb") as q:
    mp33=q.read()
with open("in.mp3","rb") as z:
    mp34=z.read()

page = st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区","基本信息"])

def page1():
    """兴趣推荐"""
    st.write(":orange[我的兴趣推荐]")
    st.write("想不出来了，放两首歌吧。")
    st.audio(mp31,format = "audio/mp3",start_time=0)
    st.audio(mp32,format = "audio/mp3",start_time=0)
    st.audio(mp33,format = "audio/mp3",start_time=0)
    st.audio(mp34,format = "audio/mp3",start_time=0)
    number = 12345
    test = {
        "一列":[1,2,3],
        "二列":["a","b","c"]
    }
    test = pd.DataFrame(test)
    st.write(test)
    st.write(number)

def page2():
    """图片处理工具"""
    st.image("bcm.jpg")

def page3():
    """智慧词典"""
    pass

def page4():
    """留言区"""
    pass

def page5():
    """基本信息"""
    st.write("made by BTCcommnue")
    st.write("对象用户:所有能找到这个网站的人")
    st.write("用途:我也不知道")
    st.write("现有模块:文字、图片、音频展示")
    st.write("改进：想不出来")
    st.write("原创模块功能：不会")

if page == "我的兴趣推荐":
    page1()
elif page == "我的图片处理工具":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
elif page == "基本信息":
    page5()
