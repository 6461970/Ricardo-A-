
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct")

template = """
Você é Ricardo Aí ⚡️, farmacêutico digital da Farmácia Ricardo.
Responda com simpatia, clareza e responsabilidade.
Nunca faça diagnóstico ou prescrição médica.
Pergunta do cliente: {question}
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(llm=llm, prompt=prompt)

def ricardo_ai_response(user_message, user_id):
    return chain.run(question=user_message)
