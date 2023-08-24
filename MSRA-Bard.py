```python
import numpy as np


class MolecularStructure:
    def __init__(self, atoms, bonds):
        self.atoms = atoms
        self.bonds = bonds

    def get_information(self):
        info = f"The molecular structure contains {len(self.atoms)} atoms: {', '.join(self.atoms)}."
        info += f"\nBonds: {', '.join([f'{bond[0]}-{bond[1]}' for bond in self.bonds])}."
        return info

    def serialize(self):
        return {'atoms': self.atoms, 'bonds': self.bonds}

    @staticmethod
    def deserialize(serialized_structure):
        return MolecularStructure(serialized_structure['atoms'], serialized_structure['bonds'])


def create_structure(atoms, bonds):
    return MolecularStructure(atoms, bonds)


# Example usage
if __name__ == "__main__":
    structure = create_structure(["H", "O", "H"], [("H", "O"), ("O", "H")])
    print(structure.get_information())
    serialized = structure.serialize()
    deserialized_structure = MolecularStructure.deserialize(serialized)
    print(deserialized_structure.get_information())
```
