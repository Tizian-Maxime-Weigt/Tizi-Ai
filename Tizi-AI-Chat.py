import time, tiziai
from tiziai import *
from pywebio import start_server,config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import local

message_id = ""

def status():
    try:
        req = tiziai.ChatCompletion.create(model='gpt-3.5-turbo', provider=tiziai.Provider.GetGpt, messages="Hey!", stream=False, temperature=0.5, max_tokens=8192, frequency_penalty=0, top_p=0, parentMessageId=message_id)
        print(f"{req['text']}")
        put_success(f"Tizi-Ai: {req['text']}",scope="body")
    except:
        put_error("Tizi-Ai Fehler",scope="body")

def ask(prompt):

    req = tiziai.ChatCompletion.create(model='gpt-3.5-turbo', provider=tiziai.Provider.GetGpt, messages=prompt, stream=False, temperature=0.5, max_tokens=8192, frequency_penalty=0, top_p=0, parentMessageId=message_id)
    
    rp=req['text']

    local.message_id=req["id"]

    print("Tizi-Ai\n"+rp)

    local.conversation.extend([{"role": "user", "content": prompt},{"role": "assistant", "content": rp}])
    print(local.conversation)
    return rp

def msg():
    while True:
        text= input_group("Du:",[textarea('DU：',name='text',rows=3, placeholder='Hier Prompt / Frage')])

        if not(bool(text)):
            break

        if not(bool(text["text"])):
            continue

        put_code("Du："+text["text"],scope="body")

        print("Frage："+text["text"])

        with use_scope('foot'):put_loading(color="info")

        rp= ask(text["text"])

        clear(scope="foot")

        put_markdown("Tizi-Ai:\n"+rp,scope="body")

@config(title="Tizi-Ai Chat",theme="dark")
def main():
    put_scope("heads")

    with use_scope('heads'):

        put_html("<h1><center>Tizi-Ai Chat</center></h1>")

    put_scope("body")

    put_scope("foot")

    status()

    local.conversation=[]

    local.message_id=""

    msg()

start_server(
    main, 
    port=8099,
    allowed_origins="*",
    auto_open_webbrowser=False,debug=False
)
