'''我的首页'''
import streamlit as st
from PIL import Image
import copy

page = st.sidebar.radio('阿短首页', ['阿短的兴趣推荐', '阿短的图片处理工具', '阿短的智慧词典', '阿短的留言区'])

def page_1():
    '''阿短的推荐'''
    with open('歌曲.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.png')
    st.write(':red[阿短的电影推荐]')
    st.write('-----------------------------')
    st.write('阿短的游戏推荐')
    st.write('-----------------------------')
    st.write('阿短的书籍推荐')
    st.write('-----------------------------')
    st.write('阿短的习题集推荐')
    st.write('-----------------------------')

def page_2():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
    # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # st.image(img)
        # st.image(img_change(img, 0, 2, 1))
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["原图", "改色1", "改色2", "改色3", "改色4", "改色5", "改色6"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        with tab5:
            st.image(img_change(img, 2, 0, 1))
        with tab6:
            st.image(img_change(img, 2, 1, 0))
        with tab7:
            st.image(img_change(img, 1, 2, 1))

def page_3():
    '''阿短的智慧词典'''
    # 局部变量区
    words_list = []
    words_dict = {}
    # 标题
    st.write('阿短的智慧词典')
    # 加载词典内容
    with open('wordsSpace.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])

def page_4():
    '''阿短的留言区'''
    # 局部变量区
    aduan_messages = [] # 信息存储列表
    show_messages = {} # 信息展示字典
    buttons = {} # 按钮存储字典
    key = 0 # 当前被点击的按钮
    name = '' # 当前使用者
    # 标题
    st.write('阿短的留言区，留下你想说的话：')
    name = st.selectbox('我是...', ['阿短', '神秘人', '编程猫', '探月兔', '圆周狸', '雷电猴', '大黄鸡'])
    # 读取留言数据
    with open('aduan_messages.txt', 'r', encoding='utf-8') as f:
        aduan_messages = f.read()
    # 处理留言数据格式
    aduan_messages = aduan_messages.split('\n')
    for i in range(len(aduan_messages)):
        aduan_messages[i] = aduan_messages[i].split('#')
    for i in aduan_messages:
        if i[1] == '0':
            show_messages[i[0]] = i[3] + '：' + i[2] + '\n\n'
        else:
            show_messages[i[1]] = show_messages[i[1]] + i[3] + '：' + i[2] + '\n\n'
    # 显示留言内容
    for i in range(int(aduan_messages[-1][0])+1):
        if str(i) in show_messages:
            with st.chat_message('user'):
                st.write(show_messages[str(i)])
                # 创建回复按钮
                buttons[i] = st.button('回复', key=i)
    # 创建输入框
    if st.button('新留言'):
        key = 0
    if key == 0:
        message = st.chat_input(name+'：新留言...')
    if message:
        with open('aduan_messages.txt', 'a', encoding='utf-8') as f:
            msg = '\n'
            msg += str(int(aduan_messages[-1][0]) + 1) + '#'
            msg += '0#'
            msg += message + '#'
            msg += name
            f.write(msg)
    # 根据被点击的回复按钮，弹出回复框
    for k, button in buttons.items():
        if button:
            message = st.chat_input(name+'：回复...')
            print(k, type(k))
            if message:
                print(message)
                with open('aduan_messages.txt', 'a', encoding='utf-8') as f:
                    msg = '\n'
                    msg += str(int(aduan_messages[-1][0]) + 1) + '#'
                    msg += k + '#'
                    msg += message + '#'
                    msg += name
                    f.write(msg)

def img_change(img, rc, gc, bc):
    '''图片改色处理'''
    res = copy.deepcopy(img)
    width, height = res.size
        # 加载图片像素点内容
    res_array = res.load()
    # 循环处理像素点
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = res_array[x, y][rc]
            g = res_array[x, y][gc]
            b = res_array[x, y][bc]
            # 将处理后的点覆盖原数据
            res_array[x, y] = (r, g, b)
    return res

if page == '阿短的兴趣推荐':
    page_1()
elif page == '阿短的图片处理工具':
    page_2()
elif page == '阿短的智慧词典':
    page_3()
elif page == '阿短的留言区':
    page_4()