import openai
from googletrans import Translator  # googletrans==4.0.0-rc1
from functions import engine_say

trans = Translator()
openai.api_key = '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'


def gpt3(prompt, engine='text-davinci-002', response_length=300,
         temperature=0.9, top_p=1, frequency_penalty=0, presence_penalty=0.6,
         start_text='', restart_text='', ):  # stop_seq=[]
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        # stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt


# Quanto maior o prompt maior vai ser o gasto de tokens
def GPT3(fala):
    prompt = """

"""
    print('...')
    while True:
        print(f'Voce: {fala}')

        prompt += fala
        answer, prompt = gpt3(prompt,
                              temperature=0.9,
                              frequency_penalty=0,
                              presence_penalty=0.8,
                              top_p=1,
                              start_text='\nEva:',
                              restart_text='\nVoce: ')
        resposta = trans.translate(answer, dest='pt').text
        print('Eva: ' + resposta)
        engine_say(resposta)
        return resposta


if __name__ == "__main__":
    while True:
        GPT3(input('...'))
