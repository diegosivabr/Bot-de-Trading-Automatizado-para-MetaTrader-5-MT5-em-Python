import MetaTrader5 as mt5
from datetime import datetime
import time

# Inicialize a conexão com o MetaTrader 5
if not mt5.initialize():
    print("Erro ao inicializar MetaTrader 5")
    mt5.shutdown()

# Lista de ativos com parâmetros definidos
ativos = [
    {"ativo": "GBPUSD", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "05:30", "horario_fechar": "10:00"},  # Forex: venda durante a sessão europeia.
    {"ativo": "USDJPY", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "03:00"},  # Forex: compra na abertura da sessão asiática.
    {"ativo": "AUDUSD", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "22:00", "horario_fechar": "02:00"},  # Forex: venda na sessão asiática.
    {"ativo": "DAX40", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "07:00", "horario_fechar": "10:30"},  # Índice alemão: venda durante a sessão europeia.
    {"ativo": "FTSE100", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "07:00", "horario_fechar": "10:30"},  # Índice britânico: venda durante a sessão europeia.
    {"ativo": "SP500", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "13:30", "horario_fechar": "16:00"},  # Índice dos EUA: compra no início da sessão americana.
    {"ativo": "NDAQ.NAS", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "14:00", "horario_fechar": "17:00"},  # Índice tecnológico dos EUA: compra durante a tarde na sessão americana.
    {"ativo": "XAUUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "12:30", "horario_fechar": "16:00"},  # Ouro: compra na transição da sessão europeia para americana.
    {"ativo": "USOIL", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "13:00", "horario_fechar": "16:00"},  # Petróleo: venda durante o início da sessão americana.
    {"ativo": "XAGUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "11:00", "horario_fechar": "15:00"},  # Prata: compra durante a transição para a sessão americana.
    {"ativo": "BTCUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Bitcoin: compra na madrugada (alta volatilidade).
    {"ativo": "ETHUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Ethereum: compra na madrugada (alta volatilidade).
    {"ativo": "EURUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "05:00", "horario_fechar": "10:00"},  # Forex: compra durante a abertura da sessão europeia.
    {"ativo": "LTCUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Litecoin: compra na madrugada (alta volatilidade).
    
    # Novos ativos sugeridos para análise:
    {"ativo": "NZDUSD", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "21:00", "horario_fechar": "01:00"},  # Forex: venda na sessão asiática.
    {"ativo": "EURGBP", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "06:00", "horario_fechar": "09:00"},  # Forex: compra na sessão europeia.
    {"ativo": "USDCHF", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "12:00", "horario_fechar": "15:00"},  # Forex: compra durante a transição para a sessão americana.
    {"ativo": "GER40", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "08:00", "horario_fechar": "11:00"},  # Índice alemão: venda durante a manhã europeia.
    {"ativo": "WTI.NYSE", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "14:00", "horario_fechar": "17:00"},  # Petróleo (WTI): compra no pico da sessão americana.
    {"ativo": "SIL.NYSE", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "09:00", "horario_fechar": "12:00"},  # Prata: compra na manhã europeia.
    {"ativo": "DOGEUSD", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "02:00", "horario_fechar": "06:00"},  # Dogecoin: compra em horários de baixa volatilidade.
]

# Função para enviar a ordem
def enviar_ordem(ativo, volume, tipo_ordem):
    symbol = ativo
    tick_info = mt5.symbol_info_tick(symbol)
    
    if tick_info is None:
        print(f"Erro: Não foi possível obter o preço para {symbol}")
        return

    price = tick_info.ask  # Preço de mercado atual
    order_type = mt5.ORDER_TYPE_BUY if tipo_ordem == "compra" else mt5.ORDER_TYPE_SELL
    deviation = 10  # Exemplo de desvio
    stop_loss = 0.0
    take_profit = 0.0
    
    order_request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": deviation,
        "type": order_type,
        "type_filling": mt5.ORDER_FILLING_IOC,  # Execução imediata
        "type_time": mt5.ORDER_TIME_GTC,  # Ordem válida até ser cancelada
        "comment": "Automated trading"
    }
    
    # Enviar a ordem
    result = mt5.order_send(order_request)
    
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Erro ao enviar ordem para {symbol}: Retcode {result.retcode}, Detalhes: {result.comment}")
    else:
        print(f"Ordem de {tipo_ordem} para {symbol} enviada com sucesso!")
        return result.order  # Retorna o número da ordem para usá-lo ao fechar

# Função para fechar a ordem
def fechar_ordem(symbol, order_ticket):
    positions = mt5.positions_get(symbol=symbol)  # Obter todas as posições abertas para o ativo
    if positions is not None:
        for position in positions:
            if position.ticket == order_ticket:  # Se a posição aberta for a ordem que queremos fechar
                # Solicitar o fechamento da ordem
                close_request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": symbol,
                    "volume": position.volume,
                    "type": mt5.ORDER_TYPE_SELL if position.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY,
                    "position": position.ticket,
                    "price": mt5.symbol_info_tick(symbol).bid,
                    "deviation": 10,
                    "type_filling": mt5.ORDER_FILLING_IOC,
                    "type_time": mt5.ORDER_TIME_GTC,
                    "comment": "Fechamento automatizado"
                }
                result = mt5.order_send(close_request)
                if result.retcode == mt5.TRADE_RETCODE_DONE:
                    print(f"Ordem de {symbol} fechada com sucesso!")
                else:
                    print(f"Erro ao fechar ordem de {symbol}: Retcode {result.retcode}, Detalhes: {result.comment}")
                return

# Função principal que verifica os horários e envia as ordens
def executar_trades():
    ordens_abertas = {}  # Armazenar o ticket da ordem aberta por ativo
    while True:
        hora_atual = datetime.now().strftime("%H:%M")
        for ativo in ativos:
            if ativo["horario_abrir"] == hora_atual:
                print(f"Abrindo ordem de {ativo['tipo_ordem']} para {ativo['ativo']} às {hora_atual}")
                order_ticket = enviar_ordem(ativo['ativo'], ativo['volume'], ativo['tipo_ordem'])
                if order_ticket:
                    ordens_abertas[ativo['ativo']] = order_ticket  # Armazena o ticket da ordem aberta
            elif ativo["horario_fechar"] == hora_atual:
                print(f"Fechando ordem para {ativo['ativo']} às {hora_atual}")
                if ativo['ativo'] in ordens_abertas:
                    fechar_ordem(ativo['ativo'], ordens_abertas[ativo['ativo']])
                    del ordens_abertas[ativo['ativo']]  # Remove a ordem da lista de abertas
        time.sleep(60)  # Verifica a cada minuto se é o horário para abrir ou fechar ordens

# Iniciar a execução
executar_trades()
