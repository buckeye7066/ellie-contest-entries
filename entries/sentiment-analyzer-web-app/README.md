# Sentiment Analyzer Web App

## Problem
Many users want quick feedback on the emotional tone of their text—whether they are writing a product review, a social media post, or an email. Existing tools often require sign‑ups, API keys, or paid subscriptions, making instant experimentation cumbersome for hobbyists, students, and small businesses.

## Who it helps
- Students learning about natural language processing who need a no‑cost, no‑setup demo.
- Bloggers and content creators who want to check tone before publishing.
- Small business owners who want to gauge customer feedback without investing in expensive SaaS platforms.
- Hackathon participants looking for a quick, demonstrable AI component that works offline after initial load.

## How it works
The app loads TensorFlow.js and a pre‑sentiment model from the TensorFlow Hub (the `sentiment` model). When the user types text and clicks **Analyze**, the model processes the input and returns a probability score for three classes: negative, neutral, and positive. The UI highlights the most likely sentiment and shows the raw scores. All computation happens in the browser; no data leaves the user's machine, preserving privacy.

## How to run it in under 5 minutes
1. Clone or download this repository.
2. Open `index.html` in any modern browser (Chrome, Firefox, Safari, Edge).
3. Wait a few seconds for the model to load (status shown at the top).
4. Type or paste text into the textarea and press **Analyze**.
5. See the sentiment result instantly.

## Limitations
- The model is English‑only and works best on short to medium length sentences; very long paragraphs may be truncated internally.
- Accuracy is not comparable to large‑scale commercial APIs; it is intended for educational and demonstrative purposes.
- The initial load requires downloading ~ few MBs of model data; on slow connections this may take a bit longer.
- No server‑side component means the app cannot be easily scaled to serve many concurrent users without each client downloading the model.

Built with AI assistance by Ellie, an AI agent working for John White, as the contest rules permit.