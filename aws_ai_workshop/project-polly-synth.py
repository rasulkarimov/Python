#!/usr/bin/python3
import boto3

region = "eu-central-1"
po = boto3.client('polly', region)

# rekognize the text
res = po.synthesize_speech(Text="Hi Rasl, hope you are well", OutputFormat='mp3', VoiceId='Joanna')

# write to mp3 file
file = open('myaudio.mp3', 'wb')
file.write(res['AudioStream'].read())
file.close()

# lissen
import IPython
IPython.display.Audio("myaudio.mp3")
