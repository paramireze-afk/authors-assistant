/**
 * Read Aloud Feature
 * 
 * Uses browser's native window.speechSynthesis API to read article content aloud.
 * 
 * Browser Compatibility Note:
 * - Chrome/Edge/Safari: Full support
 * - Firefox: Supported (may have different voice availability by OS)
 * - Mobile browsers: Varies; generally supported but voices differ by device/OS
 * 
 * Voice availability and quality vary by operating system and browser.
 * Some browsers may not have voices in all languages, and voice names differ
 * between macOS, Windows, Linux, iOS, and Android.
 */

class ReadAloudFeature {
  constructor() {
    this.synthesis = window.speechSynthesis;
    this.utterancesQueue = [];
    this.currentIndex = 0;
    this.isPaused = false;
    this.isReading = false;
    this.readableElements = [];
    this.currentUtterance = null;
    this.speed = 1;
    
    // Selectors for the UI and content
    // Try multiple selectors to support different Jekyll themes
    this.contentContainer = 
      document.querySelector('[data-readable-content]') ||  // Custom implementations
      document.querySelector('main#main-content') ||        // Just-the-Docs
      document.querySelector('main');                        // Generic fallback
    
    this.controlBar = document.querySelector('[data-read-aloud-controls]');
    this.statusElement = document.querySelector('[data-read-aloud-status]');
    
    if (!this.contentContainer) {
      console.warn('ReadAloud: Could not find main content area (tried [data-readable-content], main#main-content, main)');
      this.disableFeature();
      return;
    }
    
    if (!this.controlBar) {
      console.warn('ReadAloud: Control bar not found (data-read-aloud-controls)');
      this.disableFeature();
      return;
    }
    
    // Check browser support
    if (!this.synthesis) {
      console.warn('ReadAloud: speechSynthesis not supported in this browser');
      this.disableFeature();
      return;
    }
    
    this.setupEventListeners();
    this.extractReadableElements();
  }

  /**
   * Disable the feature if prerequisites are missing
   */
  disableFeature() {
    if (this.controlBar) {
      this.controlBar.style.display = 'none';
    }
  }

  /**
   * Set up button event listeners
   */
  setupEventListeners() {
    const readBtn = this.controlBar.querySelector('[data-action="read"]');
    const pauseResumeBtn = this.controlBar.querySelector('[data-action="pause-resume"]');
    const stopBtn = this.controlBar.querySelector('[data-action="stop"]');
    const prevBtn = this.controlBar.querySelector('[data-action="previous"]');
    const nextBtn = this.controlBar.querySelector('[data-action="next"]');
    const speedControl = this.controlBar.querySelector('[data-action="speed"]');

    if (readBtn) readBtn.addEventListener('click', () => this.startReading());
    if (pauseResumeBtn) pauseResumeBtn.addEventListener('click', () => this.togglePauseResume());
    if (stopBtn) stopBtn.addEventListener('click', () => this.stop());
    if (prevBtn) prevBtn.addEventListener('click', () => this.previousParagraph());
    if (nextBtn) nextBtn.addEventListener('click', () => this.nextParagraph());
    if (speedControl) speedControl.addEventListener('change', (e) => this.setSpeed(parseFloat(e.target.value)));

    // Cancel speech on page unload
    window.addEventListener('beforeunload', () => this.stop());
  }

  /**
   * Extract readable content blocks from the main content area.
   * Includes: headings, paragraphs, blockquotes, list items.
   * Excludes: code blocks, scripts, styles, nav, empty elements, data-speech-ignore, aria-hidden.
   */
  extractReadableElements() {
    this.readableElements = [];
    const selectors = [
      'h1:not([aria-hidden="true"]):not([data-speech-ignore])',
      'h2:not([aria-hidden="true"]):not([data-speech-ignore])',
      'h3:not([aria-hidden="true"]):not([data-speech-ignore])',
      'h4:not([aria-hidden="true"]):not([data-speech-ignore])',
      'h5:not([aria-hidden="true"]):not([data-speech-ignore])',
      'h6:not([aria-hidden="true"]):not([data-speech-ignore])',
      'p:not([aria-hidden="true"]):not([data-speech-ignore])',
      'blockquote:not([aria-hidden="true"]):not([data-speech-ignore])',
      'li:not([aria-hidden="true"]):not([data-speech-ignore])',
    ];

    const elements = this.contentContainer.querySelectorAll(selectors.join(','));

    elements.forEach(el => {
      // Skip if inside code block, script, style, nav, or marked for exclusion
      if (this.isInsideExcludedElement(el)) {
        return;
      }

      const text = el.textContent.trim();
      if (text.length > 0) {
        this.readableElements.push({
          element: el,
          text: text,
        });
      }
    });
  }

