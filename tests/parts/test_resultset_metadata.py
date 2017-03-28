# Copyright 2014, 2015 SAP SE.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from io import BytesIO
from pyhdb.protocol.parts import ResultSetMetaData
from pyhdb.protocol import constants


def test_unpack_data():
    payload = BytesIO(b'\x01\x09\x00\x00\x02\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff'
                      b'\x00\x00\x00\x00\x08\x00\x00\x00\x01\x03\x00\x00\x0a\x00\x00\x00'
                      b'\xff\xff\xff\xff\xff\xff\xff\xff\x10\x00\x00\x00\x10\x00\x00\x00'
                      b'\x07\x41\x53\x54\x52\x49\x4e\x47\x07\x41\x53\x54\x52\x49\x4e\x47'
                      b'\x07\x41\x4e\x55\x4d\x42\x45\x52')

    columns, = ResultSetMetaData.unpack_data(2, payload)

    assert len(columns) == 2

    str_col = columns[0]
    assert str_col[0] == 1  # COLUMNOPTIONS, can be NULL
    assert str_col[1] == constants.type_codes.VARCHAR
    assert str_col[2] == 0  # FRACTION
    assert str_col[3] == 2  # LENGTH
    assert str_col[4] == 0  # unused
    assert str_col[5] == None  # Table Name
    assert str_col[6] == None  # Schema Name
    assert str_col[7] == 'ASTRING'  # Column Name
    assert str_col[8] == 'ASTRING'  # Column label

    int_col = columns[1]
    assert int_col[0] == 1  # COLUMNOPTIONS, can be NULL
    assert int_col[1] == constants.type_codes.INT
    assert int_col[2] == 0  # FRACTION
    assert int_col[3] == 10  # LENGTH
    assert int_col[4] == 0  # unused
    assert int_col[5] == None  # Table Name
    assert int_col[6] == None  # Schema Name
    assert int_col[7] == 'ANUMBER'  # Column Name
    assert int_col[8] == 'ANUMBER'  # Column label
