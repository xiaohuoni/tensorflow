# 如何运行
先安装环境https://www.tensorflow.org/install/pip
因为tensorflow安装在虚拟环境，所以要切换到虚拟环境上，使用。
```sh
$ virtualenv --system-site-packages -p python3 ./venv
$ source ./venv/bin/activate  # sh, bash, ksh, or zsh
$ python ./422.py
```

## 项目说明
### 422 
检查零件是否合格，小于0.2为合格，422输出结果[[0.15625]]