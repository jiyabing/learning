from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Asset(models.Model):
    """
    所有资产的共有数据表
    说明：
        1.sn这个数据字段是所有资产都必须有，并且唯一不可重复的！通常来自自动收集的数据中；
        2.name和sn一样，也是唯一的；
        3.asset_type_choice和asset_status分别设计为两个选择类型
        4.admin和approved_by是分别是当前资产的管理员和将该资产上线的审批员；
        5.导入Django内置的User表，作为我们CMDB项目的用户表，用于保存管理员和审判员等人员信息；
        6.asset表中的很多字段内容都无法自动获取，需要我们手动输入，比如合同、备注。
    """
    asset_type_choice = (
        ('server', '服务器'),
        ('network_device', '网络设备'),
        ('storage_device', '存储设备'),
        ('security_device', '安全设备'),
        ('software', '软件资产'),
    )

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )

    asset_type = models.CharField(choices=asset_type_choice, max_length=64,
                                  default='server', verbose_name='资产类型')
    name = models.CharField(max_length=64, unique=True, verbose_name="资产名称")  # 不可重复
    sn = models.CharField(max_length=128, unique=True, verbose_name="资产序列号")  # 不可重复
    business_unit = models.ForeignKey('BusinessUnit', null=True, blank=True,
                                      verbose_name='所属业务线', on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')

    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True,
                                     verbose_name='制造商', on_delete=models.CASCADE)
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    admin = models.ForeignKey(User, null=True, blank=True, verbose_name='资产管理员',
                              related_name='admin', on_delete=models.CASCADE)
    idc = models.ForeignKey('IDC', null=True, blank=True, verbose_name='所在机房',
                            on_delete=models.CASCADE)
    contract = models.ForeignKey('Contract', null=True, blank=True, verbose_name='合同',
                                 on_delete=models.CASCADE)

    purchase_day = models.DateField(null=True, blank=True, verbose_name="购买日期")
    expire_day = models.DateField(null=True, blank=True, verbose_name="过保日期")
    price = models.FloatField(null=True, blank=True, verbose_name="价格")

    approved_by = models.ForeignKey(User, null=True, blank=True, verbose_name='批准人',
                                    related_name='approved_by', on_delete=models.CASCADE)

    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='批准日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_asset_type_display(), self.name)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        ordering = ['-c_time']


class Server(models.Model):
    """
    服务器设备
    说明：
        1.每台服务器都唯一关联着一个资产对象，因此使用OneToOneField构建了一个一对一字段，这非常重要!
        2.服务器又可分为几种子类型，这里定义了三种；
        3.服务器添加的方式可以分为手动和自动；
        4.有些服务器是虚拟机或者docker生成的，没有物理实体，存在于宿主机中，因此需要增加一个hosted_on字段；
        5.服务器有型号信息，如果硬件信息中不包含，那么指的就是主板型号；
        6.Raid类型在采用了Raid的时候才有，否则为空
        7.操作系统相关信息包含类型、发行版本和具体版本
    """
    sub_asset_type_choice = (
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机'),
    )

    created_by_choice = (
        ('auto', '自动添加'),
        ('manual', '手工录入'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)  # 非常关键的一对一关联！
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice,
                                              default=0, verbose_name="服务器类型")
    created_by = models.CharField(choices=created_by_choice, max_length=32,
                                  default='auto', verbose_name="添加方式")
    hosted_on = models.ForeignKey('self', related_name='hosted_on_server', blank=True, null=True,
                                  verbose_name="宿主机", on_delete=models.CASCADE)  # 虚拟机专用字段
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    raid_type = models.CharField(max_length=512, blank=True, null=True, verbose_name='Raid类型')

    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField('发行版本', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.asset.name, self.get_sub_asset_type_display(),
                                       self.model, self.asset.sn)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"


# 说明：
#     1.每台安全、网络、存储设备都通过一对一的方式唯一关联这一个资产对象。
#     2.通过sub_asset_type又细分设备的子类型
#     3.对于软件，它没有物理形体，因此无须关联一个资产对象；
#     4.软件只管理那些大型的收费软件，关注点是授权数量和软件版本。对于那些开源的或者免费的软件，显然不算公司的资产。


