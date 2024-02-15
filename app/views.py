from django.shortcuts import render
import csv
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_bank(self):

    with open('C:\\Users\\CHAITHANYA\\OneDrive\\Desktop\\Django projects\\hanuman\\Scripts\\project41\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()

    return HttpResponse('Bank data is inserted successfully')


def insert_branch(self):

    with open('C:\\Users\\CHAITHANYA\\OneDrive\\Desktop\\Django projects\\hanuman\\Scripts\\project41\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)

        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifsc=i[1]
                branch=i[2]
                address=i[3]
                contact=i[4]
                city=i[5]
                district=i[6]
                state=i[7]
                BO=Branch(bank_name=BO[0],IFSC=ifsc,branch=branch,address=address,contact=contact,city=city,district=district,state=state)
                BO.save()

        return HttpResponse('Branh data is inserted successfully')




