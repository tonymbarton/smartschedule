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

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 1

        self.inside = Screen()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside) # Add the interior layout to the main

        self.submit = Button(text="Submit", font_size=40)
       
        self.add_widget(self.submit) # Add the button to the main layout 
    
class dropdown_1():

# create a dropdown with provider buttons
    global dropdown
    global mainbutton
    global providernametoid
    global providerslastname
    for y in providerslastname:
        # When adding widgets, we need to specify the height manually
        # (disabling the size_hint_y) so the dropdown can calculate
        # the area it needs.

        btn = Button(text=y, size_hint_y=None, height=25)

        # for each button, attach a callback that will call the select() method
        # on the dropdown. We'll pass the text of the button as the data of the
        # selection.
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))

        # then add the button inside the dropdown
        dropdown.add_widget(btn)

    # create a big main button
    mainbutton = Button(text='Provider', size_hint=(None, None), height=25)

    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)

    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown.bind(on_select=lambda instance, y: setattr(mainbutton, 'text', y))

    #runTouchApp(mainbutton)

class dropdown_2():

# create a dropdown with provider buttons
    global dropdown2
    global mainbutton2
    global departmentnametoid
    global departmentnamelist
    for y in departmentnamelist:
        # When adding widgets, we need to specify the height manually
        # (disabling the size_hint_y) so the dropdown can calculate
        # the area it needs.

        btn2 = Button(text=y, size_hint_y=None, height=25)

        # for each button, attach a callback that will call the select() method
        # on the dropdown. We'll pass the text of the button as the data of the
        # selection.
        btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))

        # then add the button inside the dropdown
        dropdown2.add_widget(btn2)

    # create a big main button
    mainbutton2 = Button(text='Department', size_hint=(None, None), height=25)

    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton2.bind(on_release=dropdown2.open)

    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown2.bind(on_select=lambda instance, y: setattr(mainbutton2, 'text', y))

    
    runTouchApp(mainbutton2)


class MyApp(App):

    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    MyApp().run()
