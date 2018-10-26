$(function(){
    //表单验证
    $('#frmlogin').submit(function(){
        var user = $('[name=user]').val();
        var upwd = $('[name=pwd]').val();

        if (user.length==0 || upwd.length==0){
            return false;
        }
        return true;
    });
});