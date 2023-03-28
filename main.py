import openai #Fue instalada anteriormente
import config

#config:
#api_key = "api key from https://platform.openai.com/account/api-keys"

openai.api_key = config.api_key

#Contexto del asistente: https://platform.openai.com/docs/guides/chat/introduction
messages = [{"role":"system",
        "content": "Eres un asistente muy util"}] #Se puede acotar mas el contexto

#While para mantener la conversacion
while True:

    content = input('Sobre que quieres hablar?')

    #Break para parar el programa
    if content is "exit":
        break

    #Hacemos que los mensajes sean constantes y se agregue uno tras otro
    messages.append({"role":"user", "content": content})

    #Basandonos en la documentacion: https://platform.openai.com/docs/models/gpt-3-5
    #Esta es la peticion que se le hace a Chat GPT para que responda. La pregunta la enviaremos desde content.
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                messages = messages)

    print(response.choices[0].message.content)