questions = (
    ("What is the capital of Pakistan?",("Peshawar",  "Karachi", "Islamabad" , "Lahore"), "Islamabad"),
    ("What is the largest city in Pakistan?",(" Peshawar", "Lahore", "Karachi",  "Quetta"),"Karachi"),
    ("Who wrote the national anthem of Pakistan?",("Allama Muhammad Iqbal", "Faiz Ahmad Faiz", "Hafeez Jalandhari",  "Abdul Rab Nishtar"),"Hafeez Jalandhari"),
    ("What is the national language of Pakistan?", ("English",  "Punjabi","Urdu","Pushto"), "Urdu"),
    ("What is the currency used in Pakistan?", ("Rupee","Dollar", "Euro", "Pound"),"Rupee"),
    ("Who is the current Prime Minister of Pakistan?",("Nawaz Sharif", "Bilawal Bhutto", "Imran Khan","Shehbaz Sharif"), "Shehbaz Sharif"),
    ("When did Pakistan gain independence from the British?",("14 August 1947", "15 August 1947", "16 August 1947", "17 August 1947"),"14 August 1947"),
    ("What is the name of the highest peak in Pakistan?",("Nanga Parbat", "K2", "Tirich Mir", "Broad Peak"),"K2")
    
)


def present_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def capture_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if answer in (1, 2, 3, 4):
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_score(user_answers):
    score = 0
    for i, (question, options, correct_answer) in enumerate(questions):
        if options[user_answers[i] - 1] == correct_answer:
            score += 1
    return score

def run_quiz():
    user_answers = []
    for question, options, correct_answer in questions:
        present_question(question, options)
        answer = capture_answer()
        user_answers.append(answer)
    
    score = calculate_score(user_answers)
    print(f"Your score is {score} out of {len(questions)}.")


if __name__ == "__main__":
    run_quiz()



