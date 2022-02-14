from collections import Counter

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

from django.contrib import messages

import pandas as pd
import csv

# Create your views here.


#dict ={}
def index(request):

    context = {}
    global nodeid
    global startDate
    global endDate

    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        nodeid = 'NodeId'
        startDate = 'StartDate'
        endDate = 'EndDate'

        print(nodeid)

        #check if this file ends with csv
        if uploaded_file.name.endswith('.csv'):
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file) #gets the name of the file
            print(name)


            #we need to save the file somewhere in the project, MEDIA
            #now lets do the savings

            d = os.getcwd() # how we get the current dorectory
            file_directory = d+'\media\\'+name #saving the file in the media directory
            print(file_directory)
            readfile(file_directory)

            request.session['nodeid'] = nodeid

            if nodeid not in data.axes[1]:
                messages.warning(request, 'Please write the column name correctly')
            else:
                print(nodeid)
                return redirect(results)

        else:
            messages.warning(request, 'File was not uploaded. Please use .csv file extension!')


    return  render(request, 'index.html', context)


            #project_data.csv
def readfile(filename):



    #we have to create those in order to be able to access it around
    # use panda to read the file because i can use DATAFRAME to read the file
    #column;culumn2;column
    global rows,columns,data,my_file
     #read the missing data - checking if there is a null

    my_file = pd.read_csv(filename, engine='python')

    data = pd.DataFrame(data=my_file, index=None)
    print(data)

    rows = len(data.axes[0])
    columns = len(data.axes[1])


# a script to open and read a csv file in django
def results(request):
    # prepare the visualization
    message = 'There are ' + str(rows) + ' rows and ' + str(columns) + ' columns.'
    messages.warning(request, message)

    nodeID_dict  = []
    startDate_dict  = []
    endDate_dict  = []
    for x in data[nodeid]:
       nodeID_dict.append(x)
    for y in data[startDate]:
       startDate_dict.append(y)
    for z in data[endDate]:
       endDate_dict.append(z)


    print('Node ID', nodeID_dict)
    print('Start Date', startDate_dict)
    print('Start Date', endDate_dict)

    context = {
        'nodeid': nodeID_dict,
        'startdate': startDate_dict,
        'enddate': endDate_dict,
    }

    return render(request, 'results.html', context)