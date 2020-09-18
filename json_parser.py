#TO DO: 
# Make the file path url in the window and browsable


import PySimpleGUI as sg
import json
import os

# All the data labels - you can add, delete or rename them freely 
labels = ["Name", "Surname"]

# Get labels and put them onto screen
label_column = []
for label in labels:
    label_column.append([sg.Text(label)])

# Get labels and put as much input field as the length of labels[]
input_column = []
for label in labels:
    # key=label is the same as id="" in HTML/JS
    input_column.append([sg.InputText(key=label)])

# Layout schema - left column with labels, right column with input and button to add to the file
layout = [
    [
        sg.Column(label_column),
        sg.Column(input_column),
        sg.Button('Add', key='add')
    ]
]

# Create the window
window = sg.Window("JSON Parser", layout)

# Instantiate the data dictionary which will be added to the file
data_to_add = {}

# Check how much data has been put
counter = 0

# Get the file path
filePath = "C:/Users/ddor/Desktop/python/json_gui_parser/data.json"

# Set checker to see if the file was updated (to delete the comma)
is_edited = False

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        if is_edited:
            with open(filePath, 'rb+') as comma:
                comma.seek(-3, os.SEEK_END)
                comma.truncate()
        break
    # Append to file if user clicks the button "add"
    if event == 'add':
        is_edited = True
        with open(filePath, 'a') as file:
            filesize = os.stat(filePath).st_size
            print(filesize)
            if counter == 0 and filesize != 0:
                file.write(',')
                file.write('\n')
            # Append data to dictonary
            for label in labels:
                data_to_add[label] = values[label]
            # Append dictonary to output file
            file.write(json.dumps(data_to_add, sort_keys=False, indent=4))
            file.write(',')
            file.write('\n')
            counter += 1
        # Clear the input fields
        for label in labels:
            window[label]('')
        
# Window closes on while break
window.close()

# After adding the data, you need to wrap it in the [] brackets