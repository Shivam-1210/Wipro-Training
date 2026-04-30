from src.calculation import Calculation


class TestCalc:
    calc  = Calculation()

    def test_area_of_square(self):
        res = self.calc.area_of_square(10)
        assert res == 100, 'Area is wrong'


    def test_peri_of_rect(self):
        res = self.calc.peri_of_rect(10,5)
        assert res == 30, 'peri is wrong'