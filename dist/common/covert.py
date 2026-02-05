import codecs
import re


def gbk_to_utf8(input_file, output_file):
    '''
    将ctp的头文件由GBK编码转成UTF-8编码，并且将单引号的字符串替成双引号。注意，仅可执行一次，如果已经是utf-8编码，将会报错
    :param input_file: 输入文件
    :param output_file: 输出文件
    :return:
    '''
    try:
        with codecs.open(input_file, 'r', encoding='gbk') as f:
            content = f.read()
            if input_file == 'ThostFtdcUserApiDataType.h':
                content = re.sub(r"'(\d{6})'", r'"\1"', content)
        with codecs.open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"文件 {input_file} 已成功转换并保存为 {output_file}")
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")


# 使用方法
# gbk_to_utf8('commodities.json', 'commodities.json')
# gbk_to_utf8('contracts.json', 'contracts.json')
gbk_to_utf8('stk_comms.json', 'stk_comms.json')
# gbk_to_utf8('stocks.json', 'stocks.json')
