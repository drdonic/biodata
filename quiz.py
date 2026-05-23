import streamlit as st

st.title("question")

# 定义题目、选项和正确答案
questions = {
    "1. Python 的发明者是谁？": {"options": ["Guido van Rossum", "Elon Musk", "Bill Gates"],
                                "answer": "Guido van Rossum"},
    "2. 下面哪个是 Streamlit 的主要功能？": {"options": ["数据可视化", "网页应用开发", "以上都是"],
                                            "answer": "以上都是"},
    "3. 在 Python 中，2 + 2 等于多少？": {"options": ["3", "4", "5"], "answer": "4"}
}

# 用于存储用户的选择
user_answers = {}

# 循环显示题目
for i, (q, info) in enumerate(questions.items()):
    st.subheader(q)
    user_answers[q] = st.radio(f"请为第 {i + 1} 题选择答案：", info["options"], key=f"q{i}", index=None)
    st.divider()  # 使用 st.divider() 分隔题目

# 提交按钮
if st.button("提交答案"):
    score = 0
    all_answered = True

    # 检查是否所有题目都回答了
    for q in questions:
        if user_answers[q] is None:
            all_answered = False
            break

    if not all_answered:
        st.warning("请回答完所有题目后再提交！")
    else:
        # 计分和反馈
        for q, info in questions.items():
            if user_answers[q] == info["answer"]:
                st.success(f" {q} 回答正确！")
                score += 1
            else:
                st.error(f" {q} 回答错误。正确答案是: {info['answer']}")

        # 显示总分
        st.write("---")
        st.header(f"你的最终得分: {score} / 3")

        if score == 3:
            st.balloons()  # 全对有气球特效！