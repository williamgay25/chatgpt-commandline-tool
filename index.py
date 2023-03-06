import os
import openai
from dotenv import load_dotenv

## Load environment variables
load_dotenv()

## Set up prompt
prompt = "Imagine you a macOS operating system. Your purpose is to answer my questions with the corresponding terminal command when I ask you for one. Just respond with the command and nothing else."
question = "Create a directory name python, move into it, create a file name index.py, and start a .venv"

## Execute a command line function
def execute(cmd):
    os.system(cmd)

class OpenAI:
    def __init__(self) -> None:
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"
        self.organization = "org-YO7yz6T8iWfq2HCv5VxY7DLd"

        openai.organization = self.organization
        openai.api_key = self.api_key

    def create(self, prompt, temp = 0.3, freq_penalty = 0.3, pres_penalty = 0.2, max_tokens = 4000, model = None):
        response = openai.ChatCompletion.create(
            model = self.model if model is None else model,
            messages = [{"role": "user", "content": prompt}],
            temperature = temp,
            max_tokens = max_tokens,
            top_p = 1.0,
            frequency_penalty = freq_penalty,
            presence_penalty = pres_penalty
        )

        result = response.choices[0].message.content
        return result.strip()

## Main function
def main():
    openai = OpenAI()
    cmd = openai.create(prompt + " " + question)
    print(cmd)
    execute(cmd)


## Execute main function
main()