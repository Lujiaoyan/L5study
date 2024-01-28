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
def page3():
    '''我的智慧词典'''
    st.write("智慧词典")   
    with open("words_space.txt","r",encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding='utf-8') as f:
        time_list = f.read().split('\n')
        
    for i in range(len(time_list)):
        time_list[i] = time_list[i].split('#')
    time_dict = {}
    for i in time_list:
        time_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')    
    if word in word_dict:
        st.write(word_dict[word]) 
        n = word_dict[word][0]   
        if n in time_dict:
            time_dict[n] += 1  
        else:
            time_dict[n] = 1  
        with open("check_out_times.txt","w",encoding='utf-8') as f:
            message = ''
            for k,v in time_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:',time_dict[n])
def page4():
    '''留言区'''
    st.write("我的留言区")
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list.split('#')
    for i in messages_list:
        if i[1] == '用户1' :
            with st.chat_message('1'):
                st.write(i[1],':',i[2])
        elif i[1] == '用户2' :
            with st.chat_message('2'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是.....',['用户1','用户2'])
    new_message = st.text_input('想要说的话.......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
    with open('leave_messages.txt','w',encoding='utf=8') as f:
        message = ''
        for i in messages_list:
            message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
        message = message[:-1]
        f.write(message)


if page == "我的兴趣推荐":
    page1()
if page == "我的图片处理工具":
    page2()
if page == "我的智慧词典":
    page3()
if page == "我的留言区":
    page4()
