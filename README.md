# Seibi App Presentation

This repository contains the presentation slides for **Seibi (設備管理システム — Equipment Maintenance & Inspection Management System)**.

It includes two formats:
1. **Interactive Web Presentation (HTML/CSS/JS)**: Clean glassmorphic slide deck with autoplaying, looping video demonstrations of Seibi in action.
2. **PowerPoint Presentation (`.pptx`)**: Standard PowerPoint deck with high-resolution app screenshots embedded.

## Project Structure

* `index.html` - The structure of the interactive web presentation slides.
* `styles.css` - Custom styling (dark theme, glassmorphism, responsive grid, slide transitions).
* `slides.js` - Logic for slide changes, bullet indicators, and keyboard/click navigation.
* `seibi_presentation.pptx` - PowerPoint presentation deck.
* `videos/` - Directory containing WebM video recordings of the Seibi application.
  * `dashboard.webm` - Daily tasks, stats, and overdue inspection cards.
  * `wire_map.webm` - Interactive blueprint and scheduled inspection wiring.
  * `history.webm` - Audit log filtering by timeframe and abnormalities.
  * `bulletin.webm` - Incident feed, starting repairs, and posting comments.
  * `manuals.webm` - Accessing user guides and using the AI Q&A assistant.
* `capture_all_v2.py` / `record_videos.py` - Automation scripts using Playwright used to capture the screenshots and video walk-throughs.

## How to View

### 1. Web Presentation (HTML)
Double-click `index.html` or open it in any web browser.
* Use **Left/Right Arrow keys**, **Spacebar**, or the **Prev/Next buttons** at the bottom to navigate.
* Click on the bullet dots in the navigation bar to jump directly to any slide.

### 2. PowerPoint Slide Deck
Double-click `seibi_presentation.pptx` to open and edit in Microsoft PowerPoint.
