import qbreader as qb
import pyttsx3 as pyt


def getQuestionFromAL(answerline):
    questionInfo = qb.query(questionType="tossup", searchType="answer", queryString=answerline)
    targetTossups = questionInfo['tossups']['questionArray']

    sanitizedQuestions = []
    for i in range(len(targetTossups)):
        sanitizedQuestions.append(targetTossups[i].get('question'))

    return sanitizedQuestions


def speakQuestion(engine, question):
    engine.say(question)
    engine.runAndWait()
