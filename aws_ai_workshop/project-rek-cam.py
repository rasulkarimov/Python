#!/usr/bin/python3

# web cam photo click
# pip install opencv-python
import cv2

cap = cv2.VideoCapture(0)

myphoto = "image.jpg"
ret , photo = cap.read()
cv2.imwrite(myphoto , photo)
cap.release()

# upload into s3 storage
# pip install boto3
# pip install aws
import boto3
region = "eu-central-1"
bucket = "mybacket90"
upimage = "file.jpg"

s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myphoto, upimage)

# connect rekognition : ask for part method
rek = boto3.client('rekognition', region)

response = rek.detect_labels(

Image={
        "S3Object": {
            "Bucket": bucket,
            "Name": upimage
        }
    },
    MaxLabels=10,
    MinConfidence=60
)

for i in range(5):
    print ( response['Labels'][i]['Name'])

# response
resfaces = rek.detect_faces(
Image={
        "S3Object": {
            "Bucket": "console-sample-images-fra",
            "Name": "jeff_portrait.jpg"
        }
    },
    Attributes=['ALL']
)

if resfaces['FaceDetails'][0]['Smile']['Value'] == False:
    print("connect to media player, play song")
