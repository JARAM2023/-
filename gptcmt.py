import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.organization = os.environ.get('OPENAI_ORGANIZATION')

def generate_comment(code):
    prompt = f"This code is {code}."
    max_tokens = 100  # Set the desired length of the generated comment

   #Call the OpenAI API to generate the comment
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[ {"role": "system", "content": "You are a autmatic python comment generator for inputed code. You output only commented phrase in python."},
                  {"role": "user", "content": prompt}],
    )

   #Extract the generated comment from the API response
    comment = response.choices[0].message.content

    return comment