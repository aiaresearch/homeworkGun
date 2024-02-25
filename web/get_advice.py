import db_configs

from zhipuai import ZhipuAI

submits = db_configs.get_submits()
unsubmits = db_configs.get_unsubmits()

# 构造包含提交和未提交数据的字符串
def generate_data():
    submit_data = "Submits:\n" + "\n".join([str(submit) for submit in submits]) + "\n\nUnsubmits:\n" + "\n".join([str(unsubmit) for unsubmit in unsubmits])

    client = ZhipuAI(api_key="YOUR_API_KEY")
    response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": "你是一个为老师提供作业提交建议的助手，请使用中文用于根据学生提交作业和未提交作业的数据，做出预测并给老师提供建议。"},
        {"role": "user", "content": submit_data},
    ],
    stream=True,
    )

    for chunk in response:
        print(chunk.choices[0].delta)