import streamlit as st

st.set_page_config(page_title="小区视频", page_icon="❤")
st.title("凡人修仙传")
# 定义视频数据数组，每个元素是一个字典，包含视频URL和标题
video_arr = [
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/1.mp4',
        'title': '凡人修仙传第1集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/2.mp4',
        'title': '凡人修仙传第2集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/3.mp4',
        'title': '凡人修仙传第3集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/4.mp4',
        'title': '凡人修仙传第4集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/5.mp4',
        'title': '凡人修仙传第5集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/6.mp4',
        'title': '凡人修仙传第6集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/7.mp4',
        'title': '凡人修仙传第7集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/8.mp4',
        'title': '凡人修仙传第8集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/9.mp4',
        'title': '凡人修仙传第9集'
    },
    {
        'url': 'https://jrjtgmefhduhdwfvgvkw.supabase.co/storage/v1/object/public/fanren/10.mp4',
        'title': '凡人修仙传第10集'
    }
]

# 初始化当前播放索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前播放的视频标题
current_video = video_arr[st.session_state['ind']]
st.subheader(f"正在播放：{current_video['title']}")

# 显示视频播放器
st.video(current_video['url'], autoplay=True)

def play(i):
    """播放指定索引的视频"""
    st.session_state['ind'] = int(i)

# 添加视频选择器部分
st.divider()
st.subheader("选择集数")

# 设置每行列数（这里设置为5列）
columns_per_row = 5

# 计算需要多少行
total_videos = len(video_arr)
rows = (total_videos + columns_per_row - 1) // columns_per_row  # 向上取整

for row in range(rows):
    # 创建一行中的列
    cols = st.columns(columns_per_row)
    
    # 为这一行的每一列创建按钮
    for col_idx in range(columns_per_row):
        video_idx = row * columns_per_row + col_idx
        
        if video_idx < total_videos:
            with cols[col_idx]:
                # 高亮显示当前正在播放的集数
                is_current = st.session_state['ind'] == video_idx
                button_type = "primary" if is_current else "secondary"
                
                st.button(
                    f'第{video_idx + 1}集',
                    key=f'btn_{video_idx}',
                    use_container_width=True,
                    type=button_type,
                    on_click=play,
                    args=(video_idx,)
                )

# 添加视频信息统计
st.divider()
st.info(f"📺 共 {len(video_arr)} 集视频 | 当前播放：第 {st.session_state['ind'] + 1} 集")
