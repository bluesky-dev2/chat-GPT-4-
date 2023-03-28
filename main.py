import openai #Fue instalada anteriormente
import config

#config:
#api_key = "api key from https://platform.openai.com/account/api-keys"

openai.api_key = config.api_key

#Roles: https://platform.openai.com/docs/guides/chat/introduction

#Contexto del asistente
messages = [{"role":"system",
        "content": "Eres un asistente muy util"}] #Se puede acotar mas el contexto

#While para mantener la conversacion
while True:

    content = input('Sobre que quieres hablar?')

    #Break para parar el programa
    if content == "exit":
        break

    #Hacemos que los mensajes sean constantes y se agregue uno tras otro. Guarda el contexto del mensaje enviado por el usuario.
    messages.append({"role":"user", "content": content})

    #Basandonos en la documentacion: https://platform.openai.com/docs/models/gpt-3-5
    #Esta es la peticion que se le hace a Chat GPT para que responda. La pregunta la enviaremos desde content.
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                messages = messages)

    response_content = response.choices[0].message.content


    #contexto de las respuestas que el mismo chatgpt ha dado. Se guarda en el rol de asistente precisamente por eso
    messages.append({"role":"assistant", "content": response_content})

    print(response_content)