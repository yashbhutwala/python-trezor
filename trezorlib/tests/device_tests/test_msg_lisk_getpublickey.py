# This file is part of the Trezor project.
#
# Copyright (C) 2012-2018 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from binascii import hexlify
import pytest

from .common import TrezorTest
from trezorlib import lisk
from trezorlib.tools import parse_path

LISK_PATH = parse_path("m/44h/134h/0h/0h")


@pytest.mark.lisk
@pytest.mark.skip_t1
class TestMsgLiskGetPublicKey(TrezorTest):

    def test_lisk_get_public_key(self):
        self.setup_mnemonic_nopin_nopassphrase()
        sig = lisk.get_public_key(self.client, LISK_PATH)
        assert hexlify(sig.public_key) == b'eb56d7bbb5e8ea9269405f7a8527fe126023d1db2c973cfac6f760b60ae27294'
