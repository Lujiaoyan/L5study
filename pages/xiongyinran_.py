'''我的主页'''
import streamlit as st
from PIL import Image,ImageOps,ImageFilter
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
def page1():
    '''兴趣推荐'''
    with open('经典通用天气预报片头背景配乐.mp3','rb') as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    tab1,tab2,tab3,tab4=st.tabs(['我的电影推荐','我的游戏推荐','我的书籍推荐','我的习题集推荐'])
    with tab1:
        st.write('我的电影推荐')
        st.write('《流浪地球》《流浪地球2》')
        st.image('流浪地球.png')
    with tab2:
        st.write('我的游戏推荐')
        st.write('“我的世界”、“原神”、“崩坏：星穹铁道”')
    with tab3:
        st.write('我的书籍推荐')
        st.write('《中华上下五千年》《海底两万里》《骆驼祥子》')
    with tab4:
        st.write('我的习题集推荐')
        st.write('《点金卷》')
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
def img_sketch(img):
    width,height=img.size
    _,axes=plt.subplots(1,5,figsize=(30,30))
    img_gray=img.convert('L')
    img_invert=ImageOps.invert(img_gray)
    img_gaussian=img_invert.filter(ImageFilter.GaussianBlur(5))
    for x in range(width):
        for y in range(height):
            A=img_gray.getpixel((x,y))
            B=img_gaussian.getpixel((x,y))
            img_gray.putpixel((x,y),min(int(A+A*B/(255-B)),255))
    return img_gray
def page2():
    '''图片处理工具'''
    st.write(':sunglasses:图片处理小程序:sunglasses')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5=st.tabs(['原图','改色1','改色2','改色3','素描风格'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            st.image(img_sketch(img))
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass
if page=='我的兴趣推荐':
    page1()
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()
