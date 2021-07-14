from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from CadastroDesempenho import combobox


class situacao:
    def home():
        Home = uic.loadUi("Tela/Home.ui")
        
        def listar(self,Home):                    
            # Mostrar os dados. 
            print("hello Word")  
            a = combobox()
            sqldesempenho = a.situacao()
            Home.tabela.setRowCount(len(sqldesempenho))
            Home.tabela.setColumnCount(5)
            Home.header = Home.tabela.horizontalHeader()
            Home.tabela.setColumnWidth(0,80)
            Home.tabela.setColumnWidth(1,100)
            Home.tabela.setColumnWidth(2,110)
            Home.tabela.setColumnWidth(3,110)
            Home.tabela.setColumnWidth(4,410)
            for i in range(0,len(sqldesempenho)):
                for j in range(0, 5):
                    Home.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(sqldesempenho[i][j])))
        
        listar()  
        print(1)  
        Home.exec()
        
