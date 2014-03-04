from nose.tools import assert_equal
import logging

from vispy import app
from vispy.util import (logger, use_log_level, _TempDir, assert_in,
                        assert_not_in)

temp_dir = _TempDir()


def test_logging():
    """Test logging context manager"""
    ll = logger.level
    with use_log_level('warning'):
        assert_equal(logger.level, logging.WARN)
    assert_equal(logger.level, ll)
    with use_log_level('debug'):
        assert_equal(logger.level, logging.DEBUG)
    assert_equal(logger.level, ll)


def test_debug_logging():
    """Test advanced debugging logging"""
    with use_log_level('debug', 'Selected', True) as l:
        a = app.Application()
        a.use()
        a.quit()
    assert_equal(len(l), 1)
    assert_in('vispy.app.application', l[0])

    with use_log_level('debug', record=True) as l:
        a = app.Application()
        a.use()
        a.quit()
    assert_equal(len(l), 1)
    assert_in('vispy.app.application', l[0])

    with use_log_level('debug', 'foo', True) as l:
        a = app.Application()
        a.use()
        a.quit()
    assert_equal(len(l), 0)

    with use_log_level('info', record=True) as l:
        a = app.Application()
        a.use()
        a.quit()
    assert_equal(len(l), 1)
    assert_not_in('vispy.app.application', l[0])
