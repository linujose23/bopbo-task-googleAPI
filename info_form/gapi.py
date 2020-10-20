from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models import Contact
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credss.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("spread").sheet1

# Extract and print all of the values
list_of_entries = sheet.get_all_records()
# print('list_of_entries:', list_of_entries)

sheet.get_all_values()

print('values', Contact.objects.values_list('Name', flat=True)
      )

row = ["I'm", "inserting", "a", "row", "into",
       "a,", "Spreadsheet", "with", "Python"]
index = 1
sheet.insert_row(row, index)
index += 1

# below code for google drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload()  # Files.insert()
