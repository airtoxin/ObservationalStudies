# ObservationalStudies
observational study helper module

https://en.wikipedia.org/wiki/Observational_study
http://weber.hs.tmu.ac.jp/cat/project/kihon/dezain.html#cross
http://www.med.osaka-u.ac.jp/pub/kid/clinicaljournalclub5.html

## Develop

### setup

Create separated new python environment. [pyenv](https://github.com/yyuu/pyenv) and [direnv](https://github.com/direnv/direnv) are good.

0. Install `virtualenv`, `pyenv` and `direnv`
0. run `direnv edit .`

```bash
export PYENV_ROOT=.pyenv
layout python .pyenv/versions/3.4.3/bin/python
```

0. run `direnv allow .` (with few errors)
0. run `pyenv install 3.4.3`
0. re-run `direnv allow .` (no errors)
