from src.pytemplate.domain.models import Operands


def test_Operands():
    operands = Operands(first_operand=1, second_operand=2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2
