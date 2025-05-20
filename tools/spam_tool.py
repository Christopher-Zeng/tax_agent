from langchain_google_genai import ChatGoogleGenerativeAI

# 初始化 Gemini 模型
def init_model(api_key):
    return ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # ✅ 可换成 gemini-2.5-flash-preview-04-17 等
    google_api_key="AIzaSyCmLFghRyqBrs-zhQgsLxELCPlKY57zgIA"
)

# 垃圾邮件检测函数
def detect_spam(model, email_text):
    prompt = f"""
你是一个垃圾邮件识别助手。请判断下面这封邮件是否是垃圾邮件，并说明理由。

邮件内容：
{email_text}

请按照以下格式回答：
是否垃圾邮件：是/否
理由：
"""
    response = model.invoke(prompt)
    return response.content
