# -*- coding: utf-8 -*-
from dataclasses import asdict, dataclass, fields
from enum import Enum
from typing import Union


class SpaceTypeEnum(Enum):
    """
    空间类型枚举
    """

    BKCC = "bkcc"  # CMDB 业务
    BCS = "bcs"  # BCS
    BKCI = "bkci"  # 蓝盾
    BKSAAS = "bksaas"  # 蓝鲸应用


class SpaceFunction(Enum):
    """
    空间能力枚举
    """

    APM = "APM"
    CUSTOM_REPORT = "CUSTOM_REPORT"  # 自定义上报
    HOST_COLLECT = "HOST_COLLECT"  # 主机采集
    CONTAINER_COLLECT = "CONTAINER_COLLECT"  # 容器采集
    HOST_PROCESS = "HOST_PROCESS"  # 主机监控
    UPTIMECHECK = "UPTIMECHECK"  # 自建拨测
    K8S = "K8S"  # Kubernetes
    CI_BUILDER = "CI_BUILDER"  # CI构建机
    PAAS_APP = "PAAS_APP"  # 蓝鲸应用


@dataclass
class Space:
    """
    空间格式
    """

    to_dict = asdict

    id: int
    space_type_id: str
    space_id: str
    space_name: str
    status: str
    space_code: Union[None, str]
    space_uid: str
    type_name: Union[None, str]
    bk_biz_id: int

    @classmethod
    def from_dict(cls, data):
        init_fields = {f.name for f in fields(cls) if f.init}
        filtered_data = {k: data.pop(k, None) for k in init_fields}
        if filtered_data["space_type_id"] == SpaceTypeEnum.BKCC.value:
            filtered_data["bk_biz_id"] = int(filtered_data["space_id"])
        else:
            filtered_data["bk_biz_id"] = -int(filtered_data["id"])
        instance = cls(**filtered_data)
        setattr(instance, "extend", data)
        return instance
