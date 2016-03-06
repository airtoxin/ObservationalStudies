# ObservationalStudies
observational study helper module

https://en.wikipedia.org/wiki/Observational_study
http://weber.hs.tmu.ac.jp/cat/project/kihon/dezain.html#cross
http://www.med.osaka-u.ac.jp/pub/kid/clinicaljournalclub5.html

## Develop

### setup

Create separated new python environment. [pyenv](https://github.com/yyuu/pyenv) and [direnv](https://github.com/direnv/direnv) are good.

0. Install environment utils: `virtualenv`, `pyenv` and `direnv` via running `$ pip install {NAME}`
0. Edit envrc file: run `$ direnv edit .`

```bash
export PYENV_ROOT=.pyenv
layout python .pyenv/versions/3.4.3/bin/python
```

0. Setup pyenv root directory: run `$ direnv allow .` (with few errors)
0. Install python: run `$ pyenv install 3.4.3`
0. Separate python: re-run `$ direnv allow .` (no errors)

### test

0. Install test tools: `pytest` and `tox` via running `$ pip install {NAME}`
0. Install module locally: run `$ python setup.py install`
0. Execute tests: run `$ tox`
