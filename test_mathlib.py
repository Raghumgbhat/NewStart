import mathlib
import pytest
import sys
def test_calc_total():
	total = mathlib.calc_total(3,5)
	assert total == 8

@pytest.mark.skipif(sys.version_info > (3,5), reason="i dont want to run multiply")
def test_calc_multiply():
	total = mathlib.calc_multiply(3,5)
	assert total==15 
