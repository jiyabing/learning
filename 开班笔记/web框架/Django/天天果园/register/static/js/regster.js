$(function(){
    //表单验证
    $('#frmlogin').submit(function(){
        var user = $('[name=user]').val();
        var upwd = $('[name=pwd]').val();
        var uname = $('[name=uname]').var();
        var uemail = $('[name=uemail]').var();

        if (user.length==0 || upwd.length==0 || uname.length==0 || uemail.length==0){
            return false;
        }
        return true;
    });
});