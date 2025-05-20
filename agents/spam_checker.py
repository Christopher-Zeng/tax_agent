from tools.spam_tool import init_model, detect_spam

class SpamCheckAgent:
    def __init__(self, api_key):
        self.model = init_model(api_key)

    def run(self, email_text):
        result = detect_spam(self.model, email_text)
        return result
