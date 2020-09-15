import json

def lambda_handler(event, context):

    import codecs
    from boto3 import Session
    from boto3 import resource
    print("event details")
    print(event)
    print(event['text'])
    print(event['voice'])
    text=event['text']
    voice=event['voice']
    #print(event['data']['text'])
    #print(event['data']['voice'])
    session = Session(region_name="us-east-1")
    polly = session.client("polly")

    s3 = resource('s3')
    bucket_name = "pollyaudiofiles21072020"
    bucket = s3.Bucket(bucket_name)

    filename = "mynameis3.mp3"
    myText = """
    Hello,
    My name is Eralper.
    Welcome to my website kodyaz.com
    """
    
    response = polly.synthesize_speech(
    #Text=myText,
    Text=text,
    OutputFormat="mp3",
#    VoiceId="Matthew")
    VoiceId= voice)
    stream = response["AudioStream"]

    bucket.put_object(Key=filename, Body=stream.read())