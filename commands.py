import webbrowser
import os   




def execute_command(text):
    
    text = text.lower()

    if "hello" in text:
        return "Hello! How can I help you today?"

    elif "hi" in text:
        return "Hi there! What can I do for you?"

    elif "open google" in text:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in text:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open youtube" in text:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open chrome" in text:
        os.system("start chrome")
        return "Opening Chrome"

    elif "open notepad" in text:
        os.system("notepad")
        return "Opening Notepad"

    elif "open calculator" in text:
        os.system("calc")
        return "Opening Calculator"

    elif text.startswith("play "):

        song = text.replace("play", "").strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )

        return f"Playing {song}"

    elif text.startswith("open "):

        website = text.replace("open ", "").strip()

        if "." in website:
            url = website
            if not url.startswith("http"):
                url = "https://" + url
        else:
            url = f"https://www.{website}.com"

        webbrowser.open(url)

        return f"Opening {website}"

    return "Command not recognized"