import openai
import os
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("OpenAI API Key is missing!")

def chatbot_ui(request):
    return render(request, 'chatbot/chatbot.html')

@api_view(['POST'])
def chat_with_gpt(request):
    user_message = request.data.get('message', '')

    if not user_message:
        return Response({'error': 'Message is required', 'status':False})

    try:
        print(f' User message: {user_message}')  

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        print(f'User message: {user_message}')  

        bot_reply = response['choices'][0]['message']['content']
        return Response({'reply': bot_reply, 'status':False, 'message': 'Success'})

    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")  
        return Response({'status':False,'message': str(e), 'data': {}})
