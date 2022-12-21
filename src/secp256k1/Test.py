from .S256Field import S256Field
from .S256Point import S256Point, N, G
from .Signature import Signature
from ..helper.helper import hash256
from .PrivateKey import PrivateKey
import unittest

class secp256k1(unittest.TestCase):
    def test_G_N(self):
        point = G * N
        self.assertIsNone(point.x)

    def test_verify(self):
        point = S256Point(
            0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c,
            0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
        z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
        r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
        s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
        self.assertTrue(point.verify(z, Signature(r, s)))
        z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
        r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
        s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
        self.assertTrue(point.verify(z, Signature(r, s)))

    def test_sign(self):
        e = 12345
        z = int.from_bytes(hash256('Programming Bitcoin!'.encode('utf-8')), 'big')

        pk = PrivateKey(e)
        sig = pk.sign(z)
        self.assertTrue(pk.point.verify(z, sig))

    def test_sec(self):
        pk1 = PrivateKey(5000)
        pk2 = PrivateKey(2018 ** 5)
        pk3 = PrivateKey(0xdeadbeef12345)

        print(pk1.point.sec(False))
        print(pk2.point.sec(False))
        print(pk3.point.sec(False))

        pk4 = PrivateKey(5001)
        pk5 = PrivateKey(2019 ** 5)
        pk6 = PrivateKey(0xdeadbeef54321)

        print(pk4.point.sec(True))
        print(pk5.point.sec(True))
        print(pk6.point.sec(True))


