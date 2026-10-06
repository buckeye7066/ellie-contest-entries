import argparse
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='Compute CLIP similarity between an image and a text description.')
    parser.add_argument('--image', type=str, required=True, help='Path to the input image file.')
    parser.add_argument('--text', type=str, required=True, help='Text description to compare with the image.')
    args = parser.parse_args()

    # Load model and processor
    model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
    processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')

    # Prepare inputs
    image = Image.open(args.image).convert('RGB')
    inputs = processor(text=[args.text], images=image, return_tensors='pt', padding=True)

    # Get features
    with torch.no_grad():
        outputs = model(**inputs)
        image_embeds = outputs.image_embeds  # shape (1, dim)
        text_embeds = outputs.text_embeds    # shape (1, dim)

    # Cosine similarity
    similarity = torch.nn.functional.cosine_similarity(image_embeds, text_embeds).item()

    print(f'Similarity: {similarity:.4f}')

if __name__ == '__main__':
    main()