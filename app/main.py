from app.services.ollama_Service import OllamaService
obj=OllamaService()
while True:
    i=input("Hi,WELCOME let's chat but to exit-> press Enter: ")
    if i=="" :
        exit()

    else:
        print(obj.generate(i))

