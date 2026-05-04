import { Agent, tool } from "@strands-agents/sdk";
import { z } from "zod";

const jokeStyle = tool({
  name: "joke_style",
  description: "Returns style instructions for joke telling",
  inputSchema: z.object({
    style: z.enum(["dad", "dry", "nerdy"]),
  }),
  callback: (input) => {
    const styles: Record<string, string> = {
      dad: "Keep it cheesy and clean.",
      dry: "Make it subtle and deadpan.",
      nerdy: "Make it developer-themed.",
    };
    return styles[input.style] ?? "Keep it funny.";
  },
});

const agent = new Agent({ tools: [jokeStyle] });

await agent.invoke("Tell me a nerdy joke about Typescript");
