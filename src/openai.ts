import "dotenv/config";
import OpenAI from "openai";

export async function revise(prompt: string): Promise<string> {
  const apiKey = process.env.OPENAI_API_KEY;
  const model = process.env.OPENAI_MODEL ?? "gpt-4o";

  if (!apiKey) {
    console.error("Missing OPENAI_API_KEY environment variable.");
    process.exit(1);
  }

  const client = new OpenAI({ apiKey });

  const response = await client.responses.create({
    model,
    input: prompt,
  });

  return response.output_text;
}
