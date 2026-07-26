interface PromptParts {
  instruction: string;
  style: string;
  rules: string;
  draft: string;
}

export function buildPrompt(parts: PromptParts): string {
  return [
    "<instructions>",
    parts.instruction.trim(),
    "</instructions>",
    "",
    "<writing_style>",
    parts.style.trim(),
    "</writing_style>",
    "",
    "<editing_rules>",
    parts.rules.trim(),
    "</editing_rules>",
    "",
    "<draft>",
    parts.draft.trim(),
    "</draft>",
  ].join("\n");
}
