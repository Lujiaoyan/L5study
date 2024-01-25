import streamlit as st  
from PIL import Image
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

        

def img_change(img):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][0]
            g=img_array[x,y][1]
            b=img_array[x,y][2]
            img_array[x,y] =(b,g,r)
    return img


def page2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses：")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img))
if page == "我的兴趣推荐":
    page1()
if page == "我的图片处理工具":
    page2()
if page == "我的智慧词典":
    page3()
if page == "我的留言区":
    page4()
