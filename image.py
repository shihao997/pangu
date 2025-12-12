import streamlit as st

st.set_page_config(page_title="相册", page_icon="%")
st.title("大王相册")

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.HtrwUFjV3eaXWpzZYcI-NAHaGZ?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", 'text': '埃罗芒老师'},
    {'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.n4d7EQ9DcExt6pobyJR-6wHaM1?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", 'text': '超神学院天使彦'},
    {'url': "https://pic4.zhimg.com/v2-a22c981e3042aff4698cbfb62d40b3d3_r.jpg", 'text': '东京喰种金木研'}
]

st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['text'])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] -1) % len(images)


cl, c2 = st.columns(2)

with cl:
    st.button("上一张", on_click=prevImg, use_container_width=True)
with c2:
    st.button("下一张", on_click=nextImg, use_container_width=True)
