from testcase.basecase import BaseCase
from testcase.mall_member.member_controller import AuthCodeCaseData

import pytest
class TestAuthCode(BaseCase):

    # 参数化驱动
    @pytest.mark.authcode
    @pytest.mark.parametrize("data", AuthCodeCaseData.success_case(1))
    def test_authcode_success(self, client, data):
        self.execute(client, data)


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m','authcode'])