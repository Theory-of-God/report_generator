import json
from jinja2 import Environment, FileSystemLoader


def md_report_generator(
                        report_name,
                        json_data_path,
                        template_name,
                        template_path='templates',
                        output_path='ouput',
                        is_append=False
                        ):
    """
    函数功能：输入报告名称，模块输出的json文件路径，模板名，即可生成对应名称的md报告。若将is_append设置为True可追加报告内容，
    追加报告内容应使用不同的模板避免重复。
    :param report_name: 报告的名称
    :param json_data_path: json数据路径（含json文件名）
    :param template_name: 模板名称
    :param template_path: 模板路径（默认为当前文件夹下的templates文件夹）
    :param output_path: 输出路径（默认为当前文件夹下的output文件夹）
    :param is_append: 是否追加报告内容
    :return: 生成一个md格式报告
    """
    # 导入jinja2模板路径
    j2_template_loader = FileSystemLoader(template_path)
    # 定义环境调用模板
    env = Environment(loader=j2_template_loader)
    # 获取并载入模板
    j2_temp = env.get_template(template_name)
    # 获取json文件
    with open(json_data_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    # 传入数据，渲染模板
    md_report = j2_temp.render(data)
    # 判断是否追加报告内容
    if is_append:
        # 追加报告内容
        with open(f'{output_path}/{report_name}.md', 'a', encoding='utf-8') as output_file:
            output_file.write(md_report)
            # 刷新报告
            output_file.flush()
            print(f"{output_path}/{report_name}.md报告内容已追加。")
    else:
        # 生成报告
        with open(f'{output_path}/{report_name}.md', 'w', encoding='utf-8') as output_file:
            output_file.write(md_report)
            print(f"{output_path}/{report_name}.md报告已生成。")


if __name__ == '__main__':
    report_name = 'software_bastinfo'
    json_data_path = 'json_data/software_baseinfo.json'
    templates_name = 'software_baseinfo_template.html'
    # template_path = 'templates'
    # output_path = 'output'
    md_report_generator(report_name, json_data_path, templates_name)

