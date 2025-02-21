import sys
print("Python executable:", sys.executable)

try:
    import torch
    print("Torch version:", torch.__version__)
except ImportError as e:
    print("Torch not found:", e)
