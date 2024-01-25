'''我的主页'''
import streamlit as st
from PIL import Image

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
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))

def page3():
    '''智慧词典'''
    pass

def page4():
    '''留言区'''
    pass

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
        

if page == '''我的兴趣推荐''':
    page1()

elif page == '''我的图片处理工具''':
    page2()

elif page == '''我的智慧词典''':
    page3()

elif page == '''我的留言区''':
    page4()
