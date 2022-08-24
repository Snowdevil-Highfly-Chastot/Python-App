from py.config.mainImports import *

#The ButtonBoxLayout is used to encase the machine buttons on the Overview,
#and have clicking attributes
class ButtonBoxLayout(ButtonBehavior, BoxLayout):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))

#The ToggleBoxLayout is used in the Machine Delete screen.
#It is the same as ButtonBoxLayout except has toggle functionality
#to allow multiple machine selection for deleting.
class ToggleBoxLayout(ToggleButtonBehavior, BoxLayout):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))

#UiButton class widget is used in all of the single text buttons throughout
#the application
class UiButton(ButtonBehavior, Label):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))

#This is a custom widget built outside of a class
#It is the Machine Button widget for all added machines
MachineButton = Builder.load_string('''
ButtonBoxLayout:
    orientation: 'vertical'
    padding: self.width / 20, self.width / 30
    on_release:
        app.root.current = 'MachineStatusPage'
        app.root.current_screen.selectedMachine = machineLabel.text
    BoxLayout:
        orientation: 'horizontal'
        Label:
            id: machineLabel
            text: "Machine"
            font_size: self.width / 15
            text_size: self.size
            halign: 'center'
            valign: 'top'
    BoxLayout:
        orientation: 'vertical'
        spacing: self.width / 20
        HorizontalDataLayout:
            InputLabel:
                text: "Current Job: "
            OutputLabel:
                text: "None"
        HorizontalDataLayout:
            InputLabel:
                text: "Completion Time: "
            OutputLabel:
                text: "None"
    ''')

ToggleMachineButton = Builder.load_string('''
ToggleBoxLayout:
    orientation: 'vertical'
    padding: self.width / 20, self.width / 30
    BoxLayout:
        orientation: 'horizontal'
        Label:
            id: machineLabel
            text: "Machine"
            font_size: self.width / 15
            text_size: self.size
            halign: 'center'
            valign: 'top'
    BoxLayout:
        orientation: 'vertical'
        spacing: self.width / 20
        HorizontalDataLayout:
            InputLabel:
                text: "Current Job: "
            OutputLabel:
                text: "None"
        HorizontalDataLayout:
            InputLabel:
                text: "Completion Time: "
            OutputLabel:
                text: "None"
''')

#Loads all machines from db and creates a Kivy widget for each machine in db
def loadMachines(self):

    #Machine names collects all machine names from database
    machineNames = []
    #test index and machine count are used for collecting the total quantity of machines in the db
    testindex = 0
    machineCount = 0
    #index is the current machine being pulled in the loop below
    index = 0

    try:
        #This loop will run until error, the error hit will determine how many machines are in db
        while True:
            readMachines(testindex)
            testindex += 1
            machineCount += 1
    except:
        pass

    #This loop will add all the machine names to the list above and will stop before error
    while index < machineCount:
        machineNames.append(readMachines(index))
        index += 1

    #For every machine in the list above, this loop will create the kivy widgets inside the GridLayout with the respective id
    for machine in machineNames:

        #Add custom built widget from widgets.py to layout by using the MachineButton variable it was set too
        self.ids["machineButtons"].add_widget(MachineButton)
        #Change header to the machine name
        self.ids["machineButtons"].children[0].children[1].children[0].text = machine
        #Grab current job
        currentMachineJob = Job(machine)
        #Set text to Job Name
        try:
            jobName = str(currentMachineJob.grabJob(0))
            jobNameTruncate = (jobName[:19] + '..') if len(jobName) > 19 else jobName
            self.ids["machineButtons"].children[0].children[0].children[1].children[0].text = jobNameTruncate
        except:
            self.ids["machineButtons"].children[0].children[0].children[1].children[0].text = "None"

        #Set text to completion time
        try:
            self.ids["machineButtons"].children[0].children[0].children[0].children[0].text = str(currentMachineJob.grabJob(5))
        except:
            self.ids["machineButtons"].children[0].children[0].children[1].children[0].text = "None"

#Loads all machines from db and creates a Kivy widget for each machine in db
#Has different clicking features since deletion selection is different than normal
def loadMachinesForDeleting(self):

    #Machine names collects all machine names from database
    machineNames = []
    #test index and machine count are used for collecting the total quantity of machines in the db
    testindex = 0
    machineCount = 0
    #index is the current machine being pulled in the loop below
    index = 0

    try:
        #This loop will run until error, the error hit will determine how many machines are in db
        while True:
            readMachines(testindex)
            testindex += 1
            machineCount += 1
    except:
        pass

    #This loop will add all the machine names to the list above and will stop before error
    while index < machineCount:
        machineNames.append(readMachines(index))
        index += 1

    #For every machine in the list above, this loop will create the kivy widgets inside the GridLayout with the respective id
    for machine in machineNames:

        #Add custom built widget from widgets.py to layout by using the MachineButton variable it was set too
        self.ids["machineButtons"].add_widget(ToggleMachineButton)
        #Change header to the machine name
        self.ids["machineButtons"].children[0].children[1].children[0].text = machine
        #Grab current job
        currentMachineJob = Job(machine)
        #Set text to Job Name
        try:
            jobName = str(currentMachineJob.grabJob(0))
            jobNameTruncate = (jobName[:19] + '..') if len(jobName) > 19 else jobName
            self.ids["machineButtons"].children[0].children[0].children[1].children[0].text = jobNameTruncate
        except:
            self.ids["machineButtons"].children[0].children[0].children[1].children[0].text = "None"

        #Set text to completion time
        try:
            self.ids["machineButtons"].children[0].children[0].children[0].children[0].text = str(currentMachineJob.grabJob(5))
        except:
            self.ids["machineButtons"].children[0].children[0].children[0].children[0].text = "None"