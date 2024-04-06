import google.generativeai as genai
genai.configure(api_key="AIzaSyB2hI2qICRCvHp6cxOIuuCPOFjtUfLmeo0")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is java")
print(response.text)