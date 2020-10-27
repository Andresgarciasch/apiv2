import requests, os
from google.cloud import storage
from urllib.parse import urlencode
from .models import UserSpecialty

ENVIRONMENT = os.getenv('ENV',None)
BUCKET_NAME = "certificates-breathecode"

def resolve_google_credentials():
    path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS',None)
    if path is None or not os.path.exists( path ):
        credentials = os.getenv('GOOGLE_SERVICE_KEY')#.replace("\\\\","\\")
        with open(path, 'w') as credentials_file:
            credentials_file.write( credentials )

def certificate_screenshot(certificate_id):

    if ENVIRONMENT == 'development':
        return True
        
    certificate = UserSpecialty.objects.get(id=certificate_id)
    if certificate.preview_url is None or certificate.preview_url == "":
        file_name = f'{certificate.token}'
        resolve_google_credentials()
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.get_blob(file_name)

        # if the file does not exist
        if blob is None:
            query_string = urlencode({
                'key': os.environ.get('SCREENSHOT_MACHINE_KEY'),
                'url': f'https://certificate.breatheco.de/preview/{certificate.token}',
                'device': f'desktop',
                'cacheLimit': '0',
                'dimension': f'1024x707',
            })
            r = requests.get(f'https://api.screenshotmachine.com?{query_string}', stream=True)
            if r.status_code == 200:
                blob = bucket.blob(file_name)
                blob.upload_from_string(r.content)
                blob.make_public()
            else:
                print("Invalid reponse code: ",r.status_code)
        
        # after created, lets save the URL
        if blob is not None:
            certificate.preview_url = blob.public_url
            certificate.save()

def remove_certificate_screenshot(certificate_id):
    certificate = UserSpecialty.objects.get(id=certificate_id)
    if certificate.preview_url is None or certificate.preview_url == "":
        return True

    file_name = f'{certificate.token}'
    resolve_google_credentials()
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.get_blob(file_name)
    blob.delete()

    certificate.preview_url = ""
    certificate.save()
    
    return True