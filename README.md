import os
from openai import OpenAI

# O sistema busca a chave que você guardou no 'Cofre' (Secrets) do GitHub
api_key_protegida = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key_protegida)

def responder_cliente_ricardo(mensagem_cliente):
    """
    Esta função envia a pergunta do cliente para a Inteligência Artificial
    e retorna a resposta seguindo as regras da Farmácia Ricardo.
    """
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "Você é o Ricardo Aí ⚡️, farmacêutico digital da Farmácia Ricardo no Leme, RJ. "
                        "Regras: 1. Nunca dê diagnósticos. 2. Nunca prescreva remédios controlados. "
                        "3. Seja cordial e use o sotaque leve do Rio (Carioca educado). "
                        "4. Sempre mencione o programa de fidelidade Ricardo Points quando apropriado."
                    )
                },
                {"role": "user", "content": mensagem_cliente}
            ],
            temperature=0.7 # Deixa a conversa mais natural
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return "Ops! Tive um probleminha técnico. Pode repetir? Ou fale com nosso farmacêutico humano."

# Teste de funcionamento (isso aparecerá nos logs do seu GitHub)
if __name__ == "__main__":
    teste = "Como funciona o Ricardo Points?"
    print(f"Cliente: {teste}")
    print(f"Ricardo Aí: {responder_cliente_ricardo(teste)}")
