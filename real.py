import datetime


exams = {
    "dsa": datetime.date(2025, 12, 12),
    "dec": datetime.date(2025, 12, 16),
    "oops": datetime.date(2025, 12, 18),
    "python": datetime.date(2025, 12, 22),
    "maths": datetime.date(2025, 12, 24),
    "cle": datetime.date(2025, 12, 26)
}

print("Exam Helper Chatbot")
print("Type 'help' for commands or 'byee' to quit.\n")

while True:
    user = input("You: ").lower()

    if user in ["byee", "bye"]:
        print("Bot: Goodbye!")
        break

    elif any(greet in user for greet in ["hi", "hello", "hey"]):
        print("Bot: Hello! How can I help you?")

    elif "time" in user:
        print("Bot: Current time:", datetime.datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        print("Bot: Today's date:", datetime.date.today().strftime("%d-%m-%Y"))

    elif "schedule" in user or "timetable" in user:
        print("Bot: Exam Timetable:")
        for sub, dt in exams.items():
            print(f"- {sub.upper()} : {dt.strftime('%d-%m-%Y')}")

    elif "when" in user and "exam" in user:
        found = False
        for sub in exams:
            if sub in user:
                print(f"Bot: {sub.upper()} exam is on {exams[sub].strftime('%d-%m-%Y')}")
                found = True
                break
        if not found:
            print("Bot: Please mention subject name like 'When is DSA exam?'")

    elif "days left" in user or ("how many" in user and "days" in user):
        found = False
        for sub, date in exams.items():
            if sub in user:
                diff = (date - datetime.date.today()).days
                print(f"Bot: {diff} days left for {sub.upper()} exam.")
                found = True
                break
        if not found:
            print("Bot: Please mention subject name like 'Days left for OOPS?'")

    elif "help" in user:
        print("Bot: You can ask like:")
        print("- What is the time?")
        print("- What is the date?")
        print("- Show schedule")
        print("- When is DSA exam?")
        print("- Days left for Python exam?")

    else:
        print("Bot: I didn't understand. Type 'help'.")
