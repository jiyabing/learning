#instance_methon.py


#此示例示意实例方法的定义方式和调用方法
class Dog:
    '''这是一个类，用于描述一个小动物的行为'''
    def eat(self,food):
        '''小狗能够有吃东西的行为'''
        print('小狗吃了',food)
        self.food = food #为self绑定的对象添加food属性

    def food_info(self):
        '''能否在此方法内得到小狗上次吃的食物是什么'''
        print('上次吃的是：',self.food)
        


dog1 = Dog()
dog1.eat('骨头')
dog1.food_info()


dog2 = Dog()
dog2.eat('包子')
dog2.food_info()


dog3 = Dog()
Dog.eat(dog3,'狗粮')
Dog.food_info(dog3)
