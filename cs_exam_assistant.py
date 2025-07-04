import openai
openai.api_key = 'your-api-key'

def generate_summary_and_questions(subject: str, topic: str):
 
    prompt = f"""
You are an expert assistant for B.Tech Computer Science students preparing for exams.

Subject: {subject}
Topic: {topic}

1. First, clearly identify the subject and topic.
2. Provide a short conceptual summary (max 150 words) explaining the topic in simple, easy-to-understand language.
3. Generate three active recall questions of increasing difficulty to test understanding:
   - Question 1: Easy
   - Question 2: Medium
   - Question 3: Hard
4. End with a clear next step prompt asking the student if they want:
   - More questions on the same topic
   - A mnemonic to remember the topic better
   - Or to switch to a new topic for revision

Format your response with clear headings and numbered questions. Maintain an encouraging and confident tone.

Response:
"""
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def assistant():
    print("Welcome to your B.Tech Computer Science Exam Assistant!")
    while True:
        user_input = input("\nPlease enter your subject and topic (e.g., 'Data Structures: Trees') or type 'exit' to quit:\n").strip()
        if user_input.lower() == 'exit':
            print("Good luck with your studies! Keep up the great work!")
            break

        
        if ':' in user_input:
            subject, topic = map(str.strip, user_input.split(':', 1))
            if not subject or not topic:
                print("Please provide both subject and topic clearly, separated by a colon. For example: 'Data Structures: Trees'")
                continue
        else:
            
            print("Please specify the subject along with the topic for better assistance. For example: 'Data Structures: Trees'")
            continue

        print("\nGenerating your study summary and questions...\n")
        output = generate_summary_and_questions(subject, topic)
        print(output)

if __name__ == "__main__":
    assistant()
