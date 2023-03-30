import openai #pip install openai
import config #api_key = "api key from https://platform.openai.com/account/api-keys"

#Interactive apps in terminal. https://typer.tiangolo.com/
import typer #pip install "typer[all]"

from rich import print #Improve visuals. pip install rich
from rich.table import Table

#Main function
def main():

    # Language menu
    print("[bold white]Hi! Here you can interact with Chat GPT[/bold white]")
    print("[bold green]But first, choose a Language:[/bold green]")
    idiomas = {
        "ES": "Español",
        "EN": "English",
        "FR": "Francais"
    }
    opciones_idiomas = "\n".join([f"- {idioma}" for idioma in idiomas.keys()])

    #while loop to verify language
    while True:
        opciones_idiomas = "\n".join([f"- {idioma}" for idioma in idiomas.keys()])
        seleccion_idioma = typer.prompt(f"{opciones_idiomas}\n").upper()

        # Verificar selección de idioma
        if seleccion_idioma in idiomas:
            break

        # Logic if language is not valid
        elif seleccion_idioma.lower() in idiomas.values():
            for key, value in idiomas.items():
                if value.lower() == seleccion_idioma.lower():
                    seleccion_idioma = key
                    break
            break
        else:
            print("[bold red]Error:[/bold red] Idioma no válido. Por favor ingresa un idioma válido.\n")

    #Open AI API Key. taken from open ai website:
    openai.api_key = config.api_key

    #Main menu and welcome message to user
    print("")
    print(f"💬 [bold green]Now you can interact with Chat GPT in {idiomas[seleccion_idioma]}[/bold green]")
    print("Instructions")
    print("")

    #Table of commands
    table = Table("Command", "Description")
    table.add_row("exit", "Exit app")
    table.add_row("new", "Create a new conversation")
    table.add_row("cl", "Change Language")

    print(table)
    print("")

    #Roles: https://platform.openai.com/docs/guides/chat/introduction

    #Assistant context
    context = {"role":"system",
            "content": f"Eres un asistente muy util en {idiomas[seleccion_idioma]}"} #Se puede acotar mas el contexto
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
    prompt = typer.prompt("\nWhat do you want to talk about?") #\n salto de linea

    if prompt == "exit":
        exit = typer.confirm("🛑Are you sure you want to exit?🛑")
        if exit:
            print("Bye!")
            raise typer.Abort()

        return __promt()

    return prompt

if __name__ == "__main__":
    typer.run(main)