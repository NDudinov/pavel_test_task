from typing import Optional

import allure
import requests
from hamcrest import equal_to, assert_that, greater_than_or_equal_to, not_none
from requests import Response

from utils.api_const import ApiConst
from utils.http_methods import HTTPMethods


class RegressCrud:
    _users_endpoint = ApiConst.API_URL + ApiConst.USERS_ENDPOINT
    _register_endpoint = ApiConst.API_URL + ApiConst.REGISTER_USER_ENDPOINT
    headers = {
        # "accept": "application/json",
        # "sec-ch-ua": '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": '"Windows"'
        "User-Agent": "Chrome/118.0.0.0"
    }

    @classmethod
    @allure.step(f"Send POST request to {_users_endpoint} to create new user")
    def create_user(cls, new_user_data: dict[str, str]) -> Response:
        return requests.post(cls._register_endpoint, headers=cls.headers, json=new_user_data)

    @classmethod
    @allure.step(f"Send GET request to {_users_endpoint} to receive user")
    def get_single_user(cls, user_id: int = 2) -> Response:
        with allure.step(f"User ID to get: {user_id}"):
            return requests.get(cls._users_endpoint + f"/{user_id}")

    @classmethod
    @allure.step(f"Send PUT request to {_users_endpoint} to update user")
    def update_user_via_put(
            cls, new_data: dict[str, str], user_id: int = 2
    ) -> Response:
        with allure.step(f"User ID to update: {user_id}"):
            return requests.put(cls._users_endpoint + f"/{user_id}", json=new_data)

    @classmethod
    @allure.step(f"Send PATCH request to {_users_endpoint} to update user")
    def update_user_via_patch(
            cls, new_data: dict[str, str], user_id: int = 2
    ) -> Response:
        with allure.step(f"User ID to update: {user_id}"):
            return requests.patch(cls._users_endpoint + f"/{user_id}", json=new_data)

    @classmethod
    @allure.step(f"Send DELETE request to {_users_endpoint} to delete user")
    def delete_user(cls, user_id: int = 2) -> Response:
        with allure.step(f"User ID to delete: {user_id}"):
            return requests.delete(cls._users_endpoint + f"/{user_id}")

    @staticmethod
    def check_response_status_code(response: Response, expected_status: int) -> None:
        with allure.step(f"Check response status code equals to {expected_status}"):
            assert_that(
                response.status_code,
                equal_to(expected_status),
                f"Status code doesn't equal {expected_status}",
            )

    @staticmethod
    @allure.step("Check expected is part of actual response body")
    def check_response_body(
            method: HTTPMethods,
            response: Response,
            expected_body: Optional[dict[str, str | int]],
    ) -> None:
        actual_body = response.json()
        match method:
            case HTTPMethods.GET:
                assert_that(
                    actual_body,
                    equal_to(expected_body),
                    "Response body is incorrect",
                )
            case HTTPMethods.POST:
                assert_that(
                    actual_body,
                    greater_than_or_equal_to(expected_body),
                    "Response body is incorrect",
                )
                assert_that(
                    actual_body["id"],
                    not_none(),
                    "id field is missing from response body",
                )
                assert_that(
                    actual_body["createdAt"],
                    not_none(),
                    "createdAt field is missing from response body",
                )
            case HTTPMethods.PUT:
                assert_that(
                    actual_body,
                    greater_than_or_equal_to(expected_body),
                    "Response body is incorrect",
                )
                assert_that(
                    actual_body["createdAt"],
                    not_none(),
                    "createdAt field is missing from response body",
                )
            case HTTPMethods.PATCH:
                assert_that(
                    actual_body,
                    greater_than_or_equal_to(expected_body),
                    "Response body is incorrect",
                )
                assert_that(
                    actual_body["createdAt"],
                    not_none(),
                    "createdAt field is missing from response body",
                )
            case HTTPMethods.DELETE:
                assert_that(
                    actual_body, equal_to(None), "Response body for DELETE is present"
                )
            case _:
                raise NotImplementedError
