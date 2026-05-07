questions = [
    
    [
        "What is the capital of India?", "Mumbai", "Kolkata", "New Delhi", "Chennai", 3
    ],
    [
        "Who is know as the father of the Nation in India?", "Subhas Chandra Bose", "Jawaharlal Nehru" ,"Mahatma Gandhi", "Sardar Patel", 3
    ],
    [
        "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3
    ],
    [
        "How many continents are there in the world?", "5", "6", "7", "8", 3
    ],
    [
        "Who invented the telephone?", "Thomas Edison","Alexander Graham Bell", "Lsaac Newton", "Albert Einstein", 2
    ],
    [
        "What is the national animal of India?", "Lion", "Elephant", "Tiger","Peacook", 3
    ],
    [
        "Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4
    ],
    [
        "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3
    ],
    [
        "How many continents are there in the world?", "5", "6", "7", "8", 3
    ],
    [
        "Who invented the telephone?", "Thomas Edison","Alexander Graham Bell", "Lsaac Newton", "Albert Einstein", 2
    ],
    [
        "What is the national animal of India?", "Lion", "Elephant", "Tiger","Peacook", 3
    ],
    [
        "Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4
    ]

]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 10000000]

money = 0

for i in range (0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}") 
    print(f" a. {question[1]}     b. {question[2]}")
    print(f"c.  {question[3]}     d. {question[4]}")
    reply = int(input("entery your answer (1-4)  "))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 100000
        elif(i == 5):
            money = 320000
    else:
        print("Wrong answer")
        break

print(f"Your won money is {money}")