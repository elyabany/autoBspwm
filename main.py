import os, time

def menu():
    print("1 -> Instalar Requerimientos necesarios")
    print("\n2 -> Instalar bspwm")
    print("\n3 -> Instalar Polybar")
    print("\n4 -> Salir")

    option = input("\n-->> ")

    if option == "1":
        req()
    if option == "2":
        bspwm()
    if option == "3":
        polybar()
    if option == "4":
        exit()

def req():
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
    os.system("sudo apt install bspwm rofi caja feh gnome-terminal -y")

    time.sleep(2)
    print("[+] Requetimientos instalados correctamente")
    while True:
        menu()

def bspwm():
    # Instalando bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("mv bspwm/* .")
    os.system("rm -r bspwm/")
    os.system("make")
    os.system("sudo make install")
    os.system("rm -r artworks/ contrib/ doc/ src/ tests/ bspc bspc.o bspwm bspwm.o desktop.o events.o ewmh.o geometry.o helpers.o history.o jsmn.o LICENSE Makefile messages.o monitor.o parse.o pointer.o query.o README.md restore.o rule.o settings.o Sourcedeps stack.o subscribe.o tree.o VERSION window.o")
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("mv sxhkd/* .")
    os.system("rm -r sxhkd/")
    os.system("cd ../sxhkd")
    os.system("make")
    os.system("sudo make install")
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("cp examples/sxhkdrc ~/.config/sxhkd/")
    os.system("rm -r contrib/ doc/ examples/ src/ grab.o helpers.o LICENSE Makefile parse.o README.md Sourcedeps sxhkd sxhkd.o types.o VERSION")
    os.system("cp tools/sxhkdrc ~/.config/sxhkd")
    print("\n[+] Bspwm instalado correctamente!")

    while True:
        menu()

def polybar():
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("mv polybar/* .")
    os.system("rm -r polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")
    os.system("sudo make install")
    os.system("rm -r bin/ cmake/ CMakeFiles/ common/ config/ contrib/ doc/ generated-sources/ include/ lib/ libs/ polybar/ src/ tests/ banner.png build.sh CHANGELOG.md CMajeCache.txt cmake_install.cmake CMakeLists.txt compile_commands.json CONTRIBUTING.md install_manifest LICENSE Makefile README.md SUPPORT.md version.txt")

    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.system("mv picom/* .")
    os.system("rm -r picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")
    os.system("sudo ninja -C build install")
    os.system("rm -r *.md *.conf *.desktop *.txt *.build *.spdx *.glsl COPYING Doxyfile CONTRIBUTORS bin/ build/ dbus-examples/ LICENSES/ man/ media/ meson/ src/ subprojects/ tests/")
    os.system("mkdir ~/.wallpapers")
    os.system("mv tools/wallpaper.jpg ~/.wallpapers")
    os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg' >> ~/.config/bspwm/bspwmrc")
    os.system("git clone https://github.com/VaughnValle/blue-sky.git")
    os.system("mkdir ~/.config/polybar")
    os.system("cp -r blue-sky/polybar/* ~/.config/polybar")
    os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc")
    os.system("sudo cp blue-sky/polybar/fonts/* /usr/share/fonts/truetype")
    os.system("fc-cache -v")
    os.system("mkdir ~/.config/picom")
    os.system("cp blue-sky/picom.conf ~/.config/picom")
    os.system("echo 'bspc config focus_follows_pointer true' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'picom --experimental-backends &' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'bspc config border_width 0' >> ~/.config/bspwm/bspwmrc")
    os.system("mkdir ~/.config/bin")
    os.system("wget https://raw.githubusercontent.com/LevisWings/Auto-PWE/main/ethernet_status.sh")
    os.system("chmod +x ethernet_status.sh")
    os.system("mv ethernet_status.sh ~/.config/bin")
    os.system("wget https://raw.githubusercontent.com/LevisWings/Auto-PWE/main/hackthebox.sh")
    os.system("chmod +x ethernet_status.sh")
    os.system("mv hackthebox.sh ~/.config/bin")
    os.system("cp tools/target_to_hack.sh .")
    os.system("chmod +x target_to_hack.sh")
    os.system("mv target_to_hack.sh ~/.config/bin")
    os.system("echo '' > ~/.config/bin/target")
    os.system("cp tools/launch.sh ~/.config/polybar")
    os.system("cp tools/current.ini ~/.config/polybar")
    os.system("mkdir ~/.config/rofi")
    os.system("mkdir ~/.config/rofi/themes")
    os.system("cp blue-sky/nord.rasi ~/.config/rofi/themes")
    os.system("sudo cp tools/settarget /bin")
    os.system("sudo cp tools/cleartarget /bin")

    print("\n[+] POLYBAR INSTALADO!!!")
if __name__ == '__main__':
    menu()
