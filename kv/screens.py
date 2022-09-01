from py.config.mainImports import *
from kv.widgets import *

#Loads kivy screenmanager file that has the entire application static UI/UX
Builder.load_file("kv/ScreenManagement.kv")

#First screen on app open, complete overview of all machines
class MainOverview(Screen):

    #Object variable for button binding / screen switching in functions
    manager = ObjectProperty(None)

    #Varables, selected machine is for the app to know which machine is
    #active in sub-screens
    #app is used in this screens definitions
    selectedMachine = StringProperty()
    app = App.get_running_app()


    #Runs on screen open
    def start(self, **kwargs):

        #Schedules loadMachines to run 1 time
        Clock.schedule_once(self.loadMachines)

    #Loads all machines from db and creates a Kivy widget for each machine in db
    def loadMachines(self, dt):

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

            #Kivy widget group, some widgets are custom classes which are named at the top of the ScreenManagement.kv file
            machineButtonGroup = Builder.load_string('''
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
            #Add above widget to layout
            self.ids["machineButtons"].add_widget(machineButtonGroup)
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

    #This runs on screen exit, will not only save data, but also allow an easier refresh incase of new machines added or old ones deleted
    def stop(self):
        #Clears all child widgets of the GridLayout with the respective id
        self.ids["machineButtons"].clear_widgets()

class MainOverviewDelete(Screen):

    #Object variable for button binding / screen switching in functions
    manager = ObjectProperty(None)

    #Varables, selected machine is for the app to know which machine is active in sub-screens
    #app is used in this screens definitions
    selectedMachine = StringProperty()
    app = App.get_running_app()


    #Runs on screen open
    def start(self, **kwargs):

        #Schedules loadMachines to run 1 time
        Clock.schedule_once(self.loadMachines)
        #Unbinds and re-Bind back button to go back to the Overview
        Window.unbind(on_keyboard=self.Android_back_click)
        Window.bind(on_keyboard=self.Android_back_click)

    #Loads all machines from db and creates a Kivy widget for each machine in db
    def loadMachines(self, dt):

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

            #Kivy widget group, some widgets are custom classes which are named at the top of the ScreenManagement.kv file
            machineButtonGroup = Builder.load_string('''
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
            #Add above widget to layout
            self.ids["machineButtons"].add_widget(machineButtonGroup)
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

    #This runs on screen exit, will not only save data, but also allow an easier refresh incase of new machines added or old ones deleted
    def stop(self):
        #Clears all child widgets of the GridLayout with the respective id
        self.ids["machineButtons"].clear_widgets()

    #This callback binds the back/esc key to the previous page, and when returned true, will go to that page
    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='MainOverview'
            return True

    def deleteSelectedMachines(self):

        toggles = []
        for child in self.ids["machineButtons"].children:
            if isinstance(child, ToggleBoxLayout):
                if child.state == 'down':
                    toggles.append(child.children[1].children[0].text)

        for machine in toggles:
            selectedMachine = Machine(machine)
            selectedMachine.trashMachine()

#Dynamic status page for the selected machine. Loads data based upon the
#name of the machine selected
class MachineStatusPage(Screen):

    #Object variable for button binding / screen switching in functions
    manager = ObjectProperty(None)

    #For some reason I wasn't able to use Machine_Name = MainOverview.selectedMachine, so this is a workaround.
    #Collects the selected machine from the overview to be able to pull and display the corresponding data.
    selectedMachine = MainOverview.selectedMachine
    Machine_Name = selectedMachine

    #Job related variables
    Part_Name = StringProperty()
    Part_Desc = StringProperty()
    Parts_Needed = StringProperty()
    Time_Per_Part = StringProperty()

    #Bar feeder related variables
    Oal = StringProperty()
    Cut_Off_Width = StringProperty()
    Bar_Length = StringProperty()
    Bar_Parameter = StringProperty()

    #Math Variables
    Completion_Time = StringProperty()
    Time_Left = StringProperty()
    Parts_Left = StringProperty()

    #Runs on screen open
    def start(self, **kwargs):
        #Starts coundown() loop
        Clock.schedule_once(self.countdown)
        #Unbinds and re-Bind back button to go back to the Overview
        Window.unbind(on_keyboard=self.Android_back_click)
        Window.bind(on_keyboard=self.Android_back_click)

    #This callback binds the back/esc key to the previous page, and when returned true, will go to that page
    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='MainOverview'
            return True

    def countdown(self, dt):
        #Gets current job data before loop incase if job is finished or not active
        self.getCurrentJob()
        try:
            #Runs a loop by scheduling countdown() to run every 0.5 seconds basically automatically refreshing the data and counting down parts / time
            if int(self.Parts_Left) > 0:
                Clock.schedule_once(self.countdown, 0.5)
            else:
                self.getCurrentJob()
        except:
            self.getCurrentJob()

    #Runs on screen leave, will stop all clock activity relating to countdown() to avoid events stacking and crashing the app
    def stop(self):
        Clock.unschedule(self.countdown)

    #Pulls all job information from the local db by using the machine name selected from the main overview
    #Also does the math for the time left and parts left calculations
    def getCurrentJob(self, *args):

        #Creates new class with just the machine name
        currentJob = Job(self.Machine_Name)

        #Tries to pull all information below from the database and returns none/0 if there is no entry
        try:
            self.Part_Name = str(currentJob.grabJob(0))
            self.Part_Desc = str(currentJob.grabJob(1))
            self.Parts_Needed = str(currentJob.grabJob(4))
            self.Time_Per_Part = str(currentJob.grabJob(3))
            self.Completion_Time = str(currentJob.grabJob(5))

            self.Oal = str(currentJob.grabJob(7))
            self.Cut_Off_Width = str(currentJob.grabJob(8))
            self.Bar_Length = str(currentJob.grabJob(9))
            self.Bar_Parameter = str(currentJob.grabJob(10))
        except:
            self.Part_Name = "None"
            self.Part_Desc = "None"
            self.Time_Per_Part = "None"
            self.Parts_Needed = "None"
            self.Completion_Time = "None"

            self.Oal = "0"
            self.Cut_Off_Width = "0"
            self.Bar_Length = "0"
            self.Bar_Parameter = "0"

        #Creates another class with the updated information pulled from the db above
        updatedCurrentJob = Job(self.Machine_Name, " ", " ", self.Time_Per_Part, self.Parts_Needed)

        #Does the math for the parts left
        try:
            if updatedCurrentJob.partsLeft() > 0:
                self.Parts_Left = str(updatedCurrentJob.partsLeft())
            else:
                self.Parts_Left = "0"
        except:
            self.Parts_Left = "None"

        #Creates yet another class to include the parts left from the updatedCurrentJob class
        jobTimeLeft = Job(self.Machine_Name, " ", " ", self.Time_Per_Part, self.Parts_Left)

        #Does the math for the time left based on if there are any parts left
        try:
            if updatedCurrentJob.partsLeft() > 0:
                
                timeLeftDict = jobTimeLeft.timeLeft()
                
                if timeLeftDict['Days'] == 0 and timeLeftDict['Hours'] == 0 and timeLeftDict['Minutes'] == 0:
                    self.Time_Left = str(timeLeftDict['Seconds'])
                    
                elif timeLeftDict['Days'] == 0 and timeLeftDict['Hours'] == 0:
                    self.Time_Left = str(timeLeftDict['Minutes']) + ":" + str(timeLeftDict['Seconds'])
                    
                elif timeLeftDict['Days'] == 0:
                    self.Time_Left = str(timeLeftDict['Hours']) + ":" + str(timeLeftDict['Minutes']) + ":" + str(timeLeftDict['Seconds'])
                    
                else:
                    self.Time_Left = str(timeLeftDict['Days']) + ":" + str(timeLeftDict['Hours']) + ":" + str(timeLeftDict['Minutes']) + ":" + str(timeLeftDict['Seconds'])
                
            else:
                self.Time_Left = "0"
        except:
            self.Time_Left = "None"


#Form to add new machines to the app/database
class AddMachinePage(Screen):

    #Object variable for button binding / screen switching in functions
    manager = ObjectProperty(None)

    #Runs on screen open
    def start(self, **kwargs):
        #Unbinds and re-Bind back button to go back to the Overview
        Window.unbind(on_keyboard=self.Android_back_click)
        Window.bind(on_keyboard=self.Android_back_click)

    #This callback binds the back/esc key to the previous page, and when returned true, will go to that page
    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='MainOverview'
            return True

    #Variables used for collecting data for uploading to db
    machineName = StringProperty()
    desc = StringProperty()
    machineType = StringProperty()
    location = StringProperty()

    #Function to run on submit press
    def addNewMachine(self):
        #Creates new class with the collected information
        newMachine = Machine(self.machineName, self.desc, self.machineType, self.location)
        #Posts all collected data to db
        newMachine.postMachine()

#Form to add new jobs to the respective machine
class AddJobPage(Screen):

    #Object variable for button binding / screen switching in functions
    manager = ObjectProperty(None)

    def start(self, **kwargs):
        #Unbinds and re-Bind back button to go back to the Overview
        Window.unbind(on_keyboard=self.Android_back_click)
        Window.bind(on_keyboard=self.Android_back_click)

    #This callback binds the back/esc key to the previous page, and when returned true, will go to that page
    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='MachineStatusPage'
            return True

    #Uses the machine name that was originally selected from the Main Overview so the job is added to the right machine
    selectedMachine = MainOverview.selectedMachine
    Machine_Name = selectedMachine

    #Job related variables
    Part_Name = StringProperty()
    Part_Desc = StringProperty()
    Parts_Needed = StringProperty()
    Time_Per_Part = StringProperty()

    #Bar feeder related variables
    Oal = StringProperty()
    Cut_Off_Width = StringProperty()
    Bar_Length = StringProperty()
    Bar_Parameter = StringProperty()

    #Definition to run on submit press
    def addNewJob(self):
        #Creates class for the new job with all the collected information
        newJob = Job(self.Machine_Name, self.Part_Name, self.Part_Desc, self.Parts_Needed, self.Time_Per_Part, "", self.Oal, self.Cut_Off_Width, self.Bar_Length, self.Bar_Parameter)
        #Posts all collected data to db
        newJob.postJob()