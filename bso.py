"""
Yiğit Çıtak tarafından yazılmıştır.

Modern pencere kütüphanesi olan Customtkinter ile yazılış bir otomasyon programıdır
sadece iki tane kütüphane kullanılmıştır ve optimizeli şekilde yazmaya özen gösterilmiştir.

GPL lisansı ile bu programı kişiselleştirmek veya dağıtmak yasaldır.
Ama bu programdan alıntı olduğunu inkar etmediği sürece.
"""

version = 1.0

import customtkinter as ctk
from os import system

def main():
	win_root = ctk.CTk()
	win_root.title("bso")
	win_root.geometry("1200x700")
	win_root.minsize(1200,700)


	win_title = ctk.CTkLabel(win_root,
		text="Bash shell oto\n",
		font=("italic",45),
		text_color="blue",).pack(pady=20)


	def wine_menu_Button_fon():
		def geri():
			win_menu_sayfa.place(x=-1000,y=-1000)
			win_menu_Button.configure(command=wine_menu_Button_fon,fg_color="blue")

		win_menu_Button.configure(command=geri,fg_color="purple")

		win_menu_sayfa = ctk.CTkFrame(master=win_root,
			height=600,
			width=300,
			fg_color="blue")
		win_menu_sayfa.place(x=1,y=50)

		mesaj = ctk.CTkLabel(win_menu_sayfa,
		text=f"Yapımcı: Yiğit Çıtak\nsürüm:{version}",
		font=("italic",20),
		text_color="white")
		mesaj.pack(pady=10)

	win_menu_Button = ctk.CTkButton(win_root,
		text="Hakkında",
		font=("italic",20),
		width=5,
		height=10,
		command=wine_menu_Button_fon,
		fg_color="blue")
	win_menu_Button.place(x=1,y=1)


	def tema_degistir():
		if tema_ayarla_var.get() == 0:
			ctk.set_appearance_mode("light")
		elif tema_ayarla_var.get() == 1:
			ctk.set_appearance_mode("dark")

	tema_ayarla_var = ctk.IntVar(value=0)
	tema_ayarla = ctk.CTkSwitch(
		win_root,
		text="Koyu Tema",
		onvalue=1,
		offvalue=0,
		variable=tema_ayarla_var,
		command=tema_degistir)
	tema_ayarla.place(x=1,y=50)


	#İçerik boyut ayarları
	win_icerik_sayfa_genislik_width = 400
	win_icerik_sayfa_genislik_height = 70


	win_icerik_sayfa = ctk.CTkScrollableFrame(master=win_root,
		width=1000,
		height=1000)
	win_icerik_sayfa.pack()

	def paket_yonetici_fonk(choice):
		global paket_yoneticisi
		if choice == "apt":
			paket_yoneticisi = 1
		elif choice == "dnf":
			paket_yoneticisi = 2

	paket_yonetici = ctk.CTkComboBox(win_icerik_sayfa,
		values=["apt","dnf"],
		command=paket_yonetici_fonk,
		width=win_icerik_sayfa_genislik_width,
		height=win_icerik_sayfa_genislik_height)
	paket_yonetici.set("Paket yöneticisi seçin")
	paket_yonetici.pack()


		
	paketler = ctk.CTkEntry(win_icerik_sayfa,
		placeholder_text="Paket adı girin",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width)
	paketler.pack(pady=20)


	def paket_guncelle_fonk():
		son_mesaj = "işlem tamamlandı"
		try:
			if paket_yoneticisi == 1:
				system("sudo apt update && sudo apt upgrade")
			elif paket_yoneticisi == 2:
				system("sudo dnf update && sudo dnf upgrade")

			print(son_mesaj)

		except:
			print(f"Paket yöneticisi bulunamadı")

	paket_guncelle_button = ctk.CTkButton(win_icerik_sayfa,
		text="Paketleri güncelle",
		command=paket_guncelle_fonk,
		width=win_icerik_sayfa_genislik_width,
		height=win_icerik_sayfa_genislik_height)
	paket_guncelle_button.pack(pady=10)

	def paket_kur_fonk():
		son_mesaj = "işlem tamamlandı"
		try:
			if paket_yoneticisi == 1:
				system(f"sudo apt install {paketler.get()}")
			elif paket_yoneticisi == 2:
				system(f"sudo dnf install {paketler.get()}")

			print(son_mesaj)

		except:
			print(f"Paket yöneticisi bulunamadı")

	paket_kur = ctk.CTkButton(win_icerik_sayfa,
		text="Paketleri Kur",
		command=paket_kur_fonk,
		width=win_icerik_sayfa_genislik_width,
		height=win_icerik_sayfa_genislik_height)
	paket_kur.pack(pady=10)	

	button_mesafe = 15

	def command1_fonk():
		system("ip addr")
	command1 = ctk.CTkButton(win_icerik_sayfa,
		text="ip addr (ip adresi öğrenme)",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command1_fonk)
	command1.pack(pady=button_mesafe)

	def command2_fonk():
		system("neofetch")
	command2 = ctk.CTkButton(win_icerik_sayfa,
		text="neofetch",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command2_fonk)
	command2.pack(pady=button_mesafe)

	def command3_fonk():
		system("systemctl start ssh")
	command3 = ctk.CTkButton(win_icerik_sayfa,
		text="systemctl start ssh (ssh başlat)",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command3_fonk)
	command3.pack(pady=button_mesafe)

	def command4_fonk():
		system("systemctl stop ssh")
	command4 = ctk.CTkButton(win_icerik_sayfa,
		text="systemctl stop ssh (ssh kapat)",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command4_fonk)
	command4.pack(pady=button_mesafe)

	def command5_fonk():
		system("systemctl status ssh")
	command5 = ctk.CTkButton(win_icerik_sayfa,
		text="systemctl status ssh (ssh kontrol et)",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command5_fonk)
	command5.pack(pady=button_mesafe)

	def command6_fonk():
		system("clear")
	command6 = ctk.CTkButton(win_icerik_sayfa,
		text="clear (temizle)",
		height=win_icerik_sayfa_genislik_height,
		width=win_icerik_sayfa_genislik_width,
		command=command6_fonk)
	command6.pack(pady=button_mesafe)


	win_root.mainloop()



if __name__ == "__main__":
	main()