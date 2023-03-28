import openai #Fue instalada anteriormente
import config

openai.api_key = config.api_key

#Basandonos en la documentacion: https://platform.openai.com/docs/models/gpt-3-5
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                            messages = [{"role":"user", "content":"Cual es la mision de OpenAI?"}]) #

print(response.choices[0].message.content)