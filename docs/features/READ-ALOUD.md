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
_layouts/default.html              # Custom layout with data-readable-content wrapper
_includes/read-aloud.html          # Read Aloud control bar HTML
assets/css/read-aloud.css          # Styling for controls
assets/js/read-aloud.js            # JavaScript implementation
```

### How the Layout Works

The custom `_layouts/default.html` wraps the main article content with the `data-readable-content` attribute:

```html
<main id="main-content" class="page-content" role="main" data-readable-content>
  {{ content }}
</main>
```

The control bar is included immediately after the main content:

```liquid
{% include read-aloud.html %}
```

JavaScript and CSS assets are loaded in the page head and footer.

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

#### Adding Read Aloud to a Custom Layout

To add the Read Aloud feature to a custom layout:

1. **Wrap main content with the data-readable-content attribute:**
   ```html
   <main id="main-content" data-readable-content>
     {{ content }}
   </main>
   ```

2. **Include the control bar before the footer:**
   ```liquid
   {% include read-aloud.html %}
   ```

3. **Add CSS and JavaScript to the page head:**
   ```html
   <link rel="stylesheet" href="{{ '/assets/css/read-aloud.css' | relative_url }}">
   ```

4. **Add script tag before closing body:**
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

1. **Extracts content** from the `[data-readable-content]` container
2. **Filters elements** to include only readable types (headings, paragraphs, blockquotes, list items)
3. **Excludes**:
   - Elements inside `<code>`, `<pre>`, `<script>`, `<style>`, `<nav>`
   - Elements with `data-speech-ignore` attribute
   - Elements with `aria-hidden="true"`
   - Empty elements
4. **Manages queuing** of speech utterances for sequential reading
5. **Handles errors** defensively (if a voice is unavailable, continues to next block)
6. **Respects browser lifecycle** (cancels speech on page unload)

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
