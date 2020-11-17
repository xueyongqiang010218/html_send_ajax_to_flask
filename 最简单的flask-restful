from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# 1. 创建API对象  用于管理类视图(资源)
api = Api(app)


# 2.定义类视图  继承Resource
class DemoResource(Resource):
    def get(self):
        # 类视图响应的content-type默认变为json形式
        # 类视图的返回值可以是字典, 会被自动转为json字符串
        return {'foo': 'get'}

    def post(self):
        return {'foo': 'post'}


# 3.添加类视图  函数标记默认为类名小写
api.add_resource(DemoResource, '/', endpoint='demo')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
