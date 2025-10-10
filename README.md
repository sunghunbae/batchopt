# Batch Optimizer for AIMNet2

BatchOptimizer class from [Auto3D](https://github.com/isayevlab/Auto3D_pkg/)

## Install

```sh
$ pip install .
```

OR

```sh
$ pip install git+https://github.com/sunghunbae/batchopt.git

```

## Dependencies

- rdkit
- numpy
- torch
- torchani (optional for ANI2x and ANI2xt)
- aimnet ([github](https://github.com/isayevlab/aimnetcentral))
- rdworks ([pypi](https://pypi.org/project/rdworks/))

## Usage

```py
import rdworks
from batchopt import BatchOptimizer


mol = rdworks.Mol('COC1=CC2=NC=CC(=C2C=C1C(=O)N)OC3=CC(=C(C=C3)NC(=O)NC4CC4)Cl', 'lenvatinib')

batchsize_atoms = 16 * 1024

# generate and optimize each conformer with default MMFF94
mol = mol.make_confs(n=50, method='ETKDG')
# optimize with default MMFF94
mol = mol.optimize_confs()
mol = mol.drop_confs(similar=True, similar_rmsd=0.3)
mol = mol.optimize_confs(calculator=BatchOptimizer, batchsize_atoms=batchsize_atoms)
# remove similar conformers (RMSD <0.3) [and stereo-flipped conformers by default]
mol = mol.drop_confs(similar=True, similar_rmsd=0.3)
mol = mol.sort_confs().rename()
mol = mol.align_confs().cluster_confs(sort='energy')

print(f'Number of unique conformers: {mol.num_confs}')
serialized = mol.serialize()

m = rdworks.Mol().deserialize(serialized)

m = m.calculate_torsion_energies(
    calculator = BatchOptimizer,
    torsion_key = None,
    simplify = True,
    fmax = 0.05,
    interval = 20,
    use_converged_only = True,
    batchsize_atoms = batchsize_atoms,
)
```


## License

Original `Auto3D` has MIT license.
