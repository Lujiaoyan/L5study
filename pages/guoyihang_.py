import streamlit as st
from PIL import Image


page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区"])

def page1():
    '''兴趣推荐'''
    st.write("我的书籍推荐")
    st.image("书籍.jpg")
    st.write("三体")
    st.write("-----------------------------")
    st.write("我的游戏推荐")
    st.write("使命召唤19")
    st.image("游戏.jpg")
    st.write("-----------------------------")
    st.write("我的旅游地推荐")
    st.write("新疆")
    st.image("旅游地.jpg")
    st.write("-----------------------------")
    st.write("我的电影推荐")
    st.write("加勒比海盗5")
    st.image("电影.jpg")
    st.write("https://v.qq.com/x/cover/00jxecd5him5kmn/v0024zl735r.html")
    st.write("-----------------------------")
    st.write("我的动漫推荐")
    st.write("火影忍者")
    st.image("动漫.jpg")
    st.write("-----------------------------")

    
def img_change(img):

    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):

            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
        
def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:

        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))

        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))

def page3():
    '''智慧词典'''
    pass

def page4():
    '''留言区'''
    st.write("欢迎给我留言")


if page=='我的兴趣推荐':
    page1()
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()
