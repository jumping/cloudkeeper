from cloudkeeper.baseplugin import BaseCollectorPlugin
from cloudkeeper.args import ArgumentParser
from cloudkeeper.baseresources import BaseResource


class SomeTestResource(BaseResource):
    resource_type = 'some_test_resource'


class SomeTestPlugin(BaseCollectorPlugin):
    cloud = 'test'

    def collect(self) -> None:
        account = SomeTestResource('Example Account', {})
        self.graph.add_resource(self.root, account)

    @staticmethod
    def add_args(arg_parser: ArgumentParser) -> None:
        arg_parser.add_argument('--example-region', help='Example Region', dest='example_region', type=str,
                                default=None, nargs='+')


def test_plugin():
    plugin = SomeTestPlugin()
    plugin.collect()
    assert len(plugin.graph.nodes) == 2
