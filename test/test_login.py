import allure


class Testlogin:

    def test_a(self):
        print("\n1111")
        assert 1

    @allure.step("测试步骤001")
    def test_b(self):
        print("\n222")
        allure.attach("描述1","请输入用户名")
        print("\n33")
        allure.attach("描述2", "请输入用户密码")
        assert 0