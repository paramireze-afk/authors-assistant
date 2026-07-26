interface PromptParts {
  instruction: string;
  style: string;
  rules: string;
  draft: string;
}

export function buildPrompt(parts: PromptParts): string {
  return [
    "## Instructions",
    parts.instruction.trim(),
    "",
    "## Writing Style",
    parts.style.trim(),
    "",
    "## Editing Rules",
    parts.rules.trim(),
    "",
    "## Draft",
    parts.draft.trim(),
  ].join("\n");
}
