try:
    # Try to open the files
    f = open("questions.txt","r")
    g = open("answers.txt", "r")
    f.close()
    g.close()
except:
    # So. The files needed to be created.
    f = open("questions.txt","x")
    g = open("answers.txt","x")
    f.close()
    g.close()

# Add to file
while True:
    question = input("Question: ")
    answer = input("Answer: ")
    if question == "" or answer == "":
        break
    else:
        f = open("questions.txt", "a")
        g = open("answers.txt", "a")
        f.write(question+"\n")
        g.write(answer+"\n")
        f.close()
        g.close()

quit()