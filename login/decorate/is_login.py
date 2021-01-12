def is_login(func):
    def myfunction(request,*args,**kwargs):
        if request.session.get("test"):
            return func(request,*args,**kwargs)
        else:
            print("没有值嗷")
    return  myfunction