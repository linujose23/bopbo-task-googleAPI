from django.shortcuts import render
from .forms import Contact_form
from django.http import HttpResponse
from .models import Contact
from django.shortcuts import redirect
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
# Create your views here.
home_ = os.getcwd()


def FormSubmission(request):

    form = Contact_form()

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        home_ + '/info_form/credss.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("spread").sheet1

    if request.method == "POST":
        form = Contact_form(request.POST, request.FILES)
        row = []
        files_li = request.FILES.getlist('files')
        print('files', files_li)
        for file in files_li:
            print(type(file))
            myobj = Contact(0)
            myobj.files.field.upload_to = ('files/')
            print('details   :', myobj.files.field.upload_to)
            print('name', file.name)
            myobj.files = file
            myobj.save()

        # print('files', file)

        if form.is_valid():
            form.save()
            row.append(form.cleaned_data['Name'])
            row.append(form.cleaned_data['Email'])
            row.append(form.cleaned_data['Mobile'])
            row.append(form.cleaned_data['Message'])

# Below code does the authentication
# part of the code
            gauth = GoogleAuth()

            # Creates local webserver and auto
            # handles authentication.
            gauth.LocalWebserverAuth()
            drive = GoogleDrive(gauth)

            # replace the value of this variable
            # with the absolute path of the directory
            path = home_ + '/media/files/'
            print('path', path)
            # iterating thought all the files/folder
            # of the desired directory
            for x in os.listdir(path):

                f = drive.CreateFile({'title': x})
                f.SetContentFile(os.path.join(path, x))
                f.Upload()

                # os.remove(x)

            # Due to a known bug in pydrive if we
            # don't empty the variable used to
            # upload the files to Google Drive the
            # file stays open in memory and causes a
            # memory leak, therefore preventing its
            # deletion
            f = None

        else:
            print('form_errors', form.errors)

        index = 1
        sheet.insert_row(row, index)

        return render(request, 'thanks.html')

    return render(request, 'main.html', {'form': form})
