from strands import Agent, tool


@tool
def joke_style(style: str) -> str:
    styles = {
        "dad": "Keep it cheesy and clean.",
        "dry": "Make it subtle and deadpan.",
        "nerdy": "Make it developer-themed."
    }
    return styles.get(style, "Keep it funny.")


agent = Agent(tools=[joke_style])

agent("Tell me a nerdy joke about Python")
