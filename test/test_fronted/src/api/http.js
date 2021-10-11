// axios 的通用配置
// 请求头
import axios from "axios";

var instance = axios.create(
    {
        // 基地址， 当碰到环境切换的时候，可以直接修改基地址
        // 无需修改 接口信息
        baseURL: 'http://127.0.0.1:5000',
        timeout: 1000,

    }
)
export default instance