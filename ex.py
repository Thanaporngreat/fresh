import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from annotated_text import annotated_text
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🌸",
    font_size=30,
    falling_speed=10,
    animation_length="infinite",
)
st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://i.pinimg.com/originals/25/26/1f/25261f171c5e8cb8e1f6987dd70c57b9.gif");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
           [data-testid="stSidebar"]{{
           background-image: url(https://i.pinimg.com/564x/3c/82/41/3c8241eb905604ade63beb8dc8a73dcc.jpg);
           background-size: cover;
        }}
       </style>
       """,
    unsafe_allow_html=True
)
# LUV01 = Image.open('Picture/LUV01.jpg')
st.image('Picture/LUV01.jpg',width=700)
st.markdown('## best anime 🌸')
st.subheader('แนะนำอนิเมะสนุก สุดมันส์ที่ไม่ควรพลาด!!')
original_list = ['', 'อนิเมะแนวจินตนาการ', 'อนิเมะแนวความรัก', 'อนิเมะแนวตลก', 'อนิเมะแนวผจญภัย', 'อนิเมะแนวเล่าเรื่องชีวิตประจำวัน', 'อนิเมะแนววิทยาศาสตร์', 'อนิเมะแนวสืบสวน', 'อนิเมะแนวดราม่า', 'อนิเมะแนวต่อสู้']
ALL = st.selectbox('ค้นหา', original_list)
st.image('Picture/11..gif')

#stdebar--------------------------------------------------------------------------------------------------------------------------------------------------------------

st.sidebar.markdown('# ANIME HOUSE')
st.sidebar.image('Picture/LUV02.jpg', width=300)

tab1, tap2 = st.sidebar.tabs(['What is anime?', 'ข้อมูล'])
with tab1:
    annotated_text(
        ('อนิเมะคืออะไร', '?', '#FFC0CB'),
    )
    annotated_text(
    ('อนิเมะ (アニメ) หมายถึงอนิเมชั่นภาพเคลื่อนไหวในภาษาญี่ปุ่น ในญี่ปุ่นอนิเมะหมายถึงอนิเมชั่นทุกประเภทรวมถึงการ์ตูนอเมริกันและที่อื่น สำหรับประเทศอื่นๆอนิเมะมักหมายถึงอนิเมชั่นจากญี่ปุ่นโดยเฉพาะ'
    ' อนิเมะมีความโดดเด่นด้วยตัวละครที่วาดอย่างสวยงามและมีดวงตากลมโต ตัวละครจะถูกกำหนดชัดเจนและดูสมจริงและโครงเรื่องมักจะซับซ้อนมีการพัฒนาตัวละครและการดำเนินเรื่อง แต่ก็ยังมีอนิเมะบางเรื่องที่ไม่เข้ากับกฎตายตัวนี้',
    "", '#FFFAFA')
    )
    st.image('Picture/(3).jpg', width=300)

#ข้อมูล 1-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

with tap2:
    pow = st.selectbox('Choose type anime', ['โปรดเลือกแนวอนิเมะ', 'อนิเมะแนวจินตนาการ', 'อนิเมะแนวความรัก', 'อนิเมะแนวตลก','อนิเมะแนวผจญภัย', 'อนิเมะแนวเล่าเรื่องชีวิตประจำวัน', 'อนิเมะแนววิทยาศาสตร์', 'อนิเมะแนวสืบสวน','อนิเมะแนวดร่าม่า','อนิเมะแนวต่อสู้'])
    if pow == 'อนิเมะแนวจินตนาการ':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book1.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 2 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวความรัก':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book2.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book2.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book2.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวตลก':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book3.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book3.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book3.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 4 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวผจญภัย':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book4.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book4.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book4.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 5 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวเล่าเรื่องชีวิตประจำวัน':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book5.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book5.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book5.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 6 ---------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนววิทยาศาสตร์':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book6.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book6.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book6.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )
#ข้อมูล 7 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวสืบสวน':
        volume = st.columns(2)
        book = volume[0].number_input( 'ข้อมูล',min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book7.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book7.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book7.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม" ,'', '#FFC0CB'),
            )

#ข้อมูล 8 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวดร่าม่า':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book8.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book8.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book8.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

#ข้อมูล 9 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pow == 'อนิเมะแนวต่อสู้':
        volume = st.columns(2)
        book = volume[0].number_input('ข้อมูล', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลหนังสือ')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book9.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='BookSales', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินยอดขายเเต่ละปี')
        if train:
            st.write('กำลังฝึกประเมิน')
            df = pd.read_excel('Picture/Book9.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้ขาย')
        if predict:
            df = pd.read_excel('Picture/Book9.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['BookSales'])
            target = model.predict([[book]])[0]
            annotated_text(
                (f"ยอดขายในปี {book} จำนวนยอดขายหนังสิอประมาณ{target:.2f}เล่ม", '', '#FFC0CB'),
            )

# type 1***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวจินตนาการ':
    st.title('แนะนำอนิเมะแนวจินตนาการ')
    st.write('ถ้าพูดเรื่องราวแนวแฟนตาซี ส่วนใหญ่จะต้องมีเนื้อหาเกี่ยวกับเวทมนตร์ และแน่นอนว่าก็มีอนิเมะเวทมนตร์มากมายจำนวนไม่น้อยเลย'
                 ' ซึ่งแต่ละเรื่องนั้นก็ใช้เวทแตกต่างกันออกไป ไม่ว่าจะเป็นทั้งการต่อสู้ เรื่องราวเล็กน้อย '
                 'รวมไปถึงภัยพิบัติ และนี่ก็เป็น 5 อนิเมะแนวเวทมนตร์ที่คอนิเมะไม่ควรพลาดด้วยประการทั้งปวงค่ะ')
    st.markdown('### _1._ :blue[Mahouka Koukou no Rettousei]')
    st.markdown('![image](https://i.pinimg.com/originals/a3/9c/3e/a39c3e4616cca25be4fb313708006ac2.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://aisplay.ais.co.th/portal/get_section/5f78979c9e6cf8fada70873b/?fbclid=IwAR29uSDrSZBEAKc_bPaj9ERU2rpHSmqvyjwbx8KCRxSSIB1kIelPOKGypBk')
    st.markdown(' เรื่องราวของสองพี่น้องตระกูลชิบะ ที่ได้เข้าเรียนในโรงเรียนจอมเวทย์ โดยที่น้องสาวนั้นถูกจัดอยู่ในชั้นเรียนที่มีฝีมือยอดเยี่ยม '
                'และว่าฝ่ายพี่ชายนั้นกลับถูกไล่ไปอยู่ในกลุ่มของพวกไร้พรสวรรค์ทางเวทมนตร์ แต่ว่าที่จริงแล้วฝ่ายพี่ชายนั้นครอบครองพลังเวทมนตร์สุดยอด '
                'และความลับอีกมากมายอยู่ เพลง OP และ ED เพราะมากนะเรื่องนี้ขอบอก')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _2._ :blue[Tales of Vesperia: The First Strike]')
    st.markdown('![image](https://i.pinimg.com/originals/6a/b5/d5/6ab5d5eac19789a8fc75a0cce9be5196.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2004824773')
    st.markdown('เรื่องราวจากสุดยอดเกม RPG ของทาง Bandai Namco ที่กล่าวถึงตัวเอกยูริ โลวเวล ซึ่งเป็นอัศวินของจักรวรรดิ ท'
                'ี่ต้องเข้าไปผัวพันกับเหตุการณ์ลึกลับในระหว่างเดินทาง '
                'ซึ่งเป็นเนื้อหาเดียวกับเกมนั่นแหละใครเป็นคอซีรี่ส์ Tales of น่าจะต้องไม่พลาดแน่นอน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _3._ :blue[Cardcaptor Sakura]')
    st.markdown('![image](https://i.pinimg.com/originals/02/c2/06/02c20606d9b57407d7a50120b6546353.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/title/70309056')
    st.markdown('หนึ่งในอนิเมะขึ้นหิ้งที่กำลังจะมีภาคใหม่ให้ได้ชมในปีหน้า เกี่ยวสาวน้อยชั้นประถมที่สืบทอดพลังเวทมนตร์จากสุดยอดจอมเวทย์ในอดีต '
                'ซึ่งเธอนั้นได้สัมผัสกับการ์ดเวทมนตร์ครั้งแรกทำให้ การ์ดที่เต็มไปด้วยเวทมนตร์นั้นกระจายหายไป '
                'และเธอต้องเป็นคนรับผิดชอบ และรวบรวมการ์ดกลับคืนมาทั้งหมดภายใต้การช่วยเหลือของเคลเบรอส ที่เป็นอดีตผู้พิทักษ์ของจอมเวทย์คนนั้น')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _4._ :blue[Kage no Jitsuryokusha ni Naritakute]')
    st.markdown('![image](https://media.tenor.com/SSC42cUze-sAAAAd/kage-no-jitsuryokusha-ni-naritakute-the-eminence-in-shadow.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/jp-en/title/81642096')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2042328214')
    st.markdown('ชีวิตไม่ต้องเด่น ขอแค่เป็นเทพในเงา เรื่องนี้สายอ่านนิยายหรือมังงะทราบกันดี กับชื่อนี้ “กาวทมิฬ” '
                'โดยเรื่องนี้เนื่อเรื่องจะเป็นลักษณะของเด็กหนุ่มที่ได้ไปเกิดใหม่ในโลกแฟนตาซี เด็กหนุ่มคนนึ้ก็ได้พยายามทำตัวเป็นพลังในเงามืดที่คอยจำกัดลักทธิชั่วร้าย '
                'ซึ่งพี่เทพของเราก็ได้ตั้งองค์กรขึ้นมาชื่อว่า shadow garden และในองค์กรก็มีแต่เหล่าสาว ๆ ซะด้วย')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _5._ :blue[Kenja No Mago]')
    st.markdown('![image](https://i.pinimg.com/originals/89/be/e3/89bee35b65b6a17787c06a8538d05704.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.bilibili.tv/en/video/2007929923')
    st.markdown('หลานจอมปราชญ์ (Kenja No Mago) เรื่องราวของเด็กหนุ่มคนนึงที่ได้ประสบอุบัติเหตุแล้วได้ไปเกิดใหม่ในโลกแฟนตาซี และถูกมหาจอมเวทย์ชื่อดังสอนและเลี้ยงดู '
                'ไม่เพียงแค่นั้น ในรอบๆ ตัวเค้า มีแต่พวกมหาจอมเวทย์ที่คอยสอนเค้า '
                'จนวันนึงที่บ้านก็อยากให้ทางพระเอกเข้าเรียนโรงเรียนเวทมนตร์เพื่อจะได้เข้ากับคนอื่นๆ ได้ และการที่พระเอกของเราได้ไปโรงเรียนในวันนั้น '
                'ก็กลายเป็นจุดเริ่มต้นของความบันเทิง ที่ทางทีมงานอยากให้คออนิเมะแนวนี้ ต้องไปดู')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.image("Picture/k2.png", width=500)

# type 2***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวความรัก':
    st.title('แนะนำอนิเมะแนวความรัก')
    st.write('ซึ่งนอกจากอนิเมะแนว แฟนตาซี ที่รับความนิยมมาตลอดแล้วก็ยังมี ‘อนิเมะแนวโรแมนติก’ อีกแนวที่ก็ได้รับความนิยมแบบสูสีไม่แพ้กันเลยทีเดียว '
             'ในวันนี้เราจึงได้นำเอาอนิเมะแนวโรแมนติกหลากหลายสไตล์มาแนะนำกัน ทั้งแนวโรแมนติกคอมเมดี้ หรือแนวโรแมนติกดราม่าน้ำตาคลอ ซึ่งก็มีทั้งอนิเมะเก่า ๆ '
             'ที่น่าจดจำและอนิเมะใหม่ที่น่าติดตาม รวมถึงอนิเมะที่ดูได้ผ่าน NETFLIX ให้คุณได้เลือกชมกันตามชอบอีกด้วย จะมีอนิเมะเรื่องไหนบ้างที่ชวนให้อบอุ่นหัวใจ '
             'เราไปรู้สึกนุ่มฟู หัวใจพองโตมาอ่านไปพร้อม ๆ กันในบทความข้างล่างนี้เลยค่ะ')
    st.markdown('### _1._ :blue[Sono Bisque Doll wa Koi wo Suru ]')
    st.markdown('![image](https://i.pinimg.com/originals/0a/cf/b9/0acfb9b2ddaad188af69f6c27728f4fe.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.bilibili.tv/th/play/1035102')
    st.markdown('เปิดตัวเรื่องแรกด้วยอนิเมะใหม่ประจำปี 2022 ที่ได้รับความนิยมและเป็นกระแสอย่างต่อเนื่อง อย่าง Sono Bisque Doll wa Koi wo Suru หนุ่มเย็บผ้ากับสาวนักคอสเพลย์ '
                'ที่ชื่อเรื่องมาจากไลฟ์สไตล์ของตัวละครหลักอย่าง '
                '‘มาริน’ นางเอกคนสวย นิสัยร่าเริงสุดสดใสที่ตกคนดูได้แบบไม่มีแผ่ว เธอจัดว่าเป็น สาว Gal* ที่ชื่นชอบการแต่งคอสเพลย์เป็นชีวิตจิตใจ และ ‘โกโจ วาคานะ’'
                ' เพื่อนร่วมห้องหนุ่มใจดี ผู้ชื่นชอบการตัดเย็บชุดตุ๊กตา ด้วยความชอบส่วนตัวที่ขัดรูปลักษณ์ภายนอกทำให้เขาต้องการปิดเรื่องนี้เป็นความลับจากทุกคน')
    st.markdown('แต่ มาริน กลับได้ล่วงรู้ความลับนี้เข้าและได้ขอร้องให้เขาช่วยทำชุดคอสเพลย์ให้เธอ ทำให้ทั้งสองได้มีโอกาสพูดคุยกันมากขึ้น และมีโมเม้นท์ชวนเขินอีกมากมาย '
                'นอกจากนี้อนิเมะเรื่องนี้ยังนำเสนอความรักและความหนักแน่นในงานอดิเรกที่พวกเขาชื่นชอบอย่างน่าประทับใจจริง'
                ' ๆ ค่ะ พูดได้เลยว่า Sono Bisque Doll wa Koi wo Suru ถือเป็นอีกหนึ่งอนิเมะโรแมนติกงานภาพสวยที่คุณไม่ควรพลาดเลยค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _2._ :blue[Horimiya]')
    st.markdown('![image](https://i.pinimg.com/originals/c4/fc/d6/c4fcd6c786b7944cc01f594ce5fb85a4.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://pops.tv/th/series/horimiya-5fecaa1be1be4f256974813c')
    st.markdown('Horimiya โฮริมิยะ สาวมั่นกับนายมืดมน อนิเมะโรแมนติกยอดฮิตแบบ Feel Good ที่ตกคนดูให้ติดกันงอมแงมได้สุด ๆ โดยเรื่องราวเริ่มต้นจาก ‘โฮริ’ สาวสวยสุดป็อป'
                ' ที่เป็นที่นิยมของเพื่อน ๆ แถมยังเป็นคนที่เพอร์เฟ็คในทุกด้าน แต่เมื่อกลับไปที่บ้านก็ต้องแปลงร่างรับบทเป็นคุณแม่บ้านสุดเซอร์ที่ต้องทำงานบ้านทุกอย่างและยังต้องดูแลความเป็นอยู่ของน้องชายอีกด้วย')
    st.markdown('ส่วนฝั่งพระเอกของเรา ‘มิยามูระ’ เด็กหนุ่มมืดมนประจำห้องเรียน ที่เพื่อน ๆ ต่างลงความเห็นกันว่าเป็นหนุ่มแสนเฉิ่มไร้สีสัน แต่เมื่ออยู่นอกโรงเรียน เขากลับกลายเป็นหนุ่มฮอตหล่อสายพังค์ที่กร้าวใจสาว ๆ '
                'ทั้งรอยสักสุดเร้าใจและต่างหูสุดเท่ทำให้สาว ๆ หัวใจหวั่นไหวกันเป็นแถว '
                'เรียกได้ว่าดูแตกต่างเหมือนกันเป็นคนละคนกับในโรงเรียนเลยก็ว่าได้ จนในวันหนึ่งเกิดเหตุบังเอิญที่ทำให้ มิยามูระ และ โฮริ เจอในสภาพโลกอีกใบของแต่ละคน'
                ' ทำให้ทั้งสองได้รับรู้ตัวตนที่แท้จริงของอีกฝ่าย ซึ่งทั้งสองก็ได้ทำความตกลงที่จะเก็บเป็นความลับระหว่างกัน จากนั้นเรื่องราวความสัมพันธ์ชวนเขินแบบลับ ๆ ของทั้งคู่ก็ได้เริ่มต้นขึ้น '
                'รับรองว่าหวานน่ารักสุด ๆ แต่เพื่อน ๆ ต้องไปติดตามกันต่อว่าคนในโรงเรียนจะรู้ความลับนี้หรือไม่ ? ใน โฮริมิยะ สาวมั่นกับนายมืดมน เลยค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _3._ :blue[Kanojo Okarishimasu]')
    st.markdown('![image](https://i.pinimg.com/originals/80/bc/50/80bc505b93bae2d6ee8a2c2ef65e0722.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.bilibili.tv/th/play/35498')
    st.markdown('Kanojo Okarishimasu สะดุดรักยัยแฟนเช่า เป็นเรื่องราวความรักสุดยุ่งเหยิงของ ‘คาสึยะ’ หนุ่มจืดชืดที่เพิ่งอกหักหมาด ๆ จากสาวที่คบมา 1 เดือน ทำให้เขาหันมาสนใจใช้บริการแฟนเช่าจากในเว็บไซต์ ซึ่งเขาก็ได้ตัดสินใจจะเช่า ‘จิซึรุ’ สาวสวยตัวท็อปประจำเว็บมาช่วยเยียวยาหัวใจ'
                ' แต่เขาก็ต้องตกตะลึงเพราะเธอดูแลสภาพจิตใจเขาได้ดีมากจนไร้ที่ติ แน่นอนว่าคนช้ำรักใหม่ ๆ อย่าง คาสึยะ ก็คิดว่าสุดท้ายแล้วนี่คงเป็นเพียงแค่การแสดง จึงได้ตัดสินใจเช่า จิซึรุ มาเจอกันอีกครั้ง')
    st.markdown('แต่การใช้บริการแฟนเช่าในครั้งนี้ ทำให้ คาซึยะ ยิ่งพบว่า จิซึรุ นั้นสมบูรณ์แบบจนทำให้หัวใจเค้าพองโตแบบไม่รู้ตัว และยังมีเหตุบังเอิญที่บีบบังคับให้ทั้งสองต้องแกล้งทำเป็นแฟนกำมะลอกันไปเรื่อย ๆ อีกด้วย'
                ' โดยการใช้บริการแฟนเช่าในครั้งนี้จะไปสิ้นสุดที่ตรงไหน ? บทสรุปความสัมพันธ์ของทั้งคู่จะเป็นอย่างไร ? อย่าลืมติดตามชม Kanojo Okarishimasu สะดุดรักยัยแฟนเช่า กันให้ได้นะคะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _4_:blue[Hotarubi no mori e]')
    st.markdown('![image](https://i.pinimg.com/originals/49/1f/e5/491fe58b58518344e612b9a98263154a.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://reviewsnung.com/archives/5797')
    st.markdown('Hotarubi no mori e โฮตารูบิโนะโมริเอะ สู่ป่าแห่งแสงหิ่งห้อย เป็นอนิเมะ Movie ที่เราอยากแนะนำให้ทุกคนได้ดูมาก ๆ รับรองว่าดูแล้วคุณจะรู้สึกอบอุ่นหัวใจอย่างบอกไม่ถูกเลยค่ะ '
                'โดยเรื่องราวนั้นเริ่มต้นในสมัยที่ ‘ฮาโตรุ’ ยังเป็นเด็กสาว ซึ่งในทุกปิดเทอมฤดูร้อน ฮาโตรุ และครอบครัวมักจะไปเที่ยวบ้านคุณลุงที่อยู่ในชนบทเสมอ โดยในปีที่ 6'
                ' นั้นเธอได้ไปเที่ยวที่บ้านคุณลุงอีกครั้ง เธอได้เผลอหลงเข้าไปในภูเขาที่ชาวบ้านเล่าลือกันว่ามีภูตผีอาศัยอยู่ ทำให้เธอหาทางออกไม่ได้ และในตอนที่เธอกำลังตกใจร้องไห้อยู่นั้นเธอก็ได้พบกับ '
                '‘กิง’ ชายหนุ่มสวมหน้ากากจิ้งจอกที่เข้ามาปลอบและช่วยพาเธอออกจากป่า และ กิง ก็ได้บอกกับเธอว่าเขาไม่สามารถโดนตัวมนุษย์ได้เพราะตัวเขาจะสลายหายไปทันที ในตอนนั้นเอง ฮาโตรุ ก็รู้ได้ว่า กิง '
                'ไม่ใช่มนุษย์ แต่เธอก็ไม่ได้รู้สึกกลัวขนาดนั้น และเธอก็ยังมาพบเขาในทุก ๆ ปิดเทอมฤดูร้อนเหมือเดิมทุกปี')
    st.markdown('เมื่อเวลาผ่านไปหลายปีจน ฮาโตรุ โตเป็นสาว ความสัมพันธ์ของทั้งคู่ก็ดูเหมือนจะค่อย ๆ แน่นแฟ้นขึ้นเรื่อย ๆ แต่ด้วยเงื่อนไขหลาย ๆ อย่างที่ทำให้ทั้งคู่ไม่อาจอยู่ร่วมกันได้ เพราะเป็นความรักระหว่างมนุษย์กับภูตผี '
                'บทสรุปของเรื่องราวโรแมนติกเหนือธรรมชาติครั้งนี้จะเป็นอย่างไรต่อไป? ต้องติดตามชมกันให้ได้ใน Hotarubi no mori e โฮตารูบิโนะโมริเอะ สู่ป่าแห่งแสงหิ่งห้อย นะคะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Orange]')
    st.markdown('![image](https://i.pinimg.com/originals/52/cf/3c/52cf3cfb69e691c0feb3c3c3f61bb713.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.bilibili.tv/th/play/35053')
    st.markdown('Orange เป็นอนิเมะแนวโรแมนติกเรื่องนี้ขอเอาใจคนที่ชอบเนื้อหาแบบซาบซึ้งเคล้าน้ำตา _ด้วยเรื่องราวของ_:blue[‘นาโฮ’] เด็กสาวชั้นมัธยมปลายวัย 16 ปี ที่จู่ ๆ เธอก็ได้รับจดหมายที่ส่งมาจากตัวเองในอนาคตตอนอายุ 27 ปี'
                ' ซึ่งในจดหมายก็ได้บอกเล่าถึงเรื่องราวยุ่งเหยิงต่าง ๆ ที่จะเกิดขึ้นในอนาคต และหวังให้เธอช่วยแก้ไขเรื่องราวในอดีต')
    st.markdown('เมื่อ นาโฮ ได้อ่านเรื่องราวต่าง ๆ ก็ต้องการที่จะเปลี่ยนแปลงอนาคตเช่นกัน เพื่อไม่ให้ตัวเธอเองต้องมาเสียใจภายหลัง ทั้งเรื่องราวของเธอกับเพื่อน ๆ และเรื่องของเธอกับ ‘คาเครุ’ นักเรียนหนุ่มที่เพิ่งย้ายเข้ามาใหม่ในวันนั้น ซ'
                'ึ่งในจดหมายได้ขอให้ นาโฮ จับตาดูเขาเอาไว้ และจดบันทึกช่วงเวลาที่ทั้ง 2 ได้รู้จักสนิทสนม ไปจนถึงวันที่ต้องสูญเสีย คาเครุ ไป ทำให้เธอเข้าใจแล้วว่าจดหมายฉบับนี้ไม่ได้ช่วยเปลี่ยนแปลงอนาคตของเธอเท่านั้น แต่ยังหมายถึงอนาคตของเขาด้วยเช่นกัน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.image("Picture/k3.png", width=500)

# type 3 ***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวตลก':
    st.title('แนะนำอนิเมะแนวตลก')
    st.write('ถ้าหากจะพูดถึงอนิเมะที่จะช่วยคลายเครียดให้คุณได้ดีที่สุด คงจะหนีไม่พ้น ‘อนิเมะตลก’ ที่จะช่วยให้คุณผ่อนคลายความเครียดได้อย่างเต็มที่ '
             'ด้วยเนื้อเรื่องที่ปั่นป่วนชวนตลกขบขัน และการยิงมุกฮากระจายของเหล่าตัวละคร แน่นอนว่าคุณจะต้องหัวเราะท้องแข็งจนลืมความเครียดเป็นปลิดทิ้งแน่นอนในวันนี้เองเราก็ได้ทำการคัดเลือกอนิเมะตลกท'
             'ี่น่าสนใจทั้งอนิเมะเรื่องเก่าและอนิเมะเรื่องใหม่ มาฝากทุกคนหลากหลายเรื่องเลยทีเดียว ส่วนจะมีเรื่องไหนกันบ้างนั้น อย่ารอช้ารีบตามเรามาที่บทความด้านล่างนี้กันเลยค่ะ')
    st.markdown('### _1._:blue[Hoozuki no Reitetsu]')
    st.markdown('![image](https://i.pinimg.com/originals/aa/9d/88/aa9d88c2d44489de50ce7199ce8e6f91.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.bilibili.tv/th/video/2042994102?bstar_from=bstar-web.homepage.recommend.all')
    st.markdown('อนิเมะตลกเนื้อเรื่องสุดแหวกแนวที่สามารถดูได้แบบเพลิน ๆ ด้วยเรื่องราวของ ‘โฮซุกิ’ วีรบุรุษหน้าตายสุดเย็นชาที่มีฝีมือด้านการจัดการแก้ปัญหาในนรกเป็นเลิศ จึงได้มารับหน้าที่มือขวาของ '
                '‘ท่านเอ็นมะ’ ราชาแห่งนรกภูมิญี่ปุ่น ซึ่งโฮซุกิเองก็สามารถปฏิบัตหน้าที่ได้เป็นอย่างดี ด้วยความเด็ดขาดในการตัดสินใจแบบที่ไม่อาจมีใครหยั่งถึง ทำให้เขากลายเป็นปีศาจชั้นสูงที่ดูน่ายำเกรงต่อปีศาจตนอื่น ๆ '
                'ไม่เว้นแม้กระทั่งท่านราชาเอ็นมะเอง แต่ก็ดูเหมือนความน่ากลัวนี้จะไม่เป็นผลกับ ‘ฮาคุทาคุ’ ปีศาจจากแดนสุขาวดีที่ถือเป็นไม้เบื่อไม้เมากับโฮซุกิตลอดมา แบบที่ว่าเจอหน้าเป็นต้องอัดกันทุกครั้ง ด้วยเรื่องราวแฟนตาซีทำ'
                'ให้อนิเมะเรื่องนี้เป็นอนิเมะตลกที่น่าสนใจมาก ๆ เพราะนอกจากจะเรียกเสียงหัวเราะได้แล้ว เราก็ยังได้เกร็ดความรู้เล็ก ๆ น้อย ๆ เกี่ยวกับนรกภูมิของทางฝั่งญี่ปุ่นอีกด้วยค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[Back Street Girls]')
    st.markdown('![image](https://pa1.narvii.com/7057/22335b72019f16d334c3ffa04fd1386f28fe3616r1-443-253_hq.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.netflix.com/th/title/80996957')
    st.markdown('เริ่มต้นเรื่องแรกด้วยอนิเมะที่สร้างจากมังงะตลกยอดฮิต ที่ได้รับความนิยมถึงขั้นมีภาพยนตร์ฉบับคนแสดงเป็นของตนเองมาแล้ว '
                'กับเรื่องราวสุดวายป่วงของยากุซ่ามือสมัครเล่น 3 หน่อ ที่ดันทำความผิดร้ายแรงให้เจ้าพ่อของแก๊งไม่พอใจเข้า จึงโดนสั่งให้ไปที่ประเทศไทยผ่าตัดแปลงเพศซะ'
                ' เพื่อมาชดใช้ความเสียหายทั้งหมด ด้วยการใช้ชีวิตที่เหลือนี้ในฐานะวงไอดอลเกิร์ลกรุ๊ปที่ชื่อว่า ‘Gokudolls’ และที่ตลกไปกว่านั้นวงไอดอลที่ว่านี่ก็ดันดังเอามาก ๆ'
                ' ซะด้วย แล้วเรื่องราวจะเป็นอย่างไรต่อไป ? กับความลับของสาวน้อยนิยมที่แท้จริงแล้วเป็นแค่ยากูซ่าปลายแถว บอกเลยค่ะว่าห้ามพลาด')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _3._:blue[Kono Subarashii Sekai ni Shukufuku wo!]')
    st.markdown('![image](https://i.pinimg.com/originals/9e/58/9b/9e589bd08e8fd3359ddc7c6182051770.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷  https://www.netflix.com/th/title/80996957')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/80131674')
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PLxSscENEp7JiyHGbqVQuTTs9ZFqu3wYNM')
    st.markdown('อนิเมะตลุกสุดต๊องที่สร้างมาจากไลท์โนเวลชื่อดังที่ได้รับความนิยมอย่างล้นหลามจากผู้ที่ชอบเสพความฮา กับเรื่องราวของ ‘ซาโต้ คาซุมะ’'
                ' เด็กหนุ่มที่ได้เสียชีวิตอย่างน่าอนาถ แต่ด้วยกรรมดีที่เขาได้ก่อไว้ทำให้มีเทพธิดาแสนสวยมายื่นข้อเสนอให้เขาได้ไปเกิดใหม่ในต่างโลก พร้อมกับขออาวุธสุดเทพจากเธอได้ 1 อย่าง '
                'แต่คาซุมะก็ดันกวนโอ๊ย เลือกเทพธิดาไปเกิดให้กับเขาซะงั้น ก่อนที่จะได้รู้ความจริงว่าเทพธิดาที่ว่าเป็นแค่นางฟ้าเก๊ที่มีดีแค่ขายขำไปวัน ๆ ทำเอาคาซุมะเองถึงกับต้องกุมขมับ '
                'แล้วแบบนี้ชีวิตใหม่ในต่างโลกของคาซุมะจะต้องพบเจอกับเรื่องราวป่วน ๆ และคนปั่น ๆ มากแค่ไหน? บอกเลยว่าต้องติดตามมด้วยตัวเองค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[Asobi Asobase]')
    st.markdown('![image](https://i.pinimg.com/originals/ab/3f/04/ab3f04c7d2f2450470204689a04b3008.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PLIa05JMgYhha42EyA3gOFZtFw93l2Mf7U')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81264508')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/36155')
    st.markdown('อนิเมะตลกเรื่องนี้ช่วยสอนคำว่าอย่าตัดสินหนังสือที่หน้าปกได้เป็นอย่างดี เพราะอนิเมะเรื่องนี้มีเนื้อหาสุดเสื่อม แถมฮาแตกผิดกับภาพลักษณ์ของสาว ๆ '
                'สุดน่ารักพาสเทลบนหน้าปกลิบลับ ด้วยเรื่องราวของ ฮานาโกะ, โอลิเวีย และคาสึมิ สามสาวสุดเกรียนที่ได้ก่อตั้ง ‘ชมรมการละเล่น’ ขึ้น โดยสมาชิกก็มีแค่พวกเธอ 3 '
                'คนนั้นแหละที่มาผลัดกันหาอะไรเล่นแก้เบื่อ ซึ่งถึงแม้ว่าเนื้อหาของเรื่องจะวนเวียนอยู่แค่การละเล่นที่พวกเธอสรรหามาเล่น แต่ก็อย่าได้ดูถูกเชียวค่ะ เพราะในเนื้อเรื่องสุดธรรมดานี้ 3 '
                'สาวของเราทั้งชงตั้งตบมุขกันแบบวินาทีต่อวินาที เรียกได้ว่าหัวเราะกันจนเหนื่อย ใครที่ชอบอนิเมะสายฮาแบบ 300% เซอร์วิสด้วยสาว ๆ น่ารักบอกเลยค่ะว่าห้ามพลาด!!')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Nichijou]')
    st.markdown('![image](https://i.pinimg.com/originals/da/90/70/da90709f14dbee9dce13d8d0fab4a72a.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/search-result?q=Nichijou')
    st.markdown('หากคุณรู้สึกว่าอนิเมะตลกแนวชีวิตประจำวันแบบปกติมันดูน่าเบื่อไปซักหน่อย อยากให้คุณลองมาดูอนิเมะตลกเรื่องนี้กันค่ะ '
                'โดยอนิเมะเรื่องนี้จะว่าด้วยเรื่องราวของนักเรียนหญิงชั้นมัธยมศึกษากลุ่มหนึ่งที่ประกอบด้วย มินาคามิ มาอิ, อาอิโออิ ยุกโกะ และนางาโนฮาระ มิโอะ '
                'ที่ได้ใช้ชีวิตในวัยเรียนแบบไม่ค่อยปกติเท่าไหร่ เพราะมักจะมีเหตุการณ์พิลึก ๆ ชวนปวดหัวเกินขึ้นรอบ ๆ ตัวพวกเธออยู่เสมอ ไม่ว่าจะเป็นแมวพูดได้ เด็กชายที่ขี่แพะมาโรงเรียนพร้อมกับคุณพ่อบ้าน'
                ' หุ่นยนต์หญิงที่สร้างโดยนักวิทยาศาสตร์วัย 8 ปี เด็กหญิงที่ชอบทำปืนลั่น และครูใหญ่ที่ชอบเล่นมวยปล้ำกับกวาง เรียกได้ว่าเป็นอนิเมะที่ไม่มีทั้งพล็อตเรื่อง เหตุผล รวมถึงเนื้อหาสาระ แต่ทำให้คุณขำจนน้ำตาเล็ดได้แน่ ๆ ค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')

# type 4 ***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวผจญภัย':
    st.title('อนิเมะแนวผจญภัย')
    st.markdown('เป็นกระแสนิยมของการ์ตูนสมัยนี้จริงๆ กับเนื้อเรื่องแนว "Isekai" หรือการไปผจญภัยในต่างโลก ที่นำเสนอเรื่องราวความน่าสนใจว่าถ้ามนุษย์อย่างเราต้องถูกส่งไปยังโลกที่ไม่รู้จักจะเอาชีวิตรอดได้อย่างไร'
                ' โดยความแตกต่างกันสุดขั้วก็ทำให้ถูกใจเหล่าแฟนๆ การ์ตูน วันนี้ LUV Anime จึงขอนำเสนอ อนิเมะแนวผจญภัยในต่างโลก')
    st.markdown('### _1._:blue[She Professed Herself Pupil of the Wise Man]')
    st.markdown('![image](https://cms.dmpcdn.com/moviearticle/2022/07/01/61688070-f8f4-11ec-aa23-e117f6e36887_original.jpg)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/1044413/11128773')
        st.markdown('▶ 🌷 https://entertainment.trueid.net/detail/BVLKydw75Zl2')
    st.markdown('ซากิโมริ คางามิ เกมเมอร์หนุ่ม ที่จู่ ๆ ก็ตื่นมาในโลกของเกมและอยู่ในร่างของสาวน้อยหน้าตาน่ารัก '
                'เขาจึงตัดสินใจที่จะอ้างตัวเป็นลูกศิษย์ของจอมปราชญ์และออกผจญภัยในโลกแฟนตาซี')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[I have Been Killing Slimes for 300 Years and Maxed Out My Level]')
    st.markdown('![image](https://media.tenor.com/VbTFb2azUjcAAAAd/slime-taoshite300nen-ive-been-killing-slimes-for300years-and-maxed-out-my-level.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.viu.com/ott/th/th/vod/351325/Ive-Been-Killing-Slimes-for-300-Years-and-Maxed-Out-My-Level')
        st.markdown('▶ 🌷 https://movie.trueid.net/th-th/series/2NxL8GELww0N/Q6G0eLgNowrm/a1dV64pkvNPe/gRelaBXdawzk')
        st.markdown('▶ 🌷 https://www.iq.com/album/1dtp72c2h4x')
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PLIa05JMgYhhYhecy8U6XlUO_AqHKFJQEN')
    st.markdown('สาวออฟฟิศที่เสียชีวิตและได้เกิดใหม่เป็นสาวน้อยเวทมนตร์อมตะในต่างโลก'
                ' เธอต้องจัดการสไลม์เพื่อสะสมเงินเรื่อย ๆ และได้กลายเป็นสุดยอดนักเวทย์แห่งโลกใบนี้')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('###_3._:blue[Re: Zero - Starting Life in Another World]')
    st.markdown('![image](https://i.pinimg.com/originals/b3/d2/7c/b3d27c0797833905fffc809314620b27.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://aisplay.ais.co.th/portal/get_section/5f3f54df6548279d674a29a2/')
        st.markdown('▶ 🌷 https://www.viu.com/ott/th/th/vod/357122/ReZero-%E2%88%92-Starting-Life-in-Another-World-Directors-Cut-Compilation-Special-series')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/36717')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81262169')
    st.markdown('จากนวนิยาย Light Novel ของ อ.ทัปเปย์ นากะทสึกิ สู่หนังสือการ์ตูนและอนิเมะทางทีวี'
                ' กับเรื่องราวของ "นัทสึกิ สุบารุ" เด็กหนุ่มผู้รักสันโดษผู้ที่ไม่ทำอะไรเลยนอกจากเล่นเกมไปวันๆ จนในคืนหนึ่งขณะที่เข้ากำลังเดินกลับจากร้านสะดวกซื้อ จู'
                '่ๆก็ถูกส่งตัวมายังอีกโลกหนึ่ง ขณะที่เขากำลังหาว่าเขาถูกส่งตัวมาที่นี่ได้อย่างไร ก็ถูกกลุ่มโจรขโมยของๆเขา แต่ก็ได้หญิงสาวผมเงินช่วยเอาไว้ '
                'เพื่อตอบแทนบุญคุณสุบารุจึงจะช่วยเธอตามหาของที่เธอถูกขโมยไป แต่ก่อนจะได้ของคืนสุบารุและหญิงสาวคนนั้นกลับถูกฆ่าตาย!!'
                ' แต่แทนที่สุบารุจะตายเขาได้ย้อนเวลากลับมายังช่วงก่อนที่เหตุการณ์จะเกิดขึ้น สุบารุจึงติดสินใจที่จะใช้พลังนี้เพื่อช่วยเหลือหญิงสาวผู้มีพระคุณออกจากความตาย...')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[By the Grace of the Gods ]')
    st.markdown('![image](https://i.pinimg.com/originals/a9/f9/a3/a9f9a36f186fd98a03b4b080ae48f9c0.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/1004516')
        st.markdown('▶ 🌷 https://www.trueid.net/watch/th-th/series/JLz6rXO1KwGL/V7A8AElg6rJ4https://www.trueid.net/watch/th-th/series/JLz6rXO1KwGL/V7A8AElg6rJ4')
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PLxSscENEp7JjRhcXt3hp52zWsIcJL6ecv')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81341928')
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PL_YV8EWtbQXFuNUde9A-hXhz6ItKoc8mq')
    st.markdown('เรื่องราวของนักธุรกิจในญี่ปุ่นวัยกลางคนที่เสียชีวิตอย่างน่าเสียดายโดยที่เขาไม่เคยได้พบเรื่องดี ๆ ในชีวิตเลย ซึ่งเขาก็ได้รับพรชีวิตใหม่โดยการไปเกิดใหม่ในโลกที่มีดาบและเวทมนตร์'
                ' จากการได้รับพรของเหล่าพระเจ้าทำให้เขาตัดสินใจอยู่ในป่าอย่างสบาย ๆ แต่จากความขยันในการฝึกเวทมนตร์และการล่าสัตว์ก็ทำให้เขารู้สึกสนใจที่ค้นคว้าเกี่ยวกับสไลม์ สิ่งมีชีวิตทีมีหลายอย่างให้ค้นหา'
                ' ตั้งใจเลี้ยง และค้นหาสไลม์พันธุ์อื่นๆ ในโลกใหม่นี้')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Dr. Stone]')
    st.markdown('![image](https://i.pinimg.com/originals/33/14/df/3314dff33be223b714c36e5127af5bc2.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.trueid.net/watch/th-th/series/wB3O0yZzny8B/7g7OX9a02Lbg')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81046193')
        st.markdown('▶ 🌷 https://wetv.vip/th/play/andc1zd7cjfxrc5-%EF%BC%A4%EF%BD%92%EF%BC%8E%EF%BC%B3%EF%BC%B4%EF%BC%AF%EF%BC%AE%EF%BC%A5/k00313b7wyf-EP1%EF%BC%9ADr.STONE')
        st.markdown('▶ 🌷 https://www.viu.com/ott/th/th/vod/386670/Dr-Stone')
        st.markdown('▶ 🌷 https://www.iq.com/play/dr-stone-episode-1-19rvgobtzs?lang=en_us')
    st.markdown('เซนคูเด็กหนุ่มผู้มีสติปัญญาปราดเปรื่องทางด้านวิทยาศาสตร์ กับไทจูเด็กหนุ่มผู้มีพละกำลังมหาศาลแต่มีจิตใจที่ดีงาม '
                'ทั้งสองเป็นเพื่อนที่ดีต่อกัน ไทจูหลงรักยูซึริฮะมาเป็นเวลานานแล้ว และเรื่องนี้มักจะถูกเซนคูหัวเราะมาตลอด'
                ' จะอย่างไรก็ตามในที่สุดไทจูก็รวบรวมความกล้าที่จะบอกรักยูซึริฮะ แต่ในเวลานั้นเอง บนท้องฟ้าก็เกิดลำแสงสว่างจ้าขึ้น'
                ' มวลมนุษยชาติทั้งหลายได้กลายเป็นหินไปหมด เกิดปรากฏการณ์ลึกลับอะไรขึ้น... ! ! หลังจากนั้นผ่านไปประมาณ 3,700 ปี'
                ' ในโลกยุคหินซึ่งไร้อารยธรรมใด ๆ ไทจูและเซนคูที่ร่างสามารถหลุดออกมาจากพันธนาการของหินที่ห่อหุ้มอยู่ได้กลับมารวมตัวกันอีกครั้ง'
                ' และทั้งสองก็ได้ตัดสินใจช่วยกันสร้างอารยธรรมของโลกใหม่ขึ้น โดยเริ่มต้นนับจากศูนย์')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                '+++++++++++++++++++++++++++')

# type 5 ***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวเล่าเรื่องชีวิตประจำวัน':
    st.title('อนิเมะแนวเล่าเรื่องชีวิตประจำวัน')
    st.markdown('เชื่อเหลือเกินว่า ตอนนี้ใครหลายคนต่างก็ต้องมีความเครียดและความกังวลติดค้างอยู่ในใจกันบ้าง'
                ' ไม่ว่าจะเป็น เรื่องการเงิน การงาน ความรัก และอีกมากมายหลายปัญหา การจะหาอะไรช่วยผ่อนคลายความเครียดพวกนี้ลงได้บ้าง '
                'นับว่าเป็นเรื่องที่ดีเลยทีเดียว ซึ่งในแต่ละคนต่างก็มีวิธีแก้ปัญหานี้ไม่เหมือนกัน บางคนออกไปเฮฮาปาร์ตี้แล้วหายเครียด '
                'บางคนอ่านหนังสือแล้วหายเครียด บางคนนั่งเล่นเกมอยู่บ้านแล้วหายเครียด การคลายเครียดของแต่ละคนมันขึ้นอยู่กับสไตล์การใช้ชีวิตเป็นหลัก'
                ' แน่นอนว่าชาว Anime อย่างเรา วิธีคลายเครียดที่ดีที่สุดนั่นก็คือ การได้นั่งดู Anime ยาว ๆ หน้าจอคอมพิวเตอร์ ยิ่งถ้าได้เป็น Anime'
                ' แนวชีวิตประจำวัน มาช่วยคลายความเครียด รับรองได้เลยว่า เห็นผลแน่นอนร้อยเปอร์เซ็นต์')
    st.markdown('### _1._:blue[Lucky☆Star]')
    st.markdown('![image](https://i.pinimg.com/originals/b0/b6/bc/b0b6bcff3fd2b36d54f5a5f7000c3572.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/search-result?q=Lucky%20Star')
    st.markdown('เรื่องราวจะเล่าถึงชีวิตประจำของ 4 สาว ม.ปลาย ต่างบุคลิก Izumi Konata สาวโอตาคุผิวสีแทนผมสีฟ้า '
                'ผู้ชื่นชอบการเล่นเกมและการดูอนิเมะมากที่สุด Takara, Miyuki สาวแว่นผู้เรียบร้อย เรียนเก่ง แต่มีนิสัยเป็นคนเปิ่น ๆ พูดน้อย Hiiragi,'
                ' Tsukasa น้องสาวฝาแฝดของ Hiiragi, Kagami เป็นฝาแฝดที่มีนิสัยต่างกันแบบสุดขั้ว ส่วนใหญ่ใน Anime จะเน้นไปที่การพูดคุยของทั้งสี่สาว '
                'บางทีก็จะเอามุกจากเกม หรือเหตุการณ์ที่เราเองก็เจออยู่จริง ๆ ในชีวิตประจำวันมาแอบล้อเล่นขำ ๆ กัน เช่น การถกเถียงกันขำ ๆ เรื่องของวิธีการกินขนม'
                ' การทักทายกับคนต่างชาติ การไปเยี่ยมเพื่อนเวลาป่วย การไปร้องคาราโอเกะ ซึ่งบางทีก็มีการแอบเอามุกจากการ์ตูนดังมาล้อเลียนบ้าง '
                'เวลาดูอาจจะต้องคิดตามมุกคิดหน่อย แต่ก็ถือว่าดูได้เรื่อย ๆ แบบไม่ต้องเครียดได้อยู่ ไม่ถึงกับการต้องถอดสมองดูขนาดนั้น')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[Yuru Camp]')
    st.markdown('![image](https://i.pinimg.com/originals/ca/67/25/ca6725e53672fa805b75cf96b01f97a2.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81392083')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/search-result?q=Back%20Camp')
    st.markdown('หากคุณเป็นคนรักในการเสพบรรยากาศของธรรมชาติ รักในการตั้งแคมป์ รักใน Anime ที่ดูได้สบาย ๆ มีตบมุกบ้างเล็ก ๆ น้อย ๆ มีความฮาพอกรุบกริบ '
                'ผมแนะนำให้คุณมาลองดูเรื่องนี้เลยครับ "Yuru Camp" เป็น Anime ที่จะกล่าวถึงเรื่องราวของ Rin Shima สาวน้อยที่รักในการตั้งแคมป์เป็นชีวิตจิตใจ'
                ' แต่ส่วนใหญ่เธอจะชอบไปคนเดียว จนกระทั่งอยู่มาวันหนึ่งเธอได้รู้จักกับ Nadeshiko Kagamihara เพื่อนที่ชอบการตั้งแคมป์เหมือนกัน ทั้งสองคนก็เริ่มสนิทมากขึ้น เ'
                'ริ่มไปไหนมาไหนด้วยกันมากขึ้น ได้เจอเพื่อนที่ชอบแบบเดียวกันเพิ่มขึ้นเรื่อย ๆ ชีวิตของเธอก็เปลี่ยนไปจากเดิมตลอดกาล จากที่ไปไหนมาไหนคนเดียว ก็มีเพื่อนเพิ่มขึ้น'
                ' มีความสุขเพิ่มขึ้น ภายใน Anime เรื่องนี้มันไม่มีอะไรซับซ้อนเลยครับ สิ่งที่คุณจะได้จากการดูเรื่องนี้คือ ได้เยียวยาจิตใจที่เหนื่อยล้า ไปกับแก๊งสาว ๆ ที่รักในการตั้งแคมป์'
                ' ได้เห็นบรรยากาศสวย ๆ จากใน Anime ยิ่งช่วงนี้หลายคนก็ออกไปเที่ยวกันไม่ได้เพราะสถานการณ์ Covid-19 การดูเรื่องนี้ถือเป็นอะไรที่ตอบโจทย์มากเลยทีเดียว')
    st.markdown('C-Station คือชื่อสตูดิโอที่สร้าง Anime เรื่องนี้ขึ้นมา หลายคนอาจจะไม่คุ้นกันมากนัก อาจจะมองว่าเป็นค่ายธรรมดา ไม่มีอะไรพิเศษ แต่ขอบอกเอาไว้ตรงนี้เลยว่า '
                'Anime เรื่อง Yuru Camp และ Yuru Camp Season 2 เขาทำออกมาได้ดีเกินความคาดหมายสุด ๆ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _3._:blue[Himouto! Umaru-chan]')
    st.markdown('![image](https://i.pinimg.com/originals/4a/89/39/4a8939611ffbd3dce63ed5906aa966c9.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/34781')
    st.markdown('Umaru Doma หรือที่คนรู้จักกันดีในชื่อของ Umaru-chan สาวน้อยมัธยมปลายวัย 16 ปี ที่มีสองบุคลิก ตอนอยู่ที่โรงเรียนเป็นสาวสวยที่เพรียบพร้อมไปเสียทุกอย่าง'
                ' ไม่ว่าจะเป็นเรื่องการเรียน กีฬา หรือการเข้าสังคม แต่อีกบุคลิกคือตอนกลับมาที่ห้อง เธอดันเป็นคนที่ขี้เกียจตัวเป็นขน วัน ๆ เอาแต่เล่นเกม ดู Anime และอ่านหนังสือการ์ตูน'
                ' พร้อมอาวุธติดตัวอย่างขนมขบเขี้ยวและขวดน้ำอัดลมขนาดใหญ่ ความแตกต่างที่ Anime สื่อออกมาคือ อยู่ที่โรงเรียนจะเป็นร่างคนธรรมดา พอกลับมาที่ห้อง '
                'ร่างกายจะหดเล็กลงทันทีโดยที่ไม่ต้องพึ่งพายา Apotoxin4869 ด้วยนิสัยสุดประหลาดนี้เอง ทำให้พี่ชายอย่าง Taihei Doma ได้แต่เฝ้ามองน้องสาวตัวเองด้วยความเป็นห่วงปนเบื่อหน่าย เป็น Anime '
                'ที่ดูแล้วสนุกดี ได้เห็นความปั่นประสาทและความน่ารักของน้องสาวสุดเปิ่นอย่าง Umaru-chan')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[Non Non Biyori]')
    st.markdown('![image](https://i.pinimg.com/originals/69/54/8b/69548bca7db4e60f64814154d389ec76.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://aisplay.ais.co.th/portal/get_section/62b2884d60b308212a64a57f/')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/35152')
    st.markdown('ธรรมชาติที่สวยงาม ไร้ตึกสูงบดบัง เต็มไปด้วยต้นไม้ใบหญ้าสีเขียว พร้อมทั้งการใช้ชีวิตที่สุดแสนจะ Slow Life หากใครกำลังโหยหาบรรยากาศความเป็นบ้านนอก'
                ' ไร้ความวุ่นวาย ผมแนะนำให้ดูเรื่องนี้เลยครับ รับรองได้เลยว่า จากที่คุณคิดถึงบรรยากาศนี้อยู่แล้ว มันจะยิ่งทำให้คุณคิดถึงมันเข้าไปอีกได้อย่างแน่นอน สำหรับ Anime '
                'เรื่อง Non Non Biyori นั้น จะกล่าวถึง Hotaru Ichijou เด็กสาวจากเมืองกรุง ที่ต้องย้ายมาเรียนที่บ้านนอกอันแสนห่างไกลจากความเจริญ ไม่มีสิ่งอำนวยความสะดวกใด ๆ ท'
                'ี่นั่นเธอได้พบกันกับเหล่าเพื่อนสาวอีก 3 คน ที่เรียนอยู่ห้องเดียวกัน ได้แก่ Natsumi Koshigaya สาวน้อยผมแดงแกมส้ม นิสัยห้าว ๆ กล้าลุยกล้าลอง แต่เป็นมิตรกับทุกคน '
                'Komari Koshigaya สาวน้อยผมสีน้ำตาลสุดแสนใจดี อยู่ด้วยแล้วอบอุ่นหัวใจ และคนสุดท้าย Renge Miyauchi น้องเล็กอายุน้อยที่สุดในห้อง น้องชอบถือขลุ่ยติดตัวไว้ตลอดเวลา'
                ' เป็นเด็กที่น่ารัก น่าเอ็นดู ของกลุ่มพี่ ๆ ทั้งในห้องและนอกห้อง')
    st.markdown('ภายในเรื่อง จะเล่าถึงการใช้ชีวิตประจำวันของทั้ง 3 คน ในเขตบ้านนอกที่ห่างไกลจากความเจริญ พวกเธอจะพาไปสัมผัสถึงความสวยงามของธรรมชาติที่สงบและร่มรื่น '
                'ไม่ต้องใช้ชีวิตเคร่งเครียดเร่งรีบ สนุกไปกับสิ่งที่อยู่รอบตัว สนุกไปกับการเดินเล่นในเขตบ้านนอกที่แสนสนุกสนาน เรียกได้ว่า ดูแล้วแทบอยากลองไปเยือนสถานที่นั้นจริง ๆ'
                ' เลยก็ว่าได้ ท่าทางจะสงบสุข และเยียวยาจิตใจได้เยอะน่าดูเลย')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Grand Blue]')
    st.markdown('![image](https://i.pinimg.com/564x/ee/09/77/ee09775378b83bde86c123ff675ecf9b.jpg)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/download')
        st.markdown('▶ 🌷 https://www.primevideo.com/detail/0QX33LCIUYWDW377X6PCSIJ8JV/')
    st.markdown('Grand Blue คือ Anime แนว Slice of Life สุดเถื่อน ที่เล่าเรื่องราวของ'
                ' Iori Kitahara เด็กหนุ่มวัย 18 ปี ที่กำลังจะเข้ามหาลัย พร้อมกับความคาดหวังเรื่องอนาคตของตัวเอง เขาได้ย้ายมาอยู่ที่บ้านพักตากอากาศริมทะเลของญาติ '
                'เพราะว่าที่นั่นใกล้กับมหาลัยที่เขาจะเรียนอยู่ เพียงวันแรกที่เขาก้าวเข้ามา ความคาดหวังเรื่องชีวิตในรั้วมหาลัยของเขาก็ต้องพังพินาศลง เมื่อตัวเขาเองได้มาพบเจอกับเหล่ารุ่นพี่และเพื่อนร่วมรุ่นที่วัน ๆ '
                'เอาแต่บริหารร่างกายด้วยน้ำเก๊กฮวยสีเหลืองมีฟอง ใช้ชีวิตด้วยความสนุกสนานไปเรื่อย ๆ ตอนแรกตัวเขาเองก็ยังไม่ชินกับบรรยากาศ แต่พอได้รู้จัก และอยู่กันไปเรื่อย ๆ '
                'ในที่สุดก็เริ่มกลืนเข้ากับพวกเหล่ารุ่นพี่และเพื่อนร่วมรุ่นไปซะแล้')
    st.markdown('เป็น Anime ที่ดูแล้วสนุก มัน ฮา และปั่นประสาทสุด ๆ เพียงแค่ได้มาดูชีวิตประจำวันสุดกวนของเหล่าตัวละครในเรื่อง สมองของผมเองก็แทบจะปลิวออกไปนอกหน้าต่างแล้ว'
                ' เพราะมันไม่จำเป็นจะต้องหยิบสมองมานั่งดูแต่อย่างใด เสพเอาความสนุกแค่นั้นก็พอแล้ว ใครที่กำลังเรียนมหาลัยหรือเรียนจบไปแล้ว พอมาดูเรื่องนี้น่าจะอินไม่น้อย '
                'แถมบางทีอาจจะแอบรู้สึกคิดถึงเลยก็เป็นไปได้ ชีวิตปั่น ๆ ไม่ต้องเครียดกับงาน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

# type 6 **************************************************************************************************************************************************************

if ALL == 'อนิเมะแนววิทยาศาสตร์':
    st.title('อนิเมะแนววิทยาศาสตร์')
    st.markdown('มีเวลาว่างหรืออยากพัก แต่ไม่รู้จะดูอะไร เรามี Sci-Fi Anime 5 เรื่องที่คุณไม่ควรพลาดมานำเสนอกัน ไปเริ่มกันเลย')
    st.markdown('### _1._:blue[Cowboy Bebop]')
    st.markdown('![image](https://i.pinimg.com/originals/94/5f/98/945f98febd002c48fb0060cd55f6fc49.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/search-result?q=Cowboy%20Bebop')
    st.markdown('Cowboy Bebop เป็นเรื่องราวในอนาคตปี 2071  ที่ผู้ก่อการร้ายระบาดหนักไปทั่วโลก มีการลอบวางระเบิด รถบรรทุกน้ำมันบนถนนทางหลวงสายใหญ่ใกล้กับเมือง '
                'ใหญ่ที่มีผู้คนแออัด แรงระเบิดรัศมีครึ่งไมล์ ส่งผลให้มีผู้เสียชีวิตและ บาดเจ็บเป็นจำนวน 500 คน ที่น่ากลัวคือ ระเบิดนั้นบรรจุเชื้อโรคชีวเคมี ท'
                'างการได้เริ่มตั้งรางวัลนำจับหรือก็คือฆ่าหัวของผู้ก่อการร้ายเอาไว้สูงมาก จึงทำให้กลุ่มนักล่าฆ่าหัวอย่าง Bebop ซึ่งมีสมาชิก 4 คน กับอีก 1 ตัว เริ่มการออกล่าและสืบหาหลักฐานต่าง ๆ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[Eureka seven]')
    st.markdown('![image](https://i.pinimg.com/originals/38/8a/d7/388ad7e124b5c47cab83d7708718689e.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/36384')
    st.markdown('ในเมืองเบลล์ฟอร์เรสต์ มีเด็กหนุ่มอายุ 14 ปี ชื่อเรนตัน เทอร์สตัน อาศัยอยู่ เขาปรารถนาที่จะออกจากบ้านของเขาไปเข้าร่วมกลุ่มทหารรับจ้างที่รู้จักกันในชื่อ Gekkostate เพื่อที่จะได้พบกับการผจญภัยที่จะทำให้ชีวิตของเขาสดใสขึ้น'
                ' อย่างไรก็ตาม เขาติดอยู่ระหว่างการยืนกรานของปู่ที่อยากให้เขาจะกลายเป็นช่างเหมือนปู่และแรงกดดันจากมรดกของพ่อที่เสียชีวิตไปของเขา ความตื่นเต้นเพียงอย่างเดียวที่เรนตันพบ คือ การขี่อนุภาคคลื่น Trapar ท'
                'ี่กระจายไปทั่วอากาศ ทุกอย่างเปลี่ยนไปเมื่อมีวัตถุที่ไม่รู้จักเกิดขัดข้องในโรงรถ เรนตันค้นพบว่าเป็น Light Lookup Operation ซึ่งเป็นหุ่นยนต์ที่สามารถขี่คลื่น Trapar ซึ่งรู้จักกันในชื่อ Nirvash typeZERO น'
                'ักบินของมันคือเด็กสาวชื่อ ยูเรก้า ซึ่งเป็นสมาชิกของ Gekkostate เธอได้ร้องขอให้เขาปรับแต่ง Nirvash ให้ นั่นจึงเกิดเป็นการเริ่มต้นที่ทำให้เรนตันเข้าไปมีส่วนร่วมกับ Gekkostate และเขาออกบินไปข้าง ๆ'
                ' กับยูเรก้าในฐานะนักบินร่วมของ Nirvash')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

    st.markdown('### _3._:blue[Neon genesis evangelion]')
    st.markdown('![image](https://i.pinimg.com/originals/87/9b/af/879bafcf2280ee2f9819d3ad5f7ac807.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81033445')
        st.markdown('▶ 🌷 https://www.primevideo.com/detail/0K1XKKH7C44WF7VDCYDCFKF3EO/')
    st.markdown('ในปี ค.ศ. 2015 เป็นเวลา 15 ปีหลังจากหายนะที่เรียกว่า Second Impact การตกกระแทกของอุกาบาตขนาดใหญ่ที่มีสิ่งมีชีวิตพิเศษตกที่ขั้วโลกใต้ เป็นเหตุให้น้ำแข็งขั้วโลกละลายส่งผลให้ระดับน้ำทะเลสูงขึ้น '
                'ทำให้ประชากรของโลกจำนวนมากต้องล้มตายลงเกือบครึ่งหนึ่ง เหล่าผู้นำประเทศระดับสูงจึงได้เริ่มมีการจัดตั้งสหประชาคมโลกและองค์กรพิทักษ์มนุษยชาติ โดยมีการตั้งเมืองแบบใหม่แทนที่เมืองที่จมลงในทะเล '
                'ในการสำรวจความเสียหายและการวิจัยเศษซากของอุกาบาตนั้น ได้พบกับเผ่าพันธุ์ยักษ์ที่มนุษย์เรียกว่า “แองเจิล” ตื่นขึ้นมาบนโลกและเริ่มก่อให้เกิดการทำร้ายร่างกายทุกประเภท แนวป้องกันเดียวสำหรับพวกเขาคือเครื่องจักรชีวภาพที่เรียกว่า'
                ' Evangelion')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[Tengen toppa gurren lagann]')
    st.markdown('![image](https://i.pinimg.com/originals/05/94/b6/0594b68c914af9ca543705958b2000e3.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/36970')
    st.markdown('Simon อาศัยอยู่ในหมู่บ้านที่อยู่ใต้ดิน เพราะว่ามนุษย์กึ่งสัตว์ได้กวาดล้างมนุษย์ทำให้มนุษย์นั้นกระจายกันออกไป แต่ลูกพี่เขา Kamina '
                'ใฝ่ฝันที่จะหนีออกไปจากหมู่บ้านใต้ดิน แต่กฎเกณฑ์ของหมู่บ้านไม่ยอม แต่แล้วขณะที่กำลังจะหาทางขึ้นและพวกเขาถูกจับได้ ก็ได้มีหุ่นยนต์ยักษ์ที่มีใบหน้าใหญ่โต มีแขนขาติดที่หน้า '
                'ตกมาจากเบื้องบน ส่งผลให้ข้างบนหมู่บ้านกลายเป็นหลุมใหญ่ แล้วก็ตามมาด้วย Yoko ที่ต่อสู้กับกับหุ่นนั้น (เรียกว่า Gunmen) ด้วยความบ้าของ Kamina ทำให้ Yoko'
                ' ไม่สามารถทำอะไรได้ถนัด Simon ได้ช่วยเหลือทั้งสองคน และนำทั้งสองไปดูสิ่งที่เขาพบขณะที่กำลังขุด นั่นคือ Gunmen ขนาดเล็ก และแล้วการผจญภัยของทั้ง 3 คนก็เริ่มต้นขึ้น')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Psycho-pass]')
    st.markdown('![image](https://i.pinimg.com/originals/40/82/da/4082da16b0b4a804dda887d3b6a35b42.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/80006146')
        st.markdown('▶ 🌷 https://www.primevideo.com/detail/0GMA6H790B7EMLNVN83K54XMRA/')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2048558944?bstar_from=bstar-web.homepage.recommend.all')
    st.markdown('เรื่องราวได้กล่าวขึ้นในปี 2113 เป็นยุคที่การปกครองทางสังคมได้มีการนำเอาระบบกฎหมายไฮเทคที่มีชื่อว่า “Sibyl System” เข้ามาบังคับใช้พลเมือง '
                'เพื่อหวังที่จะสร้างความเป็นเสถียรภาพและแบบแผนการดำเนินชีวิตที่ดีขึ้นให้กับประชาชนในสังคม แต่ทว่าด้วยกฎหมายของ Sibyl System '
                'นั้นเป็นกฎเกณฑ์ที่ชี้นำมากกว่าความเป็นหลักประชาธิปไตยจนเกินไป ทำให้เกิดความเห็นต่างที่ยากเกินการยอมรับได้ นี่จึงไม่ต่างจากกฎหมายที่ชี้ให้คนไหนเป็นคนไหนตายได้อย่างง่ายดาย เพราะเมื่อ'
                ' “ความถูกต้อง… ความถูกผิด… และความเท่าเทียม” ได้ถูกตัดสินจากระดับสีความแตกต่างของค่าสัมประสิทธิ์อาชญากรรม หรือที่เรียกว่า “ไซโค-พาร์ท” จึ'
                'งส่งผลทำให้ความเห็นต่างแปรเปลี่ยนไปสู่แนวคิดการต่อต้านและกระบวนการล้มล้างกฎเกณฑ์การปกครอง ที่คอยกดขี่ห่มเหงอย่างไร้ซึ่งความเป็นเสรีชน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
# type 7 ***************************************************************************************************************************************************************
if ALL == 'อนิเมะแนวสืบสวน':
    st.title('อนิเมะแนวสืบสวน')
    st.markdown('หากจะพูดถึงอนิเมะหรือการ์ตูนญี่ปุ่นในปัจจุบันแล้วนั้น เชื่อว่าคงจะเป็นสิ่งที่หลายคนเคยเห็นผ่านหูผ่านตามาแล้วอย่างแน่นอน หรือบางคนก็อาจชื่นชอบจนเป็นแฟนตัวยงเลยก็มี'
                ' ซึ่งอนิเมะในปัจจุบันก็มีอยู่หลากหลายแนวให้คุณได้เลือกดูกันตามแนวความชอบ แต่นอกจากนี้ก็ยังมีอนิเมะอีกหนึ่งแนวที่ก็ได้รับความนิยมไม่แพ้แนวอื่น ๆ เลย นั่นก็คือ ‘อนิเมะนักสืบ’ นั่นเอง')
    st.markdown('ซึ่งความสนุกของเจ้าอนิเมะนักสืบนี้เป็นอะไรที่ค่อนข้างจะแตกต่างจะอนิเมะแนวอื่น ๆ อยู่พอสมควร เพราะนอกจากความสนุกเข้มข้นของเนื้อเรื่อง ที่มีความซับซ้อนซ่อนเงื่อนชวนติดตามแล้ว ก็ยังจะช่วยให้คุณได้ฝึกการสังเกตมีส่วนร่วมในการไขคดีจากปมหรือเบาะแสที่เนื้อเรื่องค่อย'
                'ๆ ปล่อยออกมา ทำให้เราได้ร่วมคิดวิเคราะห์และมีส่วนร่วมไปกับอนิเมะที่เราดูได้ ซึ่งถือเป็นเสน่ห์เฉพาะในแบบของอนิเมะนักสืบเลยค่ะในวันนี้เราจึงได้ทำการรวบรวมอนิเมะนักสืบยอดนิยมทั้งอนิเมะเรื่องเก่าและอนิเมะเรื่องใหม่ '
                'มาแนะนำให้ทุกคนได้รู้จักกัน จะมีอนิเมะเรื่องไหนที่ห้ามพลาดบ้างนั้น เราไปดูกันเลยค่ะ')
    st.markdown('### _1._:blue[The Millionaire Detective Balance]')
    st.markdown('![image](https://i.pinimg.com/originals/14/0f/54/140f540a9edb19a8633071b367c901a8.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.iq.com/album/2ffkws2tl3x')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/35526')
    st.markdown('เรื่องราวได้กล่าวขึ้นในปี 2113 เป็นยุคที่การปกครองทางสังคมได้มีการนำเอาระบบกฎหมายไฮเทคที่มีชื่อว่า “Sibyl System” เข้ามาบังคับใช้พลเมือง '
                'เพื่อหวังที่จะสร้างความเป็นเสถียรภาพและแบบแผนการดำเนินชีวิตที่ดีขึ้นให้กับประชาชนในสังคม แต่ทว่าด้วยกฎหมายของ Sibyl System นั้นเป็นกฎเกณฑ์ที่ชี้นำมากกว่าความเป็นหลักประชาธิปไตยจนเกินไป'
                ' ทำให้เกิดความเห็นต่างที่ยากเกินการยอมรับได้ นี่จึงไม่ต่างจากกฎหมายที่ชี้ให้คนไหนเป็นคนไหนตายได้อย่างง่ายดาย เพราะเมื่อ “ความถูกต้อง… ความถูกผิด… และความเท่าเทียม”'
                ' ได้ถูกตัดสินจากระดับสีความแตกต่างของค่าสัมประสิทธิ์อาชญากรรม หรือที่เรียกว่า “ไซโค-พาร์ท” จึงส่งผลทำให้ความเห็นต่างแปรเปลี่ยนไปสู่แนวคิดการต่อต้านและกระบวนการล้มล้างกฎเกณฑ์การปกครอง '
                'ที่คอยกดขี่ห่มเหงอย่างไร้ซึ่งความเป็นเสรีชน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[Kabukichou Sherlock]')
    st.markdown('![image](https://i.pinimg.com/564x/3c/22/61/3c22616a4f33f03bfb8dcf1808e13b09.jpg)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2015915194')
    st.markdown('ภายในสถานที่อันแสนสวยงามรายล้อมไปด้วยแสงสีของไฟนีออนที่นอกจากจะสวยเด่นสะดุดตาแล้ว ก็ยังทำให้สถานที่ที่เรียกว่า ‘คาบุกิโจว’ แห่งนี้สว่างไสวในตลอดค่ำคืน ซึ่งแน่นอนว่าถ้ามีความสว่างไสว '
                'แปลว่าความมืดมิดนั้นอยู่ไม่ไกล เพราะคดีฆาตกรรมปริศนาได้เกิดขึ้นอย่างอุกอาจใจกลางเมืองโดยฝีมือของฆาตรกรต่อเนื่องที่ผู้คนต่างเรียกเขาว่า ‘Jack the Ripper’ '
                'เหล่าแก๊งนักสืบสายป่วนจึงได้รับภารกิจในการไขคดีปริศนาสุดแปลกประหลาดในครั้งนี้ ด้วยลีลาการสืบคดีสุดปั่นป่วนแบบฉบับนักสืบสายฮา แต่พวกเขาจะทำได้สำเร็จหรือไม่ '
                'ไปเอาใจช่วยพวกเขากันได้ใน Kabukichou Sherlock รับรองว่าคุณจะสามารถดูอนิเมะเรื่องนี้ได้เรื่อย ๆ แบบไม่มีเบื่อเลยค่ะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _3._:blue[ Tantei wa Mou, Shindeiru]')
    st.markdown('![image](https://i.pinimg.com/originals/1a/4d/f6/1a4df6772c577a79fc103b48eba1c1b8.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.iq.com/album/%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%AA%E0%B8%B7%E0%B8%9A%E0%B8%95%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7-se8h2j6nvh')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/1010919')
    st.markdown('อนิเมะแนวสืบสวนสอบสวนที่ผสมกลิ่นอายของเรื่องราวเหนือธรรมชาติเข้ามาได้อย่างลงตัว กับเรื่องราวของ ‘คิมิฮิโกะ’ ชายหนุ่มสุดธรรมดาที่ไม่ธรรมดา '
                'เพราะชีวิตของเขามักจะต้องไปมีเหตุให้ได้ไปเกี่ยวข้องกับคดีแปลก ๆ อยู่เสมอ ในครั้งนี้ก็เช่นกันในขณะที่เขากำลังโดยสารอยู่บนเครื่องบินจู่ ๆ ก็ถูกเหล่ามนุษย์สังเคราะห์เล่นงานเข้า '
                'ก่อนที่เขาจะได้รู้จักกับ ‘เซียสต้า’ สาวน้อยนักสืบสุดน่ารักที่ได้มาช่วยเขาไขคดีถูกทำร้ายบนเครื่องบิน ทำให้คิมิฮิโกะก็ได้กลายเป็นผู้ช่วยของซิสต้าไปโดยปริยาย ซึ่งหลังจากนั้นพวกเขาก็ได้ทำคดีแปลก ๆ'
                ' ร่วมกันอีกหลายคดี ซึ่งผู้ต้องหาก็ต่างไม่ใช้มนุษย์ และดูเหมือนเซียสต้าเองก็จะมีเรื่องที่ปิดบังเขาเอาไว้เช่นกัน เรื่องราวจะเป็นอย่างไรต่อไป พวกเราตามไปสืบคดีกันต่อใน Tantei wa Mou, Shindeiru เลยจ้า')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[Bungou Stray Dogs]')
    st.markdown('![image](https://i.pinimg.com/originals/79/93/ae/7993ae08e3b1892b334294dd32b3c440.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/2073947')
        st.markdown('▶ 🌷 https://www.iq.com/play/%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%9E%E0%B8%B1%E0%B8%99%E0%B8%98%E0%B8%81%E0%B8%A3%E0%B8%88%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94-%E0%B8%A0%E0%B8%B2%E0%B8%84-4-ep-1-1whukzhk79c')
        st.markdown('▶ 🌷 https://aisplay.ais.co.th/portal/get_section/5cb18259aae731729dbea35f/')
        st.markdown('▶ 🌷 https://www.primevideo.com/detail/0M1ORLI3RWCQ3DFLY5WD0LUBJ4/')
    st.markdown('เรื่องราวเริ่มต้นขึ้นเมื่อ ‘อัตสึชิ’ ต้องออกจากบ้านพักเด็กกำพร้า ในขณะที่เขาไม่มีที่ไปก็ได้รับความช่วยเหลือจาก ‘โอซามุ’ ชายหนุ่มท่าทางประหลาดที่ต้องการจะฆ่าตัวตายตลอดเวลา เขาได้พาอัตสึชิมาอาศัยอยู่ด้วยใน'
                ' ‘สำนักงานนักสืบบุโซ’ ซึ่งในสถานมี่แห่งนี้เองนอกจากพวกเขาแล้ว ก็ยังเป็นที่อยู่คนอีกกลุ่มหนึ่งซึ่งเป็นผู้มีพลังพิเศษต่างจากคนทั่วไปที่รวมตัวกันเพื่อปฏิบัติภารกิจในการสืบสวนคดีแปลกประหลาดที่ตำรวจไม่สามารถทำได้'
                'ก่อนที่อัตสึชิจะได้รู้ว่า จริง ๆ แล้วตัวเองก็เป็นหนึ่งในผู้มีพลังวิเศษเช่นกัน และได้กลายเป็นส่วนหนึ่งของทีมสืบสวนสุดแปลกนี้ แต่เขาจะมีพลังวิเศษอะไร? เราต้องไปติดตามกันต่อใน Bungou Stray Dogs เอาเองนะคะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[Hyouka]')
    st.markdown('![image](https://i.pinimg.com/originals/58/24/9d/58249daad3e4e54dceccaa74ac583ca9.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.youtube.com/playlist?list=PLIa05JMgYhhY2ERi7KDmYeYwwSEvUDKOD')
        st.markdown('▶ 🌷https://www.bilibili.tv/th/play/34818')
    st.markdown('เรื่องราววุ่น ๆ ของกลุ่มวรรณกรรมคลาสสิกของเหล่านักเรียนชั้นมัธยมปลายที่ ‘โอเรกิ โฮทาโร่’ หนุ่มพลังงานน้อยได้จับพลัดจับผลูมาเข้าร่วมชมรมแห่งนี้ตามคำแนะนำของพี่สาว จนได้มาพบกับ ‘จิทันดะ เอรุ’ สาวน้อยน่ารักที่มีนิสัยอยากรู้อยากเห็น'
                ' นอกจากนี้สมาชิกคนอื่น ๆ ก็เป็นเพื่อนที่เขารู้จักดีอย่าง ‘ฟุคุเบะ ซาโตชิ’ เพื่อนสนิทของเขา และ ‘อิบาระ มายากะ’ เพื่อนสมัยประถม ซึ่งสมาชิกชมรมทั้ง 4 คนก็ได้ไปรับรู้เรื่องราวเกี่ยวกับเหตุการณ์ประหลาดที่เคยเกิดขึ้นเมื่อ '
                '33 ปีก่อน ที่ถูกอดีตสมาชิกชมรมในสมัยก่อนเก็บงำไว้มานานหลายปี ซึ่งพวกเขาต่างเรียกเหตุการณ์ในครั้งนั้ว่า ‘HYOUKA’ ทำให้พวกเขาได้เริ่มต้นค้นหาเบาะแส เพื่อไขปริศนาที่ถูดปิดไว้จว่าจริง ๆ แล้ว HYOUKA คืออะไรกันแน่? '
                'อย่าลืมไปติดตามให้ได้นะคะ')

# type 8 ***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวดร่าม่า':
    st.title('อนิเมะแนวดราม่า')
    st.markdown('ไม่ต่างจากหนังหรือละครรักที่มักจะมีพล็อตเศร้าให้เราร้องไห้ การ์ตูนรักเศร้าๆ ที่น่าดูเองก็มีหลายเรื่อง '
                'ทั้งเศร้าแบบฟูมฟาย เศร้าแบบเหงาๆ หรือเศร้าแบบจุกอกพูดไม่ออก สุดท้ายแล้วการ์ตูนเหล่านี้ไม่ได้ทิ้งไว้ให้เราแค่คราบน้ำตา แต่ยังมีรอยยิ้มและความประทับใจที่ทำให้เราต้องหยิบยกมาแนะนำกัน')
    st.markdown('### _1._:blue[Shigatsu wa Kimi no Uso]')
    st.markdown('![image](https://i.pinimg.com/originals/8d/31/e7/8d31e73ae0ec20f76191d7a88537922e.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/1066080')
    st.markdown('อาริมะ โควเซย์ นักเปียโนเด็กอัจฉริยะสูญเสียมารดาไปด้วยโรคร้าย เขาซึ่งมีความหลังฝังใจจึงไม่สามารถเล่นเปียโนได้อีก จนกระทั่งได้พบกับ'
                ' มิยาโซโนะ คาโอริ นักไวโอลินสาวที่เริ่มทำให้เขากลับมาเปิดใจ และพยายามทำให้เขากลับมาเล่นเปียโนอีกครั้ง แต่ขณะเดียวกันมิยาโซโนะก็คบหาดูใจกับเพื่อนของเขาอยู่')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _2._:blue[AnoHana]')
    st.markdown('![image](https://i.pinimg.com/originals/27/1a/11/271a11c278232e23af855b38e6e33c4f.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/34620')
    st.markdown('เด็ก 6 คนเคยเป็นเพื่อนรักเพื่อนเล่นกันจนกระทั่ง เมนมะ เพื่อนคนหนึ่งในกลุ่มเสียชีวิตไปด้วยอุบัติเหตุ วันหนึ่ง จินตัน '
                'อดีตหัวหน้ากลุ่มเด็กได้พบกับวิญญาณของเธอกลับมาหา พร้อมบอกว่าตนยังไปไหนไม่ได้เพราะมีเรื่องที่ยังไม่ได้ทำที่นึกไม่ออก จินตันจึงต้องรวบรวมเพื่อนเก่าที่แยกห่างกันไปกลับมาเพื่อช่วยให้เมนมะได้ไปสู่สุคติ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _3._:blue[Isshuukan Friends]')
    st.markdown('![image](https://i.pinimg.com/originals/fc/85/03/fc8503da1cf134178ac3aa74f6245ac5.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/36999')
    st.markdown('ฮาเสะ ยูกิ พยายามจะเป็นเพื่อนกับ ฟูจิมิยะ คาโอริ เพื่อนร่วมห้องที่ไม่เคยสุงสิงหรือพูดคุยกับใคร แต่ก็ถูกปฏิเสธกลับมาครั้งแล้วครั้งเล่า'
                ' เพราะฟูจิมิยะมีอาการประหลาดที่จะลืมเรื่องราวของทุกคนไปภายในเวลา 1 สัปดาห์ สุดท้ายฮาเสะจะทำให้เธอจำเขาได้และยอมเป็นเพื่อนด้วยหรือไม่')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _4._:blue[Hotarubi no Mori e]')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/37006')
    st.markdown('![image](https://i.pinimg.com/originals/f2/5c/eb/f25ceb3fa8d3e5376f59b155b0d512d9.gif)')
    st.markdown('โฮตารุในวัย 6 ขวบ หลงป่าขณะมาเที่ยวต่างจังหวัดตอนปิดเทอมฤดูร้อน แต่ได้ภูตเด็กหนุ่มใส่หน้ากากนามว่า กิน ช่วยไว้ เธอกลับมาหาและเล่นกับเขาทุกๆ ปิดเทอม โดยมีข้อแม้ว่าจะไม่สามารถสัมผัสตัวเขาได้'
                ' เมื่อเติบโตขึ้นเรื่อยๆ ความรู้สึกของโฮตารุก็เริ่มเปลี่ยนไป จากเพื่อนเป็นความรัก แต่เธอก็รู้อยู่เต็มอกว่านั่นเป็นรักที่ไม่สามารถเป็นจริงได้')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.markdown('### _5._:blue[5 cm per Second]')
    st.markdown('![image](https://i.pinimg.com/originals/29/0e/56/290e567d48cae643a9210456767843b7.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2005236059?bstar_from=bstar-web.homepage.recommend.all')
    st.markdown('ผลงานเก่าที่สร้างชื่อให้ ชินไค มาโคโตะ และคว้ารางวัลมากมาย ก่อนมากำกับอนิเมะ 2 หมื่นล้านอย่าง หลับตาฝัน ถึงชื่อเธอ')
    st.markdown('อนิเมะเล่าเรื่องราว 3 ช่วงชีวิตของ ทากากิ ที่ไม่ว่าเมื่อไหร่ในใจก็ยังมีแต่ความทรงจำต่อ อาคาริ เด็กสาวที่เป็นเพื่อนสมัยเด็กเท่านั้น'
                ' เรื่องเล่าผ่านภาพฉากสวยๆ และเพลงประกอบเพราะๆ เศร้า ทำเอาใครที่ได้ดูเป็นต้องเหงาจุกอก พูดไม่ออก หน่วงทั้งวันไปตามๆ กัน')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

# type 9 ***************************************************************************************************************************************************************

if ALL == 'อนิเมะแนวต่อสู้':
    st.title('อนิเมะแนวต่อส้')
    st.markdown('เรื่องที่เราจะนำมาฝากกันในวันนี้ ส่วนใหญ่แล้วจะเป็นเรื่องที่หลายคนอาจจะเคยคุ้นหู หรือว่าเคยผ่านตากันมาบ้างแล้ว แต่ก็อาจจะมีอีกหลายเรื่อง ที่ยังไม่รู้จักหรือยังไม่เคยดูด้วยเหมือนกัน'
                ' รวมไปถึงช่องทางการดูอนิเมะ ที่จะมีทั้งเนื้อหาบน Netflix และจากที่อื่นๆ อย่างเข่น iQiyi, LINE TV, FLIXER หรือว่า TrueID TV ขึ้นอยู่กับว่าเรื่องนั้นจะมีการฉายอยู่ที่เว็บไหนบ้างอย่างถูกลิขสิทธิ์เท่านั้น '
                'ดังนั้นทุกๆ เรื่องที่เอามาแนะนำก็จะมีช่องทางการดูครบทุกเรื่องเลย'
                ' เพื่อให้เราได้สนับสนุนการดูอนิมเอย่างถูกกฎหมาย ส่วนเรื่องของภาษาที่เว็บไหนจะมีพากย์ไทย หรือมีแค่ซับไทยอย่างเดียว อันนี้ขึ้นอยู่กับว่าแต่ละเรื่องมีมาให้อยู่แล้วหรือไม่ด้วย พร้อมแล้วก็ไปลุยกันเลย')

    st.markdown('### _1._:blue[One Punch Man]')
    st.markdown('![image](https://i.pinimg.com/originals/fd/0c/35/fd0c350027c229eb7f77a17e73cc8df8.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/80117291')
        st.markdown('▶ 🌷 https://movie.trueid.net/th-th/series/owaP8qZ4Xd8R/yWR6ZMPpXyZW/OQJA9j5o799V/2mOQbOvKkGeg')
    st.markdown('เริ่มกันที่อนิเมะแนวต่อสู้เรื่องแรก ที่เชื่อว่าหลายคนน่าจะเคยเห็นหรือเคยอ่านหนังสือแล้วเจอกันมาแล้ว กับพี่โล้นซ่าไซตามะ เจ้าพ่อหมัดเดียวจอดที่หลายๆ คนยังเอาไปเทียบกับการ์ตูนเรื่องอื่นๆ '
                'ในจักรวาลการ์ตูนญี่ปุ่นกันเลยทีเดียวว่ามีใครสู้เขาได้หรือไม่ ด้วยความเก่งกาจและพลังที่แสนจะเวอร์วัง จากการที่ไซตามะ พระเอกของเรื่องนั้นเคยเป็นคนไม่เอาไหนมาก่อน จนกระทั่งเขาได้เข้าไปช่วยเด็กคนหนึ่ง'
                ' และทำให้เขานั้นเริ่มฝึกร่างกายด้วยท่าเบสิคจนแข็งแกร่ง เพื่อที่จะก้าวเข้าสู่การเป็นฮีโร่ให้ได้ และถึงแม้ว่าเขาจะแข็งแกร่งมากแค่ไหนก็ตาม แต่ก็ยังไม่มีใครรับรู้พลังของไซตามะจริงๆ ได้ว่าแข็งแกร่งแค่ไหน '
                'นอกจากศิษย์เพียงยคนเดียวคือ จีนอส ที่ดันไปเห็นถึงความแข็งแกร่งตอนตบยุงตัวร้ายเข้า และทำให้เขานั้นต่อสู้เพื่อที่จะก้าวเข้าไปใกล้ความแข็งแกร่งเหมือนไซตามะให้ได้ และไซตามะเองก็ต้องเป็นฮีโร่ให้ได้เช่นกัน'
                ' เรื่องนี้ความจริงถึงแม้ว่าจะเป็นการต่อสู้กับสัตว์ประหลาด แต่ก็แฝงไปด้วยความตลกในหลายๆ ตอน เรียกได้ว่าดูไม่เบื่อเลย')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

    st.markdown('### _2._:blue[Shaman King]')
    st.markdown('![image](https://i.pinimg.com/originals/97/c2/ed/97c2ede9d8bb4ff25525d7bf9518ae4f.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/81239555')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/38108')
    st.markdown('อีกหนึ่งอนิเมะต่อสู้ที่มีภาค Remake ออกมาฉายบน Netflix เมื่อไม่กี่เดือนที่ผ่านมา ถ้าใครที่เคยอ่านหรือดูเรื่องนี้ทันสมัยหลายปีก่อนในยุค itv ก็น่าจะรู้กันดีว่าเนื้อหาการ์ตูนเรื่องนี้มีความสนุกมากแค่ไหน '
                'ซึ่งในภาครีเมกนี้ก็ไม่ได้ทำให้ความสนุกลดลงไปแต่อย่างใด เนื้อเรื่องนั้นจะเกี่ยวกับผู้ใช้วิญาณที่ถูกเรียกกันว่า ชาแมน และเหล่าชาแมนนั้นจะมีกระจายออกไปทั่วทุกมุมโลก จุดมุ่งหมายของแต่ละคนล้วนต้องการยืนอยู่บนจุดสูงสุดหรือ'
                ' ราชันย์แห่งภูต นั่นเอง โดยในทุก 500 ปีจะมีการจัดแข่งขันขึ้นเพื่อค้นหาชาแมนคิง และในปีนี้ก็ได้จัดขึ้นที่ประเทศญี่ปุ่น จึงทำให้ อาซากุระ โย พระเอกของเรื่องต้องลงแข่งพร้อมกับ อามิดามารุ วิญญาณซามูไรของเขาเอง '
                'ถึงแม้ว่าจะเป็นการแข่งขันแต่ความจริงก็ยังมีเบื้องหลังของ ฮาโอ ที่กลับมาเกิดใหม่และต้องการเกรทสปิริต เพื่อทำลายคนที่ไม่ชาชาแมนทิ้งทั้งหมด อาซากุระ โยและเพื่อนๆ จึงต้องช่วยกันหยุดเรื่องนี้ให้ได้')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

    st.markdown('### _3._:blue[Black Clover]')
    st.markdown('![image](https://i.pinimg.com/originals/09/33/df/0933dff960df6245c00323ecd9e01afa.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/video/2045479246?bstar_from=bstar-web.homepage.recommend.all')
        st.markdown('▶ 🌷 https://www.viu.com/ott/th/th/vod/376324/Black-Clover')
        st.markdown('▶ 🌷 https://www.iq.com/album/2dlxit4wm55')
        st.markdown('▶ 🌷 https://wetv.vip/th/play/otrgw9us2zufwn6-%E0%B9%81%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%84%20%E0%B9%82%E0%B8%84%E0%B8%A5%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%20(%E0%B8%9E%E0%B8%B2%E0%B8%81%E0%B8%A2%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2)/i00343q5nr8-EP1%3A%20%E0%B9%81%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%84%20%E0%B9%82%E0%B8%84%E0%B8%A5%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%20(%E0%B8%9E%E0%B8%B2%E0%B8%81%E0%B8%A2%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2)')
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/80238012')
    st.markdown('เนื้อเรื่องของเรื่องนี้จะเหมาะกับคนที่ชอบการ์ตูนต่อสู้แนวเวทมนต์หน่อย เพราะได้พูดถึง อัสต้า และ ยูโน เด็กที่ถูกทิ้งไว้ ณ อาณาจักรโคลเวอร์ และทั้งสองคนต้องการที่จะเป็นจักรพรรดิเวทมนตร์'
                ' หรือคนที่ยืนอยู่จุดสูงสุดของคนใช้เวทมนต์ให้ได้ ถึงแม้ว่าทั้งคู่จะโตมาด้วยกันแต่ว่ายูโนนั้นกลับมีพลังเวทที่เก่งมาก ส่วนอัสต้ากลับไม่สามารถใช้เวทได้เลยแม้แต่นิดเดียว จนกระทั่งถึงเวลาเมื่ออายุ 15 ปียูโนก็ได้รับพลังจาก '
                'กรีมัวร์ เป็นโคลเวอร์ 4 แฉกแบบเดียวกับจักรพรรดิเวทรุ่นก่อน เพราะมีพลังเวทมหาศาลอยู่ในตัวอยู่แล้ว ส่วยอัสต้านั้นไม่ได้อะไรเลย จนกระทั่งถึงช่วงเวลาที่ตกอยู่ในอัตรายชองอัสต้า เขากลับได้รับใบโคลเวอร์ 5 '
                'แฉกและดาบสีดำขนาดใหญ่จัดขึ้นมาแทน ซึ่งใบโคลเวอร์ 5 แฉกนั้นคือพลังของปิศาจนั่นเอง ส่วนเรื่องราวจะเป็นยังไงต่อต้องไปดูกันเอาเองนะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')

    st.markdown('### _4._:blue[ Attack on Titan]')
    st.markdown('![image](https://i.pinimg.com/originals/22/8b/3b/228b3b38aae5ff85adfd305b034db582.gif)')
    with st.expander("รับชมได้ที่"):
        st.markdown('▶ 🌷 https://www.netflix.com/th/title/70299043')
        st.markdown('▶ 🌷 https://www.bilibili.tv/th/play/35044')
    st.markdown('ถ้าจะพูดถึงเรื่องต่อสู้ที่ไม่ใช่กับคนกับเอง ก็คงจะหนีไม่พ้นอนิเมะต่อสู้เรื่อง Attack on Titan เรื่องนี้อย่างแน่นอน สนุกจนถึงขั้นพี สะเดิดแต่งเพลงให้เลยทีเดียว เนื้อเรื่องนี้ได้พูดถึงเหล่าไททัน '
                'ที่มีขนาดใหญ่แถมยังมีรูปร่างที่แตกต่างกันไป แต่ทั้งหมดนั้นได้เข้ามาโจมตีเหล่ามนุษย์และพร้อมจะกลืนกินทุกคนเข้าไป หลังจากที่ผ่านไป 100 ปีที่เหล่าไททันนั้นหายไปและกลับมาโจมตีอีกครั้ง '
                'โดยจุดแรกที่โดนโจมตีคือกำแพงชั้นนอก “วอลล์มาเรีย” ที่ทำให้ เอเรน เยเกอร์ นั้นสูญเสียแม่ของเขาไปกับเหตุการณ์ครั้งนี้ สิ่งที่พ่อของเอเรนที่เป็นหมอทิ้งไว้ให้มีเพียงกุญแจเพียงดอกเดียว หลังจากนั้นเขาจึงไปเข้าร่วมกับทีมสำรวจ'
                ' และร่วมต่อสู้เพื่อกำจัดเหล่าไททัน สุดท้ายแล้วเรื่องราวจะเป็นอย่างไร ต้องไปติดตามดูกันเอาได้เลย บนเว็บ Viu ก็มีนะ')
    st.markdown('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              '+++++++++++++++++++++++++++')
    st.image("Picture/k.png",width=500)
