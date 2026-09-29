import json
from groq import Groq

client = Groq()

def calculator(expression):
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"

tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Evaluate a math expression like '12 * (3 + 4)'.",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
        },
    },
}]

messages = [
    {"role": "system", "content": "Always use the calculator tool for any arithmetic."},
    {"role": "user", "content": input("Ask me something: ")},
]

while True:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
    )
    msg = response.choices[0].message
    messages.append(msg)

    if not msg.tool_calls:
        print(msg.content)
        break

    for call in msg.tool_calls:
        args = json.loads(call.function.arguments)
        print(f"[tool] calculator({args['expression']})")
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": calculator(**args),
        })
