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

**Explicação dos Argumentos:**

- `--onefile`: Cria um único arquivo executável.
- `--icon=icone_app.ico`: Define o ícone do executável.
- `--add-data "icone_app.ico;."`: Inclui o arquivo de ícone no diretório raiz do executável. **Nota:** No Windows, use ponto e vírgula (`;`) para separar o caminho da fonte e o destino. Em sistemas Unix, use dois pontos (`:`).

## 🐞 **Resolução de Problemas**

**Erro ao Criar o Executável:**

   - **Permissões de Arquivo:** Verifique se você tem permissões adequadas para ler os arquivos de entrada e escrever no diretório de saída.
   - **Dependências do PyInstaller:** Certifique-se de que todas as dependências necessárias estão instaladas no seu ambiente virtual.

## 🤝 **Contribuição**

Contribuições são bem-vindas! Se você encontrar bugs, tiver sugestões de melhorias ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## 📄 **Licença**

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 📞 **Contato**

Para mais informações ou dúvidas, entre em contato com [rebello.hiltonqueiroz@gmail.com](mailto:rebello.hiltonqueiroz@gmail.com).
