'''我的主页'''
import streamlit as st
import pandas as pd
from PIL import Image,ImageDraw, ImageOps,ImageFilter
import random as rd
import matplotlib.pyplot as plt
import requests
import wordlistenquiry
import base64
import time
import os

def page1():
    st.balloons()
    st.image('logo.png')
    st.markdown('# 网页故事|Story')
    st.write('------------------------------------------------------------------------')
    with open('MS1.mp3','rb') as f:
        page1bgm = f.read()
    st.audio(page1bgm,format='audio/mp3',start_time=0)
    st.write('------------------------------------------------------------------------')
    para_pic_num = 1
    with open('网页故事.txt','r',encoding='utf-8') as t:
        story = t.read()
        paras = story.split()
    for para in paras:
        st.write(para)
        st.image(f'page1_{para_pic_num}.png')
        st.write(' ')
        para_pic_num += 1
    st.write('------------------------------------------------------------------------')
    st.markdown('# 板块简介')
    st.write(' ')
    directions = {'板块名称':['图片编辑|Pic','词汇速查|Dictionary','留言区|Chat','数学专区|Mathematics','AI聊天'],
                '简介':['提供一些基础图片剪辑操作','更快更强更干净的查词网','发送信息的聊天留言区域','一起刷数学题吧','Artificial Intelligence']}
    directions_frame = pd.DataFrame(directions)
    st.write(directions_frame)
    st.write('------------------------------------------------------------------------')
    st.header('关注作者')
    st.link_button('关注','https://space.bilibili.com/1659873233?spm_id_from=333.1007.0.0')
    st.image('page1_8.jpg')
    st.write('------------------------------------------------------------------------')

def page2():
    st.image('logo.png')
    st.markdown('# 图片编辑|Pic')
    st.write('------------------------------------------------------------------------')
    uploaded_file = st.file_uploader(':sunglasses:上传图片:sunglasses:',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(['原图','鬼畜改色','字符画','素描滤镜','抠图'])
        with tab1:
            st.image(img)
        with tab2:
            str_sequence = st.text_input('输入RGB数字（0，1，2）','0,2,1')
            sequence = str_sequence.split(',')
            rd.shuffle(sequence)
            try:
                st.image(img_change(img,int(sequence[0]),int(sequence[1]),int(sequence[2])))
            except:
                st.write(':red[输入不规范，请重新输入！]')
        with tab3:
            st.image(shadow_img(img))
        with tab4:
            st.image(filter_image(img))
        with tab5:
            st.image(no_background(img))

def page3():
    st.image('logo.png')
    st.markdown('# 词汇速查|Dictionary')
    word = st.text_input(':books:请输入要查询的单词:books:')
    tab1,tab2 = st.tabs(['无线查询','联网查询'])
    with tab1:
        with open('words_space.txt','r',encoding='utf-8') as f:
            word_list = f.read().split('\n')
        for i in range(len(word_list)):
            word_list[i] = word_list[i].split('#')
        word_dict = {}
        for i in word_list:
            word_dict[i[1]] = [int(i[0]),i[2]]
        with open('check_out_times.txt','r',encoding='utf-8') as f:
            time_list = f.read().split('\n')
        for i in range(len(time_list)):
            time_list[i] = time_list[i].split('#')
        time_dict = {}
        for i in time_list:
            time_dict[int(i[0])] = int(i[1])
        if word in word_dict:
            st.write(word_dict[word])
            n = word_dict[word][0]
            if n in time_dict:
                time_dict[n] += 1
            else:
                time_dict[n] = 1
            with open('check_out_times.txt','w',encoding='utf-8') as f:
                message = ''
                for k,v in time_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数',time_dict[n])
        elif word == 'KEZ':
            st.snow()
            st.write(':green[你是说这只仓鼠吗？]')
            st.image('kez.jpg')
        else:
            st.write(':red[拼写有误，请重新输入！]')
    with tab2:
        st.write(wordlistenquiry.search(word,choice=1))

def page4():
    st.image('logo.png')
    st.markdown('# 留言区|Chat')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    with open('user_id.txt','r',encoding='utf-8') as f:
        name_id = f.read().split('\n')
    with open('users_pic.txt','r',encoding='utf-8') as f:
        pics = f.read().split('\n')
        for i in range(len(pics)):
            pics[i] = pics[i].split('#')
        pic_dict = {}
        for i in pics:
            pic_dict[i[0]] = i[1]
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message(pic_dict[i[1]]):
            st.write(i[1],':',i[2])
    col1,col2 = st.columns([6,1])
    with col1:
        new_message = st.text_input('想说什么')
    with col2:
        st.write(' ')
        st.write(' ')
        if st.button('发送'):
            messages_list.append([str(int(messages_list[-1][0])+1),name_id[0],new_message])
            with open('leave_messages.txt','w',encoding='utf-8') as f:
                message = ''
                for i in messages_list:
                    message += i[0]+'#'+i[1]+'#'+i[2]+'\n'
                message = message[:-1]
                f.write(message)

def page5():
    st.image('logo.png')
    st.markdown('# 数学专区|Mathematics')
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    files = os.listdir('.')
    pdfs = []
    gksx = []
    for i in range(len(files)):
        if files[i].split('.')[-1] == 'pdf':
            pdfs.append(files[i])
        if files[i].split('.')[-1] == 'doc' or files[i].split('.')[-1] == 'docx' or files[i]=='2024新高考I卷数学试题及答案.pdf':
            gksx.append(files[i])
    
    xlb_cz = []
    for i in range(len(pdfs)):
        if '小蓝本初中卷' in pdfs[i]:
            xlb_cz.append(pdfs[i])
    
    xlb_gz = []
    for i in range(len(pdfs)):
        if '小蓝本高中卷' in pdfs[i]:
            xlb_gz.append(pdfs[i])

    tab1,tab2,tab3 = st.tabs(['小蓝本初中卷','小蓝本高中卷','高考数学'])
    with tab1:
        for i in range(len(xlb_cz)):
            col1,col2 = st.columns([5,1])
            with col1:
                st.write(xlb_cz[i])
            with col2:
                st.download_button(
                                label="下载文件",
                                data=open(xlb_cz[i], "rb"),
                                file_name=xlb_cz[i],
                                mime="application/octet-stream"
                            )

    with tab2:
        for i in range(len(xlb_gz)):
            col1,col2 = st.columns([5,1])
            with col1:
                st.write(xlb_gz[i])
            with col2:
                st.download_button(
                                label="下载文件",
                                data=open(xlb_gz[i], "rb"),
                                file_name=xlb_gz[i],
                                mime="application/octet-stream"
                            )

    with tab3:
        for i in range(len(gksx)):
            col1,col2 = st.columns([5,1])
            with col1:
                st.write(gksx[i])
            with col2:
                st.download_button(
                                label="下载文件",
                                data=open(gksx[i], "rb"),
                                file_name=gksx[i],
                                mime="application/octet-stream"
                            )

def page6():
    st.image('logo.png')
    st.title('AI聊天')
    with open('user_id.txt','r',encoding='utf-8') as f:
        name_id = f.read().split('\n')[0]
    with open('chat.txt','r',encoding='utf-8') as f:
        chats_pre = f.read().split('\n')
        chats = []
        for i in range(len(chats_pre)):
            chats_pre[i] = chats_pre[i].split('#')
            if chats_pre[i][0] == name_id:
                chats.append(chats_pre[i][1])
    if chats != []:
        for i in range((len(chats))):
            if i >= len(chats)-5:
                st.write(chats[i])
    a = st.text_input('想说些什么？')
    if st.button('发送'):
        url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
        te=requests.get(url).json()
        data=te['data']['info']['text']
        chats.append(f'我：{a}')
        chats.append(f'R君AI：{data}')
        with open('chat.txt','w',encoding='utf-8') as f:
            message = ''
            for i in range(len(chats)):
                message += name_id+'#'+chats[i]+'\n'
            message = message[:-1]
            f.write(message)
        

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_color = img.copy()
    img_array = img_color.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img_color

def shadow_img(img):
    width, height = img.size       
    plt.rcParams['image.cmap'] = 'gray'
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
    txt = ''
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray[0]/256*70)
            txt += ASCII_HIGH[index] + ' '
        txt += '\n'
    img_new = Image.new('RGB', (10000,10000), 'white')
    draw = ImageDraw.Draw(img_new)
    draw.text((0, 0), txt, fill='black')
    return img_new

