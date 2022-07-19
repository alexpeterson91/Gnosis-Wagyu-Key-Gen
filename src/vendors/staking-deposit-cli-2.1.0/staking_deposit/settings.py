from typing import Dict, NamedTuple


DEPOSIT_CLI_VERSION = '2.1.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


#MAINNET = 'mainnet'
#PRATER = 'prater'
#KINTSUGI = 'kintsugi'
#KILN = 'kiln'
GNOSIS = 'gnosis'

# Mainnet setting
#MainnetSetting = BaseChainSetting(NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Testnet (spec v1.0.1)
#PraterSetting = BaseChainSetting(NETWORK_NAME=PRATER, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# Merge Testnet (spec v1.1.4)
#KintsugiSetting = BaseChainSetting(NETWORK_NAME=KINTSUGI, GENESIS_FORK_VERSION=bytes.fromhex('60000069'))
# Merge Testnet (spec v1.1.9)
#KilnSetting = BaseChainSetting(NETWORK_NAME=KILN, GENESIS_FORK_VERSION=bytes.fromhex('70000069'))
# Gnosis Mainnet setting
GnosisSetting = BaseChainSetting(NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    GNOSIS: GnosisSetting
    #MAINNET: MainnetSetting,
    #PRATER: PraterSetting,
    #KINTSUGI: KintsugiSetting,
    #KILN: KilnSetting,
}


def get_chain_setting(chain_name: str = GNOSIS) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