class SecurityDevice(models.Model):
    """安全设备"""
    sub_asset_type_choice = (
        (0, '防火墙'),
        (1, '入侵检测设备'),
        (2, '互联网网关'),
        (4, '运维审计系统'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0,
                                              verbose_name="安全设备类型")

    def __str__(self):
        return self.asset.name + "--" + self.get_sub_asset_type_display() + " id:%s" % self.id

    class Meta:
        verbose_name = '安全设备'
        verbose_name_plural = "安全设备"


class StorageDevice(models.Model):
    """存储设备"""
    sub_asset_type_choice = (
        (0, '磁盘阵列'),
        (1, '网络存储器'),
        (2, '磁带库'),
        (4, '磁带机'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0,
                                              verbose_name="存储设备类型")

    def __str__(self):
        return self.asset.name + "--" + self.get_sub_asset_type_display() + " id:%s" % self.id

    class Meta:
        verbose_name = '存储设备'
        verbose_name_plural = "存储设备"


class NetworkDevice(models.Model):
    """网络设备"""
    sub_asset_type_choice = (
        (0, '路由器'),
        (1, '交换机'),
        (2, '负载均衡'),
        (4, 'VPN设备'),
    )

    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0,
                                              verbose_name="网络设备类型")

    vlan_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="VLanIP")
    intranet_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="内网IP")

    model = models.CharField(max_length=128, null=True, blank=True, verbose_name="网络设备型号")
    firmware = models.CharField(max_length=128, blank=True, null=True, verbose_name="设备固件版本")
    port_num = models.SmallIntegerField(null=True, blank=True, verbose_name="端口个数")
    device_detail = models.TextField(null=True, blank=True, verbose_name="详细配置")

    def __str__(self):
        return '%s--%s--%s <sn:%s>' % (self.asset.name, self.get_sub_asset_type_display(),
                                       self.model, self.asset.sn)

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = "网络设备"


class Software(models.Model):
    """
    只保存付费购买的软件
    """
    sub_asset_type_choice = (
        (0, '操作系统'),
        (1, '办公\开发软件'),
        (2, '业务软件'),
    )

    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0,
                                              verbose_name="软件类型")
    license_num = models.IntegerField(default=1, verbose_name="授权数量")
    version = models.CharField(max_length=64, unique=True,
                               help_text='例如: CentOS release 6.7 (Final)',
                               verbose_name='软件/系统版本')

    def __str__(self):
        return '%s--%s' % (self.get_sub_asset_type_display(), self.version)

    class Meta:
        verbose_name = '软件/系统'
        verbose_name_plural = "软件/系统"


# 说明：
#     1.机房可以有很多其它字段，比如城市、楼号、楼层和未知等等，如有需要可自行添加；
#     2.业务线可以有子业务线，因此使用一个外键关联自身模型；
#     3.合同模型主要存储财务部门关心的数据；
#     4.资产标签模型与资产是多对多的关系。


class IDC(models.Model):
    """机房"""
    name = models.CharField(max_length=64, unique=True, verbose_name="机房名称")
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = "机房"


class Manufacturer(models.Model):
    """厂商"""
    name = models.CharField('厂商名称', max_length=64, unique=True)
    telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = "厂商"


