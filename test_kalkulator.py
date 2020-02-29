import kalkulator
import pytest


@pytest.mark.podst
def test_odejmowanie():
    assert kalkulator.odejmowanie(20, 10) == 10
    assert kalkulator.odejmowanie(100, 20) == 4 * 20

@pytest.mark.gim
def test_mnozenie():
    assert kalkulator.mnozenie(4, 10) == 40
    assert kalkulator.mnozenie(2.5, 4) == 10

@pytest.mark.gim
def test_dzielenie ():
    assert kalkulator.dzielenie(10, 2) == 5
    assert kalkulator.dzielenie(4, 1) == 4
@pytest.mark.lic
def test_reszta_zdzielenia():
    a = kalkulator.reszta_zdzielenia(10, 3)
    assert a == 1
@pytest.mark.skip(reason = "do not string test")


def test_string():
    klub = kalkulator.dodawanie("FC", " Barcelona")
    assert klub == "FC Barcelona"
    assert type(klub) is str
    assert "FC" in klub


def test_clone_string():
    clone = kalkulator.mnozenie(3, "Tomek")
    assert clone == "TomekTomekTomek"
    assert type(clone) is str
    assert "omek" in clone
    print("wykonał się test_clone_string")

def test_nazwa():
    b = kalkulator.nazwa()
    assert type(b) is str
    assert b == "Kalkulator Toms"
    assert " " in b

@pytest.mark.parametrize("n1, n2, res",
                         [
                             (7, 3, 10),
                             ("Hello", " Word", "Hello Word")
                         ]
                         )
def test_dodawanie(n1, n2, res):
    assert kalkulator.dodawanie(n1 , n2) == res




