from openai import OpenAI
import textwrap


system_prompt = """
You are an expert at victorian silverplate.  You only answer questions about
victorian silverplate.  If the user asks questions about something else,
you politely decline to answer.
"""

def chatbot():
    client = OpenAI()

    history = []

    while True:
        cmd = input('User:  ')
        history.append({"role": "user", "content": cmd})

        msgs = [{"role": "system", "content": system_prompt}]
        for i in range(len(history)):
            msgs.append(history[i])

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # model="gpt-3.5-turbo-1106",
            messages=msgs
        )

        ans = completion.choices[0].message.content

        history.append({"role": "assistant", "content": ans})

        lines = textwrap.wrap(ans,80)

        print(f'GPT:   {lines[0]}')

        for i in range(len(lines)-1):
            print(f'       {lines[i+1]}')


if __name__ == "__main__":
    chatbot()