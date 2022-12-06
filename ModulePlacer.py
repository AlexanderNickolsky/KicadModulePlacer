from math import *
import pcbnew
import wx
import os
import re

class ModulePlacer(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "Module placer"
        self.category = "Modify PCB"
        self.description = "Place modules using coordinates file"
        #self.icon_file_name = os.path.join(os.path.dirname(__file__), "./round_keepout_area.png")
        #self.show_toolbar_button = True

    def processFile(self,pathname):
        with open(pathname, 'r') as f:
           content = f.readlines()
           content = [x.strip() for x in content]
           for line in content:
               mc = re.split("\s+",line)
               if len(mc) >= 3:
                   module = self.pcb.FindFootprintByReference(mc[0])
                   if module != None:
                     module.SetPosition(pcbnew.wxPointMM(float(mc[1]),float(mc[2])))
                     if len(mc) == 4:
                        module.SetOrientationDegrees(float(mc[3]))
               else:
                   wx.LogError("|".join(mc))


    def Run(self):
        self.pcb = pcbnew.GetBoard()
        projectdir = os.path.dirname(self.pcb.GetFileName())
        with wx.FileDialog(None, "Open file", defaultDir = projectdir, wildcard="txt files (*.txt)|*.txt|all files (*)|*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

        # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.processFile(pathname)
        self.pcb.GetConnectivity().RecalculateRatsnest()
