# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import arrow
from django.db import models

from bkmonitor.utils.itsm import APPROVAL_STATUS_CHOICES
from bkmonitor.utils.model_manager import AbstractRecordModel, Model
from constants.email_subscription import (
    ChannelEnum,
    ScenarioEnum,
    SendModeEnum,
    SendStatusEnum,
    SubscriberTypeEnum,
)


class SubscriptionChannel(Model):
    """
    订阅渠道
    """

    subscription_id = models.IntegerField(verbose_name="订阅ID", db_index=True)
    channel_name = models.CharField(verbose_name="渠道名称", max_length=32, choices=ChannelEnum.get_choices())
    is_enabled = models.BooleanField(verbose_name="是否启用", default=True)
    subscribers = models.JSONField(verbose_name="订阅人", default=list)
    send_text = models.CharField(verbose_name="提示文案", max_length=256, default="", blank=True, null=True)

    class Meta:
        verbose_name = "订阅渠道"
        verbose_name_plural = "订阅渠道"
        db_table = "subscription_channel"


class SubscriptionSendRecord(Model):
    """
    订阅发送记录
    """

    subscription_id = models.IntegerField(verbose_name="订阅ID", db_index=True)
    channel_name = models.CharField(verbose_name="渠道名称", max_length=32, choices=ChannelEnum.get_choices())
    send_results = models.JSONField(verbose_name="发送结果详情", default=list)
    send_status = models.CharField(verbose_name="发送状态", max_length=32, choices=SendStatusEnum.get_choices())
    send_time = models.DateTimeField(verbose_name="发送时间")
    send_round = models.IntegerField(verbose_name="发送轮次", default=0)

    class Meta:
        verbose_name = "订阅发送记录"
        verbose_name_plural = "订阅发送记录"
        db_table = "subscription_send_record"
        unique_together = ["subscription_id", "channel_name", "send_round"]
        index_together = ["subscription_id", "send_round"]


class EmailSubscription(AbstractRecordModel):
    """
    邮件订阅
    """

    name = models.CharField(verbose_name="订阅名称", max_length=64)
    bk_biz_id = models.IntegerField(verbose_name="业务ID", default=0, db_index=True)
    scenario = models.CharField(verbose_name="订阅场景", max_length=32, choices=ScenarioEnum.get_choices())
    frequency = models.JSONField(verbose_name="发送频率", default=dict)
    content_config = models.JSONField(verbose_name="内容配置", default=dict)
    scenario_config = models.JSONField(verbose_name="场景配置", default=dict)
    start_time = models.IntegerField(verbose_name="开始时间", null=True)
    end_time = models.IntegerField(verbose_name="结束时间", null=True)
    send_mode = models.CharField(verbose_name="发送模式", max_length=32, choices=SendModeEnum.get_choices())
    subscriber_type = models.CharField(verbose_name="订阅人类型", max_length=32, choices=SubscriberTypeEnum.get_choices())
    send_round = models.IntegerField(verbose_name="最近一次发送轮次", default=0)
    is_manager_created = models.BooleanField(verbose_name="是否管理员创建", default=False)

    class Meta:
        verbose_name = "邮件订阅"
        verbose_name_plural = "邮件订阅"
        db_table = "email_subscription"

    def is_invalid(self):
        now_timestamp = arrow.now().timestamp
        if now_timestamp > self.end_time or now_timestamp < self.start_time:
            return True
        return False


class SubscriptionApplyRecord(AbstractRecordModel):
    """
    订阅审批记录
    """

    subscription_id = models.IntegerField(verbose_name="订阅ID", db_index=True)
    bk_biz_id = models.IntegerField(verbose_name="业务ID", db_index=True)
    approvers = models.JSONField("审批人", default=list)
    expire_time = models.DateTimeField("过期时间", null=True, default=None)
    approval_step = models.JSONField("当前步骤", default=list)
    approval_sn = models.CharField("审批单号", max_length=128, default="", null=True, blank=True)
    approval_url = models.CharField("审批地址", default="", max_length=1024, null=True, blank=True)
    status = models.CharField("审批状态", max_length=32, choices=APPROVAL_STATUS_CHOICES)

    class Meta:
        verbose_name = "订阅审批记录"
        verbose_name_plural = "订阅审批记录"
        db_table = "subscription_apply_record"
