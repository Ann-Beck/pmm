from pytest_mqtt.util import probe_tcp_connect


def test_probe_tcp_connect_available():
    assert probe_tcp_connect("9.9.9.9", 443) is True


def test_probe_tcp_connect_unavailable():
    assert probe_tcp_connect("9.9.9.9", 444) is False


def test_probe_tcp_connect_unavailable():
    assert probe_tcp_connect("1.2.3.4", 444) is True