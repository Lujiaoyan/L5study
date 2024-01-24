'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    '''我的兴趣推荐'''
    with open('轻松获胜.wav', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/wav', start_time=0)
    tab1, tab2, tab3 = st.tabs(['我的电影推荐', '我的游戏推荐', '我的书籍推荐'])
    with tab1:
        st.write('我的电影推荐')
        st.write('唐人街探案、流浪地球、我和我的祖国')
    with tab2:
        st.write('我的游戏推荐')
        st.write('outlast(逃生)、buckshot roulette(俄罗斯轮盘赌)、迷你世界')
    with tab3:
        st.write('我的书籍推荐')
        st.write('童年、爱的教育、鲁滨逊漂流记')

def page2():
    '''我的图片处理工具'''
    with open('你干嘛.wav', 'rb') as p:
        mymp4 = p.read()
    st.audio(mymp4, format='audio/wav', start_time=0)
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色一', '改色二', '改色三'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))




def page3():
    '''我的智慧词典'''
    pass

def page4():
    '''我的留言区'''
    pass

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == '''我的兴趣推荐''':
    page1()

if page == '''我的图片处理工具''':
    page2()

if page == '''我的智慧词典''':
    page3()

if page == '''我的留言区''':
    page4()



