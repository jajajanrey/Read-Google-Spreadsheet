""" Import required libraries """
import os
import json

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_PATH = '/tmp/credentials.json'


def get_credentials(credentials):
    """
        We have to write it to a file because gcs
        library only accepts a file path.
    """

    with open(CREDENTIALS_PATH, "w") as credentials_file:
        credentials_file.write(credentials)

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, SCOPES)

    return credentials


def main(sheet_id, range_notation_list, service_account_json):
    """ Read a google spreadsheet """

    credentials = get_credentials(service_account_json)

    if range_notation_list:
        range_notation_list = json.loads(range_notation_list)
    else:
        range_notation_list = ["A:B"]

    service = build('sheets', 'v4', credentials=credentials)
    result = None

    try:
        result = service.spreadsheets().values().batchGet(
        spreadsheetId=sheet_id, ranges=range_notation_list).execute()
    except Exception:
        result = None

    os.remove(CREDENTIALS_PATH)
    return result
