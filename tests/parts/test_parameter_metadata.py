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
from pyhdb.protocol.parts import ParameterMetadata
from pyhdb.protocol import constants


def test_unpack_data():
    payload = BytesIO(b'\x02\x09\x01\x00\xff\xff\xff\xff\x01\x00\x00\x00\x08\x00\x00\x00')
    values, = ParameterMetadata.unpack_data(1, payload)

    assert len(values) == 1
    
    first_parameter = values[0]

    assert first_parameter.mode == 2
    assert first_parameter.datatype == constants.type_codes.VARCHAR
    assert first_parameter.iotype == 1
    assert first_parameter.id == 0
    assert first_parameter.length == 1
    assert first_parameter.fraction == 0
