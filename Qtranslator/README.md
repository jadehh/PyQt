## Qtranslator
Qt语言切换

### ui文件转py文件

```bash
pyuic5 -o main.py main.ui
```

### py文件转ts文件
```bash
pylupdate5 main.py -ts zh_CN.ts
```
> 使用Qt中的Linguist.exe打开ts文件,翻译->并发布生成qm文件


### 测试py文件转pyd

```bash
easycython main.py main.pyd
```