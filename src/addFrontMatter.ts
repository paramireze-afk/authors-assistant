import * as fs from "fs";
import * as path from "path";

/**
 * Walks the repo's content directories and:
 *  1. Adds minimal Jekyll front matter (layout + title) to any Markdown file
 *     that doesn't already have front matter, so GitHub Pages renders it as
 *     a styled page instead of serving raw Markdown.
 *  2. Prints a grouped manifest (by directory) of every included file with
 *     its derived title, so the site's navigation page can be built accurately.
 *
 * Safe to re-run: files that already start with `---` are left untouched.
 */

const ROOT = path.resolve(import.meta.dirname, "..");

const INCLUDE_ROOTS = ["README.md", "articles", "analysis", "knowledge", "docs"];

// Files that are read raw and fed directly into AI prompts (src/index.ts).
// Adding front matter would leak Jekyll metadata into those prompts.
const EXCLUDE_FILES = new Set([
  "docs/PROJECT_REQUIREMENTS.md",
  "docs/WRITING_STYLE.md",
  "docs/EDITING_RULES.md",
]);

interface FileEntry {
  relPath: string;
  title: string;
  updated: boolean;
}

function humanizeFilename(filename: string): string {
  let name = filename.replace(/\.md$/, "");
  // Strip leading date prefixes like 2026-07-30- or 2025-11-4-
  name = name.replace(/^\d{4}-\d{1,2}-\d{1,2}-/, "");
  name = name.replace(/[-_]+/g, " ").trim();
  return name.replace(/\b\w/g, (c) => c.toUpperCase());
}

function deriveTitle(content: string, filename: string): string {
  const headingMatch = content.match(/^#\s+(.+)$/m);
  const heading = headingMatch?.[1];
  if (heading) {
    return heading.trim().replace(/["]/g, "'");
  }
  return humanizeFilename(filename);
}

function walk(dir: string, results: string[] = []): string[] {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full, results);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      results.push(full);
    }
  }
  return results;
}

function collectTargetFiles(): string[] {
  const files: string[] = [];
  for (const rootItem of INCLUDE_ROOTS) {
    const full = path.join(ROOT, rootItem);
    if (!fs.existsSync(full)) continue;
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      walk(full, files);
    } else {
      files.push(full);
    }
  }
  return files;
}

function processFile(absPath: string): FileEntry {
  const relPath = path.relative(ROOT, absPath).split(path.sep).join("/");
  const content = fs.readFileSync(absPath, "utf-8");

  if (EXCLUDE_FILES.has(relPath)) {
    const title = deriveTitle(content, path.basename(absPath));
    return { relPath, title, updated: false };
  }

  const alreadyHasFrontMatter = content.trimStart().startsWith("---");
  const title = deriveTitle(content, path.basename(absPath));

  if (alreadyHasFrontMatter) {
    return { relPath, title, updated: false };
  }

  const frontMatter = `---\nlayout: default\ntitle: "${title.replace(/"/g, '\\"')}"\n---\n\n`;
  fs.writeFileSync(absPath, frontMatter + content, "utf-8");
  return { relPath, title, updated: true };
}

function main(): void {
  const files = collectTargetFiles().sort();
  const entries = files.map(processFile);

  const updatedCount = entries.filter((e) => e.updated).length;
  const skippedCount = entries.length - updatedCount;

  console.log(`\n=== Front Matter Summary ===`);
  console.log(`Updated: ${updatedCount}  |  Already had front matter / excluded: ${skippedCount}\n`);

  console.log(`=== Manifest (grouped by directory) ===\n`);
  const grouped = new Map<string, FileEntry[]>();
  for (const entry of entries) {
    const dir = path.dirname(entry.relPath);
    if (!grouped.has(dir)) grouped.set(dir, []);
    grouped.get(dir)!.push(entry);
  }
  for (const [dir, list] of [...grouped.entries()].sort()) {
    console.log(`## ${dir}`);
    for (const item of list.sort((a, b) => a.relPath.localeCompare(b.relPath))) {
      console.log(`- [${item.title}](${item.relPath})`);
    }
    console.log("");
  }
}

main();
