#!/usr/bin/python
import openai
#……. [ mas Código de inicialización aqui ] …………

openai.api_key = "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"
conversation = ""
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"
#i = 1
#…..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
# Set up the model and prompt

#while True (i!=0):
print("Bienvenido a ChatGPT")
while True:
    question = input("You: ")
    try:
        conversation += "\nYou: "+ question + "\nchatGPT: "
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=conversation,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=STOP)
        pregunta = completion.choices[0].text.strip()
        conversation += pregunta
        print("chatGPT: " +pregunta + "\n")
    except Exception as e:
        print("lo siento ha ocurrido un error, Por favor vuelve a intentarlo.")
        pregunta = completion.choices[0].text.strip()



    