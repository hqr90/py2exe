# Py to Exe Converter

**Py to Exe Converter** é uma aplicação desenvolvida em Python utilizando PyQt5 que permite converter scripts Python (`.py`) em executáveis (`.exe`) de forma simples e intuitiva. A aplicação oferece funcionalidades como seleção de ícones personalizados, definição de diretórios de saída e exibição de uma interface gráfica amigável com indicadores de progresso durante o processo de conversão.

## 🛠️ **Funcionalidades**

- **Conversão Fácil:** Converta scripts Python em executáveis de uma única clique.
- **Seleção de Ícone Personalizado:** Adicione ícones personalizados aos executáveis gerados.
- **Definição de Diretório de Saída:** Escolha onde deseja salvar os executáveis convertidos.
- **Interface Gráfica Intuitiva:** Utilize uma interface amigável com indicadores de progresso durante a conversão.
- **Fechamento Automático:** A aplicação fecha automaticamente após a conclusão da conversão.
- **Resolução Personalizada:** Configure a resolução das janelas para 800x600 pixels.

## 📋 **Requisitos**

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- **Python 3.6 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Ambiente Virtual (opcional, mas recomendado)**

## 📦 **Instalação**

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/py-to-exe-converter.git
   cd py-to-exe-converter
   ```

2. **Crie e Ative um Ambiente Virtual (Opcional, mas Recomendado):**

   ```bash
   # No Windows
   python -m venv .venv
   .venv\Scripts\activate

   # No macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as Dependências Necessárias:**

   ```bash
   pip install -r requirements.txt
   ```

   **Nota:** Caso não tenha um arquivo `requirements.txt`, instale manualmente as bibliotecas:

   ```bash
   pip install PyQt5 Pillow
   ```

4. **Adicione os Arquivos de Recursos:**

   - **`icone_app.ico`:** Ícone para a aplicação. Coloque este arquivo no mesmo diretório do script principal.
   - **`spinner.gif`:** GIF animado para o indicador de progresso. Coloque este arquivo no mesmo diretório do script principal.

   **Exemplo de Estrutura de Diretórios:**

   ```
   py-to-exe-converter/
   ├── icone_app.ico
   ├── main.py
   ├── README.md
   └── requirements.txt
   ```

## 📂 **Uso**

1. **Execute a Aplicação:**

   ```bash
   python main.py
   ```

2. **Interface da Aplicação:**

   - **Nome do Programa:** Insira o nome desejado para o executável.
   - **Caminho do Programa:** Selecione o arquivo `.py` que você deseja converter.
   - **Exibir Prompt:** Marque a caixa se desejar que a janela do prompt seja exibida durante a execução do executável.
   - **Adicionar Ícone Personalizado:** Marque a caixa se desejar adicionar um ícone personalizado e selecione o arquivo de ícone.
   - **Diretório de Saída:** Selecione a pasta onde o executável será salvo.

3. **Criar Executável:**

   - Clique no botão **"Criar Executável"**.
   - A interface principal será substituída pela tela de progresso exibindo a mensagem "Convertendo .py para .exe..." e o indicador de carregamento.
   - Após a conclusão:
     - **Sucesso:** Uma mensagem de sucesso será exibida e a aplicação será fechada automaticamente.
     - **Erro:** Uma mensagem de erro detalhada será exibida, e a aplicação retornará para a página principal, permitindo que você tente novamente.

## 🔧 **Personalização e Configuração**

### **Definição do Ícone na Aplicação de Destino**

Para garantir que o ícone apareça corretamente na janela da aplicação Python que está sendo convertida, certifique-se de que o script de destino (`.py`) define o ícone da janela. Isso é feito utilizando o método `setWindowIcon`.

**Exemplo no Script de Destino (`seu_script.py`):**

```python
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

def resource_path(relative_path):
    """Obter o caminho absoluto para recursos, funciona para desenvolvimento e para executáveis PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Minha Aplicação'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        icon_path = resource_path('icone_app.ico')  # Caminho para o ícone
        if os.path.isfile(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Ícone não encontrado: '{icon_path}'")
        self.setGeometry(100, 100, 800, 600)  # Define a resolução da janela para 800x600
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```

**Notas:**

- **Função `resource_path`:** Garante que o caminho para o ícone seja resolvido corretamente, seja durante o desenvolvimento ou no executável.
- **Localização do Ícone:** Coloque o arquivo `icone_app.ico` no mesmo diretório do seu script ou ajuste o caminho conforme necessário.

### **Conversão com PyInstaller**

Ao converter o script de destino com o PyInstaller, use os seguintes argumentos para garantir que o ícone seja aplicado corretamente:

```bash
pyinstaller --onefile --icon=icone_app.ico --add-data "icone_app.ico;." seu_script.py
```

**Explicação dos Argumentos:**

- `--onefile`: Cria um único arquivo executável.
- `--icon=icone_app.ico`: Define o ícone do executável.
- `--add-data "icone_app.ico;."`: Inclui o arquivo de ícone no diretório raiz do executável. **Nota:** No Windows, use ponto e vírgula (`;`) para separar o caminho da fonte e o destino. Em sistemas Unix, use dois pontos (`:`).

## 🐞 **Resolução de Problemas**

1. **Ícone Não Aparece na Janela ou na Barra de Tarefas:**

   - **Verifique o Script de Destino:** Assegure-se de que o script Python que está sendo convertido define o ícone da janela usando `setWindowIcon`.
   - **Verifique os Caminhos dos Recursos:** Utilize a função `resource_path` para resolver corretamente os caminhos dos arquivos de ícone e GIF.
   - **Inclua os Arquivos de Recursos no Executável:** Use o argumento `--add-data` do PyInstaller para garantir que os arquivos de ícone e GIF sejam incluídos no executável.

2. **Erro ao Criar o Executável:**

   - **Permissões de Arquivo:** Verifique se você tem permissões adequadas para ler os arquivos de entrada e escrever no diretório de saída.
   - **Dependências do PyInstaller:** Certifique-se de que todas as dependências necessárias estão instaladas no seu ambiente virtual.

## 🤝 **Contribuição**

Contribuições são bem-vindas! Se você encontrar bugs, tiver sugestões de melhorias ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## 📄 **Licença**

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 📞 **Contato**

Para mais informações ou dúvidas, entre em contato com [seu-email@exemplo.com](mailto:seu-email@exemplo.com).

---

**Nota:** Este README presume que você possui os arquivos `icone_app.ico` no diretório do projeto. Certifique-se de incluir esses arquivos para que a aplicação funcione corretamente tanto no modo de desenvolvimento quanto no executável convertido.
