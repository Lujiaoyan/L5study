'''我们的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的推荐'''
    st.write(':blue我的电影推荐')
    st.write('变形金刚全部','盗梦空间','这个杀手不太冷静')
    st.write('----------------------------------------------')
    st.write(':blue我的游戏推荐')
    st.write('王者荣耀','原神','史莱姆牧场')
    dab1, dab2, dab3 = st.tabs(['王者荣耀','原神','史莱姆牧场'])
    with dab1:
        st.image("a.jpg")
    with dab2:
        st.image("b.jpg")
    with dab3:
        st.image("c.jpg")
        
    st.write('----------------------------------------------')
    st.write(':blue我的书籍推荐')
    st.write('三国演义','西游记','鲁宾逊漂流记')
    st.write('----------------------------------------------')
    st.write(':blue我的习题集推荐')
    st.write('英语语法习题集','中国文学史','数学分析解题指南')
    st.write('----------------------------------------------')
    
def page_2():
    '''图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglassses")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

        tab1, tab2, tab3, tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
def page_3():
    '''智慧词典'''
    st.write('风云翻译官','迅捷翻译')

def page_4():
    '''留言区'''
    st.write('有没有跟我兴趣相投的人，快来和我交流吧。')
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
