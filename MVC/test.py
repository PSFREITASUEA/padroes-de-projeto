from tkinter import *
from DJView import DJView
from beatModel import BeatModel
from beatController import BeatController

beatModel = BeatModel()
beatController = BeatController(beatModel)

beatController.view.runView()