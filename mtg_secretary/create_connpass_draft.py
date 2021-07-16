import os

from helium import (
    Alert,
    S,
    Text,
    click,
    find_all,
    go_to,
    kill_browser,
    start_firefox,
    wait_until,
    write,
)

start_firefox("connpass.com/login")
write(os.getenv("CONNPASS_USERNAME"), into="ユーザー名")
write(os.getenv("CONNPASS_PASSWORD"), into="パスワード")
click("ログインする")
wait_until(Text("イベント管理").exists)

# テンプレートのコピーを作成
go_to("connpass.com/editmanage")
copy_events = find_all(S(".copyEvent"))
first_copy_event = copy_events[0]  # テンプレートは未来の日付のため一番上
click(first_copy_event)
Alert().accept()

wait_until(Text("下書き中").exists)
kill_browser()
