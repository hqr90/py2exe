import sys
import os
import subprocess
import tempfile
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox,
    QFileDialog, QVBoxLayout, QHBoxLayout, QMessageBox, QStackedLayout
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QMovie


def resource_path(relative_path):
    """Obter o caminho absoluto para recursos, funciona para desenvolvimento e para executáveis PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def convert_to_ico(image_path: str) -> str:
    image_path = os.path.normpath(image_path)
    _, ext = os.path.splitext(image_path)
    if ext.lower() == '.ico':
        # Se já for um arquivo .ico, retorna o caminho diretamente
        return image_path
    # Verifica se o arquivo existe
    if not os.path.isfile(image_path):
        print(f"Arquivo de imagem '{image_path}' não encontrado.")
        return ''
    # Tenta converter a imagem
    try:
        with Image.open(image_path) as img:
            # Ajusta o tamanho para 256x256 para melhor compatibilidade
            img = img.resize((256, 256), Image.ANTIALIAS)
            ico_path = os.path.splitext(image_path)[0] + '.ico'
            img.save(ico_path, format='ICO')
            print(f"Imagem convertida para ícone: '{ico_path}'")
            return ico_path
    except Exception as e:
        print(f"Erro ao converter a imagem para ícone: {e}")
        return ''


def criar_exe(nome: str, path: str, ico: str, output_dir: str, prompt: bool = False):
    path = os.path.abspath(path)
    path = os.path.normpath(path)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Arquivo Python '{path}' não encontrado.")

    if ico:
        ico = os.path.abspath(ico)
        ico = os.path.normpath(ico)
        if not os.path.isfile(ico):
            raise FileNotFoundError(f"Arquivo de ícone '{ico}' não encontrado.")
        _, ext = os.path.splitext(ico)
        if ext.lower() != '.ico':
            novo_ico = convert_to_ico(ico)
            if novo_ico:
                ico = novo_ico
            else:
                raise ValueError("Não foi possível converter a imagem para ícone.")
        # Se já for .ico, não faz nada

    # Verifica se o diretório de saída existe, caso contrário, cria
    output_dir = os.path.abspath(output_dir)
    output_dir = os.path.normpath(output_dir)
    if not os.path.isdir(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Diretório de saída criado: '{output_dir}'")
        except Exception as e:
            raise OSError(f"Não foi possível criar o diretório de saída: {e}")

    # Cria um diretório temporário para a build e spec
    with tempfile.TemporaryDirectory() as temp_dir:
        comando = [
            sys.executable,
            '-m', 'PyInstaller',
            '--onefile',
            '--distpath', output_dir,  # Define o diretório de saída
            '--workpath', os.path.join(temp_dir, 'build'),  # Define o diretório de build temporário
            '--specpath', temp_dir,  # Define o diretório de spec temporário
            f'--name={nome}',
        ]

        if ico:
            comando.append(f'--icon={ico}')

        if not prompt:
            comando.append('--noconsole')

        comando.append(path)

        # Executa o comando
        result = subprocess.run(
            comando,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Executável '{nome}.exe' criado com sucesso em '{output_dir}'.")


class Worker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, nome, path, ico, output_dir, prompt):
        super().__init__()
        self.nome = nome
        self.path = path
        self.ico = ico
        self.output_dir = output_dir
        self.prompt = prompt

    def run(self):
        try:
            criar_exe(self.nome, self.path, self.ico, self.output_dir, self.prompt)
            self.finished.emit(f"Executável '{self.nome}.exe' criado com sucesso em:\n{self.output_dir}")
        except Exception as e:
            self.error.emit(str(e))


class ProgressScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Convertendo .py para .exe")
        self.setFixedSize(400, 300)  # Define a resolução da tela de progresso para 400x300
        layout = QVBoxLayout()

        self.message_label = QLabel("Convertendo .py para .exe...", self)
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("font-size: 24px;")

        # Adiciona um QLabel com um GIF animado de carregamento
        self.spinner_label = QLabel(self)
        self.spinner_label.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(self.message_label)
        layout.addWidget(self.spinner_label)
        layout.addStretch()

        self.setLayout(layout)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Py to Exe Converter'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(400, 300)  # Define a resolução da janela principal para 400x300

        # Definir o ícone da janela (aparece na barra de tarefas e na janela)
        app_icon_path = resource_path('icone_app.ico')  # Usar resource_path para resolver o caminho
        if os.path.isfile(app_icon_path):
            self.setWindowIcon(QIcon(app_icon_path))
        else:
            print(f"Ícone da aplicação não encontrado: '{app_icon_path}'")

        # Layouts
        main_layout = QStackedLayout()

        # Página principal
        self.main_page = QWidget()
        main_page_layout = QVBoxLayout()

        # Nome do Programa
        self.nome_label = QLabel('Nome do programa:')
        self.nome_input = QLineEdit()
        main_page_layout.addWidget(self.nome_label)
        main_page_layout.addWidget(self.nome_input)

        # Caminho do Programa
        self.caminho_label = QLabel('Caminho do programa:')
        self.caminho_input = QLineEdit()
        self.caminho_button = QPushButton('Selecionar arquivo')
        self.caminho_button.clicked.connect(self.select_program_file)

        caminho_layout = QHBoxLayout()
        caminho_layout.addWidget(self.caminho_input)
        caminho_layout.addWidget(self.caminho_button)
        main_page_layout.addWidget(self.caminho_label)
        main_page_layout.addLayout(caminho_layout)

        # Prompt
        self.prompt_checkbox = QCheckBox('Exibir janela do prompt durante a execução')
        self.prompt_checkbox.setChecked(False)
        main_page_layout.addWidget(self.prompt_checkbox)

        # Ícone
        self.icone_checkbox = QCheckBox('Adicionar ícone personalizado')
        self.icone_checkbox.stateChanged.connect(self.toggle_icone_input)
        main_page_layout.addWidget(self.icone_checkbox)

        self.icone_input = QLineEdit()
        self.icone_input.setEnabled(False)
        self.icone_button = QPushButton('Selecionar ícone')
        self.icone_button.setEnabled(False)
        self.icone_button.clicked.connect(self.select_icon_file)

        icone_layout = QHBoxLayout()
        icone_layout.addWidget(self.icone_input)
        icone_layout.addWidget(self.icone_button)
        main_page_layout.addLayout(icone_layout)

        # Caminho de Saída
        self.output_label = QLabel('Diretório de saída:')
        self.output_input = QLineEdit()
        self.output_button = QPushButton('Selecionar pasta')
        self.output_button.clicked.connect(self.select_output_directory)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_input)
        output_layout.addWidget(self.output_button)
        main_page_layout.addWidget(self.output_label)
        main_page_layout.addLayout(output_layout)

        # Botão Criar Executável
        self.criar_button = QPushButton('Criar Executável')
        self.criar_button.clicked.connect(self.on_click_criar)
        main_page_layout.addWidget(self.criar_button)

        # Adiciona a página principal ao layout empilhado
        self.main_page.setLayout(main_page_layout)
        main_layout.addWidget(self.main_page)

        # Página de progresso
        self.progress_screen = ProgressScreen()
        main_layout.addWidget(self.progress_screen)

        self.setLayout(main_layout)

    def select_program_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Selecionar arquivo Python", "",
            "Python Files (*.py);;All Files (*)", options=options)
        if fileName:
            self.caminho_input.setText(fileName)

    def select_icon_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Selecionar arquivo de ícone ou imagem", "",
            "Image Files (*.ico *.png *.jpg *.bmp);;All Files (*)", options=options)
        if fileName:
            self.icone_input.setText(fileName)

    def select_output_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(
            self, "Selecionar diretório de saída", "", options=options)
        if directory:
            self.output_input.setText(directory)

    def toggle_icone_input(self, state):
        if state == Qt.Checked:
            self.icone_input.setEnabled(True)
            self.icone_button.setEnabled(True)
        else:
            self.icone_input.setEnabled(False)
            self.icone_button.setEnabled(False)
            self.icone_input.clear()

    def on_click_criar(self):
        nomePrograma = self.nome_input.text().strip()
        caminhoPrograma = self.caminho_input.text().strip()
        prompt = self.prompt_checkbox.isChecked()
        icone = self.icone_input.text().strip() if self.icone_checkbox.isChecked() else ''
        output_dir = self.output_input.text().strip()

        if not nomePrograma:
            QMessageBox.warning(self, 'Erro', 'Por favor, insira o nome do programa.')
            return

        if not caminhoPrograma:
            QMessageBox.warning(self, 'Erro', 'Por favor, selecione o arquivo do programa.')
            return

        if self.icone_checkbox.isChecked() and not icone:
            QMessageBox.warning(self, 'Erro', 'Por favor, selecione o arquivo de ícone.')
            return

        if not output_dir:
            QMessageBox.warning(self, 'Erro', 'Por favor, selecione o diretório de saída.')
            return

        # Alterna para a tela de progresso
        self.parent_layout().setCurrentWidget(self.progress_screen)

        # Iniciar o Worker Thread
        self.worker = Worker(nomePrograma, caminhoPrograma, icone, output_dir, prompt)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_finished(self, message):
        QMessageBox.information(self, 'Concluído', message)
        QApplication.quit()

    def on_error(self, error_message):
        QMessageBox.critical(self, 'Erro', error_message)
        # Retorna para a página principal
        self.parent_layout().setCurrentWidget(self.main_page)

    def parent_layout(self):
        return self.layout()


class ProgressScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Convertendo .py para .exe")
        self.setFixedSize(400, 300)  # Define a resolução da tela de progresso para 400x300
        layout = QVBoxLayout()

        self.message_label = QLabel("Convertendo .py para .exe...", self)
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("font-size: 24px;")

        # Adiciona um QLabel com um GIF animado de carregamento
        self.spinner_label = QLabel(self)
        self.spinner_label.setAlignment(Qt.AlignCenter)
        gif_path = resource_path("spinner.gif")  # Usar resource_path para resolver o caminho

        if os.path.isfile(gif_path):
            self.movie = QMovie(gif_path)
            self.spinner_label.setMovie(self.movie)
            self.movie.start()
        else:
            print(f"Arquivo de GIF '{gif_path}' não encontrado. Usando texto como fallback.")
            self.spinner_label.setText("")
            self.spinner_label.setAlignment(Qt.AlignCenter)
            self.spinner_label.setStyleSheet("font-size: 20px;")

        layout.addStretch()
        layout.addWidget(self.message_label)
        layout.addWidget(self.spinner_label)
        layout.addStretch()

        self.setLayout(layout)


class Worker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, nome, path, ico, output_dir, prompt):
        super().__init__()
        self.nome = nome
        self.path = path
        self.ico = ico
        self.output_dir = output_dir
        self.prompt = prompt

    def run(self):
        try:
            criar_exe(self.nome, self.path, self.ico, self.output_dir, self.prompt)
            self.finished.emit(f"Executável '{self.nome}.exe' criado com sucesso em:\n{self.output_dir}")
        except Exception as e:
            self.error.emit(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
