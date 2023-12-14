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
import logging

import arrow

from alarm_backends.service.new_report.factory import ReportFactory
from alarm_backends.service.scheduler.app import app
from bkmonitor.models import Report
from bkmonitor.report.utils import is_run_time, parse_frequency

logger = logging.getLogger("bkmonitor.cron_report")


@app.task(ignore_result=True, queue="celery_report_cron")
def send_report(report, channels=None):
    """
    发送邮件订阅
    """

    logger.info(f"start to send report{report.id}, current time: {arrow.now()}")
    ReportFactory.get_handler(report).run(channels)


@app.task(ignore_result=True, queue="celery_report_cron")
def new_report_detect():
    """
    检测邮件订阅
    """
    reports = Report.objects.filter(is_enabled=True)
    for report in reports:
        # 判断订阅是否有效
        if report.is_invalid():
            logger.info(f"report{report.id} is invalid.")
            continue
        # 判断订阅是否到执行时间
        frequency = report.frequency
        run_time_strings = parse_frequency(frequency)
        if not is_run_time(frequency, run_time_strings):
            logger.info(f"report{report.id} not at sending time.")
            continue
        # 异步执行订阅发送任务
        send_report.delay(report)
