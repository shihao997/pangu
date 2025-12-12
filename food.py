import streamlit as st
import pandas as pd
import numpy as np

# 1. 定义基础餐厅数据
restaurants_data = {
    "餐厅": ["星艺荟尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分（满分5分）": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 20, 25, 35, 50],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
}

# 2. 转换为DataFrame（调整索引为“餐厅”）
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
