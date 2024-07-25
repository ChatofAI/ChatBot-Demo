import json

from openai import OpenAI

OPENAI_API_KEY = "sk-XXXXXXXX"

prompt = """You are an AI assistant that helps users find the best answer to
their questions."""


def ask_question(question):
    client = OpenAI(api_key=OPENAI_API_KEY)
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield u"data: {}\n\n".format(json.dumps({
                "type": "message",
                "content": chunk.choices[0].delta.content
            }))
    yield u"data: [DONE]\n\n"
