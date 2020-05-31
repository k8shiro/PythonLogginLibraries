# PythonLogginLibraries
Compare logging libraries of python.


# 使い方

```
docker image build -t python-logging-libraries .
docker run -it --rm --name python-logging-libraries \
    -v $(pwd)/src:/src \
    -v $(pwd)/log:/var/log \
    python-logging-libraries ash

# logzeroのサンプル
python logzero_sample/sample1.py
python logzero_sample/sample2.py

# loguruのサンプル
python loguru_sample/sample1.py
python loguru_sample/sample2.py

# pylogrusのサンプル
python pylogrus_sample/sample1.py
python pylogrus_sample/sample2.py
```
