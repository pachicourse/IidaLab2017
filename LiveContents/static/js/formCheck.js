function checkForm(){
    var flag = 0
    //formの内容をチェック
    if(document.form.password.value == ""){
        flag = 1
    }
    //検査
    if(flag){
        window.alert('必須項目に未入力がありました') // 入力漏れがあれば警告ダイアログを表示
        return false // 送信を中止
    }
    else{
        if(!window.confirm('送信してよろしいですか？')){ // 確認ダイアログを表示
            window.alert('キャンセルされました') // 警告ダイアログを表示
            return false
        }
        return true // 送信を実行
    }
}
