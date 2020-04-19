def pytest_addoption(parser):
    parser.addoption("--external-URI", action="store_true", help="to provide an external URI for testing")


def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))