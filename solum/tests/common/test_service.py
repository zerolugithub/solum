# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_service
----------------------------------

Tests for `solum.common.service` module.
"""

import testtools

from solum.common import service
from solum import objects
from solum.objects import plan as abstract
from solum.tests import base


class TestService(base.BaseTestCase):

    def test_prepare_invokes_object_load(self):
        objects.registry.clear()
        with testtools.ExpectedException(KeyError):
            objects.registry.Plan()
        service.prepare_service([])
        self.assertTrue(issubclass(objects.registry.Plan, abstract.Plan))