def filter_image(img):
    img_new = img.filter(ImageFilter.CONTOUR).filter(ImageFilter.DETAIL)
    return img_new

def no_background(img):
    pic = img.convert('RGBA')
    width,height = pic.size
    pic_pixel = []
    for y in range(height):
        row = []
        for x in range(width):
            rgb_value = pic.getpixel((x,y))
            if sum(rgb_value)/4>220:
                pic.putpixel((x,y),(255,255,255,0))
            row.append(rgb_value)
        pic_pixel.append(row)
    return pic

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last},base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def main():
    is_login = True
    page = st.sidebar.radio('RVoyage主页',['网页故事|Story','图片编辑|Pic','词汇速查|Dictionary','留言区|Chat','数学专区|Mathematics','AI聊天'])
    bar_bg('bgpic.jpg')
    
    if page == '网页故事|Story':
        page1()
    elif page == '图片编辑|Pic':
        page2()
    elif page == '词汇速查|Dictionary':
        page3()
    elif page == '留言区|Chat':
        page4()
    elif page == '数学专区|Mathematics':
        page5()
    elif page == 'AI聊天':
        page6()

def welcome():
    st.title('登录')
    username = st.text_input("用户名")
    password = st.text_input("密码",type='password')
    is_login = False
    with open('users.txt','r',encoding='utf-8') as f:
        nameword_list = f.read().split('\n')
        for i in range(len(nameword_list)):
            nameword_list[i] = nameword_list[i].split('#')
        passwords = {}
        for i in range(len(nameword_list)):
            passwords[nameword_list[i][0]] = nameword_list[i][1]
    st.write(':red 若无账号将自动创建账号！')
    if st.button('登录'):
        try:
            if password == passwords[username]:
                is_login = True  # 设置会话状态变量
                with open('user_id.txt','w',encoding='utf-8') as f:
                    f.write(username)
        except:
            if username not in passwords.keys():
                with open('users.txt','a',encoding='utf-8') as f:
                    message = '\n'+username+'#'+password
                    f.write(message)
                with open('user_id.txt','w',encoding='utf-8') as f:
                    f.write(username)
                with open('users_pic.txt','a',encoding='utf-8') as f:
                    message = '\n'+username+'#'+'😊'
                    f.write(message)
                is_login = True
            else:
                st.error("登录失败")
    return is_login,username

page_bg('bgpic.jpg')
try:
    if st.session_state.count == 0:
        main()
except:
    is_login,user = welcome()
    if is_login:
        if 'count' not in st.session_state:
            st.session_state.count = 0
