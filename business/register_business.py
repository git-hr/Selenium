from handle.register_handle import RegisterHandle
class RegisterBusiness():
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    # 执行注册操作
    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
    # 注册成功
    def register_success(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False
    # 邮箱错误
    def register_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)   
        if self.register_h.get_user_text('email_error') == None:
            return True
        else:
            return False
        
    # def register_function(self,email,username,password,file_name,assertCode,assertText):
    #     self.user_base(email,username,password,file_name)
    #     if self.register_h.get_user_text(assertCode,assertText) == None:
    #         return True
    #     else:
    #         return False
    # 用户名错误
    def register_name_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_name_error') == None:
            return True
        else:
            return False
    
    #密码错误
    def register_password_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('password_error') == None:
            return True
        else:
            return False

    # 验证码错误
    def register_code_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('code_text_error') == None:
            return True
        else:
            return False

    # ddt注册方法
    def register_function(self,email,name,password,code,assertCode):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text(assertCode) == None:
            return True
        else:
            return False