import streamlit as st

# Define the questions for the quiz
questions = [
    {
        "question": "Which of the following choices is the correct IUPAC name for the molecule below?",
        "options": ["3-ethyl-4,4-dimethylheptane", "4,4-bimethyl-3-ethylheptane", "5-ethyl-4,4-dimethylheptane", "4,4-dimethyl-3-ethylheptane"],
        "correct_answer": "3-ethyl-4,4-dimethylheptane",
        "image": "1.png"
    },
    {
        "question": "What is the functional group in an alcohol molecule?",
        "options": ["-OH", "-COOH", "-NH2"],
        "correct_answer": "-OH"
    },
    {
        "question": "What is the IUPAC name of CH3CH2OH?",
        "options": ["Methanol", "Ethanol", "Propanol"],
        "correct_answer": "Ethanol",
        #"image": "assets/molecule2.png"
    }
]

# Function to display the quiz questions and collect responses
def display_quiz(questions):
    responses = []
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question['question']}")
        if 'image' in question:
            st.image(question['image'], use_column_width=True)
        user_response = st.radio("Choose an option:", question['options'], key=i)
        responses.append(user_response)
    return responses

# Function to grade the quiz and display results
def grade_quiz(questions, responses):
    correct_answers = [question['correct_answer'] for question in questions]
    num_correct = sum([1 for user_resp, correct_resp in zip(responses, correct_answers) if user_resp == correct_resp])
    total_questions = len(questions)
    st.write(f"You got {num_correct} out of {total_questions} questions correct!")

# Main Streamlit app
def main():
    st.title("Organic Chemistry Quiz: Nomenclature & Functional Groups")
    st.write("Test your knowledge of organic chemistry!")

    # Display the quiz questions
    responses = display_quiz(questions)

    # Submit button
    submitted = st.button("Submit")

    if submitted:
        # Grade the quiz and display results
        st.subheader("Quiz Results")
        grade_quiz(questions, responses)

if __name__ == "__main__":
    main()
