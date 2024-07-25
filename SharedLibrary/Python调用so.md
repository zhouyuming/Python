# Python调用so

```C
int max(int a,int b)
{
    return a>b?a:b;
}
```

```bash
gcc max.c -fPIC -shared -o max.so
```

```python
from ctypes import cdll  
cur = cdll.LoadLibrary('./libmax.so')  
a = cur.max(1, 2)
print(a)
```

https://blog.csdn.net/qdPython/article/details/108855883

https://cloud.tencent.com/developer/article/1148454
