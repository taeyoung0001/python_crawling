
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# OpenAI 모델 실행
# OpenAI GPT-3.5
from langchain_openai import ChatOpenAI

# model
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125",
                 api_key=OPENAI_API_KEY)

# chain 실행
response = llm.invoke("지구의 자전 주기는?")
response
# Prompt Template 활용
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")

# chain 연결 (LCEL)
chain = prompt | llm

# chain 호출
response = chain.invoke({"input": "지구의 자전 주기는?"})

# 결과 확인
response
# 출력 파서
from langchain_core.output_parsers import StrOutputParser

# prompt + model + output parser
prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
output_parser = StrOutputParser()

# LCEL chaining
chain = prompt | llm | output_parser

# chain 호출
response = chain.invoke({"input": "지구의 자전 주기는?"})

# 결과 확인
response