class BusinessUnit(models.Model):
    """业务线"""
    parent_unit = models.ForeignKey('self', blank=True, null=True, related_name='parent_level',
                                    on_delete=models.CASCADE)
    name = models.CharField('业务线', max_length=64, unique=True)
    memo = models.CharField('备注', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"


class Contract(models.Model):
    """合同"""
    sn = models.CharField('合同号', max_length=128, unique=True)
    name = models.CharField('合同名称', max_length=64)
    memo = models.TextField('备注', blank=True, null=True)
    price = models.IntegerField('合同金额')
    detail = models.TextField('合同详细', blank=True, null=True)
    start_day = models.DateField('开始日期', blank=True, null=True)
    end_day = models.DateField('失效日期', blank=True, null=True)
    license_num = models.IntegerField('license数量', blank=True, null=True)
    c_day = models.DateField('创建日期', auto_now_add=True)
    m_day = models.DateField('修改日期', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"


class Tag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=32, unique=True)
    c_day = models.DateField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"


class CPU(models.Model):
    """
    CPU组件

    通常一台服务器中只能有一种CPU型号，所以这里使用OneToOneField唯一关联一个资产对象，而不是外键关系。
    服务器上可以有多个物理CPU，它们的型号都是一样的。每个物理CPU又可能包含多核。
    """
    # 设备上的cpu肯定都是一样的，所以不需要建立多个cpu数据，一条就可以，因此使用一对一。
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)

    cpu_model = models.CharField('CPU型号', max_length=128, blank=True, null=True)
    cpu_count = models.PositiveSmallIntegerField('物理CPU个数', default=1)
    cpu_core_count = models.PositiveSmallIntegerField('CPU核数', default=1)

    def __str__(self):
        return self.asset.name + ":   " + self.cpu_model

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = "CPU"


class RAM(models.Model):
    """
    内存组件

    某个资产中可能有多条内存，所以这里必须是外键关系。
    其次，内存的sn号可能无法获得，就必须通过内存所在的插槽未知来唯一确定每条内存。
    因此，unique_together = ('asset', 'slot')这条设置非常关键，相当于内存的主键了，
    每条内存数据必须包含slot字段，否则就不合法。
    """
    # 只能通过外键关联Asset。否则不能同时关联服务器、网络设备等等。
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)

    sn = models.CharField('SN号', max_length=128, blank=True, null=True)
    model = models.CharField('内存型号', max_length=128, blank=True, null=True)
    manufacturer = models.CharField('内存制造商', max_length=128, blank=True, null=True)
    slot = models.CharField('插槽', max_length=64)
    capacity = models.IntegerField('内存大小(GB)', blank=True, null=True)

    def __str__(self):
        return '%s: %s: %s: %s' % (self.asset.name, self.model, self.slot, self.capacity)

    class Meta:
        verbose_name = '内存'
        verbose_name_plural = "内存"
        unique_together = ('asset', 'slot')  # 同一资产下的内存，根据插槽的不同，必须唯一


class Disk(models.Model):
    """
    存储设备

    与内存相同的是，硬盘也可能有很多块，所以也是外键关系。
    不同的是，硬盘通常都能获取到sn号，使用sn作为唯一值比较合适，也就是unique_together = ('asset', 'sn')。
    硬盘有不同的接口，这里设置了4种以及unknown，可自行添加其它类别。
    """
    disk_interface_type_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
        ('unknown', 'unknown'),
    )

    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    sn = models.CharField('硬盘SN号', max_length=128)
    slot = models.CharField('所在插槽位', max_length=64, blank=True, null=True)
    model = models.CharField('磁盘型号', max_length=128, blank=True, null=True)
    manufacturer = models.CharField('磁盘制造商', max_length=128, blank=True, null=True)
    capacity = models.FloatField('磁盘容量(GB)', blank=True, null=True)
    interface_type = models.CharField('接口类型', max_length=16, choices=disk_interface_type_choice,
                                      default='unknown')

    def __str__(self):
        return '%s:  %s:  %s:  %sGB' % (self.asset.name, self.model, self.slot, self.capacity)

    class Meta:
        verbose_name = '硬盘'
        verbose_name_plural = "硬盘"
        unique_together = ('asset', 'sn')


class NIC(models.Model):
    """
    网卡组件

    一台设备中可能有很多块网卡，所以网卡与资产也是外键的关系。
    另外，由于虚拟机的存在，网卡的mac地址可能会发生重复，无法唯一确定某块网卡，
    因此通过网卡型号加mac地址的方式来唯一确定网卡。
    """
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    name = models.CharField('网卡名称', max_length=64, blank=True, null=True)
    model = models.CharField('网卡型号', max_length=128)
    mac = models.CharField('MAC地址', max_length=64)  # 虚拟机有可能会出现同样的mac地址
    ip_address = models.GenericIPAddressField('IP地址', blank=True, null=True)
    net_mask = models.CharField('掩码', max_length=64, blank=True, null=True)
    bonding = models.CharField('绑定地址', max_length=64, blank=True, null=True)

    def __str__(self):
        return '%s:  %s:  %s' % (self.asset.name, self.model, self.mac)

    class Meta:
        verbose_name = '网卡'
        verbose_name_plural = "网卡"
        # 资产、型号和mac必须联合唯一。防止虚拟机中的特殊情况发生错误。
        unique_together = ('asset', 'model', 'mac')


