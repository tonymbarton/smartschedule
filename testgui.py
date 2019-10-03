import kivy
import athenahealthapi
import datetime
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

####################################################################################################
# Setup
####################################################################################################
key = '5nqrgwaayz3nh5p2cyg4za4v'
secret = 'zavWQDf4BjaR2RS'
version = 'preview1'
practiceid = 1128700

api = athenahealthapi.APIConnection(version, key, secret, practiceid)

#Get provider list
providerlist = api.GET('providers')
providers = providerlist['providers']
providernametoid = {}
providerslastname = []
for x in providers:
    #print(x)
    providerid = x['providerid']
    providername = x['lastname']
    providernametoid.update({providername:providerid})
    providerslastname.append(providername)

#Get department list

departments_get = api.GET('/departments')
departments = (departments_get['departments'])
departmentnametoid = {}
departmentnamelist = []
for x in departments:
    departmentid = x['departmentid']
    departmentname = str(x['name'])
    departmentnametoid.update({departmentname:departmentid})
    departmentnamelist.append(departmentname)
print(departmentnametoid)
print(departmentnamelist)

dropdown = DropDown()
mainbutton = Button()
dropdown2 = DropDown()
mainbutton2 = Button()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):

        global dropdown
        global mainbutton
        global providernametoid
        global providerslastname
        global dropdown2
        global mainbutton2
        global departmentnametoid
        global departmentnamelist
        
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Provider: "))
        for y in providerslastname:
            self.provider = Button(text=y, size_hint_y=None, height=25)
            self.provider.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(self.provider)
        mainbutton = Button(text='Provider', size_hint=(None, None), height=25)
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, y: setattr(mainbutton, 'text', y))
        self.inside.add_widget(mainbutton)

        self.inside.add_widget(Label(text="Department: "))
        for y in departmentnamelist:
            self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.provider.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.provider.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
