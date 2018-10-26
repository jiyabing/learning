$(function(){
    //表单验证
    $('#frmlogin').submit(function(){
        var uname = $('[name=uname]').val();
        var upwd = $('[name=upwd]').val();
        if (unam.length==0 || upwd.length==0){
            return false;
        }
        return true;
    });
});