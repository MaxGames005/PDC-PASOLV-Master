from extensoes.Dependencies import *
from extensoes.glib import *


"""
-------------------/ /--------------------------------------------------------------------------------------------------
QT Aplication
"""


class PasolvMain(QtWidgets.QMainWindow,QOpenGLWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_PasolvMainWindow()
        self.ui.setupUi(self)
        self.changed = False
        self.formula_label_text = self.ui.FormulaLabel.text()
        self.formula_result_text = self.ui.FormulaResult.text()
        self.form = Formula(self)
        self.varmode = False
        self.funcaoatual = None
        self.formula_input_text = self.ui.FormulaInput.text()
        self.ui.AddFormula.clicked.connect(lambda: self.AddFormulaToList(self.ui.FormulaList, self.ui.FormulaInput))
        self.ui.FormulaInput.returnPressed.connect(lambda: self.AddFormulaToList(self.ui.FormulaList,
                                                                                 self.ui.FormulaInput))
        self.ui.FormulaInput.textChanged.connect(self.InputFormula)
        self.ui.FormulaList.clicked.connect(self.ListsOfFormulas)
        self.initializeGL()
        self.dci = {}

    def ListsOfFormulas(self, item):
        self.varmode = True
        fshow = f'{self.formula_label_text} {item.data()}'
        self.ui.FormulaLabel.setText(fshow)
        fname = item.data()[:item.data().find('(')].replace(' ', '')
        self.funcaoatual = self.dci[fname]


    def mousePressEvent(self, event):
        self.varmode = False
        self.ui.FormulaResult.setText(self.formula_result_text)
        self.ui.FormulaLabel.setText(self.formula_label_text)
        if not self.ui.FormulaInput.text():
            self.NewInputRoutine()

    """<PyQt5.QtCore.QModelIndex object at 0x0000020045F95048>"""
    def InputFormula(self):
        if not self.changed:
            self.ui.FormulaInput.clear()
            self.changed = True

    def NewInputRoutine(self):
        self.ui.FormulaInput.clear()
        self.ui.FormulaInput.setText(self.formula_input_text)
        self.ui.FormulaInput.textChanged.connect(self.InputFormula)
        self.changed = False

    def AddFormulaToList(self, List, Input):
        if not self.varmode:

            self.form.add(Input.text())
            fobj, fname, farg, fbody = self.form.get()
            if fname not in self.dci and fname and farg:
                List.addItem(f"{fname+'('+farg+')'}: {fbody}")
            self.dci[fname] = fobj
            self.NewInputRoutine()
        else:
            if self.varmode:
                self.addArgToFunction(Input.text(), self.funcaoatual)

    def addArgToFunction(self, args, funsc):
        if self.varmode:
            self.ui.FormulaResult.setText(f'{self.formula_result_text} {self.form.varadd_andgetresult(args, funsc)}')
        pass


APP = "Aplication"


class QtRun:
    def __getattr__(self, name):
        if name not in self.__dict__:
            if "Main" in name:
                self.__dict__["app"] = QtWidgets.QApplication(sys.argv)
                self.__dict__[APP] = eval(name)()
                self.__dict__[APP].show()
                sys.exit(self.__dict__["app"].exec())






"""
-------------------/ /--------------------------------------------------------------------------------------------------
Initializer
"""


if __name__ == "__main__":
    pass
    #QtRun().PasolvMain


"""
Button
background_color             cor de fundo do botao                              0
background_disabled_down     imagem do botao desabilitado pressionado           1
background_disabled_normal   imagem do botao desabilitado normal                2
background_down              imagem do botao pressionado                        3
background_normal            imagem do botao normal                             4
border                       is a ListProperty and defaults to (16, 16, 16, 16) 5
"""
