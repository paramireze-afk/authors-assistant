import "dotenv/config";
import OpenAI from "openai";

const apiKey = process.env.OPENAI_API_KEY;
const model = process.env.OPENAI_MODEL ?? "gpt-5.5";

if (!apiKey) {
  console.error("Missing OPENAI_API_KEY in .env");
  process.exit(1);
}

const client = new OpenAI({ apiKey });

async function main(): Promise<void> {
  try {
    console.log(`Testing OpenAI connection with ${model}...`);

    const response = await client.responses.create({
      model,
      input: "Reply with exactly: Author's Assistant is connected.",
    });

    console.log("Response:");
    console.log(response.output_text);
  } catch (error) {
    console.error("OpenAI request failed:");
    console.error(error);
    process.exit(1);
  }
}

void main();