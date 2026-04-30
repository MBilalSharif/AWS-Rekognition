import boto3
import json

# ==============================
# CONFIGURATION
# ==============================
BUCKET_NAME   = "image-bucket-bilal"
UPLOAD_PREFIX = "uploads/"         
IMAGE_EXTS    = (".jpg", ".jpeg", ".png", ".webp", ".gif")

# Initialize AWS clients
s3           = boto3.client('s3')
rekognition  = boto3.client('rekognition')

# ==============================
# FETCH IMAGES FROM UPLOAD FOLDER
# ==============================
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=UPLOAD_PREFIX)

results = {}

# ==============================
# LOOP THROUGH IMAGES
# ==============================
for obj in response.get('Contents', []):
    image_key = obj['Key']

    # Skip the folder "directory" entry itself and any non-image files
    if image_key == UPLOAD_PREFIX or not image_key.lower().endswith(IMAGE_EXTS):
        print(f"Skipping: {image_key}")
        continue

    print(f"Analyzing image: {image_key}")

    try:
        rekog_response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': BUCKET_NAME,
                    'Name': image_key
                }
            },
            MaxLabels=10,
            MinConfidence=70
        )

        labels_list = [
            {
                "Label":      label['Name'],
                "Confidence": round(label['Confidence'], 2)
            }
            for label in rekog_response['Labels']
        ]

        results[image_key] = labels_list

    except Exception as e:
        print(f"Error processing {image_key}: {str(e)}")

# ==============================
# SAVE OUTPUT TO JSON FILE
# ==============================
output_file = "rekognition_results.json"

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print(f"\n✅ Done! Results saved in {output_file}")