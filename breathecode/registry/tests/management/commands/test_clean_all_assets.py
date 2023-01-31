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
    def test_clean_asset_with_nothing(self):
        from django.core.management.base import OutputWrapper

        command = Command()

        result = command.handle()

        self.assertEqual(result, None)

        self.assertEqual(OutputWrapper.write.call_count, 0)

        self.assertEqual(self.bc.database.list_of('registry.Asset'), [])

        self.assertEqual(OutputWrapper.write.call_args_list, [])

    @patch('django.core.management.base.OutputWrapper.write', MagicMock())
    def test_clean_asset_with_a_readme(self):
        from django.core.management.base import OutputWrapper

        asset = {
            'readme_url': 'https://raw.githubusercontent.com/breatheco-de/exercise-postcard/main/README.md'
        }
        readme_url1 = f'https://github.com/testing-number-1.md'
        readme_url2 = f'https://github.com.md'
        assets = [{'readme_url': readme_url1}, {'readme_url': readme_url2}]

        model = self.bc.database.create(asset=assets)

        command = Command()

        result = command.handle()

        self.assertEqual(result, None)

        self.assertEqual(OutputWrapper.write.call_count, 0)

        self.assertEqual(self.bc.database.list_of('registry.Asset'),
                         [{
                             **self.bc.format.to_dict(model.asset[0]), 'readme_url':
                             f'https://github.com/testing-number-1.md'
                         }, {
                             **self.bc.format.to_dict(model.asset[1]), 'readme_url': f'https://github.com.md'
                         }])

        self.assertEqual(OutputWrapper.write.call_args_list, [])
