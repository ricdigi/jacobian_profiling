import pytest
from sympy import Matrix, simplify
from benchmark.models import generate_input_pendulum
from benchmark.models import derivative_example

from implementations.forward_jacobian_final import forward_jacobian
from implementations.forward_jacobian_sdm import forward_jacobian_sdm
from implementations.forward_jacobian_ric2 import forward_jacobian_ric2
from implementations.forward_jacobian_ric3 import forward_jacobian_ric3
from implementations.forward_jacobian_ric4 import forward_jacobian_ric4
from implementations.forward_jacobian_sdm_non_exraw import forward_jacobian_sdm_non_exraw
from implementations.forward_jacobian_sam import forward_jacobian_sam
from implementations.jacobian_classic import jacobian_classic
from implementations.jacobian_protosym import jacobian_protosym
from implementations.jacobian_symengine import jacobian_symengine


@pytest.fixture
def setup_inputs(n = 4):
    return generate_input_pendulum(n)

def test_forward_jacobian_sdm_non_exraw(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_sdm_non_exraw = forward_jacobian_sdm_non_exraw(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_sdm_non_exraw - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)

def test_forward_jacobian_final(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_final = forward_jacobian(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_final - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)

def test_forward_jacobian_sdm(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_sdm = forward_jacobian_sdm(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_sdm - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_forward_jacobian_ric2(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_ric2 = forward_jacobian_ric2(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_ric2 - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_forward_jacobian_ric3(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_ric3 = forward_jacobian_ric3(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_ric3 - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_forward_jacobian_ric4(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_ric4 = forward_jacobian_ric4(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_ric4 - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_ric4_derivative():
    expr, wrt = derivative_example()

    jacobian_ric4 = forward_jacobian_ric4(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_ric4 - jacobian_cla)

    print(diff)

    assert diff == Matrix.zeros(*diff.shape)


def test_forward_jacobian_sam(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_sam = forward_jacobian_sam(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_sam - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_jacobian_protosym(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_pro = jacobian_protosym(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_pro - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


def test_jacobian_symengine(setup_inputs):
    expr, wrt = setup_inputs

    # Compute the Jacobian using each implementation
    jacobian_sym = jacobian_symengine(expr, wrt)
    jacobian_cla = jacobian_classic(expr, wrt)

    diff = simplify(jacobian_sym - jacobian_cla)

    print(diff)

    # Check that all Jacobians are the same
    assert diff == Matrix.zeros(*diff.shape)


