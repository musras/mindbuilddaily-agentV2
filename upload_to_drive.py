import os, json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Behörighet – vi vill kunna skriva filer till Drive
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def upload_file(service, filepath, folder_id=None):
    file_metadata = {"name": os.path.basename(filepath)}
    if folder_id:
        file_metadata["parents"] = [folder_id]

    media = MediaFileUpload(filepath, resumable=True)
    file = service.files().create(
        body=file_metadata, media_body=media, fields="id"
    ).execute()
    print(f"Uploaded {filepath} → File ID {file.get('id')}")

if __name__ == "__main__":
    # Ladda credentials från GitHub secret
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    creds = None
    if creds_json:
        creds = Credentials.from_authorized_user_info(json.loads(creds_json), SCOPES)

    if not creds or not creds.valid:
        # Första gången: man får göra login lokalt, sedan spara token.json
        print("⚠️ You need to run local auth once to generate a token.json")

    service = build("drive", "v3", credentials=creds)

    out_dir = "output"
    for root, _, files in os.walk(out_dir):
        for f in files:
            upload_file(service, os.path.join(root, f))
