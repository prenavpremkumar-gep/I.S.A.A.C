import wikipedia
import wolframalpha
from Speech import chat_speak
import wikia

def websearch(string):
    try:
        #wolframalpha
        app_id = "2977GH-AH3R25WXXJ"
        client = wolframalpha.Client(app_id)
        res = client.query(string)
        answer = next(res.results).text
        print("wolf answer:\n"+answer)
        chat_speak(answer)
    except:
        #wikipedia
        answer = wikipedia.summary(string, sentences=4)
        print("wiki answer: \n" + answer)
        chat_speak(answer)
