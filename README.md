# Py2Exe

## 📄 **Visão Geral**

O **Py2Exe** é uma aplicação gráfica desenvolvida em Python utilizando a biblioteca **PyQt5**. Ela permite que você converta scripts Python (`.py`) em executáveis (`.exe`) de forma simples e intuitiva. Além disso, oferece opções para adicionar ícones personalizados e configurar o ambiente virtual (`.venv`) do script alvo, garantindo que todas as dependências sejam incluídas no executável final.

## 🚀 **Recursos Principais**

- **Interface Gráfica Intuitiva:** Facilita a seleção do script Python, ícone personalizado e diretório de saída.
- **Suporte a Ambientes Virtuais:** Detecta automaticamente um ambiente virtual `.venv` no mesmo diretório do script ou permite que você selecione manualmente o interpretador Python do venv desejado.
- **Conversão de Imagens para Ícones:** Converte automaticamente imagens (`.png`, `.jpg`, etc.) para o formato `.ico` se necessário.
- **Opções de Configuração:** Permite escolher se deseja exibir a janela do prompt durante a execução do executável.
- **Logs de Depuração:** Exibe mensagens detalhadas no console para facilitar a identificação e resolução de problemas.

## 🛠️ **Pré-requisitos**

Antes de utilizar o **Py to Exe Converter**, saiba que é obrigatório que o arquivo Python (`.py`) que será convertido esteja dentro de um ambiente virtual (`.venv`) configurado corretamente com todas as dependências necessárias. conforme estabelecido na estrutura abaixo.

## 📦 **Estrutura de Diretórios**

Para facilitar a detecção automática do ambiente virtual, é recomendado manter a seguinte estrutura de diretórios:

```
py2exe/
├── .venv/
├── main.py
├── icone_app.ico
└── outras_pastas_ou_arquivos
```

- **.venv/**: Pasta do ambiente virtual contendo todas as dependências do seu projeto.
- **main.py**: Script principal do conversor.
- **icone_app.ico**: Ícone da aplicação que aparecerá na barra de tarefas e na janela.
- **outras_pastas_ou_arquivos**: Qualquer outro arquivo ou pasta necessária.

## 📝 **Como Utilizar**

### 1. **Executar o Conversor**

Execute o script `main.py` usando o interpretador Python:

```bash
python main.py
```

### 2. **Interface da Aplicação**

A interface possui os seguintes componentes:

- **Nome do Programa:**
  - **Descrição:** Insira o nome desejado para o executável.
  - **Campo:** `Nome do programa:`
  
- **Caminho do Programa:**
  - **Descrição:** Selecione o arquivo Python (`.py`) que deseja converter.
  - **Campo:** `Caminho do programa:`
  - **Botão:** `Selecionar arquivo`

- **Exibir Janela do Prompt Durante a Execução:**
  - **Descrição:** Marque esta opção se desejar que a janela do prompt seja exibida ao executar o executável.
  - **Caixa de Seleção:** `Exibir janela do prompt durante a execução`

- **Adicionar Ícone Personalizado:**
  - **Descrição:** Marque esta opção para adicionar um ícone personalizado ao executável.
  - **Caixa de Seleção:** `Adicionar ícone personalizado`
  - **Campos e Botões:** Quando marcada, permite selecionar um arquivo de ícone ou imagem.
    - **Campo:** `Selecionar ícone`
    - **Botão:** `Selecionar ícone`

- **Diretório de Saída:**
  - **Descrição:** Escolha onde o executável será salvo.
  - **Campo:** `Diretório de saída:`
  - **Botão:** `Selecionar pasta`

- **Botão Criar Executável:**
  - **Descrição:** Inicia o processo de conversão.
  - **Botão:** `Criar Executável`

### 3. **Processo de Conversão**

1. **Selecione o Script Python:**
   - Clique no botão `Selecionar arquivo` e navegue até o script `.py` que deseja converter.

2. **Adicionar Ícone (Opcional):**
   - Marque a caixa `Adicionar ícone personalizado` se desejar.
   - Clique no botão `Selecionar ícone` e escolha um arquivo de imagem (`.png`, `.jpg`, etc.) ou `.ico`.
   - Se o arquivo não for `.ico`, o conversor tentará convertê-lo automaticamente.

3. **Configurar Diretório de Saída:**
   - Clique no botão `Selecionar pasta` para escolher onde o executável será salvo.

4. **Iniciar a Conversão:**
   - Clique no botão `Criar Executável`.
   - A aplicação exibirá uma tela de progresso durante a conversão.
   - Ao finalizar, uma mensagem informará sobre o sucesso ou possíveis erros.

### 4. **Considerações Finais**

- **Ambiente Virtual:**
  - O conversor tentará automaticamente localizar um ambiente virtual `.venv` no mesmo diretório do script `.py` selecionado.
  - Se não encontrar, você pode selecionar manualmente o interpretador Python do ambiente virtual desejado através de uma caixa de diálogo.

- **Permissões de Arquivo:**
  - Certifique-se de ter permissões adequadas para ler os arquivos selecionados e escrever no diretório de saída.


## 📚 **Recursos Adicionais**

- **Documentação do PyInstaller:**
  - [PyInstaller Official Documentation](https://pyinstaller.readthedocs.io/en/stable/)
  
- **Documentação sobre Ambientes Virtuais:**
  - [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
  
- **Documentação do Pillow:**
  - [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
  
- **Documentação do PyQt5:**
  - [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
  
- **Ferramenta de Conversão de Ícones:**
  - [IcoConverter](https://www.icoconverter.com/)

## 🧪 **Testes Recomendados**

1. **Testar com Outro Arquivo `.ico`:**
   - Utilize um arquivo de ícone diferente para verificar se o problema está relacionado ao arquivo específico `g4.ico`.

2. **Testar com Arquivos de Outros Formatos:**
   - Tente converter imagens em formatos como `.png` ou `.jpg` para `.ico` para verificar se a conversão funciona corretamente.

3. **Verificar os Logs de Depuração:**
   - Analise os prints no console para entender o fluxo do programa e identificar onde o erro está ocorrendo.

4. **Verificar a Estrutura do Ambiente Virtual:**
   - Certifique-se de que a estrutura do ambiente virtual está correta e que todas as dependências necessárias estão instaladas.

## 🤝 **Contribuições**

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## 📜 **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📧 **Contato**

Para dúvidas, sugestões ou suporte, entre em contato através do email: [rebello.hiltonqueiroz@gmail.com](mailto:rebello.hiltonqueiroz@gmail.com)

---

Esperamos que o **Py to Exe Converter** facilite a distribuição dos seus scripts Python, transformando-os em executáveis de forma rápida e eficiente. Se você tiver qualquer dúvida ou precisar de assistência adicional, não hesite em nos contatar!

## 📂 **Disponível no GitHub**

O **Py to Exe Converter** está disponível no GitHub como um ambiente virtual (`.venv`) com todos os requisitos preenchidos, facilitando a configuração e utilização da ferramenta. Você pode acessar o repositório através do seguinte link:

[Py to Exe Converter no GitHub](https://github.com/hqr90/py2exe)
