from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from brownie import network, config, MockV3Aggregator, FundMe
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    # if deploying on persistent  networks, use the associated addres
    # if not deploy mock conracts

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    return fund_me


def main():
    deploy_fund_me()
