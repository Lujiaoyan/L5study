"""我的主页"""
import streamlit as st
import pandas as pd
from PIL import Image,ImageDraw,ImageOps,ImageFilter

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
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    # st.image("bcm.jpg")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_size = uploaded_file.size
        file_type = uploaded_file.type

        img = Image.open(uploaded_file)
        st.image(img)
        #st.image(image_change(img,0,2,1))

        tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["原图","改色1","改色2","改色3","字符串风格转换","素描风格转换"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(image_change(img,0,2,1))
        with tab3:
            st.image(image_change(img,1,0,2))
        with tab4:
            st.image(image_change(img,1,2,0))
        with tab5:
            st.image(img2str(img))
        with tab6:
            st.image(img2sketch(img))

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

def image_change(img,rposition,gposition,bposition):
    width,height = img.size
    img_array = img.load()
    for y in range(height):
        for x in range(width):
            r = img_array[x,y][rposition]
            g = img_array[x,y][gposition]
            b = img_array[x,y][bposition]
            img_array[x,y] = (b,g,r)
    return img

def img2str(img):#算量过大，用那张星空图片会被识别为DOS
    img=img.convert("L")
    width,height=img.size
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
    txt = ""
    for y in range(height):
        for x in range(width):
            pos=(x,y)
            pixel=img.getpixel(pos)
            index=(ASCII_HIGH[int(pixel/256*70)])
            txt+=index+" "
        txt+="\n"
    imgn=Image.new("RGB",(width*12,height*15),"white")
    aw=ImageDraw.Draw(imgn)
    aw.text((0,0),txt,fill=(0,0,0))
    imgn.resize((width*12,width*12))
    k=imgn.resize((width*12, width*12))
    return imgn

def img2sketch(img):
    width,height = img.size
    img_l = img.convert("L")
    img_i=ImageOps.invert(img_l)
    img_g=img_i.filter(ImageFilter.GaussianBlur(10))
    for x in range (width):
        for y in range(height):
            A=img_l.getpixel((x,y))
            B=img_g.getpixel((x,y))
            if B==255:
                img_g.putpixel((x,y),min(int(A+A*B/(255-B+1)),255))
            else:
                img_g.putpixel((x, y), min(int(A+A*B/(255-B)), 255))
    return img_g

if page == "我的兴趣推荐":#内置无限循环
    page1()
elif page == "我的图片处理工具":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
elif page == "基本信息":
    page5()
