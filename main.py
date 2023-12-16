from tkinter import *
from tkinter import scrolledtext
from openai import OpenAI


class Tutor:
    def __init__(self, master):
        self.master = master
        master.title('Programming Tutor')
        master.configure(bg="#A2B9B9")

        self.chat_log = scrolledtext.ScrolledText(root, width=60, height=20, wrap=WORD, bg="#ECECE9")
        self.chat_log.pack(padx=10, pady=10)

        self.chat_input = scrolledtext.ScrolledText(root, width=45, height=4, wrap=WORD, bg="#ECECE9")
        self.chat_input.pack(side=LEFT, padx=20, pady=10)

        self.btn_send = Button(root, text="Send", command=self.show_response, height=2, width=8)
        self.btn_send.pack(side=RIGHT, padx=20, pady=10)

    def get_chatbot_response(self, input_text):
        client = OpenAI(api_key="YOUR_API_KEY")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a tutor who is an expert in all programming related things. You should answer questions that are programming related."},
                      {"role": "user", "content": input_text}],
        )
        return response.choices[0].message.content

    def show_response(self):
        self.chat_log.tag_config('chatbotresponse', foreground="#086788")
        user_input = self.chat_input.get("1.0", END).strip()
        self.chat_input.delete("1.0", END)
        self.chat_log.insert(END, "You: " + user_input + "\n")
        if user_input.lower() in ["exit", "quit", "bye"]:
            self.chat_log.insert(END, "Tutor: Goodbye!\n", 'chatbotresponse')
            return
        chatbot_response = self.get_chatbot_response(user_input)
        self.chat_log.insert(END, "Tutor: " + chatbot_response + "\n", 'chatbotresponse')

root = Tk()
mygui = Tutor(root)
root.mainloop()