print('00-1基本import')
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
# imageﾊpip install pillowｶﾞ必要 pil
import time
#from datetime import datetime
import datetime
import matplotlib.pyplot as plt

print('')
print('01-1 titleの表示')
st.title('25050601streamlit-new1')
st.caption('副題の表示 町内の為のホームページです｡')

#streamlit run e:\250519div_app\25050602streamlit-new1.py
#cd e:\250519div_app
#


#縦に分轄
col1,col2=st.columns(2)

with col1:
        st.subheader('みずき野紹介')
        
        st.text('みずき野は田んぼに囲まれたとても静かな街です｡')
        st.write('プログレスバーの表示')
        
        #streamlit run 25050602streamlit_new1.py
        #上記をｺﾏﾝﾄﾞﾌﾟﾛﾝﾌﾟﾄに打ち込みﾛｰｶﾙﾎｽﾄを起動させる
        
        #Local URL: http://localhost:8501
        #Network URL: http://192.168.1.4:8501
        #st.code(code,language='python')git
        
        #画像の登録
        #image=Image.open('iris_tree.png')
        image=Image.open(r'E:\250519div_app\data_250519\IMG241103_115831.jpg')
        
        #streamlitﾆimageｦ渡す
        st.image(image,width=400)
        
        image=Image.open(r'E:\250519div_app\data_250519\IMG241103_115841.jpg')
        st.image(image,width=400)
        
        image=Image.open(r'E:\250519div_app\data_250519\IMG241103_115956.jpg')
        st.image(image,width=400)
        
        #動画をupする
        #video_file=open('744_640x360.mov','rb')
        video_file=open(r'E:\250519div_app\data_250519\DSC231123_(3).mp4')
        
        #streamlitﾆvideoｦ渡す
        
        #video_bytes=video_file.read()
        #st.video(video_bytes)
        
        st.video(r'E:\250519div_app\data_250519\DSC231123_(3).mp4')
        st.video(r'E:\250519div_app\data_250519\VID250511.mp4')
        
        
        #text boxｦ画面上に作る
            
        with st.form(key='profile_form'):
            name=st.text_input('名前')
            address=st.text_input('住所')
        
            print(name)
        
        
            #botannの作成 送信 ｷｬﾝｾﾙ
            #submit_btn=st.button('送信')
            submit_btn=st.form_submit_button('送信')
            #cancel_btn=st.button('キャンセル')
            cancel_btn=st.form_submit_button('キャンセル')
            print(f'submit_btn:{submit_btn}')
            print(f'cancel_btn:{cancel_btn}')
            
            #select box
            #age_category=st.selectbox(
            age_category=st.radio(
                '年齢層',
                ('子供(18才未満)','大人(18才以上)'))
            
            hobby=st.multiselect(
                '趣味',
                ('スポーツ','読書','プログラミング','アニメ ・ 映画','釣り','料理'))
            
            mail_subscript=st.checkbox('メールマガジンを読む')
            
            height=st.slider('身長',min_value=110,max_value=210)
            
            start_date = st.date_input(
                 '開始日',
                 datetime.date(2025,5,1))
            
            color=st.color_picker('カラー','#00f900')
            
            
        #上記はプロンプト画面で確認される｡
        #submit_btn:True
        #cancel_btn:False ﾄ表示される
        
        if submit_btn:
            st.text(f'ようこそ!{name}さん!{address}より来ていただいてありがとう!')
            st.text(f'年齢層: {age_category}')
        hobby1=','.join(hobby)
        st.text(f'趣味: {hobby1}')
with col2:    
        image=Image.open(r'E:\250519div_app\data_250519\IMG250514_1356.jpg')
        st.image(image,width=400)
        
        
        #data分析
        df=pd.read_csv('tokyo2024.csv',index_col='年月日')
        st.dataframe(df)
        #st.table(df)
        st.line_chart(df)
        st.bar_chart(df)
        
        #matplotlib
        fig, ax=plt.subplots()
        ax.plot(df.index,df)
        ax.set_title('matplotlib graph')
        st.pyplot(fig)




