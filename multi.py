from openai import OpenAI
import textwrap


check_prompt = """
We want to make sure the user only asks questions about victorian silverplate.
Answer with YES or NO: is the user's question relevant to the topic of silverplate?
"""

system_prompt = """
You are an expert at victorian silverplate.  You only answer questions about
victorian silverplate.  If the user asks questions about something else,
you politely decline to answer.
"""

def check_question(q):
    client = OpenAI()


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": check_prompt},
            {"role": "user", "content": f"This is the user's message: ```{q}```"}
        ]
    )

    ans = completion.choices[0].message.content

    return ans == 'YES'

def chatbot():
    client = OpenAI()

    history = []

    while True:
        cmd = input('User:  ')

        if not check_question(cmd):
            print('Error: This is not a question about silverplate')
            continue

        history.append({"role": "user", "content": cmd})

        msgs = [{"role": "system", "content": system_prompt}]
        for i in range(len(history)):
            msgs.append(history[i])

        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=msgs
        )

        ans = completion.choices[0].message.content

        history.append({"role": "assistant", "content": ans})

        lines = textwrap.wrap(ans,80)

        print(f'GPT:  {lines[0]}')

        for i in range(len(lines)-1):
            print(f'      {lines[i+1]}')


if __name__ == "__main__":
    chatbot()