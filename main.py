import openai #Fue instalada anteriormente
import config #api_key = "api key from https://platform.openai.com/account/api-keys"

import typer #Crear apps un poco mas interactivas en la terminal. https://typer.tiangolo.com/
from rich import print #Libreria para mejorar visuales
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("")
    print("💬 [bold green]Hola! Aca podras interactuar con Chat GPT[/bold green]")
    print("")
    print("Instrucciones")
    print("")


    table = Table("comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicacion")
    table.add_row("new", "Crear una nueva conversacion")

    print(table)
    print("")

    #Roles: https://platform.openai.com/docs/guides/chat/introduction

    #Contexto del asistente
    context = {"role":"system",
            "content": "Eres un asistente muy util"} #Se puede acotar mas el contexto
    messages = [context]

    #While para mantener la conversacion
    while True:

        content = __promt()

        #Volver a iniciar los mensajes
        if content == "new":
            print('Nueva conversacion')
            messages = [context]
            content = __promt()

        #Hacemos que los mensajes sean constantes y se agregue uno tras otro. Guarda el contexto del mensaje enviado por el usuario.
        messages.append({"role":"user", "content": content})

        #Basandonos en la documentacion: https://platform.openai.com/docs/models/gpt-3-5
        #Esta es la peticion que se le hace a Chat GPT para que responda. La pregunta la enviaremos desde content.
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages = messages)

        response_content = response.choices[0].message.content

        #contexto de las respuestas que el mismo chatgpt ha dado. Se guarda en el rol de asistente precisamente por eso
        messages.append({"role":"assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

#Funcion para manejar la respuesta del usuario y salida
def __promt() -> str:
    prompt = typer.prompt("\nSobre que quieres hablar?") #\n salto de linea

    if prompt == "exit":
        exit = typer.confirm("🛑Seguro que quieres salir?🛑")
        if exit:
            print("Taluego!")
            raise typer.Abort()

        return __promt()

    return prompt

if __name__ == "__main__":
    typer.run(main)