import openai
import time
import re

#unique key for api requests
openai.api_key = ''

#api request instructions
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 128,
        temperature = 0.5,
        n = 1,
        stop = None
    )

    #index selection of the responses generated by ChatGPT; choosing the first one
    if response.choices:
        lines = response.choices[0].text.split('\n')
        lines[0] = lines[0].replace(', and',',')
        lines[1] = lines[1].replace(', and',',')
        lines[0] = lines[0].replace(',',' +')
        lines[1] = lines[1].replace(',',' +')
        output = '\n'.join(lines)
        output = re.sub(r'Instructions.*', '', output, re.DOTALL)
        output = re.sub(r'\n\d.*', '', output, re.DOTALL)
        return output
    else:
        return None

#prompt script
while True:
    text_input = "salt, pepper, oregano, garlic"    #line for detected ingredients
    prompt = f"Please make a recipe from the following list of ingredients: {text_input}\nAI: "

    chapt_gpt_response = chat_with_gpt(prompt)
    print(chapt_gpt_response)

    if chapt_gpt_response is None:
        print("I am sorry I didn't quite catch those ingredients, please try again in 20 seconds.")
    
    rest = 21   #rest statement included to avoid going over open ai request limit
    time.sleep(rest) 
