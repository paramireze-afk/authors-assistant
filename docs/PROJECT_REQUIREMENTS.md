# Author's Assistant

## Purpose

Author's Assistant is a local writing tool designed to reduce the amount of
copying and pasting required when revising Substack posts with an AI model.

The application will read Markdown files, apply the author's editing
instructions, and produce suggested revisions for review.

## Primary Goal

Allow Paul to revise writing directly from his local Markdown files while
preserving his wording, cadence, personality, argument, and formatting.

## Version 1

The first version will:

1. Accept the path to a Markdown file.
2. Read the original file.
3. Read the author's writing style and editing rules.
4. Read a selected prompt or editing mode.
5. send the material to the OpenAI API.
6. Save the result as a separate revised file.
7. Never overwrite the original file.

## Version 1 Non-Goals

The first version will not include:

- A graphical interface
- A VS Code extension
- Automatic replacement of text
- A database
- User accounts
- Direct Substack publishing
- File watching
- Research or web browsing
- Automatic fact-checking

## Future Possibilities

- Revise highlighted text from VS Code
- Display a diff before accepting changes
- Add multiple editing modes
- Review an entire article for consistency
- Suggest titles and subtitles
- Create Substack excerpts
- Organize source material
- Publish to Substack