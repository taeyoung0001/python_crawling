import openai

api_key : ""
openai.api_key = api_key

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "1+1은 뭐야?"}
  ],
  stream=True
)

result = ""

for chunk in completion:
  delta_data = chunk.choices[0].delta
  if 'role' in delta_data:
    continue
  elif 'content' in delta_data:
    r_tex = delta_data['content']
    result += r_tex
    print(r_tex, end="", flush=True)
print("########")
print(result)