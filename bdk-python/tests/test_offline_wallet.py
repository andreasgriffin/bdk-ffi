import bdkpython as bdk
import unittest

class TestSimpleWallet(unittest.TestCase):

    def test_new_address(self):
        descriptor: bdk.Descriptor = bdk.Descriptor(
            "wpkh([c258d2e4/84h/1h/0h]tpubDDYkZojQFQjht8Tm4jsS3iuEmKjTiEGjG6KnuFNKKJb5A6ZUCUZKdvLdSDWofKi4ToRCwb9poe1XdqfUnP4jaJjCB2Zwv11ZLgSbnZSNecE/0/*)",
            bdk.Network.TESTNET
        )
        wallet: Wallet = bdk.Wallet.new_no_persist(
            descriptor,
            None,
            bdk.Network.TESTNET
        )
        address_info: bdk.AddressInfo = wallet.get_address(bdk.AddressIndex.NEW())

        self.assertEqual("tb1qzg4mckdh50nwdm9hkzq06528rsu73hjxxzem3e", address_info.address.as_string())

    def test_balance(self):
        descriptor: bdk.Descriptor = bdk.Descriptor(
            "wpkh([c258d2e4/84h/1h/0h]tpubDDYkZojQFQjht8Tm4jsS3iuEmKjTiEGjG6KnuFNKKJb5A6ZUCUZKdvLdSDWofKi4ToRCwb9poe1XdqfUnP4jaJjCB2Zwv11ZLgSbnZSNecE/0/*)",
            bdk.Network.TESTNET
        )
        wallet: bdk.Wallet = bdk.Wallet.new_no_persist(
            descriptor,
            None,
            bdk.Network.TESTNET
        )

        self.assertEqual(wallet.get_balance().total(), 0)

if __name__ == '__main__':
    unittest.main()