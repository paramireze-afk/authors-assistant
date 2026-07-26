import * as fs from "fs";
import * as path from "path";

export function readFile(filePath: string): string {
  if (!fs.existsSync(filePath)) {
    console.error(`Missing required file: ${filePath}`);
    process.exit(1);
  }
  return fs.readFileSync(filePath, "utf-8");
}

export function writeFile(filePath: string, content: string): void {
  const resolved = path.resolve(filePath);
  const draftsDir = path.resolve("drafts");

  if (resolved.startsWith(draftsDir + path.sep) || resolved === draftsDir) {
    console.error(`Refusing to overwrite source draft: ${filePath}`);
    process.exit(1);
  }

  const dir = path.dirname(resolved);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(resolved, content, "utf-8");
}
