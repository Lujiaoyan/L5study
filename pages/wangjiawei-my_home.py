'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的主页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''兴趣推荐'''
    st.write(":orange[书籍推荐]")
    st.write("《月亮与六便士》","《追风筝的人》","《瓦尔登湖》")
    st.image("six.jpg")
    st.image("kite.png")
    st.image("lake.png")
    st.write("--------------------------------------------")
    st.write(":orange[电影推荐]")
    st.write("该片以盛唐为背景，讲述安史之乱后，整个长安因战争而陷入混乱，身处局势之中的高适回忆起自己与李白的过往的故事。")
    st.image("like.jpg")
    st.write(":orange[诗人推荐榜TOP3]")
    
    tab1,tab2,tab3 = st.tabs(["Top1:李清照","Top2:李白","Top3苏轼",])
    with tab1:
        st.write("生平简介：李清照（1084年3月13日—1155年） ，号易安居士，齐州章丘（今山东省济南市章丘区）人。",":red[宋代婉约派代表词人，有“千古第一才女”之称。]")
        st.write("后世评价：宋·朱熹：本朝妇人能文，只有李易安与魏夫人。李有诗，大略云：“两汉本继绍，新室如赘疣。所以嵇中散，至死薄殷周。“中散非汤武得国，引之以比王莽，如此等语，岂女子所能。（《朱子语类》卷一百四十）")
        st.image("李清照.png")
    with tab2:
        st.write("生平简介：李白（701年2月28日—762年12月） ，字太白，号青莲居士 ，祖籍陇西成纪（今甘肃省秦安县），出生于蜀郡绵州昌隆县（今四川省江油市青莲乡），一说出生于西域碎叶。","：red[唐朝伟大的浪漫主义诗人，凉武昭王李暠九世孙 。]")   
        st.write("后世评价：杜甫：①“笔落惊风雨，诗成泣鬼神。”（《寄李十二白二十韵》）② “清新庾开府，俊逸鲍参军”（《春日忆李白》）③“李白斗酒诗百篇，长安市上酒家眠。天子呼来不上船，自称臣是酒中仙。”（《饮中八仙歌》）④秋来相顾尚飘蓬，未就丹砂愧葛洪。痛饮狂歌空度日，飞扬跋扈为谁雄。（《赠李白》）⑤不见李生久，佯狂真可哀。世人皆欲杀，吾意独怜才。敏捷诗千首，飘零酒一杯。匡山读书处，头白好（一作始）归来。（《不见》） ⑥文章憎命达，魑魅喜人过。（《天末忆李白》） ⑦冠盖满京华，斯人独憔悴。（《梦李白二首·其二》")
        st.image("李白.jpg")   
    with tab3:
        st.write("生平简介：苏轼（1037年—1101年），字子瞻，又字和仲，号铁冠道人、东坡居士，世称苏东坡、苏仙、坡仙。眉州眉山（今属四川省眉山市）人，北宋文学家，书法家、画家，历史治水名人。与父苏洵、弟苏辙三人并称“三苏”。")
        st.write("后世评价：黄庭坚：①人谓东坡作此文，因难以见巧，故极工。余则以为不然。彼其老于文章，故落笔皆超逸绝尘耳。（《跋子瞻〈醉翁操〉》） ②挟以文章妙天下，忠义之气贯日月。（《跋东坡墨迹》）③元祐中锁试礼部，每来见过，案上纸不择精粗，书遍乃已。性喜酒，然不能四五龠已烂醉，不辞谢而就卧，鼻酣如雷。少焉苏醒，落笔如风雨，虽谑弄皆有义味，真神仙中人。此岂与今世翰墨之士争衡哉！（《题东坡字后》） ")
        st.image("苏轼.png")   
            
    st.write(":orange[诗词推荐]")
    st.write("《如梦令·常记溪亭日暮》","《如梦令·昨夜雨疏风骤》","《登科后》","《将进酒》","《侠客行》")
    st.write("--------------------------------------------")
    st.write(":orange[美食推荐]")
    st.write("兰州牛肉面：",
            "兰州牛肉面 ，始于清朝嘉庆年间（1799年），系东乡族马六七从河南省怀庆府清化陈维精处学成带入兰州的，后经后人陈和声、马宝仔等人以“一清（汤）二白（萝卜）三绿（香菜蒜苗）四红（辣子） 五黄（面条黄亮）”统一了兰州牛肉面的标准。在其后二百多年的漫长岁月里，以一碗面而享誉天下，以肉烂汤鲜、面质精细而蜚声中外，青海人将兰州牛肉面以兰州拉面的商标打入了全国各地，赢得了国内乃至全世界范围内食客的好评和荣誉。")
    st.image("兰州拉面.png")
def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))

        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
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
    pass

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()