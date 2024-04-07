from dotenv import load_dotenv
import openai
import os

load_dotenv()

# Securely fetch your OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Open and read file
def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        prompt = file.read().strip()  
    return prompt

# write to file
def write_response_to_file(file_path, response):
    with open(file_path, 'w') as file:
        file.write(response)

# Function to pass in prompt to OpenAi and returns response
def chat_with_gpt(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=100):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message['content'].strip()

# Points to the contents of the original file
article = read_prompt_from_file('input.txt')

# Summarize the article
summaryPrompt = read_prompt_from_file('prompt.txt').replace('<<article>>', article)
summary = chat_with_gpt(summaryPrompt)

# Turn summary into a tweet
tweetPrompt = read_prompt_from_file('tweet.txt').replace('<<twt>>', summary)
tweet = chat_with_gpt(tweetPrompt)
write_response_to_file('response.txt', tweet)