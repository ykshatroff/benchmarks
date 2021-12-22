# Remove duplicates

Set vs List performance on removing duplicates from an iterable.

### Run:
```shell
python -m set_vs_list
```

### Results:
  * [Python 3.9.7 `pyenv`](./python_3.9.7-pyenv.txt)   
  * [Python 3.9.9 `archlinux`](./python_3.9.9-archlinux.txt)   
  * [Python 3.10.1 `pyenv`](./python_3.10.1-pyenv.txt)   
  * [Python 3.10.1 `archlinux`](./python_3.10.1-archlinux.txt)   

### Conclusions:
  * Set starts to pay off at lengths of ~100 elements (the more of them are unique, the more the gain.)
  * List performs slightly better on numbers vs strings (20-30%), for Set there's obviously no difference.
  * String length doesn't affect both versions' results; the presence of similar characters in the strings
    doesn't positively affect list comparison, neither does length difference.
  * Function calls are still expensive. The key function (`lambda x: x` by default) slows down the Set performance 3x
    compared to pure Set version, and 2x compared to the conditional version `key(item) if key else item`.
