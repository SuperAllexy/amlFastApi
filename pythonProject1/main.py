from fastapi import FastAPI
from pydantic import BaseModel, Field

from BTC_AML_blockchain_Info import get_bitcoin_transactions, analyze_bitcoin_transactions
from ETH_AML_etherscan import get_ethereum_transactions, analyze_ethereum_transactions
from USDT_TRC20_AML_trongrid import perform_risk_check

from pydantic import BaseModel

class TransactionInfo(BaseModel):
    cryptocurrency_type: str
    address: str
    risk_score: float
    risk_assessment: str
    risk_emoji: str
    additional_info: dict

app = FastAPI()


class Item(BaseModel):
    name: str = Field(description="aml checker")
    description: str = "Hi im aml checker"
    price: float
    tax: float = None


@app.get("/aml_check/btc/{address}")
def btc_check(address: str):
    btc_transactions_data = get_bitcoin_transactions(address)
    btc_analysis_result = analyze_bitcoin_transactions(address, btc_transactions_data['txs'])
    return btc_analysis_result


@app.get("/aml_check/eth/{address}")
def eth_check(address: str):
    eth_transactions_data = get_ethereum_transactions(address)
    if eth_transactions_data['status'] == '1' and 'result' in eth_transactions_data:
        analysis_result = analyze_ethereum_transactions(address, eth_transactions_data['result'])
        return analysis_result
    else:
        return {"error": "Ошибка при получении данных транзакций Ethereum или нет транзакций для анализа."}

@app.get("/aml_check/usdt_trc20/{address}")
def usdt_trc20_check(address: str):
    return perform_risk_check(address)
