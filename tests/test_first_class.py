
class TestFirstClass():
    # Definir una clase es útil cuando se tiene un conjunto de pruebas que tienen el mismo alcance.

    def test_second_test(self):
        hello = "Hello world!"
        assert hello.upper() == "HELLO WORLD!"