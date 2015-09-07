import unittest
from mock import Mock
import plugin

class PluginProcessorsTest(unittest.TestCase):
    def test_register_function(self):
        plugin._plugin_processors = Mock(name = "PluginProcessors")
        plugin.register_processor("something", "something-else")
        plugin._plugin_processors.register.assert_called_with("something", "something-else", plugin.PluginPriority.NORMAL)

    def test_run_function(self):
        plugin._plugin_processors = Mock(name = "PluginProcessors")
        plugin.run_processor("something", "something-else", "another-something", name="A", type="b", squared="c")
        plugin._plugin_processors.run.assert_called_with("something", ("something-else", "another-something"), {'squared': 'c', 'type': 'b', 'name':'A'})

    def test_inits_processor(self):
        processors = plugin.PluginProcessors()
        self.assertFalse(processors.has_processor("something"))
        processors.get_processor("something")
        self.assertTrue(processors.has_processor("something"))

    def test_sets_processor(self):
        processors = plugin.PluginProcessors()

        orig = processors.get_processor("something")
        processors.set_processor("something", plugin.PluginFunctions())
        self.assertNotEqual(orig, processors.get_processor("something"))

    def test_registers_function(self):
        def do_something():
            1 + 1

        processors = plugin.PluginProcessors()
        processors.register("something", do_something, plugin.PluginPriority.HIGH)

        self.assertEquals(1, len(processors.processors))
        self.assertEquals(1, len(processors.processors["something"].functions))
