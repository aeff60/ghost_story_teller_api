# สร้าง Ghost Story Generator ด้วย Flask และ OpenAI API

ใน repository นี้จะใช้ Flask ต่อกับ OpenAI API ในการสร้างเรื่องสยองขวัญโดยใช้โมเดลภาษา GPT-3.5-turbo จาก OpenAI โดยผู้ใช้สามารถกำหนดพารามิเตอร์เช่น อาชีพ สาเหตุการตาย สถานที่การตาย และอายุของผู้เสียชีวิตเพื่อกำหนด Prompt ในการสร้างเรื่อง  🌕👻  

## สิ่งที่ควรเช็คก่อนใช้

ก่อนที่จะรัน API ให้เช็คก่อนว่ามีโปรแกรมต่อไปนี้หรือยัง:

- Python (>= 3.6)
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)
- ไลบรารี `dotenv` ของ Python (`pip install python-dotenv`)
- ไลบรารี OpenAI Python (`pip install openai`)

## ขั้นตอนการติดตั้ง

1. โคลน repository นี้ลงในเครื่องของคุณ:

```bash
git clone https://github.com/borntodev/ghost-story-generator.git
```

2. เข้าถึงโฟลเดอร์โปรเจค:

```bash
cd ghost-story-generator
```

3. สร้าง virtual environment (ไม่จำเป็น แต่แนะนำ):

```bash
python -m venv venv
```

4. เปิดใช้งาน virtual environment:

   - บน Windows:

```bash
venv\Scripts\activate
```

   - บน macOS และ Linux:

```bash
source venv/bin/activate
```

5. ติดตั้ง dependencies ที่จำเป็น:

```bash
pip install -r requirements.txt
```

6. สร้างไฟล์ `.env` ในโฟลเดอร์โปรเจคและเพิ่ม OpenAI API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

แทนที่ `your_api_key_here` ด้วย OpenAI API key ของคุณ

## วิธีใช้

1. เริ่มต้นเซิร์ฟเวอร์ Flask:

```bash
python app.py
```

2. แอปพลิเคชันจะสามารถเข้าถึงได้ที่ `http://localhost:5000`.

3. เพื่อสร้างเรื่องสยองขวัญ ส่งคำขอ POST ไปที่ `/result` พร้อมกับ JSON payload ดังนี้:

```json
{
  "occupation": "อาชีพที่นี่",
  "causeOfDeath": "สาเหตุการตายที่นี่",
  "placeOfDeath": "สถานที่การตายที่นี่",
  "deceasedAge": "อายุของผู้เสียชีวิตที่นี่"
}
```

แทนที่ข้อความในเครื่องหมายเร็กเตอร์ (`occupation_here`, `cause_of_death_here`, `place_of_death_here`, และ `deceased_age_here`) ด้วยค่าที่เหมาะสม

4. เซิร์ฟเวอร์จะตอบกลับด้วยออบเจกต์ JSON ที่ประกอบด้วยเรื่องสยองขวัญที่สร้างขึ้น:

```json
{
  "result": "เรื่องสยองขวัญที่สร้างขึ้นที่นี่"
}
```

## สิทธิ์การใช้งาน

โปรเจกต์นี้อยู่ภายใต้ [MIT License](LICENSE).