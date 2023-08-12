import os
from dotenv import load_dotenv
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/result", methods=['POST'])
def generate_story():
    data = request.get_json()
    occupation = data.get('occupation', '')
    cause_of_death = data.get('causeOfDeath', '')
    place_of_death = data.get('placeOfDeath', '')
    deceased_age = data.get('deceaseAge', '')

    prompt = f'ตั้งชื่อเรื่อง (เว้นบรรทัด) และเล่าเรื่องผีให้น่ากลัวจากการใช้คำเหล่านี้: ผู้ตายเป็น{occupation}ตายเพราะ{cause_of_death}เสียชีวิตที่{place_of_death}ด้วยอายุ{deceased_age}ปี'

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "You are a helpful assistant"
            },
            {
                "role" : "user",
                "content" : prompt,
            }
        ]
    )

    result = response['choices'][0]['message']['content']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)