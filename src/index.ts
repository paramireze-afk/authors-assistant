const [draftPath, outputPath] = process.argv.slice(2);

if (!draftPath || !outputPath) {
  console.error("Usage: tsx src/index.ts <draft-path> <output-path>");
  console.error("Example: tsx src/index.ts articles/drafts/my-post.md output/my-post-revised.md");
  process.exit(1);
}

async function main(): Promise<void> {
  console.error("OpenAI usage is temporarily disabled.");
  console.error("No revision request was sent. Re-enable src/openai.ts and src/index.ts when ready.");
  process.exit(1);
}

main().catch((error) => {
  console.error("Unexpected error:", error);
  process.exit(1);
});
