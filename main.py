from strands import Agent

agent = Agent(system_prompt="You are a funny comedian who tells programming jokes.")

response = agent("Tell me a joke about Python (the programming language).")
print(response)
