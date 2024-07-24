from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultantForm
from .models import Consultant
import pandas as pd
import smtplib
from . import sending_mail

df = pd.read_csv('mycsv.csv')

grouped_df = df.groupby('ConsultantName').agg({'ConsultantMail': 'first'}).reset_index()


Consultant.objects.all().delete()



def select_consultant(request):
    if Consultant.objects.count() == 0:
        for _, row in grouped_df.iterrows():
            consultant_name = row['ConsultantName']
            consultant_email = row['ConsultantMail']
            Consultant.objects.create(name=consultant_name, mail=consultant_email)

    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid():
            consultant = form.cleaned_data['consultant']
            return redirect('option_page', consultant_id=consultant.id)
    else:
        form = ConsultantForm()
    return render(request, 'select_consultant.html', {'form': form})


def option_page(request, consultant_id):
    consultant = get_object_or_404(Consultant, id=consultant_id)
    return render(request, 'option_page.html', {'consultant': consultant})


def selected_consultant(request, consultant_id):
    consultant = get_object_or_404(Consultant, id=consultant_id)
    filtered_df = df[df['ConsultantName'] == consultant.name]
    message = filtered_df.to_string()
    #print (message)
    sending_mail.send_to_consultant(consultant.mail , message)
    return render(request, 'selected_consultant.html', {'consultant': consultant})

def selected_consultant_and_assistant(request , consultant_id):
    consultant = get_object_or_404(Consultant, id=consultant_id)
    # Filter the DataFrame for the selected consultant's name
    filtered_df = df[df['ConsultantName'] == consultant.name]
    unique_assistant_mails = filtered_df['AssistantMail'].unique()
    #print(unique_assistant_mails)
    message = filtered_df.to_string()
    #print (message)
    sending_mail.send_to_consultant_and_assistant(consultant.mail ,unique_assistant_mails , message)
    return render(request, 'selected_consultant.html', {'consultant': consultant})