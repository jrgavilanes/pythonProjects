import main


def setup_module(module):
    print("\nSETUP\n")


def teardown_module(module):
    print("\nTEARDOWN\n")


def test_main():
    assert main.saluda("juanra") == "hola juanra"


def test_main2():
    assert main.saluda("demo") == "hola demo"
