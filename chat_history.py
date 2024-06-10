class ChatHistory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_context(self):
        context = ""
        for message in self.history:
            if message["role"] == "user":
                context += f"User: {message['content']}\n"
            elif message["role"] == "assistant":
                context += f"Assistant: {message['content']}\n"
        return context

    def clear_history(self):
        self.history = []