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
from alarm_backends.service.subscription.handler.clustering import (
    ClusteringSubscriptionHandler,
)
from alarm_backends.service.subscription.handler.dashboard import (
    DashboardSubscriptionHandler,
)
from alarm_backends.service.subscription.handler.scene import SceneSubscriptionHandler
from bkmonitor.models.email_subscription import EmailSubscription, ScenarioEnum

SUPPORTED_SCENARIO = {
    ScenarioEnum.CLUSTERING: ClusteringSubscriptionHandler,
    ScenarioEnum.DASHBOARD: DashboardSubscriptionHandler,
    ScenarioEnum.SCENE: SceneSubscriptionHandler,
}


class SubscriptionFactory(object):
    def __init__(self, susbcription_ids=None):
        if susbcription_ids:
            self.subscriptions = EmailSubscription.objects.filter(id__in=susbcription_ids)
        else:
            self.subscriptions = list(EmailSubscription.objects.filter(is_enabled=True))

    def get_handler(self, subscription):
        subscription_handler_cls = SUPPORTED_SCENARIO[subscription.scenario]
        return subscription_handler_cls(subscription)

    def detect_run_time(self):
        pass

    def detect_current_period_subscriptions(self):
        for subscription in self.subscriptions:
            pass
