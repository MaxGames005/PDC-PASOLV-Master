class Paths:
    def __init__(self):
        self.local = __file__.replace("GetEnvPath.py","")
        self.Bin = self.local + "Bin\\"
        self.Recursos = self.local + "Recursos\\"
        self.App = self.local + "App\\"
        self.Controle = self.local + "Controle\\"
        self.Scripts = self.local + "Scripts\\"
        self.ScriptsFolder = self.Scripts + "ScriptsFolde\\"
        self.Data = self.local + "Data\\"
        self.AppAssist = self.Bin + "AppAssist\\"
        self.AppPages = self.Bin + "AppPages\\"
        self.Extensoes = self.local + "\\Extensoes\\"
        self.Screen = self.local + "Screen\\"
        self.Setup = self.local + "Setup\\"
        self.Interfaces = self.local + "Interfaces\\"
        self.ITMG = self.local + "ITMG\\"
        self.MainInterface = self.ITMG+"MainInterface\\"


G_PATH_CLASS = Paths()
GPC = Paths()



