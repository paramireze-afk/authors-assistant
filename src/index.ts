import { readFile, writeFile } from "./fileUtils.js";
import { buildPrompt } from "./promptBuilder.js";
import { revise } from "./openai.js";

const INPUT_INSTRUCTION = "prompts/revise.md";
const INPUT_STYLE = "docs/WRITING_STYLE.md";
const INPUT_RULES = "docs/EDITING_RULES.md";
const INPUT_DRAFT = "drafts/sample.md";
const OUTPUT_PATH = "output/sample-revised.md";

async function main(): Promise<void> {
  const instruction = readFile(INPUT_INSTRUCTION);
  const style = readFile(INPUT_STYLE);
  const rules = readFile(INPUT_RULES);
  const draft = readFile(INPUT_DRAFT);

  const prompt = buildPrompt({ instruction, style, rules, draft });

  console.log("Sending draft to OpenAI for revision...");
  const revised = await revise(prompt);

  writeFile(OUTPUT_PATH, revised);
  console.log(`Revised draft saved to ${OUTPUT_PATH}`);
}

main().catch((error) => {
  console.error("Unexpected error:", error);
  process.exit(1);
});
