# Independent model comparison

The live app can use the original hosted Roboflow classifier or CLIP ViT-B/32 in a browser worker via Transformers.js 3.8.1. The CLIP model revision is pinned. Candidate labels include dog and common exotic species plus a non-animal scene option. CLIP scores are relative to this candidate set; the 70% UI threshold is heuristic and does not establish accuracy.

This is whole-image classification, not bounding-box detection. A sufficiently varied labeled evaluation dataset is still required before claiming improved general accuracy. The browser engine downloads model weights but does not upload images; the hosted engine sends images to Roboflow.

Model: https://huggingface.co/Xenova/clip-vit-base-patch32
