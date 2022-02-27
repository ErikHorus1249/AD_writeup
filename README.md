# I. Cài đặt software sử dụng GPO
### 1 . Cài đặt Active directory  
**Bước 1** - Vào “Server Manager” → Manage → Add Roles and Feature.

![](https://i.imgur.com/WnjQM1S.png)
**Bước 2** - Vì trong ví dụ này hiện đang cài đặt AAD nên bạn sẽ chọn “Role-based or feature based Installation” → Next.

![](https://i.imgur.com/pTj9ZNT.png)

**Bước 3** - Bấm vào "Select a server from the server pool", trong trường hợp nó được cài đặt cục bộ.
![](https://i.imgur.com/E07d2ar.png)

**Bước 4** - Đánh dấu vào ô bên cạnh Active Directory Domain Services. Một hộp thoại sẽ xuất hiện giải thích các dịch vụ hoặc tính năng bổ sung được yêu cầu để cài đặt các miền.
![](https://i.imgur.com/1yocARz.png)

**Bước 5** - Nhấp vào “Install”.

![](https://i.imgur.com/PSSs11G.png)

Hoàn tất cài đặt AD DC.
Tiếp theo là cấu hình tên miền (Domain) tại **Promote this server to a domain controller**.
Domain: EXAMPLE.com

### 2 . Thiết lập cài đặt phần mềm thông qua GPO

#### 2.1. Tạo điểm phân phối gói cài đặt(Create a distribution point) 
**Bước 1**: Đăng nhập vào máy chủ với tư cách quản trị viên.

![](https://i.imgur.com/7EnSgQr.png)

**Bước 2**: Tạo một thư mục mạng chia sẻ sẽ đặt gói Windows Installer (tệp .msi).
![](https://i.imgur.com/69okJsQ.png)

**Bước 3**: Đặt quyền trên chia sẻ để cho phép truy cập vào gói phân phối.
![](https://i.imgur.com/QIouchF.png)

**Bước 4**: Sao chép hoặc cài đặt gói vào điểm phân phối. 

#### 2.2. Cấu hình AC
**Bước 1**: Tại **Group Policy Managerment** right click vào Domain chọn **Create a GPO in this Domain...** để tạo mới GPO.
![](https://i.imgur.com/yaZ8t3a.png)

**Bước 2**: Thêm tên cho **GPO** chọn OK.

![](https://i.imgur.com/OCfHtQH.png)

**Bước 3**: Edit GPO mới tạo chọn **Edit**.

![](https://i.imgur.com/Wm59lOC.png)

**Bước 4**: Lựa chọn thêm package cho user hoặc cho computer và lưa chọn chế độ share **public** hoặc **assign**.

![](https://i.imgur.com/1djAAxJ.png)

Chọn gói cài đặt tại **distribution point**.

![](https://i.imgur.com/TTCZceB.png)

![](https://i.imgur.com/UpVpibq.png)

Hoàn tất quá trình thêm gói cài đặt.

#### 2.3. Chạy gói cài đặt trên máy client.
Update policy.

![](https://i.imgur.com/coOplEj.png)

Cài đặt từ máy client.

![](https://i.imgur.com/LbFGNr4.png)

### references
[Microsoft Doc](https://docs.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)
[thuvienhay.com](https://thuvienhay.com/group-policy-object-gpo-la-gi.html)
[quantrimang.com](https://quantrimang.com/cach-cai-dat-active-directory-trong-windows-server-2012-154180)