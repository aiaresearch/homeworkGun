import db_configs

from flask import Flask, Response
from zhipuai import ZhipuAI

app = Flask(__name__)

submits = db_configs.get_submits()
unsubmits = db_configs.get_unsubmits()
# 构造包含提交和未提交数据的字符串
submit_data = "Submits:\n" + "\n".join([str(submit) for submit in submits]) + "\n\nUnsubmits:\n" + "\n".join([str(unsubmit) for unsubmit in unsubmits])

client = ZhipuAI(api_key="YOUR_API_KEY")
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": "你是一个为老师提供作业提交建议的助手，用于根据学生提交作业和未提交作业的数据，做出预测并给老师提供建议。"},
        {"role": "user", "content": submit_data},
    ],
    stream=True,
)

get_query_result = []
for chunk in response:
    get_query_result.append(chunk.choices[0].delta)
    print(chunk.choices[0].delta)

# 定义API端点
@app.route('/get-data', methods=['GET'])
def data():
    query_result = get_query_result()
    return Response(query_result(), mimetype='application/json')

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)