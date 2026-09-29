# Study Agent

A minimal AI agent built in Python. It uses the Groq API and a calculator tool, and runs in a loop: the model asks for a tool, my code runs it, and the result goes back to the model.

## How it works
1. User asks a question.
2. The model decides whether it needs the calculator.
3. The code runs the tool and sends the result back.
4. The model gives the final answer.

## Setup
```
pip install -r requirements.txt
```
Get a free API key at console.groq.com, then set it:
- Windows PowerShell: `$env:GROQ_API_KEY="your-key"`
- Mac/Linux: `export GROQ_API_KEY="your-key"`

## Run
```
python agent.py
```
Example: "What is 15% of 2,340, plus 87?" → 438

## What I learned
- How the agent loop works
- How tool calling works
- Small models sometimes make mistakes

## Next steps
- Add more tools (save notes, web search)
- Add a web UI with Streamlit
