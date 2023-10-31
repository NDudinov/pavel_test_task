import allure

import steps as api_steps
from utils import api_const, http_methods, user_creator
from utils.user_creator import UserCreator


class TestApiRegressCrud:
    def test_api_crud_regres_in(self) -> None:
        new_user = user_creator.create_user_json()
        with allure.step("1. Create a User"):
            create = api_steps.reqress_crud.create_user(new_user_data=new_user)
            api_steps.reqress_crud.check_response_status_code(create, 201)
            api_steps.reqress_crud.check_response_body(
                http_methods.POST, create, new_user
            )
        with allure.step("2. Get Single User by ID (already existing #12)"):
            get = api_steps.reqress_crud.get_single_user()
            api_steps.reqress_crud.check_response_status_code(get, 200)
            api_steps.reqress_crud.check_response_body(
                http_methods.GET, get, api_const.USER
            )
        with allure.step("3. Update user by PATCH method"):
            patch = api_steps.reqress_crud.update_user_via_patch(new_data=new_user)
            api_steps.reqress_crud.check_response_status_code(patch, 200)
            api_steps.reqress_crud.check_response_body(
                http_methods.PATCH, patch, new_user
            )
        with allure.step("4. Update user by PUT method"):
            put = api_steps.reqress_crud.update_user_via_patch(
                new_data=new_user, user_id=3
            )
            api_steps.reqress_crud.check_response_status_code(put, 200)
            api_steps.reqress_crud.check_response_body(http_methods.PUT, put, new_user)
        with allure.step("5.  DELETE User by ID (already existing #12)"):
            delete = api_steps.reqress_crud.delete_user(user_id=3)
            api_steps.reqress_crud.check_response_status_code(delete, 204)
            api_steps.reqress_crud.check_response_body(
                http_methods.DELETE, delete, None
            )
