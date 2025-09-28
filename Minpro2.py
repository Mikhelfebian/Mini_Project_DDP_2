from stdiomask import getpass

data_login = {
  "users_pengurus" : {"admin", "admin123", "123admin", "staff", "staff123", "123staff",},
  "pass_pengurus" : {"adminakademik", "staff234", "staffro", "cosmos10", "1234"},
  
  "users_pengguna" : {"mahasiswa", "dosen",},
  "pass_pengguna" : {"mahasiswa25", "mahas25", "akademikSI", "praktisi25"}
}

daftar_mahasiswa_si = []
mata_kuliah_SI = []

def login():
    print("="*70)
    print("|     Aplikasi Pengumpulan Nilai Mata Kuliah Sistem Informasi        |")
    print("="*70)
    print("="*70)
    print("|                        Login Sebagai                               |")
    print("="*70)
    try:
      kesempatan = 3
      while kesempatan > 0:
          username = str(input("Masukkan Username : "))
          password = getpass(prompt="Masukkan Password: ", mask="*")

          if username in data_login["users_pengurus"] and password in data_login["pass_pengurus"]:
              print(f"Login Berhasil! Selamat Datang {username}")
              menu_pengurus()
              return True

          elif username in data_login["users_pengguna"] and password in data_login["pass_pengguna"]:
            print(f"Login Berhasil! Selamat datang {username}")
            menu_pengguna()
            return True

          else:
              kesempatan -= 1
              print("Login gagal! Username atau password salah.")
              if kesempatan == 0:
                  print("Kesempatan Habis.")
                  return False
                
    except ValueError:
      print("Input Harus Berupa Angka")
    except KeyboardInterrupt:
      print("Jangan Klik CTRL + c")
    except EOFError:
      print("Jangan Klik CTRL + Z")
        
  
