import openai #pip install openai
import config #api_key = "api key from https://platform.openai.com/account/api-keys"

#Interactive apps in terminal. https://typer.tiangolo.com/
import typer #pip install "typer[all]"

from rich import print #Improve visuals. pip install rich
from rich.table import Table

#Main function
def main():

#Open AI API Key. taken from open ai website:
    openai.api_key = config.api_key

#Main menu and welcome message to user
    print("")
    print("💬 [bold green]Hi! Here you can interact with Chat GPT[/bold green]")
    print("")
    print("Instructions")
    print("")

#Table of commands
    table = Table("comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicacion")
    table.add_row("new", "Crear una nueva conversacion")

    print(table)
    print("")

    #Roles: https://platform.openai.com/docs/guides/chat/introduction

    #Assistant context
    context = {"role":"system",
            "content": "Eres un asistente muy util"} #Se puede acotar mas el contexto
    messages = [context]

    #While to keep conmversation contexts
    while True:

        content = __promt()

        #Start messages again
        if content == "new":
            print('Nueva conversacion')
            messages = [context]
            content = __promt()

        #Save context of message sent by user. Save messages in line
        messages.append({"role":"user", "content": content})

        #Documentation: https://platform.openai.com/docs/models/gpt-3-5
        #Request to Chat GPT. Question is in mesage.
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages = messages)

        #In all response, locate only the message
        response_content = response.choices[0].message.content

        #Context of chat GPT answers. Saved in assistant role
        messages.append({"role":"assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

#Function to manage user response and exit
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