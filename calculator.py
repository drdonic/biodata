import streamlit as st

st.title("简单计算器")

# 1. 获取用户输入
number1 = st.number_input("请输入第一个数字", value=0.0)
number2 = st.number_input("请输入第二个数字", value=0.0)

# 2. 选择运算操作
operation = st.selectbox("请选择运算方式", ("加法", "减法", "乘法", "除法"))

# 3. 计算逻辑
if st.button("开始计算"):
    if operation == "加法":
        result = number1 + number2
        st.success(f"结果是: {result}")
    elif operation == "减法":
        result = number1 - number2
        st.success(f"结果是: {result}")
    elif operation == "乘法":
        result = number1 * number2
        st.success(f"结果是: {result}")
    elif operation == "除法":
        # 4. 防错处理
        if number2 == 0:
            st.error("错误：除数不能为零！")
        else:
            result = number1 / number2
            st.success(f"结果是: {result}")