class EventLog(models.Model):
    """
    日志.
    在关联对象被删除的时候，不能一并删除，需保留日志。
    因此，on_delete=models.SET_NULL

    CMDB必须记录各种日志，这是毫无疑问的！
    我们通常要记录事件名称、类型、关联的资产、子事件、事件详情、谁导致的、发生时间。这些都很重要！
    尤其要注意的是，事件日志不能随着关联资产的删除被一并删除，也就是我们设置on_delete=models.SET_NULL的意义！
    """
    event_type_choice = (
        (0, '其它'),
        (1, '硬件变更'),
        (2, '新增配件'),
        (3, '设备下线'),
        (4, '设备上线'),
        (5, '定期维护'),
        (6, '业务上线\更新\变更'),
    )

    name = models.CharField('事件名称', max_length=128)

    # 当资产审批成功时有这项数据
    asset = models.ForeignKey('Asset', blank=True, null=True, on_delete=models.SET_NULL)

    # 当资产审批失败时有这项数据
    new_asset = models.ForeignKey('NewAssetApprovalZone', blank=True, null=True, on_delete=models.SET_NULL)

    event_type = models.SmallIntegerField('事件类型', choices=event_type_choice, default=4)
    component = models.CharField('事件子项', max_length=256, blank=True, null=True)
    detail = models.TextField('事件详情')
    date = models.DateTimeField('事件时间', auto_now_add=True)

    # 自动更新资产数据时没有执行人
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='事件执行人', on_delete=models.SET_NULL)

    memo = models.TextField('备注', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '事件纪录'
        verbose_name_plural = "事件纪录"


class NewAssetApprovalZone(models.Model):
    """
    新资产待审批区

    新资产的到来，并不能直接加入CMDB数据库中，而是要通过管理员审批后，才可以上线的。
    这就需要一个新资产的待审批区。在该区中，以资产的sn号作为唯一值，确定不同的资产。
    除了关键的包含资产所有信息的data字段，为了方便审批员查看信息，
    我们还设计了一些厂商、型号、内存大小、CPU类型等字段。
    同时，有可能出现资产还未审批，更新数据就已经发过来的情况，所以需要一个数据更新日期字段。
    """
    sn = models.CharField('资产SN号', max_length=128, unique=True)  # 此字段必填
    asset_type_choice = (
        ('server', '服务器'),
        ('network_device', '网络设备'),
        ('storage_device', '存储设备'),
        ('security_device', '安全设备'),
        ('IDC', '机房'),
        ('software', '软件资产'),
    )
    asset_type = models.CharField(choices=asset_type_choice, default='server', max_length=64,
                                  blank=True, null=True, verbose_name='资产类型')

    manufacturer = models.CharField(max_length=64, blank=True, null=True, verbose_name='生产厂商')
    model = models.CharField(max_length=128, blank=True, null=True, verbose_name='型号')
    ram_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='内存大小')
    cpu_model = models.CharField(max_length=128, blank=True, null=True, verbose_name='CPU型号')
    cpu_count = models.PositiveSmallIntegerField(blank=True, null=True)
    cpu_core_count = models.PositiveSmallIntegerField(blank=True, null=True)
    os_distribution = models.CharField(max_length=64, blank=True, null=True)
    os_type = models.CharField(max_length=64, blank=True, null=True)
    os_release = models.CharField(max_length=64, blank=True, null=True)

    data = models.TextField('资产数据')  # 此字段必填

    c_time = models.DateTimeField('汇报日期', auto_now_add=True)
    m_time = models.DateTimeField('数据更新日期', auto_now=True)
    approved = models.BooleanField('是否批准', default=False)

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = "新上线待批准资产"
        ordering = ['-c_time']
