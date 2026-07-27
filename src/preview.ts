import * as fs from "fs";
import * as path from "path";
import { marked } from "marked";

const [inputPath, outputHtmlPath] = process.argv.slice(2);

if (!inputPath || !outputHtmlPath) {
  console.error("Usage: tsx src/preview.ts <input-markdown-path> <output-html-path>");
  process.exit(1);
}

if (!fs.existsSync(inputPath)) {
  console.error(`Missing file: ${inputPath}`);
  process.exit(1);
}

const markdown = fs.readFileSync(inputPath, "utf-8");
const htmlBody = marked.parse(markdown);

const fullHtml = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Post Preview</title>
    <style>
      body {
        max-width: 760px;
        margin: 2rem auto;
        padding: 0 1rem;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        line-height: 1.65;
        color: #111;
      }
      h1, h2, h3 {
        line-height: 1.25;
      }
      pre {
        background: #f5f5f5;
        padding: 1rem;
        overflow-x: auto;
      }
      blockquote {
        border-left: 4px solid #ddd;
        margin: 0;
        padding-left: 1rem;
        color: #555;
      }
    </style>
  </head>
  <body>
    ${htmlBody}
  </body>
</html>`;

const resolvedOutput = path.resolve(outputHtmlPath);
fs.mkdirSync(path.dirname(resolvedOutput), { recursive: true });
fs.writeFileSync(resolvedOutput, fullHtml, "utf-8");

console.log(`Preview written to ${outputHtmlPath}`);
