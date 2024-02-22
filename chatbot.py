from openai import OpenAI
client = OpenAI()

start_chat_log = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def askgpt(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    chat_log = chat_log + [{'role': 'user', 'content': question}]
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    
    answer = completion.choices[0].message.content
    chat_log = chat_log + [{'role': 'assistant', 'content': answer}]
    
    return answer, chat_log
  

