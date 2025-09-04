import optuna

# region Models
from pydantic import BaseModel
from abc import ABC, abstractmethod


class OptParamBase(BaseModel, ABC):
    """
    OptParamBase: 调优参数基类
    - param name: str 调优参数名称

    - property short_name: str, 缩写参数名称

    - abstract func add_to_trial(self, trial: optuna.Trial), 向optuna.trial中添加该参数的猜测值
    - abstract func to_echart_axis(self) -> dict, 转为echart的parallelAxis的坐标轴格式

    - func __repr__(self) -> str, 打印该参数的字符串表示
    """

    name: str

    @property
    def short_name(self) -> str:
        """
        缩写参数名称
        """
        return self.name.split(".")[-1]

    @abstractmethod
    def add_to_trial(self, trial: optuna.Trial):
        """
        向optuna.trial中添加该参数的猜测值
        """
        pass

    @abstractmethod
    def to_echart_axis(self) -> dict:
        """
        转为echart的parallelAxis的坐标轴格式
        """
        pass

    def __repr__(self) -> str:
        return "class " + self.__class__.__name__ + " - " + str(self.model_dump())

    def __str__(self) -> str:
        return self.__repr__()