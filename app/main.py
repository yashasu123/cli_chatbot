from app.services.ollama_Service import OllamaService
from app.memory.conversation_memory import ConversationMemory

obj=OllamaService()
memory = ConversationMemory()

while True:
    i=input("Hi,WELCOME let's chat but to exit-> press Enter: ")
    if not i :
        break

    memory.add_message("user", i)
    messages = memory.get_messages()
    prompt = ""

    for message in messages:
        prompt+=f"{message['role']}:{message['content']}\n"
    
    asst=obj.generate(prompt)
    memory.add_message("assistant", asst)
    print(asst)











