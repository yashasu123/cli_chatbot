#v2.1
# from app.services.ollama_Service import OllamaService
# from app.memory.conversation_memory import ConversationMemory

# obj=OllamaService()
# memory = ConversationMemory()

# while True:
#     i=input("Hi,WELCOME let's chat but to exit-> press Enter: ")
#     if not i :
#         break

#     memory.add_message("user", i)
#     messages = memory.get_messages()
#     prompt = ""

#     for message in messages:
#         prompt+=f"{message['role']}:{message['content']}\n"
    
#     asst=obj.generate(prompt)
#     memory.add_message("assistant", asst)
#     print(asst)

#v2.2
from app.services.ollama_Service import OllamaService
from app.memory.database import Database


ollama = OllamaService()

db = Database()
db.create_tables()

while True:

    user_input = input("You: ")

    if not user_input:
        break

    # Save user message
    db.save_message("user", user_input)

    # Get conversation history
    messages = db.get_messages()  #returns list of tuples

    # Build prompt
    prompt = ""

    for role, content in messages:
        prompt += f"{role}: {content}\n"

    # Get response from Ollama
    response = ollama.generate(prompt)

    # Save assistant response
    db.save_message("assistant", response)

    print("Bot:", response)










