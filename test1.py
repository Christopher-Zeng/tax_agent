from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

google_api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # ✅ 可换成 gemini-2.5-flash-preview-04-17 等
    api_key = google_api_key
)

prompt = "请判断以下邮件是否是垃圾邮件：You've won $1000! Click here to claim."
response = llm.invoke(prompt)
print(response.content)
