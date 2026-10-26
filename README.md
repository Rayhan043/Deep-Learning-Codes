# Deep Learning Codes

A structured collection of deep-learning study material, notebooks, implementations,
and supporting lecture resources.

## Repository map

| Area | Contents |
| --- | --- |
| `Intro M1` | Introductory deep-learning concepts |
| `Perceptron(M-2,3,)` | Perceptron implementations |
| `Back propagation` | Backpropagation reference material |
| `Module 4`, `Modules 5`, `Module 6` | Core optimization and activation topics |
| `Data_loader` | PyTorch datasets and data-loader examples |
| `AutoGrade` | PyTorch autograd examples |
| `nn Module` | PyTorch neural-network module examples |
| `Model_train_Pytorch_Scratch` | Training a model from scratch |
| `Batch Normalization` and `M-18` | Normalization and scaling |
| `M-20 Optimizer` and `Optimaizer` | Optimizer notes and examples |
| `ANN Implementation` | ANN and Fashion-MNIST work |
| `Deep-Learning-main` | Module-by-module course material |
| `Assignment-1`, `Mid` | Assignments and assessment notebooks |
| `Practice DL` | Standalone Python practice |

## Getting started

Most examples are Jupyter notebooks:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install jupyter numpy pandas matplotlib scikit-learn torch torchvision
jupyter notebook
```

Install only the dependencies required by the notebook you want to run. Some
notebooks download datasets at runtime and may require an internet connection.

## Notes

- The original learning folders and filenames are preserved to keep notebook links
  and course references intact.
- Python bytecode, virtual environments, checkpoints, secrets, and other generated
  files are excluded through `.gitignore`.
- Third-party book downloads are not included; use legally obtained copies locally.
