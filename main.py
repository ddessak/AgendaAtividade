from desempenho import Desempenho
from PyQt5 import QtGui, uic, QtWidgets
from aluno import Alunos
from assunto import Assunto
from atividade import Atividade
from consulta_aluno import Consulta_Aluno
from consulta_assunto import Consulta_Assunto
from consulta_atividade import Consulta_Atividade
from desempenho import Desempenho
from home import situacao

app = QtWidgets.QApplication([])
Home = uic.loadUi("Tela/Home.ui")
Aluno = uic.loadUi("Tela/Aluno.ui")


def btCadastroAluno():
    aluno = Alunos
    aluno.telaAluno()

def btCadastroAssunto():
    assunto = Assunto
    assunto.telaAssunto()  

def btCadastroAtividade():
    atividade = Atividade
    atividade.telaAtividade()

def btConsultaAluno():
    consultaAluno = Consulta_Aluno
    consultaAluno.telaConsultaAluno()

def btConsultaAssunto():
    consultaAssunto = Consulta_Assunto
    consultaAssunto.telaConsultaAssunto()

def btConsultaAtividade():
    consultaAtividade = Consulta_Atividade
    consultaAtividade.telaConsultaAtividade()

def btCadastroDesempenho():
    desempenho = Desempenho
    Desempenho.telaDesempenho()
    
Home.show()
Home.Bt_CadastroAluno.clicked.connect(btCadastroAluno)
Home.Bt_CadastroAssunto.clicked.connect(btCadastroAssunto)
Home.Bt_CadastroAtividade.clicked.connect(btCadastroAtividade)
Home.Bt_Consultar_Aluno.clicked.connect(btConsultaAluno)
Home.Bt_Consultar_Assunto.clicked.connect(btConsultaAssunto)
Home.Bt_Consultar_Atividade.clicked.connect(btConsultaAtividade)
Home.Bt_CadastroDesempenho.clicked.connect(btCadastroDesempenho)

app.exec()