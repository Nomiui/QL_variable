import re
import time

from com.gheaders.conn import read_yaml
from com.gheaders import logger
from com.ql import ql
from com.ql.ql_token import ql_compared, ql_write, contrast


def main_core(data: list):
    """
    主要功能运行
    :param data: [脚本名称,活动参数]
    :return:
    """
    print('-------主要执行功能-------------------')
    jst = read_yaml()
    # 判断运行必备参数是否发送了异常
    if jst['judge'] == 0:
        # 检测是否被执行过
        ctr = contrast(data[1])
        if ctr == 0:
            # 传入脚本名称返回任务ID
            ids = ql_compared(data[0], ql.Version)
            # 判断是否有脚本
            if ids[0] != -1:
                # 处理数据和去判断是否去重复,返回处理过的参数
                judge = ql_write(data[1], jst)
                # 返回-1表示有异常
                if judge != -1:
                    # 获取配置文件的内容
                    content = ql.configs_check('config.sh')
                    # 如果青龙返回200执行
                    if content["code"] == 200:
                        # 获取配置文件内容
                        bytex = content['data']
                        # 向青龙配置文件添加活动
                        print(judge)
                        revise = ql.configs_revise('config.sh', str(bytex) + '\n' + judge)
                        print(revise)
                        # 表示添加活动成功
                        # if revise["code"] == 200:
                        #     # 根据脚本id，执行脚本
                        #     qid = ql.ql_run(ids)
                        #     if qid == 0:
                        #         logger.write_log(f"执行 {data[0]} 脚本成功 ID {ids[0]}")
                        # 把原来内容添加回去
                        ql.configs_revise('config.sh', bytex)
            else:
                logger.write_log(f"{data[0]} 脚本没有找到")
        return 0
    else:
        logger.write_log("异常问题,检测到程序非正常状态,不再执行")
        return -1


def adaptation():
    """
    根据版本不同而做不同适配,死循环除非获取到版本号
    :return:
    """
    while True:
        qlv = ql.system_version()
        if qlv != -1:
            qlv = re.findall('\d+\.(\d+)\.\d+', qlv)
            return qlv[0]
        logger.write_log("无法获取版本号,程序无法自动适配,请手动去浏览器查看 青龙IP:端口/api/system 如果返回你青龙版本号请联系开发者修改")
        # n秒检测一次
        time.sleep(20)