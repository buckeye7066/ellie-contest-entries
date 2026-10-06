# CLIP Similarity Checker

## Problem
In many applications—such as content moderation, accessibility tools, and creative workflows—it is useful to quantify how well an image matches a textual description. Existing solutions often rely on proprietary APIs or require extensive machine‑learning expertise, making them inaccessible to hobbyists, students, and small teams.

## Who It Helps
This tool is aimed at developers, researchers, educators, and content creators who need a quick, offline way to test image‑text alignment without paying for third‑party services. By running locally, users retain full control over their data and can experiment with multimodal AI in a classroom or hackathon setting.

## How It Works
The script uses the open‑source CLIP (Contrastive Language–Image Pretraining) model from Hugging Face’s `transformers` library. CLIP jointly embeds images and text into a shared vector space, allowing a direct cosine similarity measurement between an image encoding and a text encoding. The workflow is:
1. Load the pretrained `clip-vit-base-patch32` model and its associated processor.
2. Read the supplied image file (any format supported by Pillow) and the text string.
3. Preprocess both modalities with the CLIP processor.
4. Obtain the image and text feature vectors.
5. Compute cosine similarity (range ‑1 to 1) and report the result.
A higher score indicates stronger alignment between the image and the description.

## How to Run (under 5 minutes)
1. Ensure you have Python 3.8+ installed.
2. Clone this repository or copy the two files (`main.py` and `requirements.txt`) into a folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (This will download the CLIP weights the first time; the download may take a few seconds to a minute depending on your connection.)
4. Run the script, providing an image path and a text description:
   ```bash
   python main.py --image examples/sample.jpg --text \"A red bicycle parked under a tree.\"
   ```
   The program will print a similarity score, e.g., `Similarity: 0.42`.
5. Optionally, experiment with different images and texts to see how the score changes.

## Limitations
- The model is relatively large (~1.3 GB) and may require a GPU for real‑time use; on CPU the inference takes a few seconds per pair.
- CLIP was trained primarily on English text‑image pairs, so non‑English inputs may yield lower scores.
- The similarity score is a raw cosine similarity; it is not calibrated to a probability of “match.”
- No internet connection is needed after the initial model download, but the first run will fetch weights from Hugging Face.
- This demo does not perform fine‑tuning; for domain‑specific tasks you would need to adapt the model further.

## Acknowledgments
Built with AI assistance by Ellie, an AI agent working for John White, as the contest rules permit.