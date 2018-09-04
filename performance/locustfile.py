# _*_ coding=utf-8 _*_
# __author__ = 'D054'
from locust import task, TaskSet, HttpLocust, events
from api import *
import Queue
import random


class WebSiteTask(TaskSet):
    # def on_start(self):
    #     self.index = index1()

    @task
    def index(self):
        # uid = random.choice(id_lists)
        # sort_list(uid)
        # print uid
        # my_asset_index(uid)
        # login("15566778800", "123456")
        _id = random.randint(34, 342)

        # query_list("286836", "201274")
        # clock("286836", "147893000", "201274")

        # salary_detail(_id)
        # query_salary_list("baa46b199e5cf9811a53ab89eaca3c9f")
        # activity("148452187", "245127430", "都会", "17900000007")
        # activity_combo("148452187", "245127430", "都会", "17900000007", "1123")
        # goods("148452187", "245127430", "都会", "17900000007", "1123", "1834")
        # exchange_info("148452187", "245127430", "都会", "17900000007")

        # pre_exchange("148452187", "245127430", "都会", "17900000007", "1123", "1834")
        # salary_index(server_sign)

        # server_index(server_sign)
        # userbase_index(server_sign)
        # strategy_index(server_sign)
        # query_list("286836", "147893000")
        # clock("286836", "147893000", "93274")
        # my_rule(server_sign)
        # city_list(server_sign)
        # air_ticket_query(server_sign)
        # air_query_info(server_sign)
        # order_detail(server_sign)
        # hotel_order_detail(server_sign)
        # hotel_order_list(server_sign)
        # hotel_query_stars(server_sign)
        # insurance_detail(server_sign)
        # pre_exchange("148452187", "245127430", "都会", "17900000007", "1123", "1834")
        # air_ticket_order(server_sign)
    # @task
    # def index(self):
    #     try:
    #         data = self.locust.user_data_queue.get()
    #         self.locust.count.append(data)
    #         # print len(self.locust.count)
    #     except Queue.Empty:
    #         print('account data run out, test ended.')
    #         exit(0)
    #     trade_invest_bank_v4(data)
        # trade_confirm_migrate_v4(data)
        # trade_investment_v4(data)
        # data = random.choice(id_lists)
        # index(data)
        # print data
        # cash_activity_sign(data)
        # cash_activity_send_sign(data)
        # cash_activity_sign_info_mew(data)
        # coupon_all_list_3(data)
        # my_asset_index(data)
        # regular_project_dtl(data)
        # project_current_dtl(data)
        # regular_project_rlist(data)

    # @task(1)
    # def my_asset(self):
    #     data = random.choice(id_lists)
    #     # my_asset_index(data)
    #     # cash_activity_sign(data)
    #     # cash_activity_send_sign(data)
    #     # cash_activity_sign_info_mew(data)
    #     # coupon_all_list_1(data)
    #     my_asset_index(data)
    #     # regular_project_dtl(data)
    #     # project_current_dtl(data)
    #     # regular_project_rlist(data)

    # @task(1)
    # def my_asset1(self):
    #     data = random.choice(id_lists)
    #     # my_asset_index(data)
    #     # cash_activity_sign(data)
    #     # cash_activity_send_sign(data)
    #     # cash_activity_sign_info_mew(data)
    #     # coupon_all_list_2(data)
    #     # my_asset_index(data)
    #     # regular_project_dtl(data)
    #     project_current_dtl(data)
    #     # regular_project_rlist(data)
    #
    # @task(1)
    # def my_asset2(self):
    #     data = random.choice(id_lists)
    #     # my_asset_index(data)
    #     # cash_activity_sign(data)
    #     # cash_activity_send_sign(data)
    #     # cash_activity_sign_info_mew(data)
    #     # coupon_all_list_3(data)
    #     # my_asset_index(data)
    #     # regular_project_dtl(data)
    #     # project_current_dtl(data)
    #     regular_project_rlist(data)
    # @task
    # def test(self):
    #     # send_sms()
    #     trade_invest()


class WebSiteUser(HttpLocust):
    task_set = WebSiteTask
    host = "http://121.41.30.64:8888"
    # enterprise_host = "http://121.40.94.182:8000" # 企业活动域名
    # user_data_queue = Queue.Queue()
    # count = []
    # for i, data in enumerate(id_lists):
    #     user_data_queue.put_nowait(data)

    min_wait = 1000
    max_wait = 5000

# from locust import web
#
# @web.app.route("/added_page")
# def my_added_page():
#     return "Another page"
