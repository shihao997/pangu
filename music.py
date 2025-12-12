import streamlit as st

st.set_page_config(page_title="音乐播放器", page_icon="🎵")
st.title("小区音乐")

# 初始化音乐索引
if 'music_index' not in st.session_state:
    st.session_state['music_index'] = 0

# 音乐库数据 - 包含音乐文件路径或URL、封面和标题
music_library = [
    {
        'title': '江南雪',
        'cover': 'http://p2.music.126.net/RFbUrR2x2JEMB0WGYvwVQg==/109951169642392307.jpg?param=130y130',
        'artist': '李越',
        'file': 'https://music.163.com/song/media/outer/url?id=2161991028.mp3'  # 示例音乐URL，请替换为实际音乐文件
    },
    {
        'title': '篝火旁',
        'cover': 'http://p1.music.126.net/sN5dTpmeJO1DhxIj1ogMLg==/109951163416453597.jpg?param=130y130',
        'artist': '吕大叶',
        'file': 'https://music.163.com/song/media/outer/url?id=518725853.mp3'
    },
    {
        'title': 'CRY FOR YOU',
        'cover': 'http://p1.music.126.net/orQQMOzoU8pmU8BciJJciA==/109951172373570140.jpg?param=130y130',
        'artist': 'karry_b',
        'file': 'https://music.163.com/song/media/outer/url?id=3323934230.mp3'
    }
]

# 获取当前音乐信息
current_music = music_library[st.session_state['music_index']]

# 创建左右两列布局
left_col, right_col = st.columns([1, 1])  # 左右等宽

with left_col:
    st.subheader("专辑封面")
    # 显示专辑封面图片
    st.image(current_music['cover'], 
             width=1000)

with right_col:
    st.subheader("音乐信息")
    
    # 显示音乐标题和艺术家
    st.markdown(f"### 🎵 {current_music['title']}")
    st.markdown(f"#### 🎤 艺术家: {current_music['artist']}")
    
    # 显示当前播放进度信息
    st.info(f"正在播放: {current_music['title']}")
    
    # 添加一些装饰性元素
    st.markdown("---")
    
    # 音乐控制函数
    def next_music():
        st.session_state['music_index'] = (st.session_state['music_index'] + 1) % len(music_library)
        st.rerun()
    
    def prev_music():
        st.session_state['music_index'] = (st.session_state['music_index'] - 1) % len(music_library)
        st.rerun()
    
    # 创建控制按钮 - 水平排列
    st.subheader("播放控制")
    control_col1, control_col2, control_col3 = st.columns(3)
    
    with control_col1:
        if st.button("⏮️", help="上一首", use_container_width=True):
            prev_music()
    
    with control_col2:
        # 显示当前播放编号
        st.markdown(f"<div style='text-align: center; padding: 10px;'><h4>{st.session_state['music_index'] + 1} / {len(music_library)}</h4></div>", 
                   unsafe_allow_html=True)
    
    with control_col3:
        if st.button("⏭️", help="下一首", use_container_width=True):
            next_music()
    
    # 在右侧添加音乐播放器
    st.subheader("音乐播放器")
    st.audio(current_music['file'], format='audio/mp3')
