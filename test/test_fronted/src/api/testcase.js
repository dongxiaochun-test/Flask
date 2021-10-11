//测试用例接口
import axios from "./http";

// testcase对象用来管理和测试用例相关的接口
const testcase = {
    //获取用例接口
    getTestcase(params) {
        // 传递接口信息
        return axios({
            // 请求的方法
            method: "get",
            // 请求的url，无需添加完整的url信息
            url: "/testcase",
            // 请求url的参数信息，通过前端传递
            params: params
        })
    },
    // 新增用例接口 
    addTestcase(data) {
        return axios(
            {
                method: "post",
                url: "/testcase",
                // 使用data属性传递请求体数据信息
                data: data

            }
        )
    },
    // 更新用例接口
    updateTestcase(data) {
        return axios({
            method: "put",
            url: "/testcase",
            data: data
        })
    },
    // 删除用例接口
    deleteTestcase(params) {
        return axios({
            method: "delete",
            url: "/testcase",
            params: params
        })
    }

}

export default testcase