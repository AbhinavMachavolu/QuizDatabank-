import streamlit as st

# Define the questions for the quiz with explanations for wrong answers
questions = [
    {
        "question": "Which of the following choices is the correct IUPAC name for the molecule below?",
        "options": ["3-ethyl-4,4-dimethylheptane", "4,4-bimethyl-3-ethylheptane", "5-ethyl-4,4-dimethylheptane", "4,4-dimethyl-3-ethylheptane"],
        "correct_answer": "3-ethyl-4,4-dimethylheptane",
        "explanation": "The correct IUPAC name for the given structure follows the longest carbon chain with substituents numbered to give the lowest numbers. In this case, the ethyl group (3 carbons) gets preference over the two methyl groups (each 2 carbons). Hence, the correct answer is '3-ethyl-4,4-dimethylheptane'."
    },
    {
        "question": "What is the functional group in an alcohol molecule?",
        "options": ["-OH", "-COOH", "-NH2"],
        "correct_answer": "-OH",
        "explanation": "The functional group in an alcohol molecule is the hydroxyl group (-OH), which consists of an oxygen atom bonded to a hydrogen atom. This group is responsible for the characteristic properties of alcohols."
    },
    {
        "question": "What is the IUPAC name of CH3CH2OH?",
        "options": ["Methanol", "Ethanol", "Propanol"],
        "correct_answer": "Ethanol",
        "explanation": "The IUPAC name of CH3CH2OH is 'Ethanol'. Ethanol consists of two carbon atoms (eth-) bonded to a hydroxyl group (-anol)."
    }
]

# Function to display the quiz questions and collect responses
def display_quiz(questions):
    responses = []
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question['question']}")
        user_response = st.radio("Choose an option:", question['options'], key=i)
        responses.append(user_response)
    return responses

# Function to grade the quiz and display results with explanations for wrong answers
def grade_quiz(questions, responses):
    correct_answers = [question['correct_answer'] for question in questions]
    num_correct = 0
    st.subheader("Quiz Results")
    for i, (user_resp, correct_resp) in enumerate(zip(responses, correct_answers)):
        st.write(f"Question {i+1}: {questions[i]['question']}")
        st.write(f"Your answer: {user_resp}")
        st.write(f"Correct answer: {correct_resp}")
        if user_resp == correct_resp:
            num_correct += 1
            st.write("Correct!")
        else:
            st.write("Incorrect!")
            st.write("Explanation:")
            # Provide explanations for wrong answers
            if 'explanation' in questions[i]:
                st.write(questions[i]['explanation'])
            else:
                st.write("Sorry, no explanation available.")
        st.write("---")
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
        grade_quiz(questions, responses)

if __name__ == "__main__":
    main()
