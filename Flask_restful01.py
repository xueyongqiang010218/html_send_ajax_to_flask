from flask import Flask, url_for, render_template
from flask_restful import Api, Resource, reqparse, inputs

'''
（输入） Flask_restful01 有一个验证、类似于wtf的验证   （输入验证）
 通过 postman 进行输入
'''
app = Flask(__name__)
api = Api(app)


#这是一个接受ajax数据的api
class LoginView(Resource):
    '''
    只定义一个post请求
    '''

    def post(self):
        # 获取解析对象
        parser = reqparse.RequestParser()
        # 获取username  是否是str类型  ，提示用户名验证错误！
        parser.add_argument("username", type=str, help="用户名验证错误！", required=True)
        # parser.add_argument("password", type=str, help="密码验证错误！")
        # parser.add_argument("home_page", type=inputs.url, help="个人链接验证错误")

        '''
        default = "鼎鼎"   默认是鼎鼎
        required = True   必须要传递的参数， 如果不传递，输出 用户名验证错误！

        1. default：默认值，如果这个参数没有值，那么将使用这个参数指定的值。 
        2. required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。 
        3. type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。 
        4. choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。 
        5. help：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。 
        6. trim：是否要去掉前后的空格。


        其中的type，可以使用python自带的一些数据类型，也可以使用flask_restful.inputs下的一些特定的数据类型来强制转换。比如一些常用的： 
        1. url：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。 
        2. regex：正则表达式。 
        3. date：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。
        '''

        # 拿到这个传来的参数
        args = parser.parse_args()

        # 打印ajax传递来的参数
        print("获取全部传来的值:",args)

        # 获取username的字段
        # print("打印前端传来的值：",args.get("username"))
        return {"username": args.get("username")}


# 方式一、在Postman里面输入：http://127.0.0.1:8888/login/?username=哇咔咔 会传递信息 哇咔咔 给username
# 方式二、通过jquery的方式、给后端进行传参、
api.add_resource(LoginView, "/login/")




#这是一个接受ajax数据的api
class Send_ajax(Resource):
    '''
    只定义一个post请求
    '''

    def post(self):
        # 获取解析对象
        parser = reqparse.RequestParser()
        # 获取username  是否是str类型  ，提示用户名验证错误！
        parser.add_argument("password", type=str, help="用户名验证错误！", required=True)
        # parser.add_argument("password", type=str, help="密码验证错误！")
        # parser.add_argument("home_page", type=inputs.url, help="个人链接验证错误")

        '''
        default = "鼎鼎"   默认是鼎鼎
        required = True   必须要传递的参数， 如果不传递，输出 用户名验证错误！

        1. default：默认值，如果这个参数没有值，那么将使用这个参数指定的值。 
        2. required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。 
        3. type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。 
        4. choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。 
        5. help：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。 
        6. trim：是否要去掉前后的空格。


        其中的type，可以使用python自带的一些数据类型，也可以使用flask_restful.inputs下的一些特定的数据类型来强制转换。比如一些常用的： 
        1. url：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。 
        2. regex：正则表达式。 
        3. date：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。
        '''

        # 拿到这个传来的参数
        args = parser.parse_args()

        # 打印ajax传递来的参数
        print("获取全部传来的值:",args)

        # 获取username的字段
        # print("打印前端传来的值：",args.get("username"))
        return {"password": args.get("password")}


# 方式一、在Postman里面输入：http://127.0.0.1:8888/login/?username=哇咔咔 会传递信息 哇咔咔 给username
# 方式二、通过jquery的方式、给后端进行传参、
api.add_resource(Send_ajax, "/yyy/")




@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8887)