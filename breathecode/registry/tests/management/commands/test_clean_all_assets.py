'''
Tests / Registry /assets
'''
from unittest.mock import MagicMock, patch, call
from mixer.backend.django import mixer

from ...mixins import RegistryTestCase
from ....management.commands.clean_all_assets import Command


class CleanAssetTestCase(RegistryTestCase):
    '''
    Tests / Registry /assets
    '''

    @patch('django.core.management.base.OutputWrapper.write', MagicMock())
    def test_clean_asset_without_readme_raw(self):
        from django.core.management.base import OutputWrapper

        command = Command()

        result = command.handle()

        self.assertEqual(result, None)

        self.assertEqual(OutputWrapper.write.call_count, 0)

        self.assertEqual(self.bc.database.list_of('registry.Asset'), [])

        self.assertEqual(OutputWrapper.write.call_args_list, [])
