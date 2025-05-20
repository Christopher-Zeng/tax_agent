from agents.spam_checker import SpamCheckAgent
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

google_api_key = os.getenv("GOOGLE_API_KEY")
# 测试样本文本
sample_email = """
Congratulations! You've been selected for a limited-time prize!
Click the link below to claim your reward.
"""

if __name__ == "__main__":
    agent = SpamCheckAgent(google_api_key)
    result = agent.run(sample_email)
    print("检测结果：\n", result)
