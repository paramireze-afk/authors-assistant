# Read Aloud Feature

## Overview

The Read Aloud feature adds accessible text-to-speech controls to article and knowledge-base pages. It uses the browser's native `window.speechSynthesis` API to read article content aloud without requiring external services or libraries.

The feature includes:
- **Read** — Start reading from the beginning
- **Pause / Resume** — Pause and resume at the current paragraph
- **Stop** — Stop reading and reset position
- **Previous / Next** — Navigate between readable paragraphs
- **Speed Control** — Choose from 0.75×, 1×, 1.25×, or 1.5×

## Browser Support

The Read Aloud feature relies on the browser's native `window.speechSynthesis` API:

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full support |
| Edge | ✅ Full support |
| Safari (macOS) | ✅ Full support |
| Safari (iOS) | ✅ Full support |
| Firefox | ✅ Supported (voice availability varies) |
| Firefox (Android) | ✅ Supported |
| Opera | ✅ Full support |
| Internet Explorer | ❌ Not supported |

**Voice Availability:** Available voices vary by operating system and browser. macOS, Windows, Linux, iOS, and Android each have their own system voices. The browser will use the system's default voice.

## How It Works

1. The feature extracts readable content from the main article area (marked with `data-readable-content`)
2. Text is segregated into readable blocks: headings, paragraphs, blockquotes, and list items
3. When "Read" is clicked, the browser reads each block sequentially
4. Readers can pause, resume, navigate forward/backward, or adjust speed
5. Navigation, controls, code blocks, and hidden content are excluded from reading

## Implementation

### Files

```
_includes/read-aloud.html          # Read Aloud control bar HTML
_includes/head_custom.html         # Custom head (loads read-aloud.css)
_includes/footer_custom.html       # Custom footer (includes controls + JS)
assets/css/read-aloud.css          # Styling for controls
assets/js/read-aloud.js            # JavaScript implementation
```

### How It Works

The implementation leverages Just-the-Docs' support for custom `head_custom.html` and `footer_custom.html` includes:

1. **_includes/head_custom.html:** Loads the read-aloud.css stylesheet
2. **_includes/footer_custom.html:** Includes the read-aloud control bar before the footer content and loads the read-aloud.js script
3. **assets/js/read-aloud.js:** Automatically finds the main article content using Just-the-Docs' standard selectors

The JavaScript detects the main content area using this priority:
1. `[data-readable-content]` — Custom implementations or overrides
2. `main#main-content` — Just-the-Docs default
3. `main` — Generic fallback for other themes

This approach avoids overriding the theme's default layout entirely, respecting the remote theme and preventing build errors.

## Usage

### For Article Authors

The Read Aloud feature is automatically available on all article and knowledge-base pages that use the `default` layout. No additional configuration is needed.

#### Excluding Elements from Reading

To exclude a specific element from being read aloud, add the `data-speech-ignore` attribute:

```html
<div data-speech-ignore>
  This content will not be read aloud.
</div>
```

Or use `aria-hidden="true"`:

```html
<div aria-hidden="true">
  This is also excluded from reading.
</div>
```

### For Theme Developers

#### Adding Read Aloud to Just-the-Docs

Just-the-Docs automatically includes custom head and footer content:

1. **_includes/head_custom.html:** Loads the read-aloud.css stylesheet
2. **_includes/footer_custom.html:** Includes the read-aloud control bar and read-aloud.js script

No custom layout override needed; add these includes and the theme will integrate the feature automatically.

#### Adding Read Aloud to Other Jekyll Themes

To add the Read Aloud feature to a custom layout:

1. **Load CSS in the page head:**
   ```html
   <link rel="stylesheet" href="{{ '/assets/css/read-aloud.css' | relative_url }}">
   ```

