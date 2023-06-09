from typing import Dict, NamedTuple


DEPOSIT_CLI_VERSION = '2.3.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


#MAINNET = 'mainnet'
#GOERLI = 'goerli'
#PRATER = 'prater'
#KILN = 'kiln'
#SEPOLIA = 'sepolia'
#ROPSTEN = 'ropsten'
GNOSIS = 'gnosis'
CHIADO = 'chiado'

# Mainnet setting
#MainnetSetting = BaseChainSetting(NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Goerli / Prater Setting
#GoerliSetting = BaseChainSetting(NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# Sepolia Setting
#SepoliaSetting = BaseChainSetting(NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'))
# Merge Testnet (spec v1.1.9)
#KilnSetting = BaseChainSetting(NETWORK_NAME=KILN, GENESIS_FORK_VERSION=bytes.fromhex('70000069'))
# Ropsten setting
#RopstenSetting = BaseChainSetting(NETWORK_NAME=ROPSTEN, GENESIS_FORK_VERSION=bytes.fromhex('80000069'))
# Gnosis Mainnet setting
GnosisSetting = BaseChainSetting(NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'))
# Gnosis Chiado Testnet setting
ChiadoSetting = BaseChainSetting(NETWORK_NAME=CHIADO, GENESIS_FORK_VERSION=bytes.fromhex('0000006f'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    GNOSIS: GnosisSetting,
    CHIADO: ChiadoSetting
    #MAINNET: MainnetSetting,
    #PRATER: GoerliSetting,
    #SEPOLIA: SepoliaSetting,
    #KILN: KilnSetting,
    #GOERLI: GoerliSetting,
    #ROPSTEN: RopstenSetting
}


def get_chain_setting(chain_name: str = GNOSIS) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
