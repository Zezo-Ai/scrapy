import sys

from twisted.internet.defer import inlineCallbacks
from twisted.trial import unittest

import scrapy
from tests.utils.testproc import ProcessTest


class TestVersionCommand(ProcessTest, unittest.TestCase):
    command = "version"

    @inlineCallbacks
    def test_output(self):
        encoding = sys.stdout.encoding or "utf-8"
        _, out, _ = yield self.execute([])
        assert out.strip().decode(encoding) == f"Scrapy {scrapy.__version__}"

    @inlineCallbacks
    def test_verbose_output(self):
        encoding = sys.stdout.encoding or "utf-8"
        _, out, _ = yield self.execute(["-v"])
        headers = [
            line.partition(":")[0].strip()
            for line in out.strip().decode(encoding).splitlines()
        ]
        assert headers == [
            "Scrapy",
            "lxml",
            "libxml2",
            "cssselect",
            "parsel",
            "w3lib",
            "Twisted",
            "Python",
            "pyOpenSSL",
            "cryptography",
            "Platform",
        ]
