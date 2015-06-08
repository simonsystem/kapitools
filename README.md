# kapitools

## Installation

```
$ pip install git+git://github.com/simonsystem/kapitools.git
```

## Documentation
kapitools.**calc\_producing\_rate**(*building, product, level, workers, alternative=True*)

Get the calcutated producing rate from the server or a local file.

- str **building**: Building in which the Product is produced. (Ae-encoding for german uml.)
- str **product**: Product which should be calulated.
- str **level**: Your current producing level.
- int **workers**: Num of workers, you want to use.
- bool **alternative**: Optional: Gets the alternative producing rate for different CapiUniverses. Means uni 2-4. (default: true)

## Usage

```python
import kapitools
kapitools.set_cache("mycachefile.json")
print kapitools.calc_producing_rate("Manufaktur", "Boote", "Freier", 34)
print kapitools.calc_producing_rate("Bauernhof", "Bienenwachs", "Weber", 34)
print kapitools.calc_producing_rate("Holzfaeller", "Holz", "Weber", 76, alternative=False)
```

