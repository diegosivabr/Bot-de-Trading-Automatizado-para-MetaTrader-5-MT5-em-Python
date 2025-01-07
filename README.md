## **Bot de Trading Automatizado para MetaTrader 5 (MT5) em Python**

### **Visão Geral**
Este projeto implementa um **bot de trading automatizado** para a plataforma **MetaTrader 5 (MT5)** utilizando a linguagem **Python**. O bot é capaz de realizar operações de compra e venda em diferentes ativos financeiros (como moedas, índices, metais e criptomoedas) em horários predefinidos. A solução foi criada para permitir uma abordagem de trading automatizada, sem a necessidade de monitoramento constante, aproveitando as funcionalidades da API do MetaTrader 5.

### **Funcionalidades**
- **Execução Automática de Ordens**: O bot abre e fecha ordens de compra ou venda para os ativos especificados, respeitando horários de abertura e fechamento definidos.
- **Ativos Diversificados**: O bot foi configurado para operar com uma ampla gama de ativos, incluindo **Forex**, **índices**, **commodities** (ouro, prata, petróleo), e **criptomoedas**.
- **Gestão de Posições**: A ferramenta monitora as ordens abertas e garante o fechamento automático no horário determinado.
- **Análise de Mercado em Tempo Real**: Utiliza dados de mercado em tempo real (preços de compra e venda) para realizar operações no MetaTrader 5.
- **Correção de Erros**: Tratamento de exceções para evitar operações em ativos indisponíveis ou outros problemas relacionados à execução de ordens.

### **Estratégia de Trading**
O bot utiliza horários específicos para abrir e fechar as ordens, com base em padrões de volatilidade e nas diferentes sessões do mercado:

#### **Forex**
- **GBPUSD**: Venda durante a sessão europeia (05:30 - 10:00).
- **USDJPY**: Compra durante a abertura da sessão asiática (00:00 - 03:00).
- **AUDUSD**: Venda na sessão asiática (22:00 - 02:00).
- **EURUSD**: Compra na abertura da sessão europeia (05:00 - 10:00).
- **NZDUSD**: Venda na sessão asiática (21:00 - 01:00).
- **EURGBP**: Compra durante a sessão europeia (06:00 - 09:00).
- **USDCHF**: Compra durante a transição para a sessão americana (12:00 - 15:00).

#### **Índices**
- **NDAQ.NAS**: Compra durante a tarde na sessão americana (14:00 - 17:00).
- **DAX40**: Venda durante a sessão europeia (07:00 - 10:30).
- **FTSE100**: Venda durante a sessão europeia (07:00 - 10:30).
- **SP500**: Compra no início da sessão americana (13:30 - 16:00).
- **GER40**: Venda durante a manhã europeia (08:00 - 11:00).

#### **Metais**
- **XAUUSD (Ouro)**: Compra durante a transição da sessão europeia para americana (12:30 - 16:00).
- **XAGUSD (Prata)**: Compra durante a transição para a sessão americana (11:00 - 15:00).
- **USOIL (Petróleo)**: Venda durante o início da sessão americana (13:00 - 16:00).
- **WTI.NYSE (Petróleo)**: Compra no pico da sessão americana (14:00 - 17:00).

#### **Criptomoedas**
- **BTCUSD (Bitcoin)**: Compra na madrugada, aproveitando a alta volatilidade (00:00 - 05:00).
- **ETHUSD (Ethereum)**: Compra na madrugada (00:00 - 05:00).
- **LTCUSD (Litecoin)**: Compra na madrugada (00:00 - 05:00).
- **DOGEUSD (Dogecoin)**: Compra em horários de baixa volatilidade (02:00 - 06:00).

### **Como Funciona**
1. **Configuração dos Ativos**: O bot é configurado com uma lista de ativos, com volume, tipo de ordem (compra ou venda) e horários de abertura e fechamento.
2. **Execução de Ordens**: Com base no horário atual, o bot executa ordens de compra ou venda para o ativo especificado.
3. **Gestão de Posições**: O bot monitora as ordens abertas e garante o fechamento no horário predefinido, sem a necessidade de intervenção manual.

### **Tecnologias Usadas**
- **MetaTrader 5 (MT5)**: A plataforma de negociação que permite o envio de ordens de trading e acesso aos dados do mercado.
- **Python**: Linguagem de programação utilizada para implementar a lógica do bot e se comunicar com o MetaTrader 5.
- **API do MetaTrader 5**: Utilizada para enviar ordens de compra/venda, obter preços de mercado em tempo real e gerenciar posições.

### **Instalação**
1. **Requisitos**:
   - MetaTrader 5 instalado no seu computador.
   - Python 3.x.
   - Biblioteca `MetaTrader5` para Python.
   
2. **Instalação da Biblioteca MT5**:
   Abra o terminal ou prompt de comando e execute o seguinte comando:
   ```bash
   pip install MetaTrader5
   ```

### **Instruções de Como Rodar**
1. **Configuração do MetaTrader 5**:
   - Certifique-se de que o MetaTrader 5 esteja instalado e que você tenha uma conta de negociação ativa.
   - Abra o MetaTrader 5 e permita a conexão via API, garantindo que o terminal esteja rodando e conectado à sua conta.

2. **Baixar ou Clonar o Repositório**:
   - Se ainda não tiver, clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   ```

3. **Configurando o Script**:
   - Abra o arquivo `bot.py` (ou o nome que você deu ao script principal) e edite a lista de ativos, volume e horários de negociação conforme suas necessidades.

4. **Executando o Bot**:
   Para rodar o bot de trading, execute o seguinte comando no terminal ou prompt de comando:
   ```bash
   python bot.py
   ```

   Isso iniciará o bot e ele começará a executar as ordens de acordo com os horários predefinidos.
