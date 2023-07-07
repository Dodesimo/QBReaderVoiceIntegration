import helperfunctions as hf
import pyttsx3 as pyt

def main():
    engine = pyt.init()
    tossups = hf.getQuestionFromAL("India")
    hf.speakQuestion(engine, tossups[0])


if __name__ == "__main__":
    main()
