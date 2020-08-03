import pandas as pd

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime, time, timezone

from typing import List, Dict, Union

class TradingBot():

    def __init__(self, client_id: str, redirect_uri: str, credientials_path: str = None, trading_account: str = None) -> None:

        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credientials_path: str = credientials_path
        self.session: TDClient = self._create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame = None

    def _create_session(self) -> TDClient:

        td_client = TDClient(
            clients_id = self.client_id,
            redirect_uri = self.redirect_uri,
            credentials_path = self.credentials_path
        )

        #Login to session
        td_client.login()

        return td_client

    