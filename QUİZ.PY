


# QUESTİON
def quiz_app():
    class Question:
        def __init__(self,text,choices,answer):
            self.text = text
            self.choices = choices
            self.answer = answer
        
        def checkAnswer(self,answer):
            return (self.answer == answer)
        


    # QUİZ

    class Quiz:
        def __init__(self,questions):
            self.questions = questions
            self.score = 0
            self.questionIndex = 0

        def getQuestion(self):
            return self.questions[self.questionIndex]

        # soruyu ekrana yazdırır ve cevap alır
        def displayQuestion(self):
            question = self.getQuestion()
            print("-"*30,"\n")
            print(f" soru {self.questionIndex + 1} -- {question.text}  ")

            for i in question.choices:
                print("- "+i)
            print("-"*30)
            answer = input("\ncevap: ")
            self.guess(answer)
            self.loadQuestion()

        # kullanıcının verdiğiği cevap kontrol edilir.
        def guess(self,answer):
            question = self.getQuestion()
            # soru doğru ise score arttırılır
            if question.checkAnswer(answer):
                self.score += 1

            self.questionIndex +=1

        
        # soruyu yeniden yüklemek için
        def loadQuestion(self):
            if len(self.questions) == self.questionIndex:
                self.showScore()
            else:
                self.displayQuestion()

        # skoru göstermek için
        def showScore(self):
            # print("score: ",self.score)
            print("-"*30)
            print(f"{len(questions)} sorudan {self.score} soru doğru.")
            puan  = (100 / len(questions)) * self.score
            print("score: ",round(puan,2))





    q1 = Question("en iyi programlama dili hangisidir?",["c","javascript","python","java"],"python")
    q2 = Question("en popüler programlama dili hangisidir?",["javascript","python","c","java"],"python")
    q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","c","javascript","java"],"python")
    q4 = Question("hangi dil mobil geliştirmede kullanılır?",["python","kotlin","c","R"],"kotlin")
    q5 = Question("hangi dil unity ile oyun geliştirmede kullanılır?",["java","kotlin","c#","go"],"c#")


    questions = [q1,q2,q3,q4,q5]

    quiz = Quiz(questions)

    quiz.displayQuestion()



def mainloop():
    while True:
        print("-"*50)
        print("[1] QUİZ\n[Q] EXİT")
        islem = input("=> ")
        if islem=="1":
           print("----- SORULAR -----")
           quiz_app()
        elif islem=="q" or "Q":
            break
        else:
            print("yanlış işlem")



mainloop()