  /**
   * Check if an element is inside an excluded container
   */
  isInsideExcludedElement(el) {
    const excluded = el.closest('code, pre, script, style, nav, [data-speech-ignore], [aria-hidden="true"]');
    return excluded && excluded !== el;
  }

  /**
   * Start reading from the beginning
   */
  startReading() {
    // Cancel any existing speech
    this.synthesis.cancel();
    this.utterancesQueue = [];
    this.currentIndex = 0;
    this.isPaused = false;
    this.isReading = true;

    if (this.readableElements.length === 0) {
      this.updateStatus('No readable content found.');
      return;
    }

    this.updateStatus('Reading');
    this.readNext();
  }

  /**
   * Read the next paragraph
   */
  readNext() {
    if (this.currentIndex >= this.readableElements.length) {
      this.isReading = false;
      this.updateStatus('Finished');
      return;
    }

    const item = this.readableElements[this.currentIndex];
    const utterance = new SpeechSynthesisUtterance(item.text);
    
    // Apply current speed
    utterance.rate = this.speed;

    utterance.onend = () => {
      if (this.isReading && !this.isPaused) {
        this.currentIndex++;
        this.readNext();
      }
    };

    utterance.onerror = (event) => {
      console.warn('SpeechSynthesis error:', event.error);
      // Continue to next paragraph on error
      if (this.isReading && !this.isPaused) {
        this.currentIndex++;
        this.readNext();
      }
    };

    this.currentUtterance = utterance;
    this.synthesis.speak(utterance);
    this.updateStatus(`Reading paragraph ${this.currentIndex + 1} of ${this.readableElements.length}`);
  }

  /**
   * Pause or resume reading
   */
  togglePauseResume() {
    if (!this.isReading) {
      return;
    }

    if (this.isPaused) {
      // Resume
      this.isPaused = false;
      this.synthesis.resume();
      this.updateStatus(`Reading paragraph ${this.currentIndex + 1} of ${this.readableElements.length}`);
      this.updateButtonLabel('[data-action="pause-resume"]', 'Pause');
    } else {
      // Pause
      this.isPaused = true;
      this.synthesis.pause();
      this.updateStatus(`Paused at paragraph ${this.currentIndex + 1} of ${this.readableElements.length}`);
      this.updateButtonLabel('[data-action="pause-resume"]', 'Resume');
    }
  }

  /**
   * Stop reading completely
   */
  stop() {
    this.synthesis.cancel();
    this.utterancesQueue = [];
    this.currentIndex = 0;
    this.isPaused = false;
    this.isReading = false;
    this.currentUtterance = null;
    this.updateStatus('Stopped');
    this.updateButtonLabel('[data-action="pause-resume"]', 'Pause');
  }

  /**
   * Jump to previous paragraph
   */
  previousParagraph() {
    if (this.readableElements.length === 0) {
      return;
    }

    this.synthesis.cancel();
    
    if (this.currentIndex > 0) {
      this.currentIndex--;
    }

    if (this.isReading) {
      this.readNext();
    } else {
      this.updateStatus(`Paragraph ${this.currentIndex + 1} of ${this.readableElements.length}`);
    }
  }

  /**
   * Jump to next paragraph
   */
  nextParagraph() {
    if (this.readableElements.length === 0) {
      return;
    }

    this.synthesis.cancel();
    this.currentIndex++;

    if (this.currentIndex >= this.readableElements.length) {
      this.currentIndex = this.readableElements.length - 1;
      this.isReading = false;
      this.updateStatus('Reached end');
      return;
    }

    if (this.isReading) {
      this.readNext();
    } else {
      this.updateStatus(`Paragraph ${this.currentIndex + 1} of ${this.readableElements.length}`);
    }
  }

  /**
   * Set reading speed
   */
  setSpeed(speed) {
    this.speed = speed;
    // Speed applies to the next utterance, not the current one
    // This is a browser limitation; we can't change speed mid-utterance
  }

  /**
   * Update the status element with aria-live announcements
   */
  updateStatus(message) {
    if (this.statusElement) {
      this.statusElement.textContent = message;
      // Ensure aria-live is set for announcements
      this.statusElement.setAttribute('aria-live', 'polite');
      this.statusElement.setAttribute('aria-atomic', 'true');
    }
  }

  /**
   * Update button label dynamically
   */
  updateButtonLabel(selector, label) {
    const btn = this.controlBar.querySelector(selector);
    if (btn) {
      const labelSpan = btn.querySelector('span');
      if (labelSpan) {
        labelSpan.textContent = label;
      }
      btn.setAttribute('aria-label', label);
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  if (window.speechSynthesis) {
    new ReadAloudFeature();
  }
});
