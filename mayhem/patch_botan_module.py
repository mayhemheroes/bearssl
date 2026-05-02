#!/usr/bin/env python3
import os

# Fix 1: modules/botan/module.cpp - add botan 3.x EC headers for PointGFp typedef
filepath = "cryptofuzz/modules/botan/module.cpp"
with open(filepath) as f:
    content = f.read()
old = "#include <botan/aead.h>"
new = "#include <botan/aead.h>\n#include <botan/ec_group.h>\n#include <botan/ec_point.h>"
content = content.replace(old, new, 1)
with open(filepath, "w") as f:
    f.write(content)
print("Patched", filepath)

# Fix 2: modules/botan/bn_ops.cpp - remove curve_nistp.h (removed from botan 3.x)
filepath2 = "cryptofuzz/modules/botan/bn_ops.cpp"
with open(filepath2) as f:
    content2 = f.read()
content2 = content2.replace("#include <botan/internal/curve_nistp.h>\n", "")
with open(filepath2, "w") as f:
    f.write(content2)
print("Patched", filepath2)
