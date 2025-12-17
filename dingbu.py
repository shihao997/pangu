import streamlit as st
import pandas as pd
import numpy as np

# 页面全局设置
st.set_page_config(
    page_title="多页面应用",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 全局样式微调
st.markdown("""
    <style>
    .stTextInput>div>div>input {padding: 4px 8px;}
    .stSelectbox>div>div>select {padding: 4px 8px;}
    .stContainer {border-radius: 8px;}
    
    /* 标签页样式调整 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 8px 8px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 创建顶部标签页
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "个人简历生成器", 
    "大王相册", 
    "南宁西乡塘美食", 
    "音乐", 
    "视频", 
    "赵信"
])

with tab1:
    # ========== 简历编辑页面内容开始 ==========
    st.title("📄 简历编辑与预览")
    st.write("这是一个简历编辑工具，左侧填写信息，右侧实时预览")
    
    # 使用两列布局：左侧输入表单，右侧简历预览
    form_col, preview_col = st.columns([1, 2])
    
    with form_col:
        # 1. 基本信息模块（简历首项）
        with st.container(border=True):
            st.markdown("#### 📋 简历信息填写")
            st.divider()
            
            st.markdown("##### 基本信息")
            name = st.text_input("姓名", placeholder="请输入全名")
            gender_age = st.columns([1, 1])
            with gender_age[0]:
                gender = st.selectbox("性别", ["", "男", "女"])
            with gender_age[1]:
                age = st.text_input("年龄", placeholder="如：25")
            phone = st.text_input("联系电话", placeholder="138XXXX1234")
            email = st.text_input("电子邮箱", placeholder="example@xxx.com")
            avatar_file = st.file_uploader("上传头像", type=["jpg", "png"])
            
            st.divider()
            
            # 2. 求职意向模块（简历核心项）
            st.markdown("##### 求职意向")
            job_target = st.selectbox("意向岗位", ["", "Python开发", "前端开发", "数据分析师", "产品经理"])
            work_city = st.selectbox("工作城市", ["", "北京", "上海", "广州", "深圳", "杭州"])
            salary = st.text_input("期望薪资", placeholder="如：15k-20k/月")
            
            st.divider()
            
            # 3. 教育背景模块（简历必备项）
            st.markdown("##### 教育背景")
            edu_school = st.text_input("毕业院校", placeholder="如：XX大学")
            edu_major = st.text_input("所学专业", placeholder="如：计算机科学与技术")
            edu_time = st.text_input("就读时间", placeholder="2018.09-2022.06")
            
            st.divider()
            
            # 4. 工作经历模块
            st.markdown("##### 工作经历")
            work_company = st.text_input("公司名称", placeholder="如：XX科技有限公司")
            work_position = st.text_input("职位名称", placeholder="如：Python开发工程师")
            work_time = st.text_input("工作时间", placeholder="2022.07-至今")
            work_desc = st.text_area("工作描述", placeholder="简述工作职责与成果...", height=80)
            
            st.divider()
            
            # 5. 技能特长模块
            st.markdown("##### 技能特长")
            skills = st.multiselect(
                "选择技能",
                ["Python", "SQL", "Java", "HTML/CSS", "JavaScript", "机器学习", "办公软件"]
            )
    
    with preview_col:
        # 简历主体卡片
        with st.container(border=True):
            # 头部：头像+基本信息
            header_col1, header_col2 = st.columns([1, 5])
            with header_col1:
                if avatar_file:
                    st.image(avatar_file, width=120)
                else:
                    st.markdown("<div style='width:120px;height:120px;border:1px dashed #ccc;display:flex;align-items:center;justify-content:center;color:#999'>暂无头像</div>", unsafe_allow_html=True)
            with header_col2:
                st.markdown(f"### {name if name else ''}")
                age_display = f"{age}岁" if age else ""
                st.markdown(f"性别：{gender if gender else ''} | 年龄：{age_display}")
                st.markdown(f"电话：{phone if phone else ''} | 邮箱：{email if email else ''}")

            st.divider()

            # 求职意向板块
            st.markdown("### 求职意向")
            target_col = st.columns(3)
            with target_col[0]:
                st.markdown(f"**意向岗位**：{job_target if job_target else ''}")
            with target_col[1]:
                st.markdown(f"**工作城市**：{work_city if work_city else ''}")
            with target_col[2]:
                st.markdown(f"**期望薪资**：{salary if salary else ''}")

            st.divider()

            # 教育背景板块
            st.markdown("### 教育背景")
            edu_col = st.columns(3)
            with edu_col[0]:
                st.markdown(f"**院校**：{edu_school if edu_school else ''}")
            with edu_col[1]:
                st.markdown(f"**专业**：{edu_major if edu_major else ''}")
            with edu_col[2]:
                st.markdown(f"**时间**：{edu_time if edu_time else ''}")

            st.divider()

            # 工作经历板块
            st.markdown("### 工作经历")
            work_col1 = st.columns(3)
            with work_col1[0]:
                st.markdown(f"**公司**：{work_company if work_company else ''}")
            with work_col1[1]:
                st.markdown(f"**职位**：{work_position if work_position else ''}")
            with work_col1[2]:
                st.markdown(f"**时间**：{work_time if work_time else ''}")
            st.markdown(f"**工作描述**：{work_desc if work_desc else ''}")

            st.divider()

            # 技能特长板块
            st.markdown("### 技能特长")
            st.markdown(", ".join(skills) if skills else "")
    
    # ========== 简历编辑页面内容结束 ==========

with tab2:
    # ========== 相册页面内容开始 ==========
    st.title("大王相册")

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    images = [
        {'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.HtrwUFjV3eaXWpzZYcI-NAHaGZ?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", 'text': '埃罗芒老师'},
        {'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.n4d7EQ9DcExt6pobyJR-6wHaM1?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", 'text': '超神学院天使彦'},
        {'url': "https://pic4.zhimg.com/v2-a22c981e3042aff4698cbfb62d40b3d3_r.jpg", 'text': '东京喰种金木研'}
    ]

    # 显示当前图片
    st.image(images[st.session_state['ind']]['url'], 
             caption=images[st.session_state['ind']]['text'],
             use_column_width=True)

    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

    def prevImg():
        st.session_state['ind'] = (st.session_state['ind'] -1) % len(images)

    # 控制按钮
    col1, col2 = st.columns(2)
    with col1:
        st.button("上一张", on_click=prevImg, use_container_width=True)
    with col2:
        st.button("下一张", on_click=nextImg, use_container_width=True)
    
    # 显示当前图片索引
    st.info(f"当前图片：{st.session_state['ind'] + 1} / {len(images)}")
    
    # ========== 相册页面内容结束 ==========

with tab3:
    # ========== 美食数据分析页面内容开始 ==========
    # 这里完全使用你提供的美食数据分析代码，不做任何修改
    
    # 1. 定义基础餐厅数据
    restaurants_data = {
        "餐厅": ["星艺荟尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分（满分5分）": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }

    # 2. 转换为DataFrame（调整索引为"餐厅"）
    df = pd.DataFrame(restaurants_data).set_index("餐厅")

    # 3. 提取需要可视化的数值列（评分、人均消费）
    visual_df = df[["评分（满分5分）", "人均消费(元)"]]
    # 提取地图数据
    map_df = df[["latitude", "longitude"]]

    # 4. 生成12个月价格走势数据
    # 设置随机种子保证数据可复现
    np.random.seed(42)
    # 定义月份
    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    # 基于基础人均消费生成带小幅波动的月度价格
    price_trend_data = {}
    base_prices = df["人均消费(元)"].values

    for i, restaurant in enumerate(df.index):
        # 基础价格 ± 随机波动（1-3元），保证价格合理
        monthly_prices = base_prices[i] + np.random.randint(-1, 4, size=12)
        # 确保价格不低于成本（最低8元）
        monthly_prices = np.maximum(monthly_prices, 8)
        price_trend_data[restaurant] = monthly_prices

    # 构建价格走势DataFrame
    price_trend_df = pd.DataFrame(price_trend_data, index=months)

    # 5. Streamlit展示布局
    st.title("😋南宁西乡塘美食-数据分析")
    # 餐厅位置地图
    st.subheader("😋美食地理位置分布")
    st.map(map_df)
    # 基础信息表格
    st.subheader("😋南宁西乡塘美食-基础信息")
    st.dataframe(visual_df)

    # 评分&人均消费可视化
    st.subheader("👍️评分 vs 人均消费")
    st.line_chart(visual_df)
    st.bar_chart(visual_df)

    # 新增：12个月价格走势折线图
    st.subheader("💰️各餐厅12个月人均消费价格走势")
    st.line_chart(
        price_trend_df,
        x_label="月份",
        y_label="人均消费(元)",
        height=400  # 调整图表高度增强可读性
    )

    # 可选：显示价格走势数据详情
    with st.expander("查看价格走势详细数据"):
        st.dataframe(price_trend_df)
    
    # ========== 美食数据分析页面内容结束 ==========

with tab4:
    # ========== 音乐播放器页面内容开始 ==========
    import streamlit as st

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
    # ========== 音乐播放器页面内容结束 ==========

with tab5:
    # ========== 视频播放页面内容开始 ==========
    import streamlit as st

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
    # ========== 视频播放页面内容结束 ==========

with tab6:
    # ========== 赵信数据档案页面内容开始 ==========
    # 从zhaoxin.txt文件复制的内容，不做任何修改
    # 导入必要的库
    import streamlit as st  # Streamlit框架，用于创建Web应用
    import pandas as pd  # pandas库，用于数据处理和分析
    from datetime import datetime  # datetime模块，用于处理日期和时间

    # 自定义CSS实现科幻风格
    st.markdown("""  # 使用markdown插入自定义CSS样式
    <style>
        /* 导入谷歌字体 */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
        
        /* 全局样式 - 设置应用背景 */
        .stApp {
            background: linear-gradient(135deg, #0a0a2a 0%, #1a1a3a 100%);  /* 渐变背景 */
            color: #e0e0ff;  /* 文字颜色 */
            font-family: 'Share Tech Mono', monospace;  /* 字体 */
        }
        
        /* 标题样式 */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;  /* 科幻风格字体 */
            color: #00e5ff;  /* 青蓝色 */
            text-shadow: 0 0 10px rgba(0, 229, 255, 0.7);  /* 发光效果 */
            border-bottom: 1px solid rgba(0, 229, 255, 0.3);  /* 底部边框 */
            padding-bottom: 10px;  /* 底部内边距 */
        }
        
        /* 指标卡样式 */
        .metric-card {
            background: rgba(10, 20, 40, 0.7);  /* 半透明深蓝色背景 */
            border: 1px solid rgba(0, 229, 255, 0.4);  /* 发光边框 */
            border-radius: 8px;  /* 圆角 */
            padding: 15px;  /* 内边距 */
            box-shadow: 0 0 15px rgba(0, 229, 255, 0.2);  /* 阴影效果 */
            transition: all 0.3s ease;  /* 过渡动画 */
        }
        
        /* 指标卡悬停效果 */
        .metric-card:hover {
            box-shadow: 0 0 25px rgba(0, 229, 255, 0.4);  /* 悬停时阴影增强 */
            transform: translateY(-2px);  /* 悬停时向上移动 */
        }
        
        /* 表格样式 */
        .dataframe {
            background: rgba(10, 20, 40, 0.7) !important;  /* 表格背景 */
            border: 1px solid rgba(0, 229, 255, 0.4) !important;  /* 表格边框 */
            color: #e0e0ff !important;  /* 表格文字颜色 */
        }
        
        /* 表格表头样式 */
        .dataframe th {
            background-color: rgba(0, 50, 100, 0.8) !important;  /* 表头背景 */
            color: #00e5ff !important;  /* 表头文字颜色 */
            font-weight: bold;  /* 粗体 */
            font-family: 'Orbitron', sans-serif;  /* 科幻字体 */
        }
        
        /* 代码块样式 */
        .stCodeBlock {
            background: rgba(10, 20, 40, 0.8) !important;  /* 代码块背景 */
            border: 1px solid rgba(0, 229, 255, 0.4) !important;  /* 代码块边框 */
            border-radius: 6px;  /* 圆角 */
        }
        
        /* 侧边栏样式 */
        .css-1d391kg {
            background: rgba(10, 20, 40, 0.9) !important;  /* 侧边栏背景 */
        }
        
        /* 分隔线样式 */
        hr {
            border-color: rgba(0, 229, 255, 0.3);  /* 分隔线颜色 */
            margin: 25px 0;  /* 上下边距 */
        }
        
        /* 流计算状态指示器样式 */
        .stream-status {
            display: inline-block;  /* 行内块元素 */
            width: 12px;  /* 宽度 */
            height: 12px;  /* 高度 */
            border-radius: 50%;  /* 圆形 */
            margin-right: 8px;  /* 右边距 */
            background-color: #00ff88;  /* 绿色 */
            box-shadow: 0 0 10px #00ff88;  /* 发光效果 */
            animation: pulse 2s infinite;  /* 脉冲动画，无限循环 */
        }
        
        /* 脉冲动画关键帧 */
        @keyframes pulse {
            0% { opacity: 1; }  /* 开始：完全不透明 */
            50% { opacity: 0.5; }  /* 中间：半透明 */
            100% { opacity: 1; }  /* 结束：完全不透明 */
        }
    </style>
    """, unsafe_allow_html=True)  # 允许HTML，用于应用CSS样式

    # 标题区域
    st.title("⚔️ 德邦总管赵信")  # 主标题
    st.markdown("---")  # 分隔线

    # 创建三列布局，比例为2:1:1
    col1, col2, col3 = st.columns([2, 1, 1])

    # 第一列：基础信息
    with col1:
        st.markdown("### 📊 基础信息")  # 三级标题
        st.markdown("""
        **作战代号:** 德邦总管  
        **所属阵营:** 德玛西亚  
        **定位:** 战士/刺客
        """)  # 显示基础信息文本

    # 第二列：胜率指标
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)  # 开始指标卡div
        st.metric(label="作战胜率", value="55%", delta="+2.3%")  # 显示胜率指标
        st.markdown('</div>', unsafe_allow_html=True)  # 结束指标卡div

    # 第三列：数据完整度指标
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)  # 开始指标卡div
        st.metric(label="数据完整度", value="87%", delta="+5.1%")  # 显示数据完整度指标
        st.markdown('</div>', unsafe_allow_html=True)  # 结束指标卡div

    # 技能矩阵部分
    st.markdown("---")  # 分隔线
    st.header("🎯 技能介绍")  # 二级标题

    # 技能数据字典
    skill_data = {
        "技能名称": ["三重爪击", "风斩电刺", "无畏冲锋", "新月守卫"],  # 技能名称列表
        "蓝耗": [92, 88, 95, 78],  # 蓝耗数值列表
        "伤害指数": [8.5, 7.2, 9.1, 8.8],  # 伤害指数列表
        "使用频率": ["高", "高", "中", "低"],  # 使用频率列表
        "连招加成": [15, 12, 18, 25]  # 连招加成列表
    }

    # 创建技能数据DataFrame
    df_skills = pd.DataFrame(skill_data)

    # 显示技能表格，使用容器宽度
    st.dataframe(df_skills, use_container_width=True)

    # Stream计算引擎状态部分
    st.markdown("---")  # 分隔线
    st.header("⚡ Stream战斗引擎")  # 二级标题

    # 创建两列布局，比例为1:2
    col1, col2 = st.columns([1, 2])

    # 第一列：计算状态
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)  # 开始指标卡div
        st.markdown('<span class="stream-status"></span> **实时计算状态: 运行中**', unsafe_allow_html=True)  # 显示状态指示器和文本
        st.metric(label="计算速度", value="68%", delta="-3.2%")  # 显示计算速度指标
        st.progress(0.68)  # 显示进度条，68%进度
        st.markdown('</div>', unsafe_allow_html=True)  # 结束指标卡div

    # 第二列：算法说明
    with col2:
        st.markdown("""
        **Stream算法 v2.1.4**  
        *实时战斗数据流处理引擎*
        
        ```python
        # 战斗算法
        def xin_zhao_combo(target_health, distance):
            # 无畏冲锋
            if distance > 0:
                cast_E(target_position)
            
            # 三重爪击
            for i in range(3):
                cast_Q()
                apply_knockup_if_third()
            
            # 风斩电刺
            cast_W()
            
            # 新月守卫
            if enemy_count > 2:
                cast_R()
            
            return calculate_damage()
        ```
        """)  # 显示算法说明和示例代码

    # 任务日志部分
    st.markdown("---")  # 分隔线
    st.header("📋 战斗日志")  # 二级标题

    # 任务数据字典
    mission_data = {
        "日期": ["2020-04-15", "2019-07-04", "2020-05-22", "2020-03-10", "2020-03-28"],  # 日期列表
        "时间": ["14:30:45", "20:15:33", "16:45:12", "11:20:05", "19:30:18"],  # 时间列表
        "任务类型": ["峡谷遭遇战", "龙团作战", "推塔行动", "野区巡逻", "守卫防御"],  # 任务类型列表
        "作战结果": ["胜利", "胜利", "胜利", "失败", "胜利"],  # 作战结果列表
        "K/D/A": ["8/2/12", "12/4/18", "5/1/9", "3/6/5", "7/3/14"],  # KDA数据列表
        "数据完整性": [92, 87, 95, 68, 89]  # 数据完整性百分比列表
    }

    # 创建任务数据DataFrame
    df_missions = pd.DataFrame(mission_data)

    # 显示任务表格，使用容器宽度
    st.dataframe(df_missions, use_container_width=True)

    # 数据源链接部分
    st.markdown("---")  # 分隔线
    st.markdown("### 🔗 数据来源")  # 三级标题

    # 创建三列布局
    col1, col2, col3 = st.columns(3)

    # 第一列：官方手册链接
    with col1:
        st.markdown('[📖 官方作战手册](https://example.com)')  # 外部链接

    # 第二列：数据分析文档链接
    with col2:
        st.markdown('[📊 数据分析文档](https://docs.example.com)')  # 外部链接

    # 第三列：实时战况链接
    with col3:
        st.markdown('[⚔️ 实时战况](https://example.com/live)')  # 外部链接

    # 底部信息部分
    st.markdown("---")  # 分隔线
    st.markdown("""
    **作战指挥系统:** Python Studio v3.7  
    **数据管理器:** ID-2022-XZ-001  
    **档案编号:** XZ-DF-20220101-087  
    
    *最后同步: 2022-01-01 23:59:59 UTC*  # 时间戳
    """)  # 显示底部系统信息

 # 显示系统状态信息
    # ========== 赵信数据档案页面内容结束 ==========
