import unittest
from mock import Mock
import plugin

class PluginProcessorsTest(unittest.TestCase):
    def test_register(self):
        plugin._plugin_processors = Mock(name = "PluginProcessors")
        plugin.register_processor("something", "something-else")
        plugin._plugin_processors.assert_called_with("something", "something-else")
