'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的主页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write(":orange[书籍推荐]")
    st.write("《月亮与六便士》","《追风筝的人》","《瓦尔登湖》")
    st.image("t.png")
    st.write("--------------------------------------------")
    st.write(":orange[电影推荐]")
    st.image("like.jpg")
    st.write(":orange[诗人推荐]")
    st.write("李清照（1084年3月13日—1155年),号易安居士，齐州章丘（今山东省济南市章丘区）人。",":red[宋代婉约派代表词人，有“千古第一才女”之称。] ")
    st.image("李清照.png")
    st.write(":orange[诗词推荐]")
    st.write("《如梦令·常记溪亭日暮》","《如梦令·昨夜雨疏风骤》","《登科后》","《将进酒》","《侠客行》")
    st.write("--------------------------------------------")
    st.write(":orange[美食推荐]")
    st.write("兰州牛肉面：",
            "兰州牛肉面 ，始于清朝嘉庆年间（1799年），系东乡族马六七从河南省怀庆府清化陈维精处学成带入兰州的，后经后人陈和声、马宝仔等人以“一清（汤）二白（萝卜）三绿（香菜蒜苗）四红（辣子） 五黄（面条黄亮）”统一了兰州牛肉面的标准。在其后二百多年的漫长岁月里，以一碗面而享誉天下，以肉烂汤鲜、面质精细而蜚声中外，青海人将兰州牛肉面以兰州拉面的商标打入了全国各地，赢得了国内乃至全世界范围内食客的好评和荣誉。")
    st.image("兰州拉面.png")
def page2():
    '''图片处理工具'''
    pass

def page3():
    '''智慧词典'''
    pass

def page4():
    '''留言区'''
    pass

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()