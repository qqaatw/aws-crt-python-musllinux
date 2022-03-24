#!/bin/bash
set -e -u -x

repair_wheel () {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w wheelhouse/
    fi
}


#cd /io

if [ ! -d aws-crt-python ] 
then
    git clone https://github.com/awslabs/aws-crt-python.git --recursive
fi

# Check out and update latest version
cd aws-crt-python/
git checkout $(git tag | sort -V | tail -1)
/opt/python/cp310-cp310/bin/python ./continuous-delivery/update-version.py
cd ..

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    "${PYBIN}/pip" wheel aws-crt-python/ --no-deps -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install awscrt --no-index -f wheelhouse
    (cd aws-crt-python/; "${PYBIN}python" -m unittest discover --failfast --verbose)
done