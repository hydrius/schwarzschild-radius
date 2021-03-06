#!/usr/bin/python
#
# Bayesian Conspiracy

# Occams Razor Seldom Lies

from tkinter import *       # Importing the Tkinter (tool box) library
from tkinter.ttk import *
from tkinter import ttk, font


class FrontEnd():

    def __init__(self):
        self.gui = Tk()

        width = 800
        height = 600
        geometry = "800x600"
        self.gui.geometry(geometry)

        self.gui.title("Schwarzchild Radius")

        self.WidgetStyles()

        #self.topBarFrame = Frame(self.gui, height=50, padding=0, width=800, style=self.topbarFrameStyle, borderwidth=0)

        self.topBar()
        self.tabBar()
        self.sideBarPlanets()
        self.planetDetails()

    def WidgetStyles(self):
        self.topbarFrameStyle = ttk.Style().configure("Top.TFrame", background="black", bordercolor="green")
        self.topbarLabelStyle = ttk.Style().configure("Top.TLabel", foreground="white", background="black")

        self.tabButtonStyle = ttk.Style().configure("Tab.TButton", foreground="white", background="#353839",
                                                    activebackground="#353839", highlightthickness=0,
                                                    activecolor="black")
        self.tabFrameStyle = ttk.Style().configure("Tab.TFrame", background="#353839")

        ttk.Style().configure("Side.TFrame", background="black")
        ttk.Style().configure("Side.TLabel", foreground="white", background="black")



    def planetDetailsCallback(name, planet):
        self.planetDetails(planet[name])


    def topBar(self, show=True, **kawgs):

        # Styles
        # Frame
        self.tframe= Frame(self.gui, height=50, padding=0, width=800, style="Top.TFrame", borderwidth=0)
        self.tframe.pack()

        # Labels
        uLabel = Label(self.tframe, text="Username", style="Top.TLabel")
        uLabel.place(x=20,y=10)

        sLabel = Label(self.tframe, text="Score", style="Top.TLabel")
        sLabel.place(x=20,y=30)

        tLabel = Label(self.tframe, text="Time", style="Top.TLabel")
        tLabel.place(x= 700, y=10)

    def tabBar(self):

        ttk.Style().configure("Tab.TButton", foreground="white", background="#353839", activebackground="#353839",
                              highlightthickness=0, activecolor="black")
        ttk.Style().configure("Tab.TFrame", background="#353839")

        tframe = Frame(self.gui, height=25, padding = 0, width = 800, style="Tab.TFrame")
        tframe.place(x=0, y=50)
        tframe.pack()

        main = Button(tframe, text="Main", style="Tab.TButton")
        main.place(x=0,y=0)

        planet = Button(tframe, text="planet", style="Tab.TButton")
        planet.place(x=100,y=0)
        #planet.grid(row=1,column=5)

        fleet = Button(tframe, text="fleet", style="Tab.TButton")
        fleet.place(x=200,y=0)


    def sideBarPlanets(self):

        self.sframe = Frame(self.gui, height=550, width=200,padding=0, style="Side.TFrame")
        self.sframe.place(y=75,x=0)

        slabel = Label(self.sframe, text = "Planets", style="Side.TLabel", underline=True)

        f = font.Font(self.slabel, slabel.cget("font"))
        f.configure(underline = True)
        slabel.configure(font=f)
        slabel.place(x=20,y=20)

    def sidebarFleets(fleets):
        self.sframe.destyp
        fleetList = fleets.list



    def planetDetails(self, planet=None,name=None):

        ttk.Style().configure("main.TFrame", background="grey")
        ttk.Style().configure("main.TLabel", foreground="black", background="white")
        pframe = Frame(self.gui, height=550, width=600,padding=0, style="main.TFrame")
        pframe.place(y=75,x=200)

        if name is None:
            name = "Home Base of the Bayesian Conspiracy"

        plabel = Label(pframe, text=name, style = "main.TLabel", anchor="center", justify="center")
        f = font.Font(plabel,plabel.cget("font"))
        f.configure(underline=True)
        plabel.configure(font=f)
        plabel.place(x=(100),y=20)
        #plabel.pack()



    def createWidgets(self):
        print("not yet")



    def planetBox(self):
        li = "foo bar".split()

        listb = Listbox(self.gui)
        for item in li:                 # Insert each item within li into the listbox
            listb.insert(0,item)
        listb.pack()

    def main(self):
        self.gui.mainloop()



if __name__ == "__main__":
    gui = FrontEnd()
    gui.main()





