# Py to Exe Converter

## 📄 **Visão Geral**

O **Py to Exe Converter** é uma aplicação gráfica desenvolvida em Python utilizando a biblioteca **PyQt5**. Ela permite que você converta scripts Python (`.py`) em executáveis (`.exe`) de forma simples e intuitiva. Além disso, oferece opções para adicionar ícones personalizados e configurar o ambiente virtual (`.venv`) do script alvo, garantindo que todas as dependências sejam incluídas no executável final.

### 🛠️ **Dica Legal**
Uma dica interessante é transformar o próprio **Py to Exe Converter** em um executável. Isso facilita a distribuição e utilização da ferramenta sem a necessidade de ter um ambiente Python configurado no sistema do usuário. Para isso, você pode usar o próprio conversor para empacotar-se como um executável, criando uma espécie de "bootstraper" para a aplicação.

Além disso, o **Py to Exe Converter** está disponível como um ambiente virtual (`.venv`) no GitHub com todos os requisitos preenchidos, permitindo uma configuração rápida e fácil para novos usuários.

## 🚀 **Recursos Principais**

- **Interface Gráfica Intuitiva:** Facilita a seleção do script Python, ícone personalizado e diretório de saída.
- **Suporte a Ambientes Virtuais:** Detecta automaticamente um ambiente virtual `.venv` no mesmo diretório do script ou permite que você selecione manualmente o interpretador Python do venv desejado.
- **Conversão de Imagens para Ícones:** Converte automaticamente imagens (`.png`, `.jpg`, etc.) para o formato `.ico` se necessário.
- **Opções de Configuração:** Permite escolher se deseja exibir a janela do prompt durante a execução do executável.
- **Logs de Depuração:** Exibe mensagens detalhadas no console para facilitar a identificação e resolução de problemas.

## 🛠️ **Pré-requisitos**

Antes de utilizar o **Py to Exe Converter**, certifique-se de que os seguintes pré-requisitos estão atendidos:

1. **Python 3.6 ou Superior:** [Download do Python](https://www.python.org/downloads/)
2. **Bibliotecas Python Necessárias:**
   - **PyQt5**
   - **Pillow**
   - **PyInstaller**
   
   Você pode instalar essas bibliotecas usando o `pip`:

   ```bash
   pip install PyQt5 Pillow PyInstaller
   ```

3. **Ambiente Virtual (Opcional):** Se o seu script Python utiliza um ambiente virtual com dependências específicas, certifique-se de que ele está configurado corretamente.

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

## 🐞 **Resolução de Problemas**

### 1. **Erro ao Converter a Imagem para Ícone**

**Mensagem de Erro:**
```
Erro ao converter a imagem para ícone: [Errno 22] Invalid argument: 'C:\\Users\\Hilton Q Rebello\\Desktop\\g4.ico'
```

**Causas Possíveis:**
- **Arquivo `.ico` Corrompido ou Inválido:** O arquivo de ícone pode estar corrompido ou não ser um `.ico` válido.
- **Permissões de Arquivo:** Falta de permissões para ler ou escrever no diretório especificado.
- **Formato de Imagem Não Suportado:** O Pillow pode não suportar certas variantes do formato `.ico`.

**Soluções:**
1. **Verifique a Integridade do Arquivo de Ícone:**
   - Abra o arquivo `g4.ico` em um visualizador de ícones para garantir que está funcionando corretamente.
   - Tente converter o arquivo manualmente usando ferramentas como o [IcoConverter](https://www.icoconverter.com/) para verificar se o arquivo pode ser convertido sem erros.

2. **Use Outro Arquivo de Imagem:**
   - Tente usar um arquivo de imagem diferente (por exemplo, `g4.png`) para verificar se a conversão para `.ico` funciona corretamente.
   - Isso ajudará a determinar se o problema está específico no arquivo `g4.ico`.

3. **Atualize o Pillow:**
   - Certifique-se de que a biblioteca Pillow está atualizada para a versão mais recente:
     ```bash
     pip install --upgrade Pillow
     ```

4. **Verifique as Permissões:**
   - Assegure-se de que você tem permissões adequadas para ler o arquivo de imagem e escrever no diretório de saída.
   - Tente executar a aplicação como administrador para descartar problemas de permissões.

5. **Modifique a Função de Conversão:**
   - A função `convert_to_ico` foi atualizada para salvar o ícone convertido com um sufixo `_converted.ico` para evitar sobrescrever o arquivo original.
   - Verifique se o arquivo convertido está sendo salvo corretamente e tente usá-lo.

### 2. **Erro: "No module named PyInstaller"**

**Mensagem de Erro:**
```
Erro ao criar o executável: E:\python\projects\backup\.venv\Scripts\python.exe: No module named PyInstaller
```

**Causas Possíveis:**
- O módulo `PyInstaller` não está instalado no ambiente virtual (`.venv`) do script alvo.

**Soluções:**
1. **Instale o PyInstaller no Ambiente Virtual do Script Alvo:**
   - Ative o ambiente virtual do script:
     ```bash
     E:\python\projects\backup\.venv\Scripts\activate
     ```
   - Instale o PyInstaller:
     ```bash
     pip install pyinstaller
     ```

2. **Utilize o PyInstaller do Ambiente Atual:**
   - O conversor foi configurado para usar o PyInstaller instalado no ambiente onde ele está sendo executado.
   - Certifique-se de que o PyInstaller está instalado no ambiente do conversor:
     ```bash
     pip install pyinstaller
     ```

3. **Reinicie o Conversor:**
   - Após instalar o PyInstaller, reinicie o conversor e tente novamente.

### 3. **Erro: "Interpretador Python não encontrado no ambiente virtual padrão."**

**Mensagem de Erro:**
```
Interpretador Python não encontrado no ambiente virtual padrão.
```

**Causas Possíveis:**
- A pasta `.venv` não está configurada corretamente ou o interpretador Python está ausente dentro dela.

**Soluções:**
1. **Verifique a Estrutura do Ambiente Virtual:**
   - Certifique-se de que a pasta `.venv` contém os arquivos e diretórios necessários, especialmente o interpretador Python (`python.exe` no Windows ou `python` no macOS/Linux).

2. **Recrie o Ambiente Virtual:**
   - Se o ambiente virtual estiver corrompido ou incompleto, recrie-o:
     ```bash
     python -m venv .venv
     ```
   - Ative o ambiente virtual e reinstale as dependências necessárias:
     ```bash
     .venv\Scripts\activate
     pip install -r requirements.txt
     ```

3. **Selecione Manualmente o Interpretador Python:**
   - Se a detecção automática falhar, você pode selecionar manualmente o interpretador Python do ambiente virtual através da caixa de diálogo que será aberta.

### 4. **Outros Erros Comuns**

- **Erro Durante a Criação do Executável:**
  - **Solução:** Verifique as mensagens de erro detalhadas no console para identificar a causa específica. Assegure-se de que todas as dependências do script estão instaladas no ambiente virtual utilizado.

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
