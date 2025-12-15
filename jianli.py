import streamlit as st

# 页面全局设置：模拟简历纸张尺寸，关闭侧边栏默认折叠
st.set_page_config(
    page_title="简历实时编辑预览",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 全局样式微调（仅用原生st.markdown，无额外CSS库）
st.markdown("""
    <style>
    .stTextInput>div>div>input {padding: 4px 8px;}
    .stSelectbox>div>div>select {padding: 4px 8px;}
    .stContainer {border-radius: 8px;}
    </style>
    """, unsafe_allow_html=True)

# ========== 左侧：表单输入区（严格按简历模块划分） ==========
with st.sidebar:
    st.markdown("### 📋 简历信息填写")
    st.divider()

    # 1. 基本信息模块（简历首项）
    st.markdown("#### 基本信息")
    name = st.text_input("姓名", placeholder="请输入全名", label_visibility="collapsed")
    gender_age = st.columns([1, 1])
    with gender_age[0]:
        gender = st.selectbox("性别", ["", "男", "女"], label_visibility="collapsed")
    with gender_age[1]:
        # 将年龄改为自由文本输入
        age = st.text_input("年龄", placeholder="如：25", label_visibility="collapsed")
    phone = st.text_input("联系电话", placeholder="138XXXX1234", label_visibility="collapsed")
    email = st.text_input("电子邮箱", placeholder="example@xxx.com", label_visibility="collapsed")
    avatar_file = st.file_uploader("上传头像", type=["jpg", "png"], label_visibility="collapsed")

    st.divider()

    # 2. 求职意向模块（简历核心项）
    st.markdown("#### 求职意向")
    job_target = st.selectbox("意向岗位", ["", "Python开发", "前端开发", "数据分析师", "产品经理"], label_visibility="collapsed")
    work_city = st.selectbox("工作城市", ["", "北京", "上海", "广州", "深圳", "杭州"], label_visibility="collapsed")
    salary = st.text_input("期望薪资", placeholder="如：15k-20k/月", label_visibility="collapsed")

    st.divider()

    # 3. 教育背景模块（简历必备项）
    st.markdown("#### 师资背景")
    edu_school = st.text_input("毕业院校", placeholder="如：XX大学", label_visibility="collapsed")
    edu_major = st.text_input("所学专业", placeholder="如：计算机科学与技术", label_visibility="collapsed")
    edu_time = st.text_input("就读时间", placeholder="2018.09-2022.06", label_visibility="collapsed")

    st.divider()

    # 4. 工作经历模块
    st.markdown("#### 工作经历")
    work_company = st.text_input("公司名称", placeholder="如：XX科技有限公司", label_visibility="collapsed")
    work_position = st.text_input("职位名称", placeholder="如：Python开发工程师", label_visibility="collapsed")
    work_time = st.text_input("工作时间", placeholder="2022.07-至今", label_visibility="collapsed")
    work_desc = st.text_area("工作描述", placeholder="简述工作职责与成果...", height=80, label_visibility="collapsed")

    st.divider()

    # 5. 技能特长模块
    st.markdown("#### 技能特长")
    skills = st.multiselect(
        "",
        ["Python", "SQL", "Java", "HTML/CSS", "JavaScript", "机器学习", "办公软件"],
        label_visibility="collapsed"
    )

# ========== 右侧：简历预览区（严格还原纸质简历样式） ==========
st.markdown("# 📄 简历预览")
# 简历主体卡片（模拟纸质简历边框+底色）
with st.container(border=True):
    # 头部：头像+基本信息（简历标准顶部布局）
    header_col1, header_col2 = st.columns([1, 5])
    with header_col1:
        if avatar_file:
            st.image(avatar_file, width=120)
        else:
            st.markdown("<div style='width:120px;height:120px;border:1px dashed #ccc;display:flex;align-items:center;justify-content:center;color:#999'>暂无头像</div>", unsafe_allow_html=True)
    with header_col2:
        st.markdown(f"### {name if name else ''}")
        # 更新年龄显示，添加单位"岁"（如果用户输入了年龄）
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
    st.markdown("### 师资背景")
    edu_col = st.columns(4)
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
