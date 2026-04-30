# 🖼️ Image Analysis with AWS Rekognition

This project demonstrates how to perform **image analysis using AWS cloud services**. It uses **Amazon S3** for image storage and **Amazon Rekognition** for detecting objects, scenes, and concepts within images.

## 🚀 Project Overview

In this project, multiple images are uploaded to an S3 bucket and analyzed using AWS Rekognition. The system detects labels (such as objects or scenes) in each image along with their confidence scores. The results are then stored in a structured JSON file for further use or analysis.

## 🧰 Technologies Used

* Python
* Boto3 (AWS SDK for Python)
* AWS S3 (Storage Service)
* AWS Rekognition (Image Analysis Service)

## ⚙️ How It Works

1. Images are uploaded to an Amazon S3 bucket.
2. A Python script uses Boto3 to access the images.
3. The script calls the Rekognition `detect_labels` API for each image.
4. Detected labels and their confidence scores are extracted.
5. Results are saved into a JSON file (`rekognition_results.json`).

## 📂 Project Structure

* `rekognition.py` → Main Python script
* `rekognition_results.json` → Output file containing detected labels
* `README.md` → Project documentation

## 📊 Sample Output

```json
{
  "image1.jpg": [
    {
      "Label": "Car",
      "Confidence": 97.85
    },
    {
      "Label": "Vehicle",
      "Confidence": 95.12
    }
  ]
}
```

## 🧠 Key Learnings

* How to integrate Python applications with AWS services
* Working with cloud storage using S3
* Using AI-powered APIs for image analysis
* Handling and storing structured results in JSON format

## 📌 Future Improvements

* Automate image analysis using AWS Lambda triggers
* Store results in a database (e.g., DynamoDB)
* Build a web interface for uploading and analyzing images
* Add support for more Rekognition features (face detection, text detection)

## 🔗 AWS Services Used

* Amazon S3
* Amazon Rekognition

---

✨ This project is a simple yet powerful example of building **AI-powered cloud applications** using AWS.
