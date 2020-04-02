import rhinoscriptsyntax as rs
import System
import time

import Rhino

GH = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

dateandtimenow = time.strftime("%Y%m%d")
save_date = dateandtimenow[2:]

desktop_path = "D:\\David Kay\\Dropbox\\Desktop\\"

current_name = rs.DocumentName()

if ('_') in current_name:
	current_name = current_name.split('_',1)[1]

rhino_save_file_name = chr(34) + desktop_path + save_date + '_' + current_name + chr(34)

cmd = '-_SaveAs ' + rhino_save_file_name 

rs.Command(cmd, True)

if GH.IsEditorLoaded():
	
	import clr
	clr.AddReference('Grasshopper')
	import Grasshopper 
	
	gh_save_file_name = desktop_path + save_date + '_' + current_name.split('.')[0] + '.gh'
	
	Grasshopper.Plugin.GH_RhinoScriptInterface.SaveDocumentAs(GH, gh_save_file_name)
	
	
