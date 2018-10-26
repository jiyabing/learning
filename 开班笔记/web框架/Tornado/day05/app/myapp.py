from tornado.web import Application

from Tornado.day05.util.dbutil import DBUtil


class MyApplication(Application):
    def __init__(self,hs, tp, sp, um):
        super().__init__(handlers=hs,
                         template_path=tp,
                         static_path=sp,
                         ui_modules=um)
        self.dbutil = DBUtil()