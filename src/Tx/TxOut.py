from ..helper import int_to_little_endian
from ..Script import Script

class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = Script.parse()

    def __repr__(self):
        return '{}:{}'.format(self.amount, self.script_pubkey)

    def parse(cls, s):
        amount = little_endian_to_int(s.read(8))
        script_pubkey = Script.parse()

    def serialize(self):
        result = int_to_little_endian(self.amount(8))
        result += self.script_pubkey.serialize()
        return result
