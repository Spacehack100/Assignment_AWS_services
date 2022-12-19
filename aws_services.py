import boto3
REGION = 'eu-west-1'

def find_dominant_language(text):
    comprehend = boto3.client('comprehend',region_name=REGION)
    response = comprehend.detect_dominant_language(Text=text)
    score = (float(response['Languages'][0]['Score']))*100
    print(f"The text is of language \'{response['Languages'][0]['LanguageCode']}\' with a probability of {score}%.\n")

ExitValue = 0
while ExitValue == 0:
    print('Select the service you want to use?')
    print('1) Find the dominant language in an input string')
    print('2) Find the dominant language in the text.txt file in the same folder as this script')
    print('3) Turn text into speech')
    print('4) Exit')
    choice = int(input('Enter your choice here: '))
    if(choice == 1):
        text = input('Enter the text you want to get the language of: ')
        find_dominant_language(text)
    elif(choice == 2):
        text_file = open("text.txt","r")
        text = text_file.read()
        text_file.close()
        find_dominant_language(text)
    elif(choice == 3):
        inputSpeech = input('Enter the text you want to turn into speech: ')
        polly = boto3.client('polly',region_name=REGION)
        response = polly.synthesize_speech(OutputFormat='mp3',SampleRate='8000',Text=inputSpeech,TextType='text',VoiceId='Joanna')
        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        print("The speech was successfully saved to speech.mp3 in the folder of this script.\n")
    elif(choice == 4):
        ExitValue = 1
    else:
        print('Invalid option, try again.')

    