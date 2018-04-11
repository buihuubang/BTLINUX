clear
echo "Bùi Hữu Bằng"
read -p "Nhập vào đường dẫn thư mục cần xem:" link
cd $link
ls -a
sudo ls -a >NDTM.txt

