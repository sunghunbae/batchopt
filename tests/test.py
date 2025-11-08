from rdworks import Mol
from batchopt import BatchOptimizer, BatchSinglePoint


def test_singlepoint_batch():
    mol = Mol("CC(=O)NC1=CC=C(O)C=C1", "acetaminophen")
    mol = mol.make_confs(n=5, method='ETKDG')
    mol = mol.singlepoint_confs(calculator=BatchSinglePoint, batchsize_atoms=16384)
    assert all([_.props.get('E_tot(kcal/mol)') is not None for _ in mol.confs])


def test_optimize_confs_batch():
    mol = Mol("CC(=O)NC1=CC=C(O)C=C1", "acetaminophen")
    mol = mol.make_confs(n=5, method='ETKDG')
    mol = mol.optimize_confs(calculator=BatchOptimizer, batchsize_atoms=16384)
    assert all([_.props.get('E_tot_init(kcal/mol)') is not None for _ in mol.confs])
    assert all([_.props.get('E_tot(kcal/mol)') is not None for _ in mol.confs])
    assert all([_.props.get('Converged') is not None for _ in mol.confs])