2. **Optionally wrap main content with the data-readable-content attribute:**
   ```html
   <main id="main-content" data-readable-content>
     {{ content }}
   </main>
   ```
   *(Note: If you don't add this attribute, the JavaScript will auto-detect content using standard selectors like `main#main-content` or `main`)*

3. **Include the control bar before the footer:**
   ```liquid
   {% include read-aloud.html %}
   ```

4. **Load JavaScript before closing body:**
   ```html
   <script src="{{ '/assets/js/read-aloud.js' | relative_url }}" defer></script>
   ```

## Accessibility

The Read Aloud feature is built with accessibility in mind:

- **Semantic HTML:** Uses proper `<button>` elements with clear `aria-label` attributes
- **Keyboard Navigation:** All controls are fully keyboard-accessible
- **Focus Styles:** Clear, visible focus indicators on all interactive elements
- **ARIA Announcements:** Uses `aria-live="polite"` to announce reading status and position
- **Graceful Degradation:** Feature is hidden if the browser does not support `speechSynthesis`

## JavaScript Implementation Details

The implementation uses a `ReadAloudFeature` class that:

1. **Detects content** using this priority:
   - `[data-readable-content]` — Custom implementations
   - `main#main-content` — Just-the-Docs default
   - `main` — Generic fallback for other themes

2. **Extracts readable elements** (headings, paragraphs, blockquotes, list items)

3. **Excludes**:
   - Elements inside `<code>`, `<pre>`, `<script>`, `<style>`, `<nav>`
   - Elements with `data-speech-ignore` attribute
   - Elements with `aria-hidden="true"`
   - Empty elements

4. **Manages speech** via sequential SpeechSynthesisUtterance objects

5. **Handles errors** defensively (continues to next block on error)

6. **Cleans up** on page unload (cancels any ongoing speech)

### Key Features

- **Paragraph-by-paragraph reading:** Rather than passing entire content as one utterance, the feature breaks content into manageable blocks for better control
- **Automatic continuation:** When one paragraph finishes, reading automatically moves to the next
- **Mobile-friendly:** Control labels hide on narrow screens; buttons remain functional with aria-labels
- **Dark mode support:** CSS respects theme color scheme via CSS custom properties
- **No external dependencies:** Uses only browser APIs and vanilla JavaScript

## Styling Customization

The control bar uses CSS custom properties that respect the site's color scheme. To customize colors, override these in your site's CSS:

```css
:root {
  --color-bg: #fff;
  --color-bg-secondary: #f5f5f5;
  --color-text: #333;
  --color-border: #ddd;
  --color-accent: #0969da;
}
```

The control bar automatically adapts to dark mode based on the Just-the-Docs theme settings.

## Limitations and Considerations

1. **Voice Availability:** Some operating systems or browsers may have limited voice selection
2. **Language Support:** Voice availability varies by language and OS
3. **Pronunciation:** The speech synthesizer may mispronounce certain words, technical terms, or names
4. **Speed Changes:** Speed adjustments apply to the next utterance, not the currently speaking paragraph (browser limitation)
5. **Mobile Behavior:** On some mobile browsers, playing audio in the background may pause when the app is backgrounded

## Troubleshooting

**Feature not showing up:**
- Verify the browser supports `window.speechSynthesis` (check browser compatibility table)
- Check that the page uses the `default` layout
- Check browser console for errors

**Reading stops unexpectedly:**
- Some mobile browsers pause audio when the app is backgrounded
- Check if `data-speech-ignore` was accidentally applied to content
- Verify the content has the `data-readable-content` attribute

**Controls are disabled:**
- Ensure the content area has the `data-readable-content` attribute
- Check that `[data-read-aloud-controls]` and `[data-read-aloud-status]` elements exist

## Performance

The Read Aloud feature has minimal performance impact:
- JavaScript file: ~8 KB (minified)
- CSS file: ~3 KB (minified)
- No external HTTP requests or API calls
- Content extraction runs once on page load
- Speech synthesis uses native browser API (no processing overhead)

## Browser API Reference

The implementation uses these browser APIs:
- `window.speechSynthesis` — Main API for text-to-speech
- `SpeechSynthesisUtterance` — Individual speech request object
- `document.querySelector()` — DOM selection
- `element.textContent` — Text extraction

These APIs are standardized in the [Web Speech API specification](https://w3c.github.io/speech-api/).
