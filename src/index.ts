import { readFile, writeFile } from "./fileUtils.js";
import { buildPrompt } from "./promptBuilder.js";
import { revise } from "./openai.js";

const INPUT_INSTRUCTION = "prompts/revise.md";
const INPUT_STYLE = "docs/WRITING_STYLE.md";
const INPUT_RULES = "docs/EDITING_RULES.md";

const [draftPath, outputPath] = process.argv.slice(2);

if (!draftPath || !outputPath) {
  console.error("Usage: tsx src/index.ts <draft-path> <output-path>");
  console.error("Example: tsx src/index.ts articles/drafts/my-post.md output/my-post-revised.md");
  process.exit(1);
}

const INPUT_DRAFT = draftPath;
const OUTPUT_PATH = outputPath;

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