def menu_pengurus():
  while True :
    try:
      print("\n")
      print("="*70)
      print("|                      Menu Pengurus                                 |")
      print("="*70)
      print("1. Tambah Data Mahasiswa.")
      print("2. Tambah Mata Kuliah dan Nilai Mahasiswa.")
      print("3. Tampilkan Data Mahasiswa dan Mata Kuliah.")
      print("4. Hapus Data Mahasiswa.")
      print("5. Update Data Mahasiswa / Nilai.")
      print("6. Kembali Ke Menu Login.")
      
      menu_pengurus = input("Masukkan Pilihan Menu : ")
      if menu_pengurus == "1":
        nama = input("Masukkan Nama : ")
        nim = int(input("Masukkan NIM : "))
        semester = input("Masukkan Semester : ")
        daftar_mahasiswa_si.append([nama, nim, semester, []])
        print("Data mahasiswa berhasil ditambahkan.")
        
      elif menu_pengurus == "2":
          if not daftar_mahasiswa_si: 
              print("Belum ada Mahasiswa.")
          else:
              print("\nPilih Mahasiswa:")
              for i, mahas in enumerate(daftar_mahasiswa_si, start=1):
                  print(f"{i}. {mahas[0]} ({mahas[1]})")

              pilih = int(input("Masukkan urutan mahasiswa: ")) - 1
              if 0 <= pilih < len(daftar_mahasiswa_si):
                  matkul = input("Masukkan Nama Mata Kuliah : ")
                  nilai = int(input("Masukkan Nilai Mata Kuliah : "))
                  daftar_mahasiswa_si[pilih][3].append([matkul, nilai])
                  print("Mata kuliah dan nilai berhasil ditambahkan.")
              else:
                  print("Pilihan tidak ada.")
                
      elif menu_pengurus == "3":
          if not daftar_mahasiswa_si:
              print("Belum ada data mahasiswa.")
          else:
              print("\nData Mahasiswa dan Mata Kuliah")
              for mahas in daftar_mahasiswa_si:
                  print(f"\nNama : {mahas[0]}, NIM: {mahas[1]}, Semester: {mahas[2]}")
                  if not mahas[3]:
                      print("   Belum ada mata kuliah.")
                  else:
                      for makul in mahas[3]:
                          print(f"- {makul[0]} : Nilai: {makul[1]}")
                
      elif menu_pengurus == "4":
        nama = input("Masukkan Nama : ")
        nim = int(input("Masukkan NIM : "))
        semester = input("Masukkan Semester : ")
        for mahas in daftar_mahasiswa_si :
          if mahas[0] == nama and mahas[1] == nim and mahas[2] == semester:
            daftar_mahasiswa_si.remove(mahas)
            print("Data mahasiswa berhasil dihapus.")
            break
        else:
          print("Data Mahasiswa Tidak Ada.")
          
      elif menu_pengurus == "5":
          if not daftar_mahasiswa_si:
              print("Belum ada data mahasiswa.")
          else:
              print("\nPilih Mahasiswa untuk Update:")
              for i, mahas in enumerate(daftar_mahasiswa_si, start=1):
                  print(f"{i}. {mahas[0]} ({mahas[1]})")
              pilih = int(input("Masukkan urutan mahasiswa: ")) - 1
              
              if 0 <= pilih < len(daftar_mahasiswa_si):
                  print("Apa yang ingin diupdate?")
                  print("1. Nama")
                  print("2. NIM")
                  print("3. Semester")
                  print("4. Nilai Mata Kuliah")
                  pilihan_update = input("Pilih menu update: ")
                  
                  if pilihan_update == "1":
                      daftar_mahasiswa_si[pilih][0] = input("Masukkan Nama Baru: ")
                      print("Nama berhasil diupdate.")
                  elif pilihan_update == "2":
                      daftar_mahasiswa_si[pilih][1] = int(input("Masukkan NIM Baru: "))
                      print("NIM berhasil diupdate.")
                  elif pilihan_update == "3":
                      daftar_mahasiswa_si[pilih][2] = input("Masukkan Semester Baru: ")
                      print("Semester berhasil diupdate.")
                  elif pilihan_update == "4":
                      if not daftar_mahasiswa_si[pilih][3]:
                          print("Mahasiswa ini belum punya mata kuliah.")
                      else:
                          print("\nPilih Mata Kuliah:")
                          for j, mk in enumerate(daftar_mahasiswa_si[pilih][3], start=1):
                              print(f"{j}. {mk[0]} : {mk[1]}")
                          pilih_mk = int(input("Pilih urutan mata kuliah: ")) - 1
                          if 0 <= pilih_mk < len(daftar_mahasiswa_si[pilih][3]):
                              daftar_mahasiswa_si[pilih][3][pilih_mk][1] = int(input("Masukkan Nilai Baru: "))
                              print("Nilai berhasil diupdate.")
                          else:
                              print("Pilihan mata kuliah tidak valid.")
                  else:
                      print("Pilihan update tidak valid.")
              else:
                  print("Pilihan tidak ada.")        
        
      elif menu_pengurus == "6":
        print("Anda telah Keluar Dari menu pengurus")
        print("\n")
        login()
      else:
        print("Pilihan Tidak Ada.")
        
    except ValueError:
      print("Input Harus Berupa Angka")
    except KeyboardInterrupt:
      print("Jangan Klik CTRL + c")
    except EOFError:
      print("Jangan Klik CTRL + Z")

def menu_pengguna():
  while True:
    try:
      print("\n")
      print("="*70)
      print("|                       Menu Pengguna                                 |")
      print("="*70)
      print("1. Tampilkan Data Mahasiswa dan Mata Kuliah..")
      print("2. Lihat Mata Kuliah.")
      print("3. Keluar Aplikasi.")
      
      menu_pengguna = input("Masukkan Pilihan : ")
      
      if menu_pengguna == "1":
        if not daftar_mahasiswa_si:
          print("Belum ada data mahasiswa.")
        else:
          print("\nData Mahasiswa dan Mata Kuliah")
          for mahas in daftar_mahasiswa_si:
            print(f"\nNama : {mahas[0]}, NIM: {mahas[1]}, Semester: {mahas[2]}")
            if not mahas[3]:
              print("   Belum ada mata kuliah.")
            else:
              for makul in mahas[3]:
                print(f"- {makul[0]} : Nilai: {makul[1]}")
      elif menu_pengguna == "2":
        if not daftar_mahasiswa_si:
          print("Belum ada data mahasiswa.")
        else:
          print("\nDaftar Mata Kuliah")
          for mahas in daftar_mahasiswa_si:
              if not mahas[3]:
                    continue
              for makul in mahas[3]:
                print(f"- {makul[0]}")
      elif menu_pengguna == "3":
        print("Anda Telah Keluar Dari Program")
        exit()
    except ValueError:
      print("Input Harus Berupa Angka")
    except KeyboardInterrupt:
      print("Jangan Klik CTRL + c")
    except EOFError:
      print("Jangan Klik CTRL + Z")
      
login()
