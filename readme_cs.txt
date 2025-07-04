B.Tech Computer Science Exam Assistant
A command-line AI assistant to help B.Tech Computer Science students prepare for exams using active recall and concise conceptual summaries. Powered by OpenAI’s GPT models, this tool generates simple explanations and tailored questions for any CS topic you provide.

Features
Custom topic support: Enter any subject and topic (e.g., Data Structures: Trees)

Concise summaries: Get a clear, easy-to-understand explanation (max 150 words)

Active recall questions: Three questions of increasing difficulty to test your understanding

Next-step guidance: Choose to get more questions, a mnemonic, or switch topics

Polite clarification: Asks for more details if your input is vague

Getting Started
Prerequisites:

Python 3.7 or higher

An OpenAI API key (get one at https://platform.openai.com/api-keys)

Installation:

Clone the repository:
git clone https://github.com/your-username/cs-exam-assistant.git
cd cs-exam-assistant

Install dependencies:
pip install openai

Add your OpenAI API key:

Open cs_exam_assistant.py

Replace 'your-api-key' with your actual OpenAI API key

Usage
Run the assistant with:
python cs_exam_assistant.py

Example interaction:
Please enter your subject and topic (e.g., 'Data Structures: Trees'):
Data Structures: Trees

[Assistant generates a summary, three questions, and a next-step prompt]

Security
Never upload your OpenAI API key to GitHub or share it publicly!
Consider using environment variables or a .env file (add .env to .gitignore).

Example Output
Subject: Data Structures
Topic: Trees

Conceptual Summary:
Trees are hierarchical data structures consisting of nodes connected by edges...

Active Recall Questions:

What is the root node in a tree? (Easy)

Explain the difference between preorder and postorder traversal. (Medium)

How does a binary search tree maintain its order during insertion? (Hard)

Would you like more questions, a mnemonic, or to switch topics?

Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.