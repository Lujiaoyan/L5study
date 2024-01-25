'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('我的电影推荐')
    st.write('-----------------------------------------------------')
    st.write('我的游戏推荐')
    st.write('--------------------------------------------------------')
    st.write('我的书籍推荐')
    st.write('----------------------------------------------------------')
    st.write('我的习题推荐')
    st.write('----------------------------------------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write("sunglasses：图片换色小程序：sunglasses：")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取图片文件的名称类型大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 1, 2))

        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height =img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取rgb
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4
