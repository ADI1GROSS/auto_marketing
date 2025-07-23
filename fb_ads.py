import json

def simulate_facebook_ad(ad_text: str, image_path: str):
    simulated_payload = {
        "ad_text": ad_text,
        "image_path": image_path,
        "audience": "Auto-selected",
        "budget": "10₪",
        "objective": "Engagement",
        "platform": "Facebook"
    }
    print("📣 סימולציית פרסום בפייסבוק:")
    print(json.dumps(simulated_payload, indent=4, ensure_ascii=False))
    return simulated_payload
