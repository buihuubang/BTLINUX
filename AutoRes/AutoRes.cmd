clear
echo "Hãy chắc chắn bạn đã tạo kho trên github.com"
echo "Xin hãy chọn chức năng:"
echo "- Nhập vào 1 để tạo kho mới tại thư mục hiện hành"
echo "- Nhập vào 2 để tự động push lên github"
read -p "Nhập vào chức năng:" chucnang
case $chucnang in 
1)
	echo "#MY PROJECT" > README.md
	git init
	git add README.md
	read -p "Nhập vào tin nhắn của bạn để push lên github:" tinnhan
	git commit -m "$tinnhan"
	read -p "NHập vào đường dẫn kho github bạn đã tạo (copy ở clone or download):" duongdan
	git remote add origin $duongdan
	git push -u origin master
	echo "Bạn đã tạo kho thành công!";;
2)
	git add .
	read -p "Nhập vào tin nhắn của bạn để push lên github:" message
	git commit -m "$message"
	git push -f origin master
	echo "Đẩy file lên thành công";;
*)
	echo "Nhập sai chức năng!"
esac 

