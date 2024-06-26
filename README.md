# Article-to-Tweet

## Introduction
Article-to-Tweet is a Python-based project designed to automate the process of summarizing text and posting it to Twitter. Utilizing the power of OpenAI's GPT models, this bot reads input from text files, generates concise summaries, and tweets them out, making it an excellent tool for sharing insights and information efficiently on social media.

## Setup Instructions

### Requirements
- Python 3.6+
- OpenAI API Key

### Installation
1. Clone the repository:
```bash
git clone https://github.com/darekbtw/Article-to-Tweet.git
```

2. Navigate to the project directory:
```bash
cd Summary2Tweet.py
```

3. Set up your .env file for the OpenAi API:
You will create a file called .env and put in OPENAI_API_KEY = 'your-API-key'

4. Paste in your article into the input.txt file that you want to summarize and turn into a tweet.

5. Run the program
```bash
python Summary2Tweet.py
```

6. Open the response.txt file to see your tweet.