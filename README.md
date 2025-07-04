🎓 B.Tech Computer Science Exam Assistant 🤖
A command-line AI assistant to supercharge your B.Tech Computer Science exam preparation!
Get concise summaries, active recall questions, and smart revision prompts—powered by OpenAI’s GPT models.

✨ Features
📝 Custom Topic Support: Enter any CS subject & topic (e.g., Data Structures: Trees)

📚 Concise Summaries: Clear, easy-to-understand explanations (max 150 words)

🧠 Active Recall: Three questions of increasing difficulty to test your understanding

🔄 Next-Step Guidance: Get more questions, a mnemonic, or switch topics

🙋 Polite Clarification: Asks for more details if your input is vague

🚀 Getting Started
Prerequisites
Python 3.7 or higher

An OpenAI API key (get yours here)

Installation
Clone this repository:

bash
git clone https://github.com/your-username/cs-exam-assistant.git
cd cs-exam-assistant
Install dependencies:

bash
pip install openai
Add your OpenAI API key:

Open cs_exam_assistant.py

Replace 'your-api-key' with your actual OpenAI API key

🖥️ Usage
Run the assistant:

bash
python cs_exam_assistant.py
Example:

text
Please enter your subject and topic (e.g., 'Data Structures: Trees'):
Data Structures: Trees

[Assistant generates a summary, three questions, and a next-step prompt]
🔒 Security
Never upload your OpenAI API key to GitHub or share it publicly!
Consider using environment variables or a .env file (add .env to .gitignore).

🎯 Example Output
text
Subject: Data Structures
Topic: Trees

Conceptual Summary:
Trees are hierarchical data structures consisting of nodes connected by edges...

Active Recall Questions:
1. What is the root node in a tree? (Easy)
2. Explain the difference between preorder and postorder traversal. (Medium)
3. How does a binary search tree maintain its order during insertion? (Hard)

Would you like more questions, a mnemonic, or to switch topics?
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


Happy studying and good luck with your exams! 🚀📚
