import "dotenv/config";
import OpenAI from "openai";

async function main(): Promise<void> {
  console.log("Key loaded:", Boolean(process.env.OPENAI_API_KEY));

  const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  const response = await client.responses.create({
    model: "gpt-5.5",
    input: "Reply with exactly: Author's Assistant is connected.",
  });

  console.log(response.output_text);
}

main().catch((error: unknown) => {
  console.error("OpenAI test failed:", error);
  process.exitCode = 1;
});