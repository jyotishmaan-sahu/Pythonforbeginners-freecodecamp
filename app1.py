from Question import Question1
question_prompts = [
    "What color are apples?\n(a) Red/Green\n (b) purple\n (c)Orange\n\n",
    "what color Bananas?\n (a)Teal\n (b)Magenta\n (c)Yellow\n\n",
    "what color are strawberries?\n (a)Yellow\n (b)Red\n (c)Blue\n\n"
]

questions = [
    Question1(question_prompts[0], "a"),
    Question1(question_prompts[1], "c"),
    Question1(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    print("You Got "+ str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)
