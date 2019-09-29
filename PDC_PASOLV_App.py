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
        self.operate_mode = False
        self.funcaoatual = None
        self.formula_input_text = self.ui.FormulaInput.text()
        self.ui.AddFormula.clicked.connect(lambda: self.add_to_list(self.ui.FormulaList,
                                                                    self.ui.FormulaList_2,
                                                                    self.ui.FormulaInput))
        self.ui.FormulaInput.returnPressed.connect(lambda: self.add_to_list(self.ui.FormulaList,
                                                                            self.ui.FormulaList_2,
                                                                            self.ui.FormulaInput))
        self.ui.FormulaList.clicked.connect(self.set_operation)
        self.ui.FormulaList.clicked.connect(self.operate)
        self.ui.VariavelInput.returnPressed.connect(lambda: self.add_var(self.ui.FormulaList,
                                                                        self.ui.FormulaList_2,
                                                                        self.ui.VariavelInput))
        self.ui.AddVariavel.clicked.connect(lambda: self.add_var(self.ui.FormulaList,
                                                                 self.ui.FormulaList_2,
                                                                 self.ui.VariavelInput))
        self.ui.RemoveItem.clicked.connect(self.remove)
        self.initializeGL()
        self.dci = {}
        self.ItemsList = {}
        self.selected_item = None
        self.VarList = {}
        self.ui.AboutCreator.triggered.connect(self.about_creator)


    def set_operation(self, item):
        self.selected_item = item.data(5)

    def operate(self, item):
        self.ui.FormulaLabel.setText(str(Eqt.show_function(item.data(-1))))
        self.operate_mode = True

    def add_var(self, List, List2, Input):
        if Input.text():
            if Eqt.add_var(Input.text()):
                self.ui.FormulaResult.setText(Eqt.add_var(Input.text()))
            else:
                if not Eqt.last_var()[0] in self.VarList:
                    item = QListWidgetItem(QIcon(GPC.Recursos + 'varicon.png'),
                                           Eqt.last_var()[2])
                    item.setData(-1, Eqt.last_var()[0])
                    item.setData(4, Eqt.last_var()[1])
                    item.setData(5, item)
                    List.addItem(item)
                    List2.addItem(item)
                    self.VarList[Eqt.last_var()[0]] = self.find_match(List, Eqt.last_var()[0])
                    Input.clear()
                    self.ui.FormulaResult.setText(self.formula_result_text)
                else:
                    self.VarList[Eqt.last_var()[0]].setData(4, Eqt.last_var()[1])
                    self.VarList[Eqt.last_var()[0]].setData(0, Eqt.last_var()[2])
                    Input.clear()
                    self.ui.FormulaResult.setText(self.formula_result_text)

    def mousePressEvent(self, event):
        self.operate_mode = False
        self.ui.FormulaLabel.setText(self.formula_label_text)
        self.ui.FormulaResult.setText(self.formula_result_text)
        self.ui.FormulaList.clearSelection()
        self.selected_item = None

    def format_formula_input(self):
        pass

    def formula_input_routine(self):
        pass

    def add_to_list(self, List, List2, Input):
        if Input.text():
            if not self.operate_mode:
                if Eqt.add(Input.text()):
                    self.ui.FormulaResult.setText(Eqt.add(Input.text()))
                else:
                    if Eqt.last_added()[0] not in [keys for keys in self.ItemsList]:
                        item = QListWidgetItem(QIcon(GPC.Recursos + 'functionicon.png'), Eqt.last_added()[1].replace('=', ' = '))
                        item.setData(-1, Eqt.last_added()[0])
                        item.setData(4, lambda args: Eqt.operate(Eqt.last_added()[0], args))
                        item.setData(5, item)
                        List.addItem(item)
                        List2.addItem(item)
                        self.ItemsList[Eqt.last_added()[0]] = self.find_match(List, Eqt.last_added()[0])
                        Input.clear()
                    else:
                        self.ItemsList[Eqt.last_added()[0]].setData(4, lambda args: Eqt.operate(Eqt.last_added()[0], args))
                        self.ItemsList[Eqt.last_added()[0]].setData(0, Eqt.last_added()[1].replace('=', ' = '))
                        Input.clear()
            else:
                string = self.ui.FormulaInput.text()
                self.ui.ResultOutPut.setText(str(Eqt.operate(self.selected_item.data(-1), string)))
                if isinstance(Eqt.operate(self.selected_item.data(-1), string), str):
                    self.mousePressEvent(None)
                self.ui.FormulaInput.clear()

    def remove(self, event):
        if self.selected_item:
            self.ui.FormulaLabel.setText(self.formula_label_text)
            self.operate_mode = False
            self.ui.FormulaList.clearSelection()
            msg = Eqt.remove(str(self.selected_item.data(-1)))
            if msg:
                print(msg)
            self.ui.FormulaList.model().removeRow(self.ui.FormulaList.row(self.selected_item))
        else:
            self.ui.ResultOutPut.setText('Nenhum Item Selecionado')

    @staticmethod
    def find_match(List, name1, ids=-1):
        for i in range(List.count()):
            if List.item(i).data(ids) == name1:
                return List.item(i)

    def addArgToFunction(self, args, funsc):
        if self.operate_mode:
            self.ui.FormulaResult.setText(f'{self.formula_result_text} {self.form.varadd_andgetresult(args, funsc)}')
        pass

    def about_creator(self, event):
        about = QMessageBox()
        about.setStyleSheet("background-color: rgb(175, 175, 175);")
        about.information(about, "Creator", "Guilherme R. Chiodi\nENFI: 2018-2019")

APP = "Aplication"


class QtRun:
    def __getattr__(self, name):
        if name not in self.__dict__:
            if "Main" in name:
                self.__dict__["app"] = QtWidgets.QApplication(sys.argv)
                self.__dict__[APP] = eval(name)()
                self.__dict__[APP].show()
                sys.exit(self.__dict__["app"].exec())


Eqt.add('f(x)=-')



"""
-------------------/ /--------------------------------------------------------------------------------------------------
Initializer
"""


if __name__ == "__main__":
    QtRun().PasolvMain




