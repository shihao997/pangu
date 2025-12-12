# 导入必要的库
import streamlit as st  # Streamlit框架，用于创建Web应用
import pandas as pd  # pandas库，用于数据处理和分析
from datetime import datetime  # datetime模块，用于处理日期和时间

# 页面配置
st.set_page_config(
    page_title="赵信数据档案",  # 浏览器标签页标题
    page_icon="⚔️",  # 浏览器标签页图标
    layout="wide",  # 使用宽屏布局
    initial_sidebar_state="collapsed"  # 初始状态侧边栏折叠
)

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

# 侧边栏（初始状态为折叠，需要点击展开）
with st.sidebar:
    st.markdown("### 🎮 作战控制面板")  # 侧边栏标题
    
    st.markdown("#### 数据筛选")  # 筛选器标题
    mission_type = st.selectbox(
        "选择任务类型",  # 下拉框标签
        ["全部", "峡谷遭遇战", "龙团作战", "推塔行动", "野区巡逻", "守卫防御"]  # 选项列表
    )
    
    st.markdown("#### 显示设置")  # 设置标题
    show_details = st.toggle("显示详细数据", value=True)  # 切换按钮，默认开启
    auto_refresh = st.toggle("实时数据流", value=True)  # 切换按钮，默认开启
    
    refresh_rate = st.slider("数据刷新频率 (Hz)", 1, 60, 10)  # 滑块，范围1-60，默认10
    
    # 数据同步按钮
    if st.button("🚀 强制数据同步", type="primary"):  # 主要按钮样式
        st.success("数据同步请求已发送...")  # 成功提示
        
    st.markdown("---")  # 分隔线
    st.markdown("""
    **系统状态:**  
    ✅ 核心数据库连接正常  
    ✅ 数据流处理运行中  
    ⚠️ 历史档案索引中...  
    ✅ 实时计算引擎就绪
    """)  # 显示系统状态信息
