# kapitools

## Installation

```
$ pip install git+git://github.com/simonsystem/kapitools.git
```

## Usage

```python
import kapitools
print kapitools.calc_producing_rate("Manufaktur", "Boote", "Freier", 34)
print kapitools.calc_producing_rate("Bauernhof", "Bienenwachs", "Weber", 34)
print kapitools.calc_producing_rate("Holzfaeller", "Holz", "Weber", 76, alternative=False)
```

