import "dotenv/config";
import { readFile, writeFile } from "./fileUtils.js";
import { buildPrompt } from "./promptBuilder.js";
import { revise } from "./openai.js";

const [draftPath, outputPath] = process.argv.slice(2);

if (!draftPath || !outputPath) {
  console.error("Usage: tsx src/index.ts <draft-path> <output-path>");
  console.error("Example: tsx src/index.ts drafts/my-post.md output/my-post-revised.md");
  process.exit(1);
}

async function main(): Promise<void> {
  // Load documentation and configuration
  const instruction = readFile("docs/PROJECT_REQUIREMENTS.md");
  const style = readFile("docs/WRITING_STYLE.md");
  const rules = readFile("docs/EDITING_RULES.md");
  const draft = readFile(draftPath);

  // Build the prompt
  const prompt = buildPrompt({
    instruction,
    style,
    rules,
    draft,
  });

  // Send to OpenAI for revision
  console.error(`Revising ${draftPath}...`);
  const revised = await revise(prompt);

  // Write the output
  writeFile(outputPath, revised);
  console.error(`✓ Revised version written to ${outputPath}`);
}

main().catch((error) => {
  console.error("Unexpected error:", error);
  process.exit(1);
